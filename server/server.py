from time import sleep
from socket import *
from multiprocessing import Process
from db import storeindb
from db import fetchfromdb
from db import searchpwdacordingmid
from db import mailexits
from sendmail import sendmail

def main():
    sobj=socket(AF_INET,SOCK_STREAM,IPPROTO_TCP)
    ipaddr='192.168.43.57'
    port=2000
    addr=(ipaddr,port)
    sobj.bind(addr)
    sobj.listen(1)

    while 1:
        cobj,caddr=sobj.accept()
        def operation() :

            print (caddr)
            clientwork = cobj . recv( 100000 )
            print (clientwork)

            if b'signup' in clientwork :
                print ('client wants signup')
                print ( clientwork )
                data = eval ( clientwork . decode () . replace( 'signup', ''))
                print (data)

                if mailexits( data ['mailid']):
                    cobj . send (  b'not okay' )
                else:
                    insert_data='insert into information values ("' \
        + data['firstname'] +'","'+ data ['lastname'] +'","'+ data['username'] +'","'+ data['mailid'] +'","'+ data['password'] +'","'+ data['gender'] +'");'
                    print (insert_data)
                    storeindb( insert_data)
                    sendmail( data ['username'] , data['password'], data['gender'], data['mailid']   )
                    cobj . send( b'okay' )
                cobj.close()

            elif b'login' in clientwork:
                print ('client wants login')
                print (clientwork )
                data = eval ( clientwork . decode () . replace( 'login', ''))
                print (data)
                status = fetchfromdb( data [ 'username'],data['password'])
                cobj . send( status . encode()  )
                #fetchfromdb()

                cobj.close()
            elif b'forgotpassword' in clientwork:
                getdata = clientwork . decode() . replace('forgotpassword','')

                searchpwdacordingmid( getdata )

            elif b'save' in clientwork:
                print ( 'server saving the file')
                print (clientwork )
                data = eval ( clientwork . decode () . replace( 'save', ''))
                print (data)
                filename = data['filename']
                filetext = data['filetext']
                fileobj = open( filename , 'w')
                fileobj . write( filetext )
                fileobj . close()

            elif b'get' in clientwork:
                print('server sending the file')
                print (clientwork )
                data = eval ( clientwork . decode () . replace( 'get', ''))
                print (data)
                filename = data['filename']
                fileobj = open( filename , 'r')
                filetext = fileobj . read( )
                fileobj . close()
                cobj . send( filetext . encode () )


        #child = Process ( target = operation )
        operation()

    #sleep(1)
    sobj.close()
main()
