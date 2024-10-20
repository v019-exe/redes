# Sistemas de numeración (Hexadecimal)

El hexadecimal es un sistema numérico en base 16, que utiliza dieciséis símbolos diferentes para representar sus valores.

## Decimal a hexadecimal
Para convertir un decimal a hexadecimal, podemos hacerlo de 2 maneras primeramente convirtiendo el número a binario o dividiendo por 16.

### Decimal a hexadecimal (Dividiendo)
Convertiremos el número 450 a hexadecimal.

$$
\begin{align*}
450 \div 16 = 28 (2) \\
28 \div 16 = 1 (12) \\
1 \div 16 = 0 (1) \\
\newline
\text{Hex} = 0x1C2
\end{align*}
$$

## Decimal a hexadecimal (Binario)
$$
\begin{align*}
450 \div 2 & = 225 \quad \text{(0)} \\
225 \div 2 & = 112 \quad \text{(1)} \\
112 \div 2 & = 56 \quad \text{(0)} \\
56 \div 2 & = 28 \quad \text{(0)} \\
28 \div 2 & = 14 \quad \text{(0)} \\
14 \div 2 & = 7 \quad \text{(0)} \\
7 \div 2 & = 3 \quad \text{(1)} \\
3 \div 2 & = 1 \quad \text{(1)} \\
1 \div 2 & = 0 \quad \text{(1)} \\
\end{align*}
$$
$$
\text{Ahora leemos los restos de abajo hacia arriba:} 
$$
$$
450_{10} = 111000010_2
$$

$$
\text{Agrupamos en grupos de 4 bits:}
$$
$$
0011\ 1000\ 0010
$$
$$
\text{Los valores correspondientes son:}
\begin{align*}
2^7 & = 0 \\
2^6 & = 0 \\
2^5 & = 1 \\
2^4 & = 1 \\
2^3 & = 1 \\
2^2 & = 0 \\
2^1 & = 0 \\
2^0 & = 0 \\
\end{align*}
$$