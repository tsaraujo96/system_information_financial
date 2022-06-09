from tkinter import *
from tkinter import ttk

from domain import NameStockError
from presenter.components import first_tab, second_tab


class TkinterPresenter(Tk):
    def __init__(self):
        super().__init__()
        self.notebook_style = None

        self.width = 380
        self.height = 150

    def run(self):

        try:
            self._default_configs()

            stock_frame = first_tab(self)
            option_frame = second_tab(self)

            self.notebook_style.add(stock_frame, text="Ações")
            self.notebook_style.add(option_frame, text="Opções")
        except NameStockError:
            print('e ai')
        finally:
            return self

    def _default_configs(self):
        self.title("SIF - System Information Financial")
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(0, 0)

        self.notebook_style = ttk.Notebook(self)
        self.notebook_style.place(x=0, y=0, width=self.width, height=self.height)


