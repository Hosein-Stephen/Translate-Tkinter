from tkinter import *
from translate import Translator
from tkinter import messagebox
import tkinter as tk
import webbrowser 
import requests
import datetime
import time


window = Tk()
window.title("Hosein Stephen")
window.geometry("700x200")
window.resizable(width=False , height=False)


def translate_message():
    input_text = text2.get()
    source_lang = 'fa'
    target_lang = 'en'
    translator = Translator(from_lang=source_lang, to_lang=target_lang)
    translation = translator.translate(input_text)
    var1 = StringVar()
    var1.set(translation)
    label.config(text=var1)

    label.config(text=translation)
    if text2.get():
        text = text2.get()
        with open("Hosein_translate.txt", "a", encoding="utf-8") as file:
            file.write(f"{translation}: {text}\n")
    if label.get() == "":
        messagebox.showerror("Error","""Input is Empty!!
write something""")


def translate_fa():
    input_text = text2.get()
    source_lang = 'en'
    target_lang = 'fa'
    translator = Translator(from_lang=source_lang, to_lang=target_lang)
    translation = translator.translate(input_text)
    var = StringVar()
    var.set(translation)
    label.config(text=var)
    if text2.get():
        text = text2.get()
        with open("Hosein_translate.txt", "a", encoding="utf-8") as file:
            file.write(f"{translation}: {text}\n")
    if label.get() == "":
        messagebox.showerror("Error","""Input is Empty!!
write something""")


lblinput = Label(window,text="Input:" ,font=("bold","15"))
lbloutput = Label(window,text="Output:",font=("bold","15"))

text2 = Entry(window,font="bold",width=20)
label = Entry(window,font="bold",width=20)
button = Button(window, text="Translate En", command=translate_message , activebackground="black",activeforeground="white")
btn = Button(window,text="Trnslate Fa",command=translate_fa, activebackground="black",activeforeground="white")

menu = tk.Menu(window)
def menu_command(command):
    if command == "Cut":
        label.event_generate("<<Cut>>")
    elif command == "Copy":
        label.event_generate("<<Copy>>")
    elif command == "Paste":
        text2.event_generate("<<Paste>>")
    elif command == "Clear":
        label.delete(0,END)
        text2.delete(0,END)
    elif command == "Exit":
        if messagebox.askyesno("Confirm Exit", "Are you sure you want to exit?"):
            window.quit()
    elif command == "Contact":
        webbrowser.get('C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s').open_new("https://mail.google.com/mail/u/0/?hl=tr#inbox?compose=CllgCJlHnMdMlJHkfbMgZGWGZhxMSsdRWrdfDWkmszkNXfVmJpSFRCxFGfhPTBXBLBPpCwgCZTg")
        messagebox.showinfo("Email FeedBack","Send message to stephen.amel9990@gmail.com")
    else:
        messagebox.showerror("Error installer","You don't have any Microsoft Edge in your")
        pass

menu.add_command(label="Cut", command=lambda: menu_command("Cut"))
menu.add_command(label="Copy", command=lambda: menu_command("Copy"))
menu.add_command(label="Paste", command=lambda: menu_command("Paste"))
menu.add_command(label="Clear", command=lambda: menu_command("Clear"))
menu.add_command(label="Exit", command=lambda: menu_command("Exit"))
menu.add_command(label="Contact", command=lambda: menu_command("Contact"))

window.config(menu=menu)
if window.quit():
    messagebox.showerror("Error installer","You don't have any Microsoft Edge in your")
        

def tick():
    setTime = time.strftime('%I: %M %S %p ' + '%A')
    
    clock.config(text=setTime )
    clock.after(200, tick)
clock = Label(window,height="1",width="20", font=('time','15','bold'),fg="black")
clock.place(x =-10,y=170)
if __name__ == '__main__' :
    tick()

lblinput.place(x=270,y=20)
lbloutput.place(x=270,y=115)
text2.place(x=270,y=50)
button.place(x=220,y=88)
label.place(x=270,y=140)
btn.place(x=410,y=88)
window.mainloop()
