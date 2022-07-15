from datetime import timedelta
from tkinter import NORMAL, DISABLED


def enable_button_info(event, date_start, date_end, button, stock_button, var):

    var.set(var.get().upper())

    if date_start.get_date() == date_end.get_date():
        date = date_start.get_date() - timedelta(days=1)
        date_start.set_date(date)

    if date_end.get_date() >= date_start.get_date() and len(stock_button.get()) >= 4:
        button["state"] = NORMAL
    else:
        button["state"] = DISABLED


def enable_button_calendar(event, date_start, date_end, combo_box, fake_label):

    if combo_box.get() not in ['Hora', 'Minuto']:
        fake_label.config(text="")
        date_start["state"] = NORMAL
        date_end["state"] = NORMAL

    else:
        periodo = '7' if combo_box.get() == 'Minuto' else '200'
        fake_label.config(text=f"Período dos últimos {periodo} dias")
        date_start["state"] = DISABLED
        date_end["state"] = DISABLED
