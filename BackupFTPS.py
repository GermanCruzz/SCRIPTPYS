#SCRIPT COPIAS DE SEGURIDAD DE ALONSO Y GERMÁN
import os
import shutil
import shutil
import ftplib
import datetime
from datetime import date
import sys

#Se necesitarán 8 argumentos.
if len(sys.argv) != 8:
    print ("Sintaxis: Se deberá introducir: <usuario_sistema> <carpeta_sistema> <ip_servidor> <usuario_ftp> <clave_usuario_ftp> <directorio_ftp_usuario> <correo_de_destino>")
    sys.exit(1)
else:
	#Fecha del archivo. <dia><mes><año>.zip
	today=date.today()
	dia = today.day #Sacar dia
	mes= today.month #Sacar mes
	año = today.year #Sacar año
	usuariosistema = sys.argv[1]
	carpeta_public = sys.argv[2] #Carpeta del sistema la cuál se le hará el backup
	nombre_archivo = f"backup{dia}{mes}{año}.zip" #Nombre que tendrá el .zip. Ejemplo: <<backup29012023.zip>>
	format = "zip"
	shutil.make_archive(nombre_archivo, format, sys.argv[2])
	
	#------- Enviar a servidor FTP -----------
	#Datos FTP
	ftp_servidor =  sys.argv[3] #IP del servidor
	ftp_usuario  =  sys.argv[4] #Usuario virtual/local del ftp
	ftp_clave    = 	sys.argv[5] #Clave del usuario virtual/local
	ftp_raiz     = 	sys.argv[6] #Directorio del usuario virtual/local donde queremos subir el fichero

	# Datos del fichero a subir
	fichero_origen = f'/home/{usuariosistema}/{nombre_archivo}' #Ruta del archivo.
	fichero_destino = nombre_archivo #Nombre del archivo a subir

	# Conectamos con el servidor FTPS con SSL.
	ftps = ftplib.FTP_TLS()
	ftps.connect(ftp_servidor)		#Conectarse al servidor
	ftps.login(ftp_usuario,ftp_clave)	#Login
	ftps.prot_p()				#Activar Conexión segura con SSL
	f = open(fichero_origen,'rb')		#Abrir fichero
	ftps.cwd(ftp_raiz)
	ftps.storbinary('STOR ' + fichero_destino, f) #Subir fichero
	f.close()
	#--- Maximo 10 copias. Se borra la más antigua ---
	listassl=ftps.nlst()		 	#Lista de archivos del directorio del usuario ftp
	while len(listassl) > 10:
		ftps.delete(listassl[0])	#Eliminar el más antiguo 1en el directorio si hay mas de 10. 	
		del listassl[0]			#Eliminar elemento de la lista
	ftps.quit()
	print ("Se subió correctamente la copia al servidor FTP.")
	print ("Habrá un máximo de 10 copias en el servidor. Se borrará la más antigua si se supera el límite")
	# Eliminar la copia en el sistema cuando se sube al servidor.
	os.remove(nombre_archivo)
	print ("Para ahorrar espacio en el sistema del usuario, se borrará la copia .zip del directorio: /home/{}".format(usuariosistema))
	#Envío de correo
	from email.message import EmailMessage
	import smtplib
	remitente = "gpena166@ieszaidinvergeles.org"
	destinatario = sys.argv[7] #Correo de destino
	mensaje = "El script de copia de seguridad se ejecutó correctamente"
	email = EmailMessage()
	email["From"] = remitente	#Envío del correo, utilizando el remitente y destinatario
	email["To"] = destinatario
	email["Subject"] = "Copia de seguridad"  #Asunto del correo
	email.set_content(mensaje)
	smtp = smtplib.SMTP_SSL("smtp.gmail.com")			#Utilizar protocolo SMTP seguro.
	smtp.login(remitente, "npahaejqwodcvxhw")			#Contraseña para la aplicación Python para que pueda enviar correos a través de SMTP con gmail.
	smtp.sendmail(remitente, destinatario, email.as_string())
	smtp.quit()
	print ("El correo de confirmación de ejecución éxitosa fue enviado correctamente a su destinatario")
