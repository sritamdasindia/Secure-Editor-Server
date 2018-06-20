from socket import *
from terminal import editor
from tkinter import messagebox
def connecttoserver():

    sobj = socket( AF_INET, SOCK_STREAM, IPPROTO_TCP )

    sobj . connect( ('192.168.43.57', 2000))

    return sobj

def client_want_signup( dataindict ):

    obj = connecttoserver()

    print ( str ( dataindict )  . encode())
    data = b'signup' + str ( dataindict ) . encode ( )

    obj . send ( data )
    status = obj . recv( 10 )
    if status == b'okay':
        print ('signup successfull')

        messagebox.showinfo("Success", "SIGNUP SUCCESSFULLY :) ")

    else:
        print ('mail id is exists previously ')
        messagebox.showinfo("Failure", "SIGNUP failure :( ")
    obj . close()

def client_want_login( dataindict, window  ):

    obj = connecttoserver()

    print ( str ( dataindict )  . encode())
    data = b'login' + str ( dataindict ) . encode ( )

    obj . send ( data )
    status = obj . recv(10) . decode()
    if status == 'red':
        print ( 'you are invalid user ')
    else:
        print ('you are valid user , welcome you .... ')
        window . destroy()
        editor()
    obj . close()

def forgotpassword( mid, newwin ):

    obj=connecttoserver()

    getvalue= mid .get().encode()
    newwin . destroy()
    obj.send(b'forgotpassword' + getvalue)
    obj.close()
