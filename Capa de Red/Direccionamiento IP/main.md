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

![La imagen no carga]()

Aquí es donde entra en juego la máscara de red, una máscara de red es básicamente la que delimita que es red de que es hosts, la estructura básica de una máscara de red:

**Dirección IP:** 192.168.1.10  
**Máscara de red:** 255.255.255.0  

**Binario:**  
$$
\underline{11111111.11111111.11111111.}\underline{00000000}
$$  
**Red:** $$\underline{11111111.11111111.11111111}.00000000$$ 
**Host:**$$ \underline {00000000}$$





