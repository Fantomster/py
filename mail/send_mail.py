import smtplib
from email.mime.text import MIMEText

msg = MIMEText("The body of the email is here")

msg['Subject'] = "An Email Alert"
msg['From'] = "ryan@test.com"
msg['To'] = "webmaster@test.com"

s = smtplib.SMTP('localhost')
s.send(msg)
s.quit()