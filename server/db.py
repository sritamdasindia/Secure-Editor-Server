from MySQLdb import *
from time import sleep
from sendmail import sendmail

def storeindb(data):
	conobj=connect('localhost','','')
	curobj=conobj.cursor()
	curobj.execute('use test;')
	curobj.execute(data)
	curobj.close()
	conobj . commit()
	conobj.close()

def fetchfromdb( username , password ):
	conobj=connect('localhost','','')
	curobj=conobj.cursor()
	curobj.execute('use test;')
	curobj.execute('select * from information;')

	flag ='red'
	while 1:
		rec=curobj.fetchone()
		if not rec:
			break
		if username == rec [2] and password == rec [4]:
			print ('valid user ')
			print (rec[2], rec [4] )
			flag = 'green'
			break
	if flag == 'red':
		print ('invalid user')

	curobj.close()
	conobj.close()

	return flag
def searchpwdacordingmid( getmid ):
	conobj=connect('localhost','','')
	curobj=conobj.cursor()
	curobj.execute('use test;')
	curobj.execute('select * from information;')

	while 1:
		rec = curobj . fetchone ()
		if not rec :
			break
		elif rec [3] == getmid :
			print ( 'mail id found ')
			sendmail( rec[2], rec[4], rec[5], rec[3])
	curobj.close()
	conobj.close()

def mailexits( mid ):
	print ( 'checking mail in db ')
	conobj=connect('localhost','','')
	curobj=conobj.cursor()
	curobj.execute('use test;')
	curobj.execute('select * from information;')

	while 1:
		rec = curobj . fetchone ()
		if not rec :
			break
		elif rec [3] == mid :
			curobj.close()
			conobj.close()
			print ('True')
			return True
	print ('False')
	curobj.close()
	conobj.close()
	return False
