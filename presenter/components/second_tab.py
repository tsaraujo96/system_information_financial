from tkinter import *


def second_tab(root) -> Frame:
    option_frame = Frame(root.notebook_style)
    option_frame.pack(fill=BOTH, expand=1)
    Label(option_frame, text="Obter informações de Opções:").place(x=8, y=5)

    return option_frame
