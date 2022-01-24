import datetime as dt
import time
import smtplib


sender = 'abhidipu863@gmail.com'
receiver = 'akuma294@asu.edu'


def send_email(message):
    # email_user = 'myemail@gmail.com'
    # server = smtplib.SMTP ('smtp.gmail.com', 587)
    # server.starttls()
    # server.login(email_user, 'email pass')
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(sender , 'pagal@nitk')
        server.sendmail(sender, receiver, message)
    #EMAIL
    # message = 'sending this from python!'
    # server.sendmail(email_user, email_user, message)
        server.quit()
    except smtplib.SMTPException:
        print('Message Sending Failed')

send_time = dt.datetime(2021,12,17,2,58,0) # set your sending time in UTC
print(str(send_time))
time.sleep(send_time.timestamp() - time.time())
message = 'heelo, this is ABhinav auto' + str(send_time)
send_email(message)
print('email sent')