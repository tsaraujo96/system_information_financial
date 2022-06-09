from datetime import datetime
from tkinter import *

from tkcalendar import DateEntry

from presenter.binds import bind_date_entry
from threads import ThreadController


def first_tab(root) -> Frame:
    stock_frame = Frame(root.notebook_style)
    stock_frame.pack(fill=BOTH, expand=1)

    Label(stock_frame, text="Obter informações de Ações:").place(x=8, y=5)
    Label(stock_frame, text="Ativo").place(x=8, y=30)

    var = StringVar()
    stock_button = Entry(stock_frame, width=15, borderwidth=3, textvariable=var)
    stock_button.place(x=10, y=50)

    date_start = DateEntry(stock_frame, locale="pt_BR")
    Label(stock_frame, text="Data inicial").place(x=118, y=28)
    date_start.place(x=120, y=50)

    date_end = DateEntry(stock_frame, locale="pt_BR", maxdate=datetime.today())
    Label(stock_frame, text="Data final").place(x=218, y=28)
    date_end.place(x=220, y=50)

    get_info = Button(
        stock_frame,
        text="Gerar relatório",
        command=lambda: ThreadController(root).start_process_stock(date_start, date_end, stock_button, get_info, var),
        state="disabled",
    )

    get_info.place(x=10, y=80)

    bind_date_entry(date_start, date_end, get_info, stock_button, var)

    return stock_frame

