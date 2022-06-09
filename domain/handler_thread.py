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

    def _handler_run(self):
        try:
            self._real_run()
        except Exception as e:
            showinfo(title='Pocesso', message=e, icon='question')
        else:
            showinfo(title='Processo', message='Processo concluido', icon='question')


