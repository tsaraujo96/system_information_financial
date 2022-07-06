from datetime import datetime, timedelta
from tkinter import *
from tkinter.ttk import Combobox

from tkcalendar import DateEntry

from presenter.binds import bind_date_entry
from presenter.binds.bind_combo_box import bind_combo_box
from threads import ThreadController


def first_tab(root) -> Frame:
    stock_frame = Frame(root.notebook_style)
    stock_frame.pack(fill=BOTH, expand=1)

    Label(stock_frame, text="Obter informações de Ações:").place(x=8, y=5)
    Label(stock_frame, text="Ativo").place(x=8, y=30)

    options = ("Dia", "Mes", "Hora", "Minuto")
    Label(stock_frame, text="Nível").place(x=106, y=28)
    combo_box = Combobox(root, width=5, values=options)
    combo_box.current(0)
    combo_box.place(x=110, y=73)

    var = StringVar()
    stock_button = Entry(stock_frame, width=15, borderwidth=3, textvariable=var)
    stock_button.place(x=10, y=50)

    date_start = DateEntry(stock_frame, locale="pt_BR", maxdate=datetime.today() - timedelta(days=1))
    Label(stock_frame, text="Data inicial").place(x=170, y=28)
    date_start.place(x=172, y=50)

    date_end = DateEntry(stock_frame, locale="pt_BR", maxdate=datetime.today())
    Label(stock_frame, text="Data final").place(x=270, y=28)
    date_end.place(x=272, y=50)

    get_info = Button(
        stock_frame,
        text="Gerar relatório",
        command=lambda: ThreadController(root).start_process_stock(
            date_start, date_end, stock_button, get_info, combo_box
        ),
    )

    get_info.place(x=10, y=80)

    bind_date_entry(date_start, date_end, get_info, stock_button, var)
    bind_combo_box(date_start, date_end, combo_box)

    return stock_frame
