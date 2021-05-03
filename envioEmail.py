from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

meu_email = ('chewbaccanoesquilo@gmail.com')
senha = ('oaufutzibwdwgatf')

email_destino = ('marcos_henrique@outlook.com')
corpo_msg = ('Este é um corpo de email')

msg = MIMEMultipart()
msg['from'] = meu_email
msg['to'] = email_destino
msg['subject'] = 'Assunto.'

#chewbaccanoesquilo@gmail.com
#JavaScript123

corpo = MIMEText('Texto Corpo do Email - esse é um conteudo')
msg.attach(corpo)
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    try:
        print('Ate aqui foi')
        smtp.ehlo()
        smtp.starttls()
        smtp.login(meu_email, senha)
        smtp.send_message(msg)
        print('E-mail enviado com sucesso.')
    except Exception as e:
        print('E-mail não enviado...')
        print('Erro:', e)


        #smtp.office365.com