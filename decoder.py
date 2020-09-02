from stegano import lsb
import tkinter
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import tkinter.messagebox
from tkinter import ttk



root = Tk()
root.geometry("550x300+300+150")
root.resizable(width=True, height=True)


def openfn():
    filename = filedialog.askopenfilename(title='open')
    return filename
def open_img():
    global img
    x = openfn()
    img = Image.open(x)
    img.save("output.png")
    img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.image = img
    panel.pack()


def decode():


    clear_message = lsb.reveal('output.png')
    print(clear_message)
    if clear_message == None:
        tkinter.messagebox.showinfo('Secret message', "No Secrets")
    else:
        tkinter.messagebox.showinfo('Secret message', clear_message)



w = ttk.Label(root, text="Steganography Decoder").pack()
btn = ttk.Button(root, text='open image', command=open_img).pack()
btn = ttk.Button(root, text='Decode', command=decode).pack()


root.mainloop()