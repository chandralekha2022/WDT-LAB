from tkinter import *
from tkinter.ttk import *
from time import strftime
root=Tk()
root.title("Menu demonstration")
menubar=Menu(root)
file=Menu(menubar,tearoff=0)
menubar.add_cascade(label='file',menu=file)
file.add_command(label='New file',command='None')
file.add_command(label='Open',command='None')
edit=Menu(menubar,tearoff=0)
menubar.add_cascade(label='edit',menu=edit)
root.config(menu=menubar)
mainloop()
