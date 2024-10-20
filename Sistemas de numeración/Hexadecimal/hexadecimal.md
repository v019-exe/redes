# Sistemas de numeración (Hexadecimal)

El hexadecimal es un sistema numérico en base 16, que utiliza dieciséis símbolos diferentes para representar sus valores.

## Decimal a hexadecimal
Para convertir un decimal a hexadecimal, podemos hacerlo de 2 maneras primeramente convirtiendo el número a binario o dividiendo por 16.

### Decimal a hexadecimal (Dividiendo)
Convertiremos el número 450 a hexadecimal.

$$
\begin{align*}
450 \div 16 = 28 \quad (2) \\
28 \div 16 = 1 \quad (12) \\
1 \div 16 = 0 \quad (1) \\
\newline
\text{Hex} = 0x1C2
\end{align*}
$$

## Decimal a hexadecimal (Binario)
$$
\textbf{Conversión de 450 de Decimal a Hexadecimal}
$$

1. **Convertir de Decimal a Binario**:

$$
\begin{align*}
450 \div 2 = 225 \quad \text{(0)} \\
225 \div 2 = 112 \quad \text{(1)} \\
112 \div 2 = 56 \quad \text{(0)} \\
56 \div 2 = 28 \quad \text{(0)} \\
28 \div 2 = 14 \quad \text{(0)} \\
14 \div 2 = 7 \quad \text{(0)} \\
7 \div 2 = 3 \quad \text{(1)} \\
3 \div 2 = 1 \quad \text{(1)} \\
1 \div 2 = 0 \quad \text{(1)} \\
\newline
R = 111000010_2
\end{align*}
$$

Seguidamente agrupamos los números de 4 en 4:

$$
0001 \ 1100 \ 0010
$$

Ahora que tenemos los números agrupados, los convertiremos a hexa:

$$
\begin{align*}
0001_2 = 1_{16} \\
1100_2 = C_{16} \\
0010_2 = 2_{16} \\
\newline
Hex = 0x1C2_{16}
\end{align*}
$$