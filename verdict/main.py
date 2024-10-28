import tkinter as tk
from modules import (  # type: ignore
    case_details,
    cause_list,
    draft_petition,
    legal_library,
    settings,
    logs,
)


class Verdict:
    def __init__(self, root):
        root.geometry("1920x1080")
        root.configure(bg="#ffeedb")
        root.title("Verdict")

        button_frame = tk.Frame(root, bg="#ffeedb")
        button_frame.pack(side=tk.TOP, anchor="w")

        self.page_frame = tk.Frame(root, bg="#ffeedb")
        self.page_frame.pack(fill=tk.BOTH, expand=True)

        self.buttons = []
        self.pages = {}

        self.create_buttons(button_frame)
        self.select_page(0)

    def create_buttons(self, master):
        button_data = [
            ("Case Details", case_details.create_page),
            ("Cause List", cause_list.create_page),
            ("Draft Petition", draft_petition.create_page),
            ("Legal Library", legal_library.create_page),
            ("Settings", settings.create_page),
            ("Logs", logs.create_page),
        ]

        for i, (button_text, page_creator) in enumerate(button_data):
            button = tk.Button(
                master,
                text=button_text,
                font=("Arial", 13),
                command=lambda i=i: self.select_page(i),
                relief=tk.RAISED,
            )
            button.pack(side=tk.LEFT)
            self.buttons.append(button)

            page = page_creator(self.page_frame)
            page.grid(row=0, column=0, sticky="nsew")
            page.grid_remove()
            self.pages[i] = page

    def select_page(self, page_index):
        for button in self.buttons:
            button.config(relief=tk.RAISED)

        selected_button = self.buttons[page_index]
        selected_button.config(relief=tk.SUNKEN)

        for page in self.pages.values():
            page.grid_remove()
        self.pages[page_index].grid()


if __name__ == "__main__":
    root = tk.Tk()
    root.state("zoomed")
    app = Verdict(root)
    root.mainloop()
