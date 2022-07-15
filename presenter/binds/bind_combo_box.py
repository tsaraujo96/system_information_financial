from utils import enable_button_calendar


def bind_combo_box(date_start, date_end, combo_box, fake_label):

    combo_box.bind(
        "<<ComboboxSelected>>",
        lambda event: enable_button_calendar(
            event, date_start, date_end, combo_box, fake_label
        ),
    )
