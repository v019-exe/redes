# DIRECCIONAMIENTO IP

Para empezar a entender que es el direccionamiento IP nos tenemos que meter en lo que es una IP como tal, la podríamos definir como un identificador en la red:

Ejemplo de una IP muy típica: 192.168.1.1

Dentro de las IP tenemos diferentes tipos de IP, existen 2 tipos de IP:

1. Públicas
2. Privadas

Estos tipos de IP tienen unos rangos reservados, esos rangos aseguran que ninguna IP del rango privado coincida con una pública y viceversa.

Estos rangos les llamamos clases:

Rangos de IP pública y sus respectivas clases:

| Clase  | Rango de IPs                          |
|--------|---------------------------------------|
| A      | 1.0.0.0 - 9.255.255.255               |
| A      | 11.0.0.0 - 126.255.255.255            |
| B      | 129.0.0.0 - 169.253.255.255           |
| B      | 169.255.0.0 - 172.15.255.255          |
| B      | 172.32.0.0 - 191.0.1.255              |
| C      | 192.0.3.0 - 192.88.98.255             |
| C      | 192.88.100.0 - 192.167.255.255        |
| C      | 192.169.0.0 - 198.17.255.255          |
| C      | 198.20.0.0 - 223.255.255.255          |


Rango de IP privadas y sus clases:

| Clase  | Rango de IPs                          |
|--------|---------------------------------------|
| A      | 10.0.0.0 - 10.255.255.255             |
| B      | 172.16.0.0 - 172.31.255.255           |
| C      | 192.168.0.0 - 192.168.255.255         |


Una vez entendemos esta parte de las IP tenemos que saber algo que es muy básico, IP de diferente red dentro de una red no se verán a continuación un ejemplo:

![La imagen no carga](https://github.com/v019-exe/redes/blob/master/Assets/Images/image.png)

Aquí es donde entra en juego la máscara de red, una máscara de red es básicamente la que delimita que es red de que es hosts, la estructura básica de una máscara de red:

**Dirección IP:** 192.168.1.10  
**Máscara de red:** 255.255.255.0  

**Binario:** `11111111.11111111.11111111.00000000`

**Red:** `11111111.11111111.11111111`.00000000

**Host:**`00000000`



### Introducción al Subnetting

El **subnetting** (o subdivisión de redes) es una técnica que permite dividir una red en subredes más pequeñas. Esto es útil por varias razones:

- **Eficiencia**: Ayuda a utilizar más eficazmente el espacio de direcciones IP.
- **Seguridad**: Permite segmentar la red para mejorar la seguridad.
- **Rendimiento**: Reduce el tráfico en la red al limitar el tamaño de las subredes.

#### Conceptos Clave en Subnetting

1. **Máscara de Subred**: Similar a la máscara de red, una máscara de subred determina qué parte de la dirección IP identifica la red y qué parte identifica a los hosts. 

2. **CIDR (Classless Inter-Domain Routing)**: Es un método para asignar direcciones IP y enrutamiento, que reemplaza las clases tradicionales de IP. Por ejemplo, en vez de `192.168.1.0/24`, donde `/24` indica que los primeros 24 bits son para la red.

3. **Cálculo de Subredes**:
   - Para calcular cuántas subredes y hosts se pueden crear, usamos la fórmula:
     - **Número de subredes** = $$\(2^n\)$$, donde $$\(n\)$$ es el número de bits que se han tomado prestados de la parte del host.
     - **Número de hosts por subred** = $$\(2^m - 2\)$$, donde $$\(m\)$$ es el número de bits restantes para los hosts (restamos 2 para las direcciones de red y broadcast).

#### Ejemplo de Subnetting

Supongamos que tenemos la red `192.168.1.0/24` y queremos crear 4 subredes. 

1. **Número de bits necesarios para las subredes**:
   - $$\(2^n \geq 4 \Rightarrow n = 2\)$$ (tomamos prestados 2 bits).

2. **Nueva máscara de subred**:
   - Original: `255.255.255.0` (que es /24)
   - Nueva: `/26` (porque tomamos prestados 2 bits, así que 24 + 2 = 26).

3. **Rangos de Subredes**:
   - `192.168.1.0/26` -> Hosts: `192.168.1.1` a `192.168.1.62`
   - `192.168.1.64/26` -> Hosts: `192.168.1.65` a `192.168.1.126`
   - `192.168.1.128/26` -> Hosts: `192.168.1.129` a `192.168.1.190`
   - `192.168.1.192/26` -> Hosts: `192.168.1.193` a `192.168.1.254`

# Operación AND en Direccionamiento IP

La operación **AND** es fundamental en el contexto de redes y direccionamiento IP, especialmente cuando se trabaja con direcciones IP y máscaras de red. Esta operación se utiliza para determinar a qué red pertenece una dirección IP.

## ¿Qué es la operación AND?

La operación AND toma dos valores binarios y produce un resultado en el que cada bit es el resultado de la comparación de los bits correspondientes de los dos valores. Solo produce un bit `1` si ambos bits son `1`, de lo contrario, produce un `0`. La tabla de verdad de la operación AND es la siguiente:

| A | B | A AND B |
|---|---|---------|
| 0 | 0 |    0    |
| 0 | 1 |    0    |
| 1 | 0 |    0    |
| 1 | 1 |    1    |

## Aplicación de la operación AND

Para determinar la dirección de red a la que pertenece una dirección IP, realizamos la operación AND entre la dirección IP y la máscara de red.

### Ejemplo:

Supongamos que tenemos la siguiente dirección IP y máscara de red:

- **Dirección IP:** `192.168.1.10`  
- **Máscara de red:** `255.255.255.0`  

#### Representación Binaria:

- **Dirección IP:** 11000000.10101000.00000001.00001010

- **Máscara de red:**  11111111.11111111.11111111.00000000

#### Aplicando la operación AND:

Realizamos la operación AND bit a bit:

**11000000.10101000.00000001.00001010 (192.168.1.10) AND 11111111.11111111.11111111.00000000 (255.255.255.0)
11000000.10101000.00000001.00000000 (192.168.1.0)**


### Resultado:

La dirección de red resultante es `192.168.1.0`. Esto significa que la dirección IP `192.168.1.10` pertenece a la red `192.168.1.0` con la máscara de red `255.255.255.0`.

## Resumen

La operación AND es esencial para determinar a qué red pertenece una dirección IP, ya que permite identificar la parte de red de la dirección IP. Esta operación se utiliza comúnmente en el enrutamiento y la administración de redes.




