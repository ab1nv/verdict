import tkinter as tk


def create_button(master):
    button = tk.Button(
        master, text="Draft Petition", font=("Arial", 13), command=on_click
    )
    return button


def on_click():
    print("Draft Petition button clicked")


def create_page(master):
    page = tk.Frame(master, bg="#ffeedb")
    tk.Label(page, text="Draft Petition Page", font=("Arial", 24), bg="#ffeedb").pack(
        expand=True
    )
    return page
