import tkinter as tk
from modules import case_details, cause_list, draft_petition, legal_library


class Verdict:
    def __init__(self, root):
        root.geometry("1920x1080")
        root.configure(bg="#ffeedb")
        root.title("Verdict")

        button_frame = tk.Frame(root, bg="#ffeedb")
        button_frame.pack(side=tk.TOP, fill=tk.X)

        buttons = [
            case_details.create_button(button_frame),
            cause_list.create_button(button_frame),
            draft_petition.create_button(button_frame),
            legal_library.create_button(button_frame),
        ]

        for button in buttons:
            button.pack(side=tk.LEFT)


if __name__ == "__main__":
    root = tk.Tk()
    root.state("zoomed")
    app = Verdict(root)
    root.mainloop()
