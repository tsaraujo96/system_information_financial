import threading
from tkinter.messagebox import showinfo


class HandlerThread(threading.Thread):

    """
    I did this as it is not able to catch an exception directly
    from one thread to another.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._real_run = self.run
        self.run = self._handler_run

        self.date_start = kwargs.get("args")[0]
        self.date_end = kwargs.get("args")[1]
        self.stock_button = kwargs.get("args")[2]
        self.get_info = kwargs.get("args")[3]
        self.combo_box = kwargs.get("args")[4]

    def _handler_run(self):
        try:
            self._real_run()

        except Exception as e:
            showinfo(title="Pocesso", message=str(e), icon="question")
            self._enable_all_button()
        else:
            showinfo(title="Processo", message="Processo concluido", icon="question")
            self._enable_all_button()

    def _enable_all_button(self):

        if self.combo_box.get() not in ["Hora", "Minuto"]:
            self.date_start.config(state="enable")
            self.date_end.config(state="enable")

        self.stock_button.config(state="normal")
        self.get_info.config(state="normal")
        self.combo_box.configure(state="enable")
