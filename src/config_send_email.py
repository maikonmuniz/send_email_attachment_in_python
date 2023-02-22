import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
 
 
host  = "smtp.gmail.com"
port  = "587"
login = ""
senha = ""

server = smtplib.SMTP(host, port)

server.ehlo()
server.starttls()
server.login(login, senha)

corpo_email = "<p>Envio de email pithon</p>"
messagem_email = MIMEMultipart()

messagem_email["From"] = login
messagem_email["To"] = "email direcionado"
messagem_email["Subject"] = "Testando"
messagem_email.attach(MIMEText(corpo_email, "html"))

# caminho arquivo arquivo para ser anexado
arquivo = r""

anexo_banario = open(arquivo, 'rb')
anexo         = MIMEBase('application', 'octet-stream')
anexo.set_payload(anexo_banario.read())
encoders.encode_base64(anexo)

anexo.add_header('Content-Disposition', f'attachment; filename=teste.xlsx')
anexo_banario.close()
messagem_email.attach(anexo)

server.sendmail(messagem_email["From"], messagem_email["To"], messagem_email.as_string())

server.quit()
