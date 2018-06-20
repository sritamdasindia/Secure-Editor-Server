from tkinter import *
from functools import partial
from signup import signupfun
from login import loginfun

window=Tk()

window.geometry('600x600')
window.title('myapp')
message=Label(height=3, width=100, text='welcome to the new log in page', bg='blue', fg='white')

labelfont = ('times', 20, 'bold')
message.config(font=labelfont)
#message.config(height=3, width=100)

message.pack()

action=partial(signupfun ,window )
signup=Button(command=action ,height=5 , width=5 , text='SignUp', bg='blue', fg='white')
signup.pack()

action_login=partial(loginfun,window)
login=Button(command=action_login ,height=5 , width=5, text='LogIn' ,bg='blue', fg='white', activebackground='green')
login.pack()

window.mainloop()
