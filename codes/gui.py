from Tkinter import *
def close_window():
    app.destroy()
def show_entry_fields():
    f=open("P1",'rb')
    l=[]
    for row in f:
            l.append(row)
    date=e1.get()
    date = date.encode(encoding='UTF-8')
    f=0
    for i in range(len(l)):
            if date in l[i]:
                    doc=l[i+1]
                    f=1
                    break
    proper_set=[]
    if(f==1):
        movie_set=(doc.decode("UTF-8")).split("$")
        for movie in movie_set:
            movie=movie.split('#')
            movie[1]=movie[1].strip('\t').strip('\n')
            proper_set.append(movie)
        print ((" Movie Name{0:38} Rating{1} \n ").format("",""))
        for movie in proper_set:
                print (("{0:50} {1}").format(movie[0],movie[1]))
    else:
        print("Invalid Date Entered!!!")
        print ("Sorry Try Again Later...")  
    e1.delete(0,END)
    e2.delete(0,END)
def show_movie():
    f=open("P1",'rb')
    l=[]
    for row in f:
            l.append(row)
    date=e2.get()
    date = date.encode(encoding='UTF-8')
    f=0
    for i in range(len(l)):
            if date in l[i]:
                    doc=l[i]
                    f=1
                    break
    proper_set=[]
    if(f==1):
        movie_set=(doc.decode("UTF-8")).split("$")
        for movie in movie_set:
            movie=movie.split('#')
            movie[1]=movie[1].strip('\t').strip('\n')
            proper_set.append(movie)
        date = date.decode("UTF-8")
        print ((" Movie Name{0:38} Rating{1} \n ").format("",""))
        for movie in proper_set:
           if str(movie[0]) == str(date) :
                   print (("{0:50} {1}").format(movie[0],movie[1]))           
    else:
        print("SORRY No Information Available !!!")  
app =Tk()
v = IntVar()
app.title("Movie_Dekho!!!")
app.geometry("900x900")
app.resizable(500,500)
canvas = Canvas(app, width=900, height=900)
canvas.pack()
Radiobutton(app, 
            text="Python",
            padx = 20, 
            variable=v, 
            value=1).pack(anchor=W)
Radiobutton(app, 
            text="Perl",
            padx = 20, 
            variable=v, 
            value=2).pack(anchor=W)

img = PhotoImage(file="12345.gif")
canvas.create_image(400,400,image=img)

canvas.create_text(215, 40, font=("Monospace", 14), text= "Please Enter the date : ")
e1 = Entry(canvas,font=("Calibri",12),justify="center",width=30,bg="#1E6FBA",fg="yellow",disabledbackground="#1E6FBA",disabledforeground="yellow",highlightbackground="black",highlightcolor="red",highlightthickness=1,bd=0)
canvas.create_window(490,40,window=e1)
canvas.create_text(205, 70, font=("Monospace", 14), text= "Please Enter Movie Name : ")
e2 = Entry(canvas,font=("Calibri",12),justify="center",width=30,bg="#1E6FBA",fg="yellow",disabledbackground="#1E6FBA",disabledforeground="yellow",highlightbackground="black",highlightcolor="red",highlightthickness=1,bd=0)
canvas.create_window(490,70,window=e2)


e1.insert(20,"yyyy-mm-dd")
e2.insert(20,"Only Now_playing and Upcoming Movies")
quit_button=Button(canvas, text='New', command=close_window,anchor='w',width=10,activebackground ="#33B5E5")
quit_button_window = canvas.create_window(780,60,anchor='nw',window=quit_button)
show_button=Button(canvas, text='Upcoming', command=show_entry_fields,anchor='e',width=10,activebackground="#33B5E5")
show_button_window = canvas.create_window(890,30,anchor='ne',window=show_button)
show_button=Button(canvas, text='new_release', command=show_entry_fields,anchor='e',width=10,activebackground="#33B5E5")
show_button_window = canvas.create_window(785,60,anchor='ne',window=show_button)
show_button=Button(canvas, text='Upcom_rel', command=show_entry_fields,anchor='e',width=10,activebackground="#33B5E5")
show_button_window = canvas.create_window(785,30,anchor='ne',window=show_button)
show_button=Button(canvas, text='Quit', command=show_entry_fields,anchor='e',width=5,activebackground="#33B5E5")
show_button_window = canvas.create_window(810,90,anchor='ne',window=show_button)


app.mainloop()
