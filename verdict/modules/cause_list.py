import tkinter as tk


def create_button(master):
    button = tk.Button(master, text="Cause List", font=("Arial", 13), command=on_click)
    return button


def on_click():
    print("Cause List button clicked")


def create_page(master):
    page = tk.Frame(master, bg="#ffeedb")
    tk.Label(page, text="Cause List Page", font=("Arial", 24), bg="#ffeedb").pack(
        expand=True
    )
    return page
