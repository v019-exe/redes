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
