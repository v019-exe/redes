# Segmentación

La **segmentación** es un proceso fundamental en el manejo de datos en redes. Se refiere a la división de grandes bloques de datos en partes más pequeñas, conocidas como **segmentos**, para facilitar su transmisión a través de la red.

## ¿Por Qué es Importante la Segmentación?

1. **Eficiencia en la Transmisión**: Dividir los datos en segmentos más pequeños permite un manejo más efectivo del ancho de banda, reduciendo la posibilidad de congestión en la red.
2. **Facilitación del Control de Errores**: Al enviar datos en segmentos más pequeños, es más fácil detectar y corregir errores en la transmisión. Si un segmento se pierde o corrompe, solo ese segmento necesita ser retransmitido, no todo el bloque de datos.
3. **Optimización de Recursos**: Permite a los sistemas de red y a los protocolos gestionar de manera más eficiente los recursos de transmisión y almacenamiento.

## Proceso de Segmentación

1. **División de Datos**: Cuando un dispositivo necesita enviar grandes cantidades de datos, la capa de transporte (por ejemplo, TCP) se encarga de dividir esos datos en segmentos.
2. **Asignación de Encabezados**: Cada segmento se acompaña de un encabezado que contiene información importante, como el número de secuencia, que permite al receptor reorganizar los segmentos en el orden correcto.
3. **Transmisión de Segmentos**: Los segmentos son enviados a través de la red, donde pueden tomar diferentes rutas hacia el destino.
4. **Reensamblaje**: Al llegar al destino, los segmentos son reensamblados en el orden correcto utilizando la información del encabezado.

## Tipos de Segmentación

- **Segmentación en la Capa de Transporte**: Protocolos como TCP dividen los datos en segmentos para su transmisión.
- **Segmentación en la Capa de Enlace de Datos**: En esta capa, los datos se organizan en tramas, que son unidades de datos que incluyen dirección de destino y control de errores.


# Dominios de difusión

## ¿Qué es un dominio de difusión?

## ¿Por qué son tan peligrosos los broadcasts?

## Protocolos de broadcast

| **Protocolo**        | **Descripción**                                                                                          | **Capa del modelo OSI** |
|----------------------|----------------------------------------------------------------------------------------------------------|-------------------------|
| **ARP (Address Resolution Protocol)** | Se utiliza para mapear direcciones IP a direcciones MAC. El broadcast se usa para encontrar la dirección MAC correspondiente a una IP en la red local. | Capa 2 (Enlace de Datos) |
| **DHCP (Dynamic Host Configuration Protocol)** | Permite a los dispositivos obtener automáticamente una dirección IP de un servidor. Usa broadcast en el proceso de descubrimiento y solicitud. | Capa 7 (Aplicación)      |
| **RIP (Routing Information Protocol)** | Protocolo de enrutamiento que utiliza broadcast para enviar actualizaciones de tablas de enrutamiento. | Capa 3 (Red)            |
| **NetBIOS Name Service (NBNS)**       | Utilizado para la resolución de nombres en redes locales, usando broadcast para resolver nombres de dispositivos. | Capa 7 (Aplicación)      |
| **Spanning Tree Protocol (STP)**      | Protocolo de capa 2 usado para prevenir bucles en una red conmutada. Usa broadcast para intercambiar información entre switches. | Capa 2 (Enlace de Datos) |
| **SMB (Server Message Block)**        | Permite compartir archivos y recursos en una red. Utiliza broadcast para descubrir servicios en la red. | Capa 7 (Aplicación)      |
| **LLDP (Link Layer Discovery Protocol)** | Protocolo de descubrimiento de dispositivos vecinos que usa broadcast para anunciar información en la red local. | Capa 2 (Enlace de Datos) |
| **Cisco Discovery Protocol (CDP)**    | Protocolo propietario de Cisco para descubrir otros dispositivos Cisco en la misma red. Usa broadcast para enviar anuncios. | Capa 2 (Enlace de Datos) |
