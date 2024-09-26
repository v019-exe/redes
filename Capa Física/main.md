# Capa física

La **capa física** es la primera capa del modelo OSI y se encarga de la transmisión y recepción de datos sin estructurar a través de un medio físico. Esta capa define las características eléctricas y mecánicas de los dispositivos de red.

## Funciones Principales

1. **Transmisión de Bits**: Convierte los datos en señales eléctricas, ópticas o de radio y las envía a través del medio.
2. **Definición de Medios**: Especifica los tipos de medios de transmisión (cableado, fibra óptica, inalámbrico).
3. **Sincronización**: Mantiene el sincronismo entre el emisor y el receptor.
4. **Segmentación**: Aunque la segmentación es más relevante en la capa de transporte, la capa física se encarga de dividir los datos en paquetes adecuados para la transmisión eficiente a través del medio.
5. **Codificación de Señales**: Se ocupa de la representación de los bits en señales para la transmisión.

## Medios de Transmisión

- **Cobre**: Utiliza cables de cobre (como UTP y STP) para transmitir datos. Es susceptible a interferencias electromagnéticas.
- **Fibra Óptica**: Usa luz para transmitir datos, ofreciendo alta velocidad y resistencia a interferencias.
- **Inalámbrico**: Utiliza ondas de radio o microondas, permitiendo la transmisión sin cables.

## Características de la Capa Física

- **Topología de Red**: Define cómo están dispuestos los dispositivos en la red (estrella, anillo, bus, etc.).
- **Velocidad de Transmisión**: Se mide en bps (bits por segundo) y varía según el medio utilizado.
- **Distancia de Transmisión**: Cada medio tiene una distancia máxima de transmisión antes de que la señal se degrade.
- **Tráfico de Datos**: La capa física maneja el tráfico de datos en términos de bits, sin preocuparse por el contenido de los mismos.

## Tramas y Encapsulamiento

En la capa física, los datos se transmiten como **tramas**, que son unidades de datos formadas en capas superiores (como la capa de enlace de datos). La capa física se encarga de enviar estas tramas a través del medio.

### Estructura de una Trama

Aunque la capa física no se ocupa del formato de las tramas, es importante entender que se componen de:

- **Datos**: La información que se quiere transmitir.
- **Direcciones**: Información sobre el origen y destino.
- **Control de Errores**: Información para detectar y corregir errores.

## Protocolos de la Capa Física

Aunque la capa física no tiene protocolos en sí, hay estándares que regulan cómo deben funcionar:

- **IEEE 802.3**: Estándar para Ethernet.
- **IEEE 802.11**: Estándar para redes inalámbricas (Wi-Fi).
- **ITU-T G.703**: Estándar para interfaces de transmisión de telecomunicaciones.
