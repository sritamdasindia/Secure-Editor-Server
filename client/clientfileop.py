
from socket import *

def savetoserver( filename , filetext ):

    sid= socket( AF_INET, SOCK_STREAM, IPPROTO_TCP )

    sid. connect( ('192.168.43.57', 2000))

    dict = {'filename' : filename , 'filetext' : filetext}
    sid . send( b'save' + str ( dict ) . encode () )
    #sid . send( filename . encode () )
    #sid . send( filetext . encode() )

    sid . close()

def getfromserver( filename ):
    sid= socket( AF_INET, SOCK_STREAM, IPPROTO_TCP )
    sid. connect( ('192.168.43.57', 2000))
    dict={'filename':filename}
    sid . send(b'get' + str(dict).encode())
    #sid . send( filename. encode ()  )
    filetext = sid . recv ( 100000 )
    sid . close()
    return filetext . decode ()
