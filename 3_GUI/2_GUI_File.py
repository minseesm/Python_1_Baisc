# GUI (Graphic User Interface) // cf) LUI (Line User Interface)
from tkinter import *
import os
from tkinter import filedialog
from pathlib import Path

window = Tk()
window.title("[MINSOO] GUI")
window.geometry("640x480+2300+300")
window.resizable(FALSE, TRUE)

change_txt = ''
filename = ""

def open_file():
    global filename
    filename = filedialog.askopenfilename(title = "Select Open File",
                                          filetypes=(("Text File", "*.txt"), ("All Files", "*.*")),
                                          initialdir="/Users/vision/academy/python/Python_YS")
    if os.path.isfile(filename):
        file = open(filename, "r")
        txt.delete("1.0",END)
        txt.insert(END, file.read())

def browse_dest_path() :
    filesave = filedialog.asksaveasfilename(title="Save",
                                            defaultextension=".txt",
                                            filetypes=(("Text File", "*.txt"), ("All Files", "*.*")),
                                            initialdir="/Users/vision/academy/python/Python_YS")
    if filesave == "":
        return
    return filesave

def save_file():
    global filename
    global change_txt
    file_path = browse_dest_path()
    with open(file_path, "w") as file:
        file.write(change_txt)

menu = Menu(window)
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="Open", command=open_file)
menu_file.add_command(label="Save", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="Exit", command=window.quit)
menu.add_cascade(label="File", menu=menu_file)

frame_btn = Frame(window, relief="solid", bd=1)
frame_btn.pack(fill="x")

def change():
    global change_txt
    change_txt = txt.get("1.0", END)
    label.config(text=change_txt)
    txt.delete("1.0",END)

def delete():
    txt.delete("1.0",END)
    label.config(text="")

# Button SectionChange_txt

btn1 = Button(frame_btn, text="Change", command=change)
btn1.pack(side="left")

def save():
    global change_txt
    txt_file = open("save.txt", 'w', newline='')
    txt_file.write(change_txt)
    txt_file.close()

btn_save = Button(frame_btn, text="Save", command=save)
btn_save.pack(side="right")

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


window.config(menu=menu)
window.mainloop()