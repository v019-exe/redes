
1. Definiciones
	1. Hostname o nombre del host: Nombre que identifica a un host por ejemplo pc1 o pc1.dominio.com
	2. Dominio: Nombre que identifica un espacio de autonomía administrativa, control etc. Dentro puede tener varios hostnames y varios subdominios.
		1. Ejemplo:
			1. dominio
			2. dominio.com
			3. subdominio.dominio.com
	3. FQDN (Fully Qualified Domain Name):
		1. Es un hostname o dominio nombrado de forma completa, especificando todos los niveles en la jerarquía.
		2. Zona: Es una zona de autoridad, es un dominio menos todos los subdominios delegados a otros servidores DNS.

## INFORMACIÓN EXTRA

1. Traduce entre nombres e IPs gracias a los servidores de nombres de dominio (DNS)
2. Puerto 53
3. UDP para resoluciones
4. TCP para transferencias de zona
	1. AXFR:
		1. AXFR (Authority Transfer Full) es un tipo de transferencia de zona en el DNS que implica la transferencia completa de la información de una zona DNS desde un servidor maestro a un servidor esclavo. En otras palabras, todo el conjunto de registros de la zona se copia de un servidor DNS primario al servidor DNS secundario.
	2. IXFR:
		1. IXFR (Incremental Zone Transfer) es un método de transferencia de zona que solo transfiere las actualizaciones o cambios realizados desde la última transferencia de zona. En lugar de enviar la zona completa, solo se transmiten los cambios realizados, lo que reduce significativamente el uso de ancho de banda y acelera el proceso de actualización en servidores secundarios.
	3. ZXFR:
		1. ZXFR (Zone Transfer for Specific Zones) es un término que a veces se utiliza para referirse a la transferencia de una zona específica dentro de un dominio de nivel superior. Aunque no es un término comúnmente utilizado ni estandarizado, podría referirse a una transferencia de zona específica dentro de un dominio mayor.
5. El dominio superior es el root o `"."`. Los dominios que le siguen como:
	1. .com
	2. .net
		1. Estos dominios son TLDs (Top Level Domains).
6. Los programas utilizados del lado del cliente se llaman *resolvers*
7. Un FQDN es simplemente un nombre de dominio completo, especifica todos los niveles, incluyendo al menos un TLD y un SLD (Second Level Domain)

## JERARQUÍA

1. Se delega la autoridad sobre un dominio a un servidor autoritativo, este servidor puede delegar la autoridad sobre un subdominio a otro servidor.
2. Cada dominio tiene al menos un servidor autoritativo que informa sobre ese dominio y sobre los servidores de los subdominios.
	 1. **Delegación de Autoridad:**
    
	    - La delegación de autoridad es un proceso en el cual la autoridad sobre un dominio se transfiere a un servidor autoritativo designado. Esto permite una distribución eficiente de la gestión de nombres de dominio en Internet. Por ejemplo, el servidor autoritativo para el dominio ".com" puede delegar la autoridad sobre "ejemplo.com" a otro servidor.
	1. **Servidor Autoritativo para Dominios y Subdominios:**
	    - Cada dominio, incluyendo los subdominios, tiene al menos un servidor autoritativo asociado. Este servidor tiene la información autoritativa sobre los registros DNS para ese dominio específico y, si es necesario, puede delegar la autoridad sobre subdominios a otros servidores autoritativos.
![[Pasted image 20231113230056.png]]

## TIPOS DE SERVIDORES

1. Solo caché: No es autoridad para ninguna zona. No posee base de datos (DB). Almacena las consultas.
2. Autoritativos: Responden con datos que están almacenados localmente.
	1. Primario (Maestro):
		1. Posee una base de datos con todos los registros, los cuales son administrados localmente. Solamente hay un solo servidor primario
	2. Secundario (Esclavo):
		1. Trabaja con transferencia de zona, que significa tomar las zonas de un primario y almacenarlas localmente. Pueden haber múltiples servidores secundarios.

*Los servidores raíz (root name servers) responden por el dominio raíz y responden con los servidores de los TLDs (Top level Domains)*


## TIPOS DE REGISTROS

1. A
2. AAAA
3. NS
4. CNAME
5. PTR
6. MX
7. TXT
8. SOA

## TIPOS DE CONSULTAS

1. Iterativas: El servidor responde con información parcial ya que generalmente no conoce la respuesta completa, deriva al cliente a otro servidor con más información
2. Recursivas: El servidor asume la responsabilidad de proporcionar la respuesta, si la desconoce, se encarga de consultar otros servidores hasta obtenerla para finalmente proporcionar dicha respuesta al cliente.

## GLUE RECORDS

En respuestas iterativas, el siguiente servidor de nombres a consultar se identifica por nombre de dominio y no por IP, por lo tanto puede que haga falta hacer otra consulta para resolverlo.

Por ejemplo supongamos que el servidor autoritativo de `ejemplo.com` es `ns1.ejemplo.com`, que le delega el subdominio `a.ejemplo.com` a `ns1.a.ejemplo.com`.

Si se quiere resolver `host.a.ejemplo.com` primero se consulta al servidor autoritativo `ns1.ejemplo.com`, que te lleva a consultar a `ns1.a.ejemplo.com`. El problema es que si no te da la IP de este servidor se crea una dependencia circular ya que se debe preguntar por la dirección de ese servidor.

Por lo tanto el servidor que provee la delegación debe también indicar una o más direcciones IP para el servidor mencionado en la delegación, esto se llama *glue*.

## CACHÉS

1. Las cachés son muy importantes, de lo contrario, todas las consultas comenzarían en un servidor raíz, lo que haría el proceso ineficiente.
2.  Almacenan registros por un tiempo determinado en el Time to live de cada registro. Valores típicos son del orden de los 5 días.
3. Normalmente tienen el algoritmo recursivo
4. La caché negativa es cuando se cachea la inexistencia de un cierto nombre de dominio.


## DNS REVERSO

- Es la consulta de nombres de dominio para cuando la dirección IP es conocida.
    
- Se usa el TLD `arpa`. Para IPv4 se usa `in-addr.arpa`, para IPv6 se usa `ip6.arpa`. Las direcciones se ponen al revés.
    
- Se hace una consulta DNS usando un nombre de dominio que contiene en realidad la dirección IP, de atrás para adelante.
    
- Al hacer la consulta se van explorando los servidores de nombres autoritativos partiendo desde `in-addr.arpa` hacia abajo. Como los bloques de direcciones IP son asignados a organizaciones, cada organización tiene un servidor de nombre de dominio configurado para hacer DNS reverso a su bloque. En el caso en el cual la organización transfiere una subred a otra organización, de forma paralela se hace la delegación del bloque correspondiente para que funcione el DNS reverso.
    
- En el caso de IPv4, cada dominio abarca un octeto, por ejemplo para `10.20.30.40` se hace una consulta por `40.30.20.10.in-addr.arpa`.
    
- Como originalmente las direcciones eran clase A, B o C (`/8`, `/16` y `/24`). Asignar un octeto a cada dominio tenía sentido, pero al incorporar CIDR comenzaron a asignarse bloques de direcciones que no están alineados en los octetos. Por ejemplo hay dos `/25` en un mismo nombre de dominio reverso que abarca a una `/24`. Por lo tanto la RFC 2317 estableció el truquito a usar para delegar lo que sería algo así como medio nombre de dominio.
    
- En el caso de IPv6 los dominios se corresponden a 4 bits, por ejemplo para `2001:db8::567:89ab` se hace una consulta por `b.a.9.8.7.6.5.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.8.b.d.0.1.0.0.2.ip6.arpa`.


## TIPOS DE DOMINIOS


- Dominios de nivel superior genéricos (gTLD, generic Top-Level Domain)
	- Los __dominios de nivel superior genérico__ están formados por 3 letras. Son dominios como para webs comerciales __.COM__, __.NET__, __.ORG__, que son los más habituales, pero también incluyen otros como __.INFO__ o __.BIZ__.
- Dominios de nivel superior geográfico (ccTLD, country code Top-Level domain)
	- Los dominios de nivel superior geográfico o ccTLD son los que hacen referencia a un país, como __.ES__, __.PT__, __.FR__, etc.
- Dominios de tercer nivel
	- Son los que se forman juntando un dominio genérico y uno de código de país:
		- Ejemplo: midominio.com.es
	- Su finalidad es delimitar la información del dominio genérico de nivel superior al territorio que se encuentra la marca.
- Dominio de Segundo nivel (STLD)
	- Es la parte principal y específica del dominio que se encuentra directamente a la izquierda del TLD. Por ejemplo, en `ejemplo.com`, `ejemplo` es el SLD.
	- Los SLDs son únicos dentro de un TLD, lo que significa que el mismo SLD puede existir bajo diferentes TLDs.

- Subdominios (Tercer nivel):
	- Los subdominios sirven para identificar un dispositivo dentro de una empresa:
		- hola.dominio.com




## HTTPS (DoH) DNS over HTTPS

- DNS over HTTPS (DoH) es una extensión que permite la resolución de nombres de dominio a través de conexiones HTTPS en lugar de las conexiones DNS tradicionales no cifradas.

## DNSSEC - DOMAIN NAME SYSTEM SECURITY EXTENSIONS

- DNSSEC es una extensión del sistema de nombres de dominio (DNS) que proporciona una capa adicional de seguridad mediante la firma criptográfica de los registros DNS.

	- Funcionamiento:
		- Los registros DNS son firmados digitalmente por la entidad emisora de la zona, y los servidores DNS pueden verificar la autenticidad de la información antes de proporcionarla a los usuarios.

## DOT - DNS over TLS

- DNS over TLS (DoT) es una extensión del protocolo DNS que cifra las consultas DNS mediante el uso de TLS (Transport Layer Security), el mismo protocolo de seguridad utilizado en HTTPS.

### TLS

- TLS, o Transport Layer Security, es un protocolo de seguridad que proporciona privacidad y seguridad en las comunicaciones a través de una red.
	- **Cifrado de Datos:**
	    - TLS cifra los datos transmitidos entre dos sistemas, asegurando que solo el destinatario previsto pueda descifrar y comprender la información.

	-  **Autenticación:**
	    - Facilita la autenticación mutua entre el cliente y el servidor, lo que garantiza que ambas partes sean quienes dicen ser. Esto se realiza mediante el intercambio de certificados digitales.

	- **Integridad de los Datos:**
	    - Garantiza la integridad de los datos transmitidos, lo que significa que no se han manipulado ni alterado durante la transmisión.

	- **Protección contra Ataques:**
	    - Ofrece protección contra diversos ataques, como la interceptación de datos (intercepción) y la modificación no autorizada de la información.

	- **Versiones de TLS:**
	    - Hay varias versiones de TLS, desde TLS 1.0 hasta TLS 1.3. Se alienta el uso de las versiones más recientes para aprovechar las mejoras en seguridad y rendimiento.

	-  **Puerto Predeterminado:**
	    - El puerto predeterminado para TLS es el 443. Cuando se utiliza en combinación con HTTP, se denomina HTTPS (HTTP Secure).

	-  **Usos Comunes:**
	    - TLS es ampliamente utilizado en aplicaciones web para asegurar la comunicación entre navegadores y servidores. También se utiliza en otras aplicaciones para garantizar la seguridad de las transmisiones de datos confidenciales.
 
# COMANDOS PARA COMPROBAR LA CONFIGURACIÓN

![image](https://github.com/josedaniel12345/Redes/assets/151370313/84a61c20-51fa-41bc-9ca3-482749fb8b5b)

![image](https://github.com/josedaniel12345/Redes/assets/151370313/df10f4c9-1ccd-4d93-8723-3629de448bd4)

![image](https://github.com/josedaniel12345/Redes/assets/151370313/762ab28a-61a5-4234-bf02-9786cc419ad0)

# CONFIGURACIÓN ARCHIVOS BIND9

## NAMED.CONF.OPTIONS
![image](https://github.com/josedaniel12345/Redes/assets/151370313/58dd614d-4fad-413c-8bcf-c60d172d8f23)

## NAMED.CONF.LOCAL
![image](https://github.com/josedaniel12345/Redes/assets/151370313/93c2f605-2659-49f5-b1fd-0897663f2c41)

## DB.JOSEM7SMX.COM
![image](https://github.com/josedaniel12345/Redes/assets/151370313/4f2ba7cf-7986-4e3b-8434-66d04bcf62fe)

## DB.1.16.172

![image](https://github.com/josedaniel12345/Redes/assets/151370313/d4cd8755-38bd-4a35-b979-408489b6baf7)


# COMPROBACIÓN TRANSFERENCIA DE ZONA

![image](https://github.com/josedaniel12345/Redes/assets/151370313/794544da-4d55-47d9-b836-855076e17207)

![image](https://github.com/josedaniel12345/Redes/assets/151370313/cb462836-efd1-4bc6-a474-4041b1303f00)




