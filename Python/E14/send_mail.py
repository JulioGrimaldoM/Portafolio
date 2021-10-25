import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import getpass

sender_email = input("Cuenta> ")
password=getpass.getpass("Pasword>")
receiver_email = input("Cuenta Destino> ")
subject = input("Asunto> ")
mess = input("Mensaje> ")
name=input("Tu nombre> ")
body=mess+"\n"+name

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message["Bcc"] = receiver_email  
message.attach(MIMEText(body, "plain"))

filename = input("direccion de la imagen> ")
namearch=input("nombre del archivo> ")


with open(filename, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

encoders.encode_base64(part)
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {namearch}",
)


message.attach(part)
text = message.as_string()

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)
