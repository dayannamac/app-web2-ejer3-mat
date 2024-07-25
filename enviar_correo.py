import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configuración del servidor SMTP y las credenciales
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_user = 'dayannamacay6@gmail.com'
smtp_password = 'gpqp xyjw ptlf ljzo'

# Configuración del correo electrónico
de = 'dayannamacay6@gmail.com'
para = 'pruebasenviopython@yopmail.com'
asunto = 'Notificación'
cuerpo = 'Esta es una prueba de envio con python.'

# Crear el objeto del mensaje
mensaje = MIMEMultipart()
mensaje['From'] = de
mensaje['To'] = para
mensaje['Subject'] = asunto

# Adjuntar el cuerpo del mensaje
mensaje.attach(MIMEText(cuerpo, 'plain'))

try:
    # Conectarse al servidor SMTP
    servidor = smtplib.SMTP(smtp_server, smtp_port)
    servidor.starttls()  # Iniciar el modo TLS
    servidor.login(smtp_user, smtp_password)  # Iniciar sesión
    texto = mensaje.as_string()
    servidor.sendmail(de, para, texto)  # Enviar el correo
    servidor.quit()  # Cerrar la conexión
    print("Correo enviado exitosamente")
except Exception as e:
    print(f"Error al enviar el correo: {e}")
