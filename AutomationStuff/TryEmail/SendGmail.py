
import smtplib


sender = 'abhidipu863@gmail.com'
receiver = 'akuma294@asu.edu'

message = 'heelo, this is ABhinav 2'

# server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
# server.login(sender , 'pagal@nitk')
try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(sender , 'pagal@nitk')
    # server.login(sender , 'wyqdnvhesxepxijx')
    print('Credentials done')
    server.sendmail(sender , receiver , message)
except smtplib.SMTPException:
    print('Error : unable to send mail')
    server.quit()

# server.quit()


