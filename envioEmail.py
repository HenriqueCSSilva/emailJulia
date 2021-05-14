from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import mimetypes
import os
import smtplib
import config as cf

meu_email = ('chewbaccanoesquilo@gmail.com')
senha = ('oaufutzibwdwgatf')
email_destino = ('marcos_henrique@outlook.com')

msg = MIMEMultipart()

msg['from'] = meu_email
msg['to'] = email_destino
msg['subject'] = 'Entrega TCC.'



corpo = MIMEText(cf.msgDoEmail)
msg.attach(corpo)
pastaEnvio = os.getcwd() + '/ArquivosParaEnvio'
fileName = 'ArquivosParaEnvio/teste.docx'
attachment = open(fileName,'rb')

#http//www.freeformater
mimetypeAnexo = mimetypes.guess_type(fileName)[0].split('/')
part = MIMEBase(mimetypeAnexo[0],mimetypeAnexo[1])

part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', f'attachment; filename={fileName}')

msg.attach(part)


server =  smtplib.SMTP(host='smtp.gmail.com', port=587)
server.ehlo()
server.starttls()
server.login(meu_email, senha)
text = msg.as_string()
server.sendmail(meu_email,email_destino,text    )
print(text)
server.quit()

