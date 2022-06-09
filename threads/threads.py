from domain import HandlerThread
from use_case import TabOneUseCase


class ThreadController:
    def __init__(self, root):
        self.root = root

    def _refresh(self):
        self.root.update()
        self.root.after(1000, self._refresh)

    def start_process_stock(self, date_start, date_end, stock_button, get_info, var):

        self._refresh()
        HandlerThread(
            target=TabOneUseCase().run,
            args=(date_start, date_end, stock_button, get_info, var),
        ).start()

