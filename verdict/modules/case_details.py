import tkinter as tk


def create_button(master):
    button = tk.Button(
        master,
        text="Case Details",
        font=("Arial", 13),
    )
    return button


def create_page(master):
    page = tk.Frame(master, bg="#ffeedb")
    tk.Label(page, text="Case Details Page", font=("Arial", 24), bg="#ffeedb").pack(
        expand=True
    )
    return page
