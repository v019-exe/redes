El protocolo DHCP se basa en las siglas DORA:

- DISCOVER
- OFFER
- REQUEST
- ACK

![image](https://github.com/josedaniel12345/Redes/assets/151370313/c8d2d1b8-9f80-473a-bb67-be8576eb48b3)


Como se puede apreciar el DHCP REQUEST que algunos piensan que es unicast es un broadcast por el simple hecho de que la dirección de destino es 255.255.255.255.


DORA:
- DHCP DISCOVER → BROADCAST
- DHCP OFFER → UNICAST
- DHCP REQUEST → BROADCAST
- DHCP ACK → UNICAST
- DHCP NACK → UNICAST

EXPLICACIÓN PETICIONES/PROCESO DHCP
- DISCOVER:
  - El DHCP Discover es el primer paso en el proceso de asignación dinámica de direcciones IP en una red. En este paso, un dispositivo, como un equipo u ordenador, envía un mensaje de descubrimiento DHCP a la red con el fin de obtener una dirección IP. Este mensaje es transmitido a través de la red y es la manera en que un dispositivo busca un servidor DHCP disponible para obtener una configuración de red, que incluye la dirección IP asignada, la máscara de subred, la puerta de enlace y otros parámetros de red necesarios.
- OFFER:
  - En el proceso de asignación dinámica de direcciones IP en una red, después de que un dispositivo, como un equipo u ordenador, envía un mensaje de descubrimiento DHCP (DHCP Discover), los servidores DHCP disponibles responden con un mensaje llamado DHCP Offer. Este mensaje contiene una oferta de configuración de red, que incluye una dirección IP disponible para el dispositivo, así como otros parámetros de red como la máscara de subred, la puerta de enlace y la configuración de DNS. El dispositivo receptor evalúa las ofertas y selecciona una para aceptar, marcando así el siguiente paso en el proceso DHCP.

### RESUMEN

En resumen, el proceso completo implica el "DHCP Discover" del dispositivo, seguido por el "DHCP Offer" de los servidores disponibles, luego el "DHCP Request" del dispositivo para solicitar la configuración deseada, y finalmente, el "DHCP Acknowledgment" o "DHCP Negative Acknowledgment" del servidor para confirmar o rechazar la solicitud.


![image](https://github.com/josedaniel12345/Redes/assets/151370313/b710fe08-e10a-471f-9c18-65f5659ac41e)

# CONFIGURACIÓN ISC-DHCP-SERVER LINUX
__RUTA:__ */etc/dhcp/dhcpd.conf*
![image](https://github.com/josedaniel12345/Redes/assets/151370313/a83abe4c-5429-4b79-be66-cde20dbedf45)

![image](https://github.com/josedaniel12345/Redes/assets/151370313/b50b0be1-296b-4c53-b99d-8915a9037ca5)

![image](https://github.com/josedaniel12345/Redes/assets/151370313/5f56530e-c785-4cb7-83e1-6da275e785ae)






