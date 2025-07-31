from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os
from stegano import lsb

win = Tk()
win.geometry("700x480")
win.config(bg="black")

#Buttons Functionality
def open_image():
    global open_file
    open_file = filedialog.askopenfilename(initialdir=os.getcwd(), title= "Select File Type", filetypes=(("PNG file", '*.png'),("JPG file", '*.jpg'), ("All file", '*.txt')))
    img = Image.open(open_file)
    img = img.resize((250, 220), Image.LANCZOS)  # Resize the image to fit the label
    img = ImageTk.PhotoImage(img)
    lf1.configure(image=img)
    lf1.image = img

def save_image():
    hide_msg.save("Secret File.png")
    messagebox.showinfo("Success", "Image Saved Successfully")

def hide_data():
    global hide_msg
    password = code.get()
    if password == "":
        messagebox.showerror("Error", "Please Enter Secret Key")
        return
    elif password != "1234":
        messagebox.showerror("Error", "Invalid Secret Key")
        code.set("")
        return
    else:
        msg = text1.get(1.0, END)
        hide_msg = lsb.hide(str(open_file), msg)
        messagebox.showinfo("Success", "Data Hidden Successfully, please Save the Image")
    msg = text1.get(1.0, END)
    hide_msg = lsb.hide(str(open_file), msg)

def show_data():
    password = code.get()
    if password == "":
        messagebox.showerror("Error", "Please Enter Secret Key")
        return
    elif password != "1234":
        messagebox.showerror("Error", "Invalid Secret Key")
        code.set("")
        return
    else:
        show_msg = lsb.reveal(open_file)
        text1.delete(1.0, END)
        text1.insert(END, show_msg)

#Logo
#logo = PhotoImage(file="logo.png")
#Label(win, image=logo, bd=0).place(x=190,y=0)

#Heading
Label(win, text="Secure Data Hiding in image using Steganography", font="arial 20 bold", bg="black", fg="white").place(x=15,y=21)

#Frame1
f1 = Frame(win, width=250, height=220, bg="purple")
f1.place(x=50, y=100)
lf1 = Label(f1, bg="purple")
lf1.place(x=0, y=0)

#Frame2
f2 = Frame(win, width=320, height=220, bg="white")
f2.place(x=330, y=100)
text1 = Text(f2, width=40, height=10, font="arial 11", wrap=WORD)
text1.place(x=0, y=0, width=310, height=210)

#Label for Secret Key
Label(win, text="Enter Secret Key", font="arial 11 bold", bg="black", fg="yellow").place(x=270,y=330)

#Entry widget for Secret Key
code = StringVar()
e = Entry(win,textvariable= code, bd = 2, font="arial 11", bg="white", fg="black", show="*")
e.place(x=245,y=360)

#Buttons
open_button = Button(win, text="Open Image", font="arial 11 bold", bg="blue", fg="white", cursor="hand2", command=open_image)
open_button.place(x=60, y=417)

save_button = Button(win, text="Save Image", font="arial 11 bold", bg="green", fg="white", cursor="hand2", command=save_image)
save_button.place(x=190, y=417)

hide_button = Button(win, text="Hide Data", font="arial 11 bold", bg="red", fg="white", cursor="hand2", command=hide_data)
hide_button.place(x=380, y=417)

show_button = Button(win, text="Show Data", font="arial 11 bold", bg="orange", fg="white", cursor="hand2", command=show_data)
show_button.place(x=510, y=417)

mainloop()