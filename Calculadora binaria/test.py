comparacion = {
        "0000": "0",
        "0001": "1",
        "0010": "2",
        "0011": "3",
        "0100": "4",
        "0101": "5",
        "0110": "6",
        "0111": "7",
        "1000": "8",
        "1001": "9",
        "1010": "A",
        "1011": "B",
        "1100": "C",
        "1101": "D",
        "1110": "E",
        "1111": "F"
    }

hexa = "2ABCF"
binario = ''
for key, values in comparacion.items():
  for i in range(0, len(hexa), 1):
    if hexa[i] == values:
      binario += key

import platform

print(platform.system())
