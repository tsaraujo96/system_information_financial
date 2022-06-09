from tkinter import NORMAL, DISABLED


def enable_button(event, date_start, date_end, button, stock_button, var):

    var.set(var.get().upper())

    if date_end.get_date() >= date_start.get_date() and len(stock_button.get()) >= 4:
        button["state"] = NORMAL
    else:
        button["state"] = DISABLED
