from tkinter import *
from two_interface_tkinter import MyGui

# Главное окно приложения
mainwin = Tk()
Label(mainwin, text=__name__).pack()

# Окно диалога
popup = Toplevel()
Label(popup, text='Attach').pack(side=LEFT)
MyGui(popup).pack(side=RIGHT)
mainwin.mainloop()