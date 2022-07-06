from domain import HandlerThread
from use_case import TabOneUseCase


class ThreadController:
    def __init__(self, root):
        self.root = root

    def _refresh(self):
        self.root.update()
        self.root.after(1000, self._refresh)

    def start_process_stock(self, date_start, date_end, stock_button, get_info, combo_box):
        self._refresh()
        self._disable_all_button(date_start, date_end, stock_button, get_info, combo_box)
        HandlerThread(
            target=TabOneUseCase().run,
            args=(date_start, date_end, stock_button, get_info, combo_box),
        ).start()

    @staticmethod
    def _disable_all_button(date_start, date_end, stock_button, get_info, combo_box):
        date_start.config(state="disabled")
        date_end.config(state="disabled")
        stock_button.config(state="disabled")
        get_info.config(state="disabled")
        combo_box.configure(state="disabled")
