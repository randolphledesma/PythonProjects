import smtplib
import email.utils
import time
import datetime

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

msg = MIMEMultipart('alternative')
msg['Subject'] = "TEST ONLY " + st
msg['From'] = email.utils.formataddr(('Author', 'author@example.com'))
msg['To'] = email.utils.formataddr(('Recipient', 'recipient@example.com'))
msg['Cc'] = email.utils.formataddr(('Recipient', 'test@example.com'))
msg['Bcc'] = email.utils.formataddr(('Recipient', 'test@example.com'))
msg['X-Mailer'] = "test"

text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
html = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       How are you?<br>
       Here is the <a href="http://www.python.org">link</a> you wanted.
    </p>
  </body>
</html>
"""

part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

msg.attach(part1)
msg.attach(part2)

#server = smtplib.SMTP('192.168.99.100', 1025)
server = smtplib.SMTP('127.0.0.1', 8025)
server.set_debuglevel(True)  # show communication with the server
try:
    server.sendmail('author@example.com',
                    ['recipient@example.com'],
                    msg.as_string())
finally:
    server.quit()