import tkinter as tk
from datetime import datetime
import pytz


class Logger:
    def __init__(self):
        self.text_widget = None
        self.log_buffer = []

    def time_now(self) -> str:
        time = datetime.now(pytz.timezone("Asia/Kolkata"))
        formatted_date = time.strftime("%d/%m")
        formatted_time = time.strftime("%H:%M")
        return formatted_date, formatted_time

    def set_text_widget(self, text_widget):
        self.text_widget = text_widget
        for level, message, color in self.log_buffer:
            self._log(level, message, color)
        self.log_buffer = []

    def _log(self, level, message, color):
        date, time = self.time_now()
        if self.text_widget:
            self.text_widget.configure(state="normal")
            self.text_widget.insert(
                tk.END, f"{time} {date} [{level}]: {message}\n", level
            )
            self.text_widget.tag_config(level, foreground=color)
            self.text_widget.configure(state="disabled")
            self.text_widget.yview(tk.END)
        else:
            self.log_buffer.append((level, message, color))

    def INFO(self, message):
        self._log("INFO", message, "green")

    def WARN(self, message):
        self._log("WARN", message, "orange")

    def ERROR(self, message):
        self._log("ERROR", message, "red")


log = Logger()
