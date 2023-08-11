from __future__ import annotations

from tkinter import *
from tkinter import ttk

from presenter.components import first_tab


class TkinterPresenter(Tk):
    def __init__(self):
        super().__init__()
        self.notebook_style = None

        self.width = 380
        self.height = 150

    def run(self) -> TkinterPresenter:

        self._default_configs()

        stock_frame = first_tab(self)
        # option_frame = second_tab(self)

        self.notebook_style.add(stock_frame, text="Ações")
        # self.notebook_style.add(option_frame, text="Opções")

        return self

    def _default_configs(self):
        self.title("SIF - System Information Financial")
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(0, 0)
        self.iconbitmap("icon.ico")

        self.notebook_style = ttk.Notebook(self)
        self.notebook_style.place(x=0, y=0, width=self.width, height=self.height)
