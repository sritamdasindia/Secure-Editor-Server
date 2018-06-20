
from tkinter import *
#from os import fork
#from thread import start_new_thread
from threading import Thread
#from db import storeindb
from client import client_want_signup


class signupform:

	def __init__( self , firstname , lastname , username , mailid , password , gender ):

		self . firstname = firstname
		self . lastname = lastname
		self . username=username
		self . mailid = mailid
		self . password = password
		self . gender = gender

		#print self . __dict__
'''
	def store(self):
		data='insert into information values ("' \
+ self.firstname +'","'+ self.lastname +'","'+ self.username +'","'+ self.mailid +'","'+ self.password +'","'+ self.gender +'");'
		print (data)
		sendtoserver(data)
		#storeindb(data)

		sendmail( self . username , self . password, self . gender, self . mailid   )
'''

def signupfun(window):


        print ('signup button is pressed ')
        window.destroy()

        window=Tk( )
        window.title('myapp')
        window.geometry('600x600')

        message=Label(text='welcome to sign up page ',  bg='blue' ,fg='white')
        labelfont = ('times', 20, 'bold')
        message.config(font=labelfont)
        message.config(height=3, width=100)
        message.pack()

        f=Frame(window)

        space = Frame(f)
        Label(f).pack()
        space . pack()

        f1=Frame(f)
        Label(f1,text='First name		' ).pack(side=LEFT)
        e1=Entry(f1);e1.pack(side=RIGHT)
        f1.pack()

        space = Frame(f)
        Label(f).pack()
        space . pack()

        f2=Frame(f)
        Label(f2,text='Last name		').pack(side=LEFT)
        e2=Entry(f2); e2.pack(side=RIGHT)
        f2.pack()

        space = Frame(f)
        Label(f).pack()
        space . pack()

        f2below=Frame(f)
        Label(f2below,text='Username		').pack(side=LEFT)
        e3u=Entry(f2below);e3u.pack(side=RIGHT)
        f2below.pack()

        space = Frame(f)
        Label(f).pack()
        space . pack()

        f3=Frame(f)
        Label(f3,text='Emailid			' ).pack(side=LEFT)
        e3=Entry(f3);e3.pack(side=RIGHT)
        f3.pack()

        space = Frame(f)
        Label(f).pack()
        space . pack()

        f4=Frame(f)
        Label(f4,text='Password		' ).pack(side=LEFT)
        e4=Entry(f4);e4.pack(side=RIGHT)
        f4.pack()

        space = Frame(f)
        Label(f).pack()
        space . pack()

        f5 = Frame( f )
        Label( f5 , text="Confirm password	") . pack(side = LEFT  )
        e5 = Entry(f5); e5 . pack( side = LEFT )
        f5 . pack()

        f5below = Frame(f)
        l5 = Label( f5below, text = 'Please Provide the same passowrd as above ', fg = 'red') ; l5 .  pack( side = RIGHT)
        f5below . pack()

        space = Frame(f)
        Label(f).pack()
        space . pack()

        f6 = Frame( f )
        Label( f6 , text=" Gender") . pack(side = LEFT  )
        v = StringVar()
        Radiobutton(f6,
              text="Male",
              padx = 20,
              variable=v,
              value= 'Male').pack( side = RIGHT )
        Radiobutton(f6,
              text="Female",
              padx = 20,
              variable=v,
              value= 'Female').pack(side = RIGHT )
        f6 . pack()

        space = Frame(f)
        Label(f).pack()
        space . pack()

        f7 = Frame( f )
        def exitfun():
                window . destroy ()

        exit = Button( f7, height = 1 , width =3 , activebackground = 'red', font=("Courier", 12 ), text = 'EXIT', command = exitfun  )
        exit . pack( side = LEFT)

        def okayfun():
                print (e1 . get() , e2 . get() , e3u. get() , e3 . get() , e4 . get() , e5 . get() , v . get() )
                signupobj = signupform( e1 . get() , e2 . get() , e3u.get() , e3 . get() , e4 . get() , v . get() )
                #signupobj.store()
                print ( signupobj . __dict__ )
                client_want_signup( signupobj . __dict__ )
                window . destroy()

        def placeokay():
                while 1:
                        #print 'i am child working for okay buton and checking the length of every entry', type (e1), e1 . get () , type( e1 . get() )
                        if  e1 . get() and e2. get() and e3u.get() and e3 . get() and e4.get() and e5.get() and v . get() :
                                if e4 . get() != e5 . get() :
                                        msg = 'password mis match, please check the confirm password'
                                        l5.configure(text= msg )
                                else:
                                        okay = Button( f7, height = 1 , width = 3 , activebackground = 'green', font=("Courier", 12 ), text = 'OKAY', command = okayfun )
                                        okay . pack( side = RIGHT)
                                        f5below . pack_forget()
                                        break
        Thread ( target = placeokay  ). start ()
        f7 . pack()

        f.pack()
        window.mainloop()
