from two_interface_tkinter import MyGui
from tkinter.messagebox import showinfo
from tkinter import mainloop

class CustomGui(MyGui):
    def reply(self):
        showinfo(title='popup2', message='Ouch!')


if __name__=='__main__':
    CustomGui().pack()
    mainloop()
