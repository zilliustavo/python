import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import requests

response = requests.get("https://api.github.com/users/gabriel")
data = response.json()

fromaddr = ""
toaddr = ""

#instancia do MIMEMultipart
msg = MIMEMultipart()

msg['From'] = fromaddr

msg['To'] = toaddr

msg['Subject'] = "E-mail de Teste"

body  = """E-mail enviado do nosso robo"""


msg.attach(MIMEText(body, 'plain'))

#Anexo
filename = "panfleto.pdf"
anexo = open("panfleto.fpd", "rb")

p = MIMEBase('application', 'octet-stream')

p.set_payload((anexo).read())

#Encode em base 64
encoders.encode_base64(p)

p.add_header('Content-Disposition', "attachment; filename- %s" % filename)

msg.attach(p)

#serviuor smpt 
s = smtplib.SMTP('smtp.gmail.com', 587)

#segurança
s.starttls()

s.login(fromaddr, 'minhasenhaesecreta')

text = msg.as_string()

s.sendmail(fromaddr, toaddr, text)

s.quit()
