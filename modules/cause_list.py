import tkinter as tk


def create_button(master):
    button = tk.Button(master, text="Cause List", font=("Arial", 13), command=on_click)
    return button


def on_click():
    print("Button 2 clicked")