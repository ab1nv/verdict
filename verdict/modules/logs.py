import tkinter as tk
from tkinter import messagebox
from verdict.handlers.logging import log


def create_page(master):
    page = tk.Frame(master, bg="#ffeedb")
    tk.Label(page, text="Logs", font=("Arial", 24), bg="#ffeedb").pack(pady=10)

    log_text = tk.Text(
        page,
        wrap="word",
        font=("Arial", 12),
        state="disabled",
        bg="#f7f7f7",
        height=20,
        width=100,
    )
    log_text.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
    log.set_text_widget(log_text)

    v_scrollbar = tk.Scrollbar(page, command=log_text.yview)
    log_text.configure(yscrollcommand=v_scrollbar.set)
    v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    clear_button = tk.Button(
        page,
        text="Clear",
        font=("Arial", 12),
        command=lambda: clear_logs(log_text),
    )
    clear_button.pack(pady=10, side=tk.LEFT, padx=(20, 10))

    copy_button = tk.Button(
        page,
        text="Copy",
        font=("Arial", 12),
        command=lambda: copy_last_500_lines(log_text, copy_button),
    )
    copy_button.pack(pady=10, side=tk.LEFT)

    return page


def clear_logs(log_text):
    log_text.configure(state="normal")
    log_text.delete("1.0", tk.END)
    log_text.configure(state="disabled")


def copy_last_500_lines(log_text, copy_button):
    log_text.configure(state="normal")
    all_text = log_text.get("1.0", tk.END)
    lines = all_text.splitlines()
    last_500_lines = "\n".join(lines[-500:])
    log_text.configure(state="disabled")

    log_text.clipboard_clear()
    log_text.clipboard_append(last_500_lines)

    copy_button.config(text="Copied")
    log_text.after(900, lambda: copy_button.config(text="Copy"))
