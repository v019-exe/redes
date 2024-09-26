## Modelo OSI (Interconexión de Sistemas Abiertos)

El modelo OSI es un marco de referencia que describe cómo se comunican los sistemas en red. Se divide en siete capas:

| Capa          | Descripción                                                   | Ejemplos                       |
|---------------|---------------------------------------------------------------|--------------------------------|
| **Capa 7: Aplicación**  | Proporciona servicios de red directamente a las aplicaciones del usuario. | HTTP, FTP, SMTP, DNS          |
| **Capa 6: Presentación**| Se encarga de la traducción de formatos de datos, cifrado y compresión. | Conversión de formatos         |
| **Capa 5: Sesión**      | Maneja las conexiones y sesiones entre aplicaciones. | Protocolo de sesión para archivos |
| **Capa 4: Transporte**  | Garantiza la entrega de datos de extremo a extremo. | TCP (orientado a conexión), UDP (sin conexión) |
| **Capa 3: Red**        | Se encarga del enrutamiento de datos y la dirección lógica. | Protocolo IP                   |
| **Capa 2: Enlace de Datos** | Proporciona la transferencia de datos entre dispositivos en la misma red. | Ethernet, Wi-Fi                |
| **Capa 1: Física**     | Define las características físicas de la red, como cables, conectores y señales eléctricas. | Transmisión de bits            |

---

## Modelo TCP/IP

El modelo TCP/IP es un conjunto de protocolos que rige cómo se comunican los dispositivos en una red. Se divide en cuatro capas:

| Capa          | Descripción                                                   | Protocolos Clave               |
|---------------|---------------------------------------------------------------|--------------------------------|
| **Capa de Aplicación**  | Interacción directa con las aplicaciones del usuario. | HTTP, FTP, SMTP, DNS          |
| **Capa de Transporte**  | Proporciona comunicación de extremo a extremo. | **TCP** y **UDP**             |
| **Capa de Internet**    | Se encarga del direccionamiento y enrutamiento de los datos. | IP, ICMP                       |
| **Capa de Acceso a Red** | Controla cómo se transmiten los datos a través de la red física. | Ethernet, Wi-Fi, PPP           |

### Protocolo TCP (Transmission Control Protocol)
- **Descripción**: Protocolo orientado a conexión que garantiza la entrega de datos de extremo a extremo.
- **Características**:
  - Establece una conexión antes de enviar datos (handshake).
  - Asegura que los datos lleguen en el orden correcto.
  - Realiza control de errores y retransmisión de paquetes perdidos.
- **Uso**: Ideal para aplicaciones que requieren fiabilidad, como la transferencia de archivos (FTP) y la navegación web (HTTP).

### Protocolo UDP (User Datagram Protocol)
- **Descripción**: Protocolo sin conexión que permite el envío de datos sin garantizar la entrega.
- **Características**:
  - No establece una conexión previa.
  - Envía datos en forma de datagramas, sin asegurar el orden o la entrega.
  - Menor sobrecarga en comparación con TCP, lo que permite una transmisión más rápida.
- **Uso**: Adecuado para aplicaciones donde la velocidad es crítica y la pérdida de algunos datos es aceptable, como en streaming de video, juegos en línea y llamadas VoIP.
