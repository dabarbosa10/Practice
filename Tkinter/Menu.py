from tkinter import *

def function1():
    print('Menu item clicked')


root=Tk()
myMenu=Menu(root)
root.config(menu=myMenu)
submenu=Menu(myMenu)
myMenu.add_cascade(label='File', menu=submenu)
submenu.add_command(label='Project', command=function1)
submenu.add_command(label='Save',command=function1)

status=Label(root,text='This is the current status',bd=1,relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM,fill=X)

toolbar=Frame(root,bg='Green')
insertButton= Button(toolbar,text='Insert Files', command=function1)
deleteButton=Button(toolbar,text='Delete Files', command=function1)

insertButton.pack(side=LEFT, padx=2, pady=3)
deleteButton.pack(side=LEFT,padx=2, pady=3)
toolbar.pack()


root.mainloop()