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
\textbf{Conversión de 450 de Decimal a Hexadecimal}
$$

1. **Convertir de Decimal a Binario**:

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

Ahora leemos los restos de abajo hacia arriba:

$$
450_{10} = 111000010_2
$$

2. **Agrupar en grupos de 4 bits**:

Agrupamos los bits en grupos de 4:

$$
0011\ 1000\ 0010
$$

3. **Convertir de Binario a Hexadecimal**:

Cada grupo de 4 bits se convierte a su valor hexadecimal:
$$
\begin{align*}
0010 & \rightarrow 2 \\
1000 & \rightarrow 8 \\
0010 & \rightarrow 2 \\
\end{align*}
$$


Por lo tanto, el número \( 450 \) en decimal se representa como \( 0x282 \) en hexadecimal.

### Resultado Final:

$$
450_{10} = 111000010_2 = 0011\ 1000\ 0010 \Rightarrow 0x1C2_{16}
$$