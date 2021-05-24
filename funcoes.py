import pandas as pd
import shutil
import os.path
from pathlib import Path
#from glob import glob
from os import listdir
from os.path import isfile, join
# Bibliotecas P/ Email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import mimetypes
from datetime import datetime
import smtplib
import config as cf




hoje = datetime.today().strftime('%d-%m-%y_%H-%M-%S')
pastaClientes = r"C:\GITHUB\SATEL\emailJulia\ExcelBase"
pastaIds = r"C:\GITHUB\SATEL\emailJulia\ArquivosParaEnvio"

onlyfiles = [f for f in listdir(pastaClientes) if isfile(join(pastaClientes, f)) and "~$" not in f]
docs = [f for f in listdir(pastaIds) if isfile(join(pastaIds, f)) and "~$" not in f]

dataFrames = [ pd.read_excel(pastaClientes + "/" + x) for x in onlyfiles]

todos = df1 = pd.DataFrame()
for df in dataFrames:
    todos = pd.concat([todos,df], ignore_index=True)

for doc in docs:
    os.chdir('ArquivosParaEnvio/')
    #form = doc
    idCliente = doc.split(".docx")[0]
    row = todos.loc[todos['id_cliente'].str.contains(idCliente)]

    if len(row):
        email = row["email"].values[0]
        ###----MeuCodigo----####
        print('Enviando: ' + doc + '...Aguarde...')
        email_destino = email
        msg = MIMEMultipart()
        msg['from'] = cf.meu_email
        msg['to'] = email_destino
        msg['subject'] = 'Entrega TCC.'

        corpo = MIMEText(cf.msgDoEmail)
        msg.attach(corpo)
        pastaEnvio = os.getcwd() + '/ArquivosParaEnvio'
        fileName = doc
        attachment = open(fileName, 'rb')
        # http//www.freeformater
        mimetypeAnexo = mimetypes.guess_type(fileName)[0].split('/')
        part = MIMEBase(mimetypeAnexo[0], mimetypeAnexo[1])

        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename={fileName}')

        msg.attach(part)
        server = smtplib.SMTP(host='smtp.gmail.com', port=587)
        server.ehlo()
        server.starttls()
        server.login(cf.meu_email, cf.senha)
        text = msg.as_string()
        server.sendmail(cf.meu_email, email_destino, text)
        print('Enviado com sucesso: ' + doc + '\n')
        attachment.close()

        Path(f'../Enviados/{hoje}').mkdir(parents=True, exist_ok=True)
        shutil.move(doc,f'../Enviados/{hoje}')
        server.quit()
        #--------------------------------------------------------------------#
        #ENVIA O EMAIL

    else:
        print("nao achou o cliente")
        print('Falha em: ' + doc)
    os.chdir('../')




