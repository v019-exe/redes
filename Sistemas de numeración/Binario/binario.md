# Sistemas de numeración

## Binario
El binario o base 2 es un sistema númerico formado por 2 números, el 0 y el 1. Es muy facil convertir un binario a decimal y de decimal a binario.


### Divisiones
Para convertir un número a binario solo dividimos el número consecutivamente hasta que no podamos dividir ese número por 2, por ejemplo si queremos convertir el número 10 a binario:

$$
\begin{align*}
10 \div 2 & = 5 \, (0) \\
5 \div 2 & = 2 \, (1) \\
2 \div 2 & = 1 \, (0) \\
1 \div 2 & = 0 \, (1) \\
\\
R = 1010_2
\end{align*}
$$


### Tabla de conversión
Ahora veremos el mismo ejemplo pero con una tabla de conversión, aquí se ven los 8 bits, 8 bits = 1 byte.

| Potencia | $$2^7$$| $$2^6$$   | $$2^5$$   | $$2^4$$   | $$2^3$$   | $$2^2$$   | $$2^1$$   | $$2^0$$   |
|----------|-------|-------|-------|-------|-------|-------|-------|-------|
| Valor    |  128  |  64   |  32   |  16   |   8   |   4   |   2   |   1   |
| Número   |   1   |   1   |   0   |   0   |   0   |   0   |   0   |   0   |

Aquí podemos ver que hemos convertido el decimal 192 a binario.

Este método consiste en poner unos en las potencias hasta que los valores sumen el valor deseado.

## De binario a decimal
Para convertir un binario a decimal, tomaremos el número 1010 para convertirlo

$$
\begin{align*}
D = 1 \cdot 2^3 + 0 \cdot 2^2 + 1 \cdot 2^1 + 0 \cdot 2^0 \\
D = 8 + 0 + 2 + 0 \\
D = 10
\end{align*}
$$

## Tabla de referencia

| Decimal | Binario  |
|---------|----------|
|    0    |  0000    |
|    1    |  0001    |
|    2    |  0010    |
|    3    |  0011    |
|    4    |  0100    |
|    5    |  0101    |
|    6    |  0110    |
|    7    |  0111    |
|    8    |  1000    |
|    9    |  1001    |
|   10    |  1010    |
|   11    |  1011    |
|   12    |  1100    |
|   13    |  1101    |
|   14    |  1110    |
|   15    |  1111    |


