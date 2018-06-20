from tkinter import *
from client import client_want_login
from client import forgotpassword
from functools import partial
#from db import fetchfromdb

class loginform:
        def __init__(self,username,password):
                self.username=username
                self.password=password
        '''
        def checklogin(self):
                fetchfromdb(self.username,self.password)
        '''


def loginfun(window):
        print ('log in button pressed')
        window.destroy()

        window=Tk()
        window.geometry('500x500')


        message=Label(text='welcome to log in  page ',  bg='blue' ,fg='white')
        labelfont = ('times', 20, 'bold')
        message.config(font=labelfont)
        message.config(height=3, width=100)
        message.pack()


        f=Frame(window)

        space = Frame(f)
        Label(f) . pack()
        space . pack()

        f0 = Frame( f )
        def callback(event):
            #window . destroy()
            newwin = Tk()
            newwin.geometry('600x600')
            mid = Entry( newwin )
            mid . pack ()
            action=partial( forgotpassword ,mid, newwin )
            okay = Button( newwin, text = 'Send Mail', command = action )
            okay . pack()

            newwin . mainloop()



        lbl = Label( f0, text=r"Forgot Password", fg="blue", cursor="hand2")
        lbl.pack()
        lbl.bind("<Button-1>", callback)
        f0 . pack()

        f1=Frame(f)
        Label(f1,text='Username ' ).pack(side=LEFT)
        e1=Entry(f1);e1.pack(side=RIGHT)
        f1.pack()

        space = Frame(f)
        Label(f) . pack()
        space . pack()

        f2=Frame(f)
        Label(f2,text='Password ' ).pack(side=LEFT)
        e2=Entry(f2); e2.pack(side=RIGHT)
        f2.pack()

        space = Frame(f)
        Label(f) . pack()
        space . pack()

        def checkfun():
                loginobj=loginform(e1.get(),e2.get())
                client_want_login( loginobj . __dict__, window  )
                #loginfunobj.checklogin()
                #window.destroy()

        f3 = Frame( f )
        Login= Button( f3, height = 1 , width =6 , activebackground = 'green', font=("Courier", 12 ), text = 'LOGIN', command=checkfun)
        Login. pack(side= LEFT)

        def cancelfun():
                window . destroy()

        Cancel=Button( f3, height=1 , width=6 , activebackground='red' , font=("Courier",12) , text='CANCEL', command = cancelfun )
        Cancel. pack(side = RIGHT)

        f3.pack()

        f.pack()

        window.mainloop()
