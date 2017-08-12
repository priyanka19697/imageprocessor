from tkinter.filedialog import askopenfilename
from tkinter import Frame,Tk,Label,TOP,Button
from PIL import Image, ImageEnhance, ImageTk



def ask(event):
    directory = ""
    directory = askopenfilename()
    global im
    im = Image.open(directory)


def brighten(event):
    o = ImageEnhance.Brightness(im)
    im2 = ImageTk.PhotoImage(o.enhance(5))
    imglabel = Label(root,image= im2)
    imglabel.pack()
    root.pack()


def split(event):
   r, g, b = im.split()
   """a = Label(root,image=ImageTk.PhotoImage(r))
   a.pack()
   b=Label(root,image=ImageTk.PhotoImage(g))
   b.pack()
   c = Label(root,image=ImageTk.PhotoImage(b))
   c.pack()


def sharpen(event):
    o = ImageEnhance.Sharpness(im)
    o.enhance(7).show()


def contrast(event):
    o = ImageEnhance.Contrast(im)
    img = ImageTk.PhotoImage(o.enhance(3))
    imglabel= Label(root,image= img)
    imglabel.pack()
    root.pack()




def show(event):
    img = ImageTk.PhotoImage(Image.open("A:/mario.jpg"))
    imglabel = Label(root, image=img)
    imglabel.pack()
    root.pack()

root = Tk()
fr = Frame(root)
fr.pack()
b0 = Button(fr,text="choose image")
b0.bind("<Button-1>",ask)
b1 = Button(fr,text="brightness")
b1.bind("<Button-1>",brighten)
b2 = Button(fr,text="split")
b2.bind("<Button-1>",split)
b3 = Button(fr,text="sharpness")
b3.bind("<Button-1>",sharpen)
b4 = Button(fr,text="contrast")
b4.bind("<Button-1>",contrast)
b5 = Button(fr,text="show output image")
b5.bind("<Button-1>",show)
b0.pack(side=TOP);
b1.pack(side=TOP);
b2.pack(side=TOP);
b3.pack(side=TOP);
b4.pack(side=TOP);
b5.pack(side=TOP);
root.mainloop()

#nadantlo paste chesi try chesta agu 1 sec
