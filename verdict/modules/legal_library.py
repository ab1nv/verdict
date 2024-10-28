import tkinter as tk
from tkinter import ttk
from datetime import datetime
import webbrowser


def create_button(master):
    button = tk.Button(
        master,
        text="Legal Library",
        font=("Arial", 13),
    )
    return button


def create_page(master):
    page = tk.Frame(master, bg="#ffeedb")
    label = tk.Label(page, text="Legal Library", font=("Arial", 22), bg="#ffeedb")
    label.pack(pady=20)

    main_frame = tk.Frame(page, bg="#ffeedb")
    main_frame.pack(expand=True)

    doc_type_frame = tk.Frame(main_frame, bg="#ffeedb")
    doc_type_frame.pack(side=tk.LEFT, padx=20, pady=20)

    doc_type_label = tk.Label(
        doc_type_frame, text="Document Type", font=("Arial", 17), bg="#ffeedb"
    )
    doc_type_label.pack(anchor=tk.W)

    doc_type_var = tk.StringVar(value="All")
    doc_types = [
        "All",
        "Laws",
        "Judgments (All Courts)",
        "Judgments (Allahabad HC)",
        "Judgments (Supreme Court)",
        "Tribunals",
        "Highcourts & Supremecourt",
    ]
    for doc_type in doc_types:
        radio_button = tk.Radiobutton(
            doc_type_frame,
            text=doc_type,
            variable=doc_type_var,
            value=doc_type,
            font=("Arial", 12),
            bg="#ffeedb",
            padx=10,
            pady=5,
        )
        radio_button.pack(anchor=tk.W, padx=10, pady=5)

    year_frame = tk.Frame(main_frame, bg="#ffeedb")
    year_frame.pack(side=tk.LEFT, padx=20, pady=20)

    year_label = tk.Label(year_frame, text="Year", font=("Arial", 17), bg="#ffeedb")
    year_label.pack(anchor=tk.W)

    year_var = tk.StringVar(value="Any Year")
    current_year = datetime.now().year
    year_options = ["Any Year"] + [str(year) for year in range(current_year, 1799, -1)]

    year_dropdown = ttk.Combobox(
        year_frame,
        textvariable=year_var,
        values=year_options,
        state="readonly",
        font=("Arial", 12),
        width=12,
    )
    year_dropdown.pack(pady=10)

    search_frame = tk.Frame(main_frame, bg="#ffeedb")
    search_frame.pack(side=tk.LEFT, padx=20, pady=20)

    input_label = tk.Label(
        search_frame, text="Search Query", font=("Arial", 17), bg="#ffeedb"
    )
    input_label.pack(anchor=tk.W)

    input_box = tk.Entry(search_frame, width=30, font=("Arial", 14))
    input_box.pack(side=tk.LEFT, pady=10)
    input_box.bind(
        "<Return>", lambda event: get_data(doc_type_var, year_var, input_box)
    )

    go_button = tk.Button(
        search_frame,
        text="Go",
        command=lambda: get_data(doc_type_var, year_var, input_box),
        font=("Arial", 14),
    )
    go_button.pack(side=tk.LEFT, padx=10)

    return page


def get_data(doc_type_var, year_var, input_box):
    selected_doc_type = doc_type_var.get()
    selected_year = year_var.get()
    search_term = input_box.get()

    base_url = "https://indiankanoon.org/search/?formInput="
    search_query = search_term.replace(" ", "+")

    if selected_doc_type == "Judgments (Allahabad HC)":
        doc_type_param = "+doctypes:allahabad"
    elif selected_doc_type == "Judgments (All Courts)":
        doc_type_param = "+doctypes:judgements"
    elif selected_doc_type == "Judgments (Supreme Court)":
        doc_type_param = "+doctypes:supremecourt"
    else:
        doc_type_param = (
            f"+doctypes:{selected_doc_type.lower().replace(' & ', '')}"
            if selected_doc_type != "All"
            else ""
        )

    year_param = (
        f"+fromdate:1-1-{selected_year}+todate:31-12-{selected_year}"
        if selected_year != "Any Year"
        else ""
    )

    final_url = f"{base_url}{search_query}{doc_type_param}{year_param}"
    webbrowser.open(final_url)
