from utils import enable_button_info


def bind_date_entry(date_start, date_end, get_info, stock_button, var):
    for f in [date_start, date_end, stock_button]:

        var_event = "<KeyRelease>" if f == stock_button else "<<DateEntrySelected>>"

        f.bind(
            var_event,
            lambda event: enable_button_info(
                event, date_start, date_end, get_info, stock_button, var
            ),
        )
