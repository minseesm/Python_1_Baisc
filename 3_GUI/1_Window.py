# GUI (Graphic User Interface) // cf) LUI (Line User Interface)
from tkinter import *

window = Tk()
window.title("[MINSOO] GUI")
window.geometry("640x480+2300+300")
window.resizable(FALSE, TRUE)

frame_btn = Frame(window, relief="solid", bd=1)
frame_btn.pack(fill="x")

def change():
    change_txt = txt.get("1.0", END)
    label.config(text=change_txt)
    txt.delete("1.0",END)

def delete():
    txt.delete("1.0",END)
    label.config(text="")

# Button Section
btn1 = Button(frame_btn, text="Change", command=change)
btn1.pack(side="left")

btn2 = Button(frame_btn, fg='red', bg='yellow', text="Delete", command=delete)
btn2.pack(side="right")

# btn3 = Button(frame_btn, padx=5, pady=10, text="Hello")
# btn3.pack(side="right")

# Frame section
frame_txt = Frame(window, relief="solid", bd=1)
frame_txt.pack(fill="both")

# Scrollber Section
scr = Scrollbar(frame_txt)
scr.pack(side="right", fill="y")

# Text section
txt = Text(frame_txt, yscrollcommand=scr.set)
txt.pack(fill="both")
scr.config(command=txt.yview)

# Label section
label = Label(window, text="Hello")
label.pack()

window.mainloop()