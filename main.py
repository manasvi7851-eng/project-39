from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
screen = Tk()
screen.title("Denomination counter")
screen.configure(bg="grey")
screen.geometry("650x400")
upload = Image.open("app_img.jpg")
upload = upload.resize((300,300))
image = ImageTk.PhotoImage(upload)
l = Label(screen,image = image,bg = "grey")
l.place(x = 180,y = 20)
l1 = Label(screen,text = "Hey user! Welcome to denomination counter application",bg = "grey")
l1.place(relx = 0.5,y = 340,anchor = CENTER)

def topwindow():
    top = Toplevel()
    top.title("Denomination calculator")
    top.configure(bg = "red") 
    top.geometry("600x600")
    l2 = Label(top,text = "Enter total amount",bg = "red")
    l2.place(x = 230,y = 50)
    e = Entry(top)
    e.place(x = 200,y = 80)
    def calculate():
        try:
            amount = int(e.get())
            note50 = amount//50
            amount%= 50
            note20 = amount//20
            amount%= 20
            note10 = amount//10
            amount%= 10
            note5 = amount//5
            e1.delete(0,END)
            e2.delete(0,END)
            e3.delete(0,END)
            e4.delete(0,END)
            e1.insert(END,str(note50))
            e2.insert(END,str(note20))
            e3.insert(END,str(note10))
            e4.insert(END,str(note5))
        except ValueError:
            messagebox.showerror("error","PLEASE ENTER THE VALID INPUT")
    b2 = Button(top,text = "Calculate",command = calculate)
    b2.place(x=240,y = 120)
    l3 = Label(top,text = "Here are number of notes for each denomination")
    l3.place(x = 140,y = 170)
    l4 = Label(top,text = "50",bg = "blue")
    l5 = Label(top,text = "20",bg = "blue")
    l6 = Label(top,text = "10",bg = "blue")
    l7 = Label(top,text = "5",bg = "blue")
    e1 = Entry(top)
    e2 = Entry(top)
    e3 = Entry(top)
    e4 = Entry(top)
    l4.place(x = 180,y = 200)
    l5.place(x = 180,y = 230)
    l6.place(x = 180,y = 260)
    l7.place(x = 180,y = 290)
    e1.place(x = 270,y = 200)
    e2.place(x = 270,y = 230)
    e3.place(x = 270,y = 260)
    e4.place(x = 270,y = 290)
    top.mainloop()
def message():
    box = messagebox.showinfo("Alert","Do you want to calculate the denominatioon count")
    if box == "ok":
        topwindow()
b1 = Button(screen, text = "Let's get started",bg = "yellow",fg = "white",command = message)
b1.place(x = 260,y = 360)
screen.mainloop()