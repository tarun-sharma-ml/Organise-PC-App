"""Guided setup for the optional Gemini key used by AI renaming."""

import webbrowser

from config import settings


def _finish(window, *, skip: bool = False):
    if skip:
        settings.AI_RENAME_ENABLED = False
        settings.clear_gemini_api_key()
    window.destroy()


def _test_and_save(entry, status_label, root):
    from utils import ai_namer

    value = (entry.get() or "").strip()
    if not value:
        status_label.config(text="Paste a Gemini API key first.")
        return

    ok, text = ai_namer.validate_api_key(value)
    if not ok:
        status_label.config(text=text)
        return

    if settings.save_gemini_api_key(value):
        settings.AI_RENAME_ENABLED = True
        status_label.config(text="Key works — AI naming is enabled.")
        root.after(700, lambda: root.destroy())
    else:
        status_label.config(text="Could not save the key. Please try again.")


def show_setup_if_needed() -> bool:
    """Show the first-run setup wizard for the optional Gemini key, if needed."""
    if settings.GEMINI_API_KEY and settings.AI_RENAME_ENABLED:
        return True

    try:
        import tkinter as tk
    except ImportError:
        return False

    root = tk.Tk()
    root.title("Organise_PC setup")
    root.geometry("460x260")
    root.resizable(False, False)
    root.attributes("-topmost", True)

    frame = tk.Frame(root, padx=18, pady=18)
    frame.pack(fill="both", expand=True)

    title = tk.Label(
        frame,
        text="Optional: enable AI renaming",
        font=("Segoe UI", 12, "bold"),
        anchor="w",
    )
    title.pack(fill="x", pady=(0, 8))

    info = tk.Label(
        frame,
        text=(
            "Create a free API key in Google AI Studio to let Organise_PC suggest cleaner names.\n"
            "You can skip this and continue without AI."
        ),
        justify="left",
        wraplength=420,
        anchor="w",
    )
    info.pack(fill="x", pady=(0, 10))

    open_button = tk.Button(
        frame,
        text="Open Google AI Studio",
        command=lambda: webbrowser.open("https://aistudio.google.com/app/apikey"),
    )
    open_button.pack(fill="x", pady=(0, 10))

    entry_var = tk.StringVar(value=settings.GEMINI_API_KEY or "")
    entry = tk.Entry(frame, textvariable=entry_var, width=50)
    entry.pack(fill="x", pady=(0, 8))

    status_label = tk.Label(frame, text="", fg="darkgreen", justify="left", wraplength=420)
    status_label.pack(fill="x", pady=(2, 8))

    actions = tk.Frame(frame)
    actions.pack(fill="x")

    test_button = tk.Button(
        actions,
        text="Test key",
        command=lambda: _test_and_save(entry, status_label, root),
    )
    test_button.pack(side="left")

    skip_button = tk.Button(
        actions,
        text="Skip",
        command=lambda: _finish(root, skip=True),
    )
    skip_button.pack(side="right")

    root.protocol("WM_DELETE_WINDOW", lambda: _finish(root, skip=True))
    root.mainloop()
    return settings.AI_RENAME_ENABLED
