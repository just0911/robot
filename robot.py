from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import requests
import smtplib
import os
from pyquery import PyQuery as pq

doc = requests.get("http://www.jxfnet.com/zh-cn/promotion/kingmeal_index.php")
doc = doc.content
doc = pq(doc)
tt = (doc.find('.kingmeal_text3')).text()
if os.path.exists('kingmeal.txt'):
    with open('./kingmeal.txt', 'r') as f:
        ttt = f.read()
        if tt == ttt:
            exit()

if(len(tt) > 0):
    with open('./kingmeal.txt', 'w') as f:
        f.write(tt)
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


from_addr = ''
password = ''
to_addr = ''
smtp_server = 'smtp.163.com'

msg = MIMEText(tt, 'plain', 'utf-8')
msg['From'] = _format_addr(from_addr)
msg['To'] = _format_addr(to_addr)
msg['Subject'] = Header('准备……', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
