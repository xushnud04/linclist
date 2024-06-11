from tkinter import *
from tkinter import Button

root = Tk()
root.geometry('500x500')
# label
label = Label(root, text="Hello World", fg="red", height=5, font=("Arial", 20))
label.grid(column=0, row=0,columnspan=2)
a = ""


# button
def click():
    label.config(text="Hello World " + str(a) + "  ")


bt = Button(root, bg="green", fg="red", text="0", font="Areal", width=25, borderwidth=1, command=click)

# textbox
tx = Entry(root, font="Areal", bg="pink", fg="red", width=50)
tx.insert(0, "")
tx.grid(column=0, row=1, columnspan=2)


def bt_click(number) -> None:
    global a
    if number == 1:
        a = str(number)
        label.config(text="Hello World " + str(1) + " um tugma ")
    elif number == 2:
        a = str(number)
        label.config(text="Hello World " + str(2) + " um tugma ")
    elif number == 3:
        a = str(number)
        label.config(text="Hello World " + str(3) + " um tugma ")
    elif number == 4:
        a = str(number)
        label.config(text="Hello World " + str(4) + " um tugma ")
    elif number == 5:
        a = str(number)
        label.config(text="Hello World " + str(5) + " um tugma ")
    elif number == 6:
        a = str(number)
        label.config(text="Hello World " + str(6) + " um tugma ")
    elif number == 7:
        a = str(number)
        label.config(text="Hello World " + str(7) + " um tugma ")
    elif number == 0:
        a = str(number)
        label.config(text="Hello World " + str(8) + " um tugma ")

    tx.insert(0, a)


# button list
bt0 = Button(root, bg="green", fg="red", text="0", font="Areal", width=25, borderwidth=3, command=lambda: bt_click(0))
bt1 = Button(root, bg="green", fg="red", text="1", font="Areal", width=25, borderwidth=3, command=lambda: bt_click(1))
bt2 = Button(root, bg="green", fg="red", text="2", font="Areal", width=25, borderwidth=3, command=lambda: bt_click(2))
bt3 = Button(root, bg="green", fg="red", text="3", font="Areal", width=25, borderwidth=3, command=lambda: bt_click(3))
bt4 = Button(root, bg="green", fg="red", text="4", font="Areal", width=25, borderwidth=3, command=lambda: bt_click(4))
bt6 = Button(root, bg="green", fg="red", text="5", font="Areal", width=25, borderwidth=3, command=lambda: bt_click(5))
bt7 = Button(root, bg="green", fg="red", text="6", font="Areal", width=25, borderwidth=3, command=lambda: bt_click(6))
bt8 = Button(root, bg="green", fg="red", text="7", font="Areal", width=25, borderwidth=3, command=lambda: bt_click(7))

bt_l: list[Button] = [bt0, bt1, bt2, bt3, bt4, bt6, bt7, bt8]
k = 1
h = 0
for i in bt_l:
    k += 1
    if k == 6:
        h += 1
        k = 2
    i.grid(column=h, row=k)
root.mainloop()
