import tkinter as tk


def create_button(master):
    button = tk.Button(
        master, text="Legal Library", font=("Arial", 13), command=on_click
    )
    return button


def on_click():
    print("Legal Library button clicked")


def create_page(master):
    page = tk.Frame(master, bg="#ffeedb")
    tk.Label(page, text="Legal Library Page", font=("Arial", 24), bg="#ffeedb").pack(
        expand=True
    )
    return page
