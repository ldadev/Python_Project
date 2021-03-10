import smtplib
import email.utils
from email.mime.text import MIMEText

mailServer = smtplib.SMTP('smtp.gmail.com',587)
mailServer.ehlo()
mailServer.starttls()
mailServer.ehlo()
mailServer.login("ldavidme7@gmail.com","****")
print (mailServer.ehlo())

# Construimos el mensaje simple
mensaje = MIMEText("""Este es el mensaje
de las narices""")
mensaje['From']="ldavidme7@gmail.com"
mensaje['To']="ldavidme7@gmail.com"
mensaje['Subject']=str(lista)

# Envio del mensaje
mailServer.sendmail("ldavidme7@gmail.com",
                "ldavidme7@gmail.com",
                mensaje.as_string())
