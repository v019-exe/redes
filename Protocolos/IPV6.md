
1. Tipos de IPv6:
	1. Unicast → Uno a Uno → identifican una interfaz de manera única de un dispositivo ipv6
	2. Multicast → Uno a muchos → Se usa para enviar un único paquete IPv6 a varios destinos
	3. Anycast → Difusión por proximidad → cualquier dirección IPv6 de unidifusión que puede asignarse a varios dispositivos.

__*NO EXISTEN DIRECCIONES DE BROADCAST*__

2. UNICAST LOOPBACK
	1. :1/128 → 127.0.0.0/8
	2. :1/128 → 0:0:0:0:0:0:0:0:1/64
		1. Se usa para enviar paquetes de regreso a su origen.
		2. También se usa para pruebas

3. LINK LOCAL
	1. Bloque de direcciones FE80:/10 son direcciones IPv6 link-local, que corresponden en IPv4 a 19.254.0.0/16
	2. Solo son válidas para realizar comunicaciones en un segmento de red local
		1. Segmento de red local:
			1. Un segmento de red local se refiere a una porción de una red de área local (LAN)
	3. No son enrutables, básicamente el router no responde a ninguna petición link-local.

4. UNICAST GLOBAL
	1. Similares a las IPv4 públicas
	2. Los prefijos de red de las direcciones IPv6 globales asignadas por la IANA es 2000::/3 es decir 3 bits.

5. DIRECCIONES SIN ESPECIFICAR
	1. __::/128__ → es lo mismo que __0.0.0.0__
		1. Normalmente se usa como dirección de origen cuando aún no se ha determinado una dirección única.
		2. En términos de routing, __::/128__ indica la ruta estática predeterminada, __0.0.0.0__ en IPv6

6. LOCAL ÚNICA
	1. Corresponden a las IPv4 privadas.
	2. Rango de las __IPv6 locales únicas__:
		1. *FC00:/7 a FDFF::/7*
	3. Se suelen usar dentro de organizaciones
	4. Solo se pueden enrutar dentro de redes privadas.

7. IPv4 INTEGRADA
	1. Las direcciones IPv4 compatibles que se asignan  a dispositivos que pueden manejar ambos IPv4 e IPv6
		1. Empiezan por 96 bits en ceros, seguido de 32 bits de la dirección IPv4.
			1. Ejemplo: __::123.25.135.1__

