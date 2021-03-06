
import smtplib

import config

#this is the send email function 

def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail( config.EMAIL_ADDRESS,config.SEND_EMAIL, message)
        server.quit()
        print("Success: Email sent!")
    except:
        print("Email failed to send.")



#Test Area
#subject = "Test subject"
#msg = "Hello there, how are you today?"

#send_email(subject, msg)
