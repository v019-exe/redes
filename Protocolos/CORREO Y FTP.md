# APUNTES DE SISTEMAS OPERATIVOS EN RED

En estos apuntes trataremos el correo electrónico y el FTP, estos apuntes están hechos por v019.exe

## FTP

# Empezaremos definiendo FTP:

1. **¿Qué es FTP?**:
   - FTP es un protocolo de transferencia de archivos por red, creado en 1971. Este protocolo, como su nombre indica (File Transfer Protocol), sirve para transferir archivos por red. Los puertos del FTP son el 21 para control y el 22 para transferencias de archivos. Es un protocolo de capa 7 (APLICACIÓN) y usa TCP para las conexiones.

2. **MODOS FTP**:
   - **MODO ACTIVO**: 
     - El modo activo es una conexión directa al servidor. Básicamente, el servidor no se espera recibir una conexión directa de un cliente. El inconveniente principal del modo activo serán los cortafuegos a los que no les gusta que hagas conexiones directas con un servidor FTP.
   - **MODO PASIVO**: 
     - En el modo pasivo (también conocido como "modo PASV"), la conexión de datos se inicia desde el cliente hacia el servidor. Esto significa que el cliente solicita al servidor un puerto de datos para establecer la conexión, en lugar de que el servidor inicie la conexión directamente al cliente, como ocurre en el modo activo.
       - **FUNCIONAMIENTO PASV**:  
         1. Cliente solicita conexión: El cliente envía una solicitud al servidor FTP para iniciar una transferencia de archivos.
         2. Servidor asigna puerto de datos: En respuesta a la solicitud del cliente, el servidor asigna un puerto de datos disponible.
         3. Cliente se conecta al puerto de datos: Una vez que el servidor ha asignado un puerto de datos, el cliente establece una conexión de datos con ese puerto.
         4. Transferencia de archivos: Después de que se haya establecido la conexión de datos, la transferencia de archivos puede tener lugar entre el cliente y el servidor.
        
3. **Autenticación y seguridad**:
   - Se realiza mediante nombre de usuario y contraseña.
   - Opciones de seguridad incluyen FTPS (FTP sobre SSL/TLS) y SFTP (SSH File Transfer Protocol).

4. **Comandos FTP**:
   - Algunos comandos comunes incluyen LIST, GET, PUT, CD, MKDIR y DELETE.

# CORREO
1. **¿QUÉ ES UN CORREO ELECTRÓNICO?**: El correo electrónico es un sistema de comunicación digital que permite a los usuarios enviar mensajes de texto, archivos adjuntos y otros contenidos a destinatarios específicos a través de internet. SMTP es el protocolo estándar utilizado para enviar correos electrónicos desde un cliente de correo electrónico (como Outlook, Gmail o Thunderbird) a un servidor de correo electrónico.
2. **SMTP**:
   - **PUERTO 25**
   - **TEXTO PLANO**
   - **INSEGURO**
   - **SIMPLE MAIL TRANSFER PROTOCOL**
3. MTA, MDA, MUA:
   - **MTA**: MAIL TRANSFER AGENT (SERVIDOR SMTP)
   - **MDA**: MAIL DELIVERY AGENT (EL QUE ENTREGA EL MENSAJE CUANDO ESTÁ EN EL BUZÓN)
     1. POP3:
       a. Protocolo de Oficina Postal, este protocolo entrega el mensaje con la peculiaridad de que no guarda el mensaje en el servidor simplemente lo entrega y una vez que lo ha leído el destinatario se guarda en la carpeta local de correos
     3. IMAP:
        a. Protocolo de acceso a mensajes de Internet, este protocolo entrega el mensaje pero lo guarda en el servidor.
   - **MUA**: MAIL USER AGENT (THUNDERBIRD, OUTLOOK)


# SMTP Seguro (SMTPS)

El SMTP Seguro (SMTPS) es una extensión del Protocolo Simple de Transferencia de Correo (SMTP) que utiliza un nivel adicional de seguridad mediante el cifrado de la conexión entre el cliente de correo electrónico y el servidor SMTP. Este cifrado garantiza que los datos enviados durante la comunicación no puedan ser interceptados ni leídos por terceros.

## Funcionamiento

El funcionamiento del SMTPS es similar al del SMTP estándar, pero agrega una capa de seguridad mediante el uso de cifrado SSL/TLS (Secure Sockets Layer/Transport Layer Security). Cuando un cliente de correo electrónico se conecta a un servidor SMTP a través de SMTPS, se inicia una conexión segura utilizando SSL/TLS antes de que se intercambien los datos de autenticación y del mensaje.

## Ventajas del SMTPS

- **Confidencialidad**: El cifrado SSL/TLS asegura que la información enviada durante la comunicación, como nombres de usuario, contraseñas y contenido del mensaje, esté protegida contra posibles interceptaciones.
  
- **Integridad de los datos**: El cifrado SSL/TLS garantiza que los datos transmitidos entre el cliente y el servidor SMTP no sean modificados ni alterados durante la transferencia.

- **Autenticación del servidor**: El cliente puede verificar la autenticidad del servidor SMTP mediante la verificación del certificado SSL/TLS proporcionado por el servidor. Esto ayuda a prevenir ataques de suplantación de identidad.

## Configuración

La configuración del SMTPS en un cliente de correo electrónico generalmente requiere especificar el puerto SMTPS (generalmente el puerto 465) y activar la opción de cifrado SSL/TLS en la configuración de la cuenta de correo electrónico.


# Puerto 587 en el Contexto del Correo Electrónico

El puerto 587 es un puerto alternativo utilizado comúnmente para el envío de correos electrónicos de manera segura a través del Protocolo Simple de Transferencia de Correo (SMTP). A menudo se asocia con el envío de correos electrónicos autenticados utilizando STARTTLS, una extensión del protocolo SMTP que permite iniciar una conexión SMTP segura incluso en un puerto tradicionalmente no seguro.

## Uso de SMTP con STARTTLS en el Puerto 587

El puerto 587 es conocido como el puerto SMTP Submission y está designado específicamente para el envío de correos electrónicos de usuarios finales a servidores de correo electrónico. A diferencia del puerto SMTP estándar (puerto 25), que generalmente se utiliza para la comunicación entre servidores de correo electrónico, el puerto 587 está destinado a la comunicación entre clientes de correo electrónico (como Outlook, Thunderbird o aplicaciones móviles) y servidores de correo saliente (SMTP).

## Ventajas de Utilizar el Puerto 587

- **Seguridad Mejorada**: Al utilizar el puerto 587 con STARTTLS, se puede establecer una conexión segura entre el cliente de correo electrónico y el servidor SMTP, lo que protege los datos sensibles, como nombres de usuario, contraseñas y contenido del mensaje, contra posibles interceptaciones.

- **Compatibilidad con Cortafuegos**: Algunos proveedores de servicios de Internet bloquean el tráfico saliente en el puerto 25 para evitar el spam. El uso del puerto 587 suele ser una solución alternativa aceptada por la mayoría de los proveedores de servicios de Internet y cortafuegos.

- **Cumplimiento de Estándares**: El uso del puerto 587 para el envío de correos electrónicos cumple con las recomendaciones de seguridad y las mejores prácticas establecidas por organizaciones como el Grupo de Trabajo de Ingeniería de Internet (IETF).



