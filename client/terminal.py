import os
import wikipedia
from tkinter import *
from datetime import datetime
from threading import Thread
from clientfileop import savetoserver
from clientfileop import getfromserver

def donothing():
   filewin = Toplevel(mainwin)
   button = Button(filewin, text="Do nothing button")
   button.pack()


def editor():
    def searchfun ():
       search_reasult.delete('1.0', END)
       def threadsearchfun():
            search_reasultwiki = wikipedia.page( searchbox . get() )
            print(search_reasultwiki.url)
            print(search_reasultwiki.title)
            content = search_reasultwiki.content # Content of page.
            print ( u''.join(content).encode('utf-8').strip())
            print ( type( content ), '***********************')
            '''content = list( content )
            index = 0
            while index < len ( content ):
               if index % 40 == 0 :
                   content . insert( index , '\n')
               index +=1
            '''
            search_reasult . insert  ( END ,u''.join( content ).encode('utf-8').strip() )

       Thread ( target = threadsearchfun ) . start ()

    mainwin = Tk()
    #import tkMessageBox
    mainwin . geometry( '800x800')
    def showdatetime():
            while 1:
                    data = str(datetime.now())
                    labeldatetime . configure ( text =  data )


    frame1 = Frame( mainwin , width=300, height=800)
    frame11 = Frame( frame1 , width = 300, height = 100)
    spaceframe = Frame (frame11)
    space = Label( spaceframe , font = ( 'courier', 10))
    space . pack ()
    spaceframe. pack()
    searchframe= Frame( frame11)
    searchbox = Entry( searchframe )
    searchbox . pack( side = LEFT )

    searchbutton = Button( searchframe, text = 'Search', command = searchfun )
    searchbutton . pack ( side = RIGHT )

    searchframe.pack()
    spaceframe = Frame (frame11)
    space = Label( spaceframe , font = ( 'courier', 10))
    space . pack ( fill = BOTH , expand = YES )
    spaceframe. pack()
    frame11.pack()

    frame12 = Frame( frame1 , width = 300 , height = 700, background = 'white')

    frame12 .pack_propagate(False)

    search_reasult = Text( frame12 ,bg = 'white' )
    search_reasult .insert(END, 'default text')
    search_reasult . pack()

    frame12.pack()
    frame1 . pack( side = LEFT)

    frame2 = Frame(mainwin, width=500, height = 800)
    frame21=Frame(frame2,width=600,height=10)
    frame211 = Frame( frame21 , width = 600, height=1)

    def showdatetime():
    	while 1:
    		data = str(datetime.now())
    		labeldatetime . configure ( text =  data )

    labeldatetime  = Label( frame211 )
    labeldatetime . pack( fill = BOTH , expand = YES )

    Thread( target = showdatetime ) . start ()

    frame211 . pack( fill = BOTH, expand = YES )

    frame210=Frame(frame21, width = 300 , height =9)

    def savefun():
        print ( filename , type( filename ))
        print ( filename . get() )
        savetoserver( filename . get() , filetext . get('1.0', END) )
    Savebutton = Button(frame210, text="Save", command = savefun )
    Savebutton.pack(side=LEFT)

    filename = Entry(frame210, bd =5)
    filename.pack(side = LEFT)
    print ( filename , type( filename ))

    def getfun():
        print ( filename , type( filename ))
        print ( filename . get() )
        datafromserver = getfromserver( filename . get())
        filetext.delete('1.0', END)
        filetext . insert  ( END ,u''.join( datafromserver ).encode('utf-8').strip() )
    Getbutton=Button(frame210,text="Get", command = getfun)
    Getbutton.pack(side=LEFT)
    frame210.pack()
    frame21.pack(fill=BOTH,expand=YES)
    frame22=Frame(frame2,width=600,height=790, bg = 'white')

    filetext = Text( frame22, font = ('courior', 12 ))
    filetext . pack( fill = BOTH, expand = YES)
    frame22.pack(fill=BOTH, expand=YES)
    frame2 . pack( fill = BOTH, expand = YES )
    mainwin . mainloop ()
