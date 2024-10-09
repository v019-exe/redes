
## DEFINICIÓN DE VPN

Una red privada virtual (Virtual Private Network) es una tecnología que permite extender una red local sobre una red pública, generalmente Internet. El proceso se realiza por medio de encapsulación de paquetes que deben pasar por la red pública y, en caso de necesitar una privacidad en la información enviada, la encriptación de esos paquetes de datos enviados.

# TIPOS

- VPN de acceso remoto
	-  Es aquella que se utiliza para permitir el acceso de un ordenador cliente remoto a una red local. Se suele asignar al cliente IP mediante la VPN una dirección perteneciente a la red local.
- VPN punto a punto
	- Es aquella en que los ordenadores establecen entre ellos una VPN permitiendo el acceso entre los ordenadores que se encuentran en sus LAN. Generalmente se usa para unir distintas sedes de empresas, permitiendo el intercambio de información con la privacidad necesarios.

# IPSEC

Internet Protocol SECurity es una extensión del protocolo IP que permiten asegurar las comunicaciones sobre IP, autenticando y se desea cifrando los paquetes IP de una comunicación.


### IKE EXCHANGE PHASE

Se usa para negociar y establecer los túneles VPN, protocolo híbrido que implementa:
- ISAKMP FRAMEWORK
	1. Oakley
	2. SKEME

IKEV1 posee 2 fases:

1. Creación de canal de comunicación bidireccional entre los 2 extremos del túnel
	1. Atributos:
		- CIFRADO
			- DES (64 bits)
			- 3 DES (168 bits)
			- AES (128, 192 y 256 bits)
		- Hashing:
			- MD5
			- SHA
			- INTERCAMBIO DE LLAVES
				- PARTES SIN CONTACTO PREVIO
				- MEDIANTE UN CANAL INSEGURO
				- DE FORMA ANONIMA
		- MÉTODO DE AUTETICACIÓN
			- Llave previamente compartida (PSK)
			- Certificado digital
			- Atributos específicos del vendor 

ISAMKP PORT: 500

### IPSEC MENSAJES

1. MAIN MODE
	1. Negociación ISAKMP
	2. Intercambio DIFFIE-HELLMAN
	3. Autentificación de los peers
2. AGRESSIVE MODE
	1. Provee integrity protection en caso de usar certificados digitales.
3. QUICK MODE
	1. Se negocian los parámetros necesarios para establecer un canal seguro entre los extremos, además de especificar el tráfico que se enviará a través de la VPN
	2. Se negocia el tipo de cifrado y las funciones hash
	3. Modos de operación
		1. Transport Mode:
			1. Comunicaciones End-to-End
				1. Cifra el payload del paquete
		2. Tunnel Mode:
			1. Utilizado en comunicaciones en VPN entre gateways cifrando el paquete original añadiendo un encabezado
![[AH-ESP1.png]]




## PROTOCOLOS

IPsec puede utilizar uno de dos protocolos:

- Authentication Header (AH)
	- AH proporciona:
		- Integridad
		- Autenticación
		- No repudio de todo el paquete enviado, incluyendo cabecera IP
- Encapsulationg Security Payload (ESP)
	- Cifrado
	- No incluye cálculos de cabecera IP

![[MODOS VPN.excalidraw]]

## COMANDOS DE CONFIGURACIÓN ISAKMP

```
crypto isakmp policy <1-1000>
authetication pre-share
hash sha
encryption aes 256
group 2
lifetime <time>
crypto isakmp key hola address <ip-del-otro-router>
# Creamos al transformación
crypto ipsec transform-set <nombre> esp-aes esp-sha-hmac
# Conf ACL
access-list <numero> permit ip <ip-red-1> <wildcard-1> <ip-red-2> <wildcard-2>
#Creamos el mapa
crypto map <name> <numero-policy> ipsec-isakmp
set peer <router-ip-2>
match address <acl-num>
set transform-set <name>
exit
int <interfaz-hacia-router>
crypto map <name>
```

# SIMULACIÓN DE VPN EN RED SIMPLE

![image](https://github.com/josedaniel12345/Redes/assets/151370313/e1b014c7-a186-44f5-82f9-7e8c08102cdc)



