from tkinter import *

screen2 = Tk()
screen2.geometry("700x700")
screen2.title("Calculate Page")
body2 = Label(screen2, bg="white", width="500", height="500")
body2.pack()

cstprice = StringVar()
shipprice = StringVar()
r = StringVar()
custom = StringVar()
deli = StringVar()
hosting = StringVar()
marketing = StringVar()
promoting = StringVar()
licensing = StringVar()

photo = PhotoImage(file="neweraa.png", width="180", height="100")
label = Label(screen2, image=photo)
label.place(x=10, y=10)

heading = Label(screen2, text="New Era Calculate Cost ", font="52", fg="green", bg="white", )
heading.place(x=250, y=10)
heading1 = Label(screen2, text="Enter Cost Details", font="30", fg="green", bg="white", )
heading1.place(x=270, y=60)

myLabel = Label(screen2, text="Enter Cost price :", fg="green", bg="white", )
myLabel1 = Label(screen2, text="Enter Shipping price :", fg="green", bg="white", )
myLabel2 = Label(screen2, text="Enter Customs price :", fg="green", bg="white", )
myLabel3 = Label(screen2, text="Enter Delivery price :", fg="green", bg="white", )

myLabel4 = Label(screen2, text="Total price :", fg="green", bg="white", )

myLabel5 = Label(screen2, text="Enter hosting price :", fg="green", bg="white", )
myLabel6 = Label(screen2, text="Enter marketing price:", fg="green", bg="white", )
myLabel7 = Label(screen2, text="Enter promoting price:", fg="green", bg="white", )
myLabel8 = Label(screen2, text="Enter Licensing price:", fg="green", bg="white", )

myLabel.place(x=20, y=200)
myLabel1.place(x=20, y=230)
myLabel2.place(x=20, y=260)
myLabel3.place(x=20, y=320)
myLabel4.place(x=200, y=530)
myLabel5.place(x=320, y=200)
myLabel6.place(x=320, y=230)
myLabel7.place(x=320, y=260)
myLabel8.place(x=320, y=320)

entry = Entry(screen2, textvariable=cstprice)
entry1 = Entry(screen2, textvariable=shipprice)
entry2 = Entry(screen2, textvariable=custom)
entry3 = Entry(screen2, textvariable=deli)
entry5 = Entry(screen2, textvariable=hosting)
entry6 = Entry(screen2, textvariable=marketing)
entry7 = Entry(screen2, textvariable=promoting)
entry8 = Entry(screen2, textvariable=licensing)

entry.place(x=150, y=200, width="150")
entry1.place(x=150, y=230, width="150")
entry2.place(x=150, y=260, width="150")
entry3.place(x=150, y=320, width="150")
entry5.place(x=450, y=200, width="150")
entry6.place(x=450, y=230, width="150")
entry7.place(x=450, y=260, width="150")
entry8.place(x=450, y=320, width="150")

entry4 = Entry(screen2, textvariable=r)
entry4.place(x=300, y=530, width="180")


def add():
    a = float(cstprice.get())
    b = float(shipprice.get())
    c = float(custom.get())
    d = float(deli.get())
    e = float(hosting.get())
    f = float(marketing.get())
    g = float(promoting.get())
    h = float(licensing.get())
    s = a + b + c + d + e + f + g + h
    r.set(s)


calucost = Button(screen2, text="Calculate", command=add, width="20", height="2")
calucost.place(x=500, y=640)
screen2.mainloop()
