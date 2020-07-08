import tkinter
from tkinter import messagebox
import img2pdf 
import os
#pyinstaller --onefile --windowed --icon="images\myicon.ico" myApp.py 

imagelist = []
ext = (".jpg",".png",".jpeg")
name = "_kai.pdf"
window = tkinter.Tk()
window.title(" Image to Pdf")
#window.geometry("400x300")
window.iconbitmap(default='images\\myicon.ico')
window.resizable(0, 0)


def show_success():
    messagebox.showinfo('Notify', 'Successfully made pdf file')

def getTextInput():
    imagelist = []
    folder=textExample.get("1.0", tkinter.END+"-1c")
    for dirpath, dirnames, filenames in os.walk(folder):
        for filename in [f for f in filenames if f.endswith(ext)]:
            full_path = os.path.join(dirpath, filename)
            imagelist.append(full_path)

    imagelist.sort()
    if folder:
        with open(folder + name,"wb") as f:
            f.write(img2pdf.convert([i for i in imagelist]))
        show_success()

textExample=tkinter.Text(window, height=15)
textExample.pack()
btnRead=tkinter.Button(window, height=1, width=10, text="Convert", 
                    command=getTextInput)
btnRead.pack()


window.mainloop()
