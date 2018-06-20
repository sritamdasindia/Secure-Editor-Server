import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendmail( username , password, gender , recvmailid ) :
	

        sender = 'sritamk.das@gmail.com'
        receivers = [recvmailid ]

        msg = MIMEMultipart()       # create a message

        # add in the actual person name to the message template
        #message = message_template.substitute(PERSON_NAME=name.title())

        # setup the parameters of the message
        msg['From']= 'sritamk.das@gmail.com'
        msg['To']= recvmailid 
        msg['Subject']="WELCOM TO MY PROJECT "
        if gender == 'Male':
                message = "hello sir," + username + ' your password is : ' + password
        else:
                message = "hello mam ," + username + ' your password is : ' + password

       # add in the message body
        msg.attach(MIMEText(message, 'plain'))


        
        
        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpObj.starttls()
        smtpObj.login('sritamk.das@gmail.com', 'litindia')
        print ( msg , type( msg ))
        smtpObj.sendmail(sender, receivers, str ( msg ) )
        print ("Successfully sent email")

#sendmail( 'sritamdas', 'litindia', 'Male', 'sritamk.lit@gmail.com')
        

