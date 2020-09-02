from stegano import lsb
import tkinter
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import tkinter.messagebox
from tkinter import ttk


root = Tk()
root.geometry("700x700")
root.resizable(width=True, height=True)


class SeaofBTCapp(tkinter.Tk):

    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)

        tkinter.Tk.iconbitmap(self, default='clienticon.ico')
        tkinter.Tk.wm_title(self, "Sea of BTC Client")


def openfn():
    filename = filedialog.askopenfilename(title='open')
    return filename
def open_img():
    global img
    x = openfn()
    img = Image.open(x)
    img.save("output.png")
    img = img.resize((400, 400), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.image = img
    panel.pack()

def encode():
    result = textExample.get(1.0, tkinter.END + "-1c")
    print(result)
    secret = lsb.hide('output.png', result)
    secret.save("output.png")


def savefile():
    image = Image.open('output.png')
    photo = ImageTk.PhotoImage(image)
    a = image.filename = filedialog.asksaveasfilename( title="Select file", filetypes = [("image", '*.png')])
    image.save(a)


w = ttk.Label(root, text="Steganography Encoder").pack()

btn = ttk.Button(root, text='open image', command=open_img).pack()

textExample=tkinter.Text(root, height=10,bg = "light cyan")
textExample.pack()

btn=ttk.Button(root, text="Encode", command=encode).pack()
button = ttk.Button(root, text="Save Image", command=savefile).pack()


root.mainloop()