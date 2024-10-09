
1. **Protocolo de Capa de Aplicación:** HTTP opera en la capa de aplicación del modelo OSI (Open Systems Interconnection).
    
2. **Basado en el Protocolo TCP:** HTTP utiliza el Protocolo de Control de Transmisión (TCP) como su protocolo de transporte subyacente. TCP proporciona una comunicación confiable y orientada a la conexión.
    
3. **Puertos Estándar:** El puerto estándar para las conexiones HTTP es el puerto 80. Cuando un cliente envía una solicitud HTTP a un servidor, generalmente se conecta al puerto 80 a menos que se especifique lo contrario.
    
4. **Mensajes de Solicitud y Respuesta:** Las interacciones en HTTP se basan en mensajes de solicitud y respuesta. Una solicitud HTTP incluye un método (GET, POST, etc.), la URL del recurso solicitado y la versión de HTTP. La respuesta incluye un código de estado (200 OK, 404 Not Found, etc.) y los datos solicitados.
    
5. **Métodos HTTP Comunes:**
    
    - **GET:** Solicita la recuperación de un recurso.
    - **POST:** Envía datos al servidor para ser procesados (por ejemplo, formularios HTML).
    - **PUT:** Actualiza un recurso existente.
    - **DELETE:** Elimina un recurso.

### HTTPS (Hypertext Transfer Protocol Secure):

1. **SSL/TLS para Cifrado:** HTTPS utiliza SSL (Secure Sockets Layer) o su sucesor TLS (Transport Layer Security) para cifrar la comunicación entre el cliente y el servidor. Esto asegura que los datos no puedan ser interceptados fácilmente por terceros.
    
2. **Puerto Estándar:** El puerto estándar para conexiones HTTPS es el puerto 443. Cuando un cliente se conecta a un servidor a través de HTTPS, generalmente lo hace en el puerto 443, a menos que se especifique de otra manera.
    
3. **Certificados Digitales:** Para establecer una conexión segura, el servidor presenta un certificado digital al cliente. Este certificado es emitido por una entidad de certificación y verifica la autenticidad del servidor.
    
4. **Cifrado Asimétrico y Simétrico:** HTTPS utiliza cifrado asimétrico para el intercambio de claves y cifrado simétrico para la transmisión de datos una vez establecida la conexión segura.
    
5. **Indicadores de Seguridad en el Navegador:** Los navegadores web indican la presencia de una conexión segura mediante un candado en la barra de direcciones y, a menudo, el uso de "https://" en lugar de "http://".


# EXPLICACIÓN DE LAS CONEXIONES CON EL SERVIDOR WEB

Para iniciar la conexión usa three-way handshakes

1. SYN
2. SYN-ACK
3. ACK

Una vez establecida la conexión se envían los datos a través de esa conexión

Se segmentan para ser transmitidos por la red.

TCP implementa mecanismos de control de flujo y congestión para garantizar que la red no se sature y que los datos se transmitan eficientemente.

La conexión termina con los paquetes de ambos, servidor y cliente:

1. FIN
2. ACK

Una vez terminada la conexión entran en un período de TIME_WAIT para asegurarse de que no queda ningún paquete residual antes de cerrar completamente la conexión.

# *IMPORTANTE!!!!!!!!*

**Multiplexación HTTP/2:**

- HTTP/2 es un protocolo que permite la multiplexación, lo que significa que varias solicitudes y respuestas pueden compartir una única conexión TCP. Esto mejora significativamente la eficiencia, ya que elimina la necesidad de abrir múltiples conexiones para manejar solicitudes concurrentes.


# HTTPS

HTTPS (HyperText Transfer Protocol Secure)

Propósito:
1. Auth, cifrado extremo a extremo (TLS, SSL)

## FUNCIONAMIENTO

1. Handshake TLS o SSL:
	1. Se realiza un handshake para establecer la conexión segura
	2. Negociación de parámetros de cifrado y se autentican por medio de certificados digitales.

2. Certificados digitales:
	1. CA (Autoridad de certificación):
		1. Emisión de certificados que autentican un sitio web
		2. Navegadores confian en los CAs

3. TLS o SSL:
	1. TLS sucesor a SSL
	2. Cifrado extremo a extremo

4. Algoritmos criptográficos:
	1. Tipos:
		1. AES
		2. RSA
		3. ECC
		4. Para cifrar y asegurar la conexión.
5. HSTS (HTTP Strict Transport Security):
	1. Política de seguridad que ayuda a proteger a un sitio web de ataques SSL stripping.
	2. Exige que todas las interacciones futuras con un sitio web se realicen de forma segura.
6. Perfect Forward Secrecy (PFS):
	1. PFS garantiza que, incluso si las claves de cifrado a largo plazo se ven comprometidas, las sesiones anteriores permanezcan seguras.
	2. Utiliza claves de sesión efímeras que no pueden ser derivadas de las claves maestras a largo plazo.
7. Multiplexación y Rendimiento:
	- HTTP/2 permite la multiplexación de múltiples flujos en una sola conexión, mejorando la eficiencia.
	- QUIC, un protocolo de transporte desarrollado por Google, proporciona conexiones seguras y de baja latencia.
