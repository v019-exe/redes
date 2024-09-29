try: 
  import shutil
  import os
  import time
  import platform
  import requests
  from colorama import Fore, Style
  from datetime import datetime
  from rich.console import Console
  from rich.text import Text
except ImportError as e:
    import os
    import sys
    print(f"Instalando dependencias...")
    os.system("pip install colorama rich requests datetime")
    print("Dependencias instaladas")
    python = sys.executable
    os.execv(python, [python] + ['main.py'])

console = Console()



def convertir_mascara_binario(mascara: str):
    mascara = mascara.split(".")
    mascara_binaria = []

    for num in mascara:
        binario = bin(int(num)).replace("0b", "").zfill(8)
        mascara_binaria.append(binario)

    return ".".join(mascara_binaria)

def convertir_bin_decimal(binary):
    binario = str(binary)
    result = 0
    for position, digit in enumerate(binario[::-1]):
        digit1 = int(digit)
        algorithm = digit1 * 2 ** position

        result += algorithm
    
    print(result)

def convertir_bin_hex(binary):
    convert_bin = bin(int(binary)).replace("0b", "")

    binario = convert_bin.zfill(len(convert_bin) + (4 - len(convert_bin) % 4) % 4)
    hex_resultado = ''
    for i in range(0, len(binario), 4): # => Secuencia de índices desde 0 a la longitud del binario, avanzando de 4 en 4
        bloque = binario[i:i+4] # => Agrupa de 4 en 4
        hex_resultado += hex(int(bloque, 2))[2:] # => convierte en hex quitando los 2 primeros caracteres
    
    return hex_resultado.upper()

def convertir_hex_bin(hexa: str):
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
    binario = ''
    for key, values in comparacion.items():
      for i in range(0, len(hexa), 1):
        if hexa[i] == values:
          binario += key
    return binario

def convertir_decimal_hex(decimal: int):
   return hex(decimal)[2:].upper()

class GradientText:
    def __init__(self, colors):
        self.colors = colors

    def rgb_to_ansi(self, r, g, b):
        return f"\033[38;2;{r};{g};{b}m"

    def apply_gradient_to_characters(self, text):
        gradient_text = ""
        total_chars = len(text)
        num_colors = len(self.colors)

        for i, char in enumerate(text):
            color_index = int((i / total_chars) * num_colors) % num_colors
            r, g, b = self.colors[color_index]
            gradient_text += f"{self.rgb_to_ansi(r, g, b)}{char}"

        gradient_text += "\033[0m"
        return gradient_text

class GradientMenu:
    def __init__(self, colors):
        self.colors = colors

    def rgb_to_ansi(self, r, g, b):
        return f"\033[38;2;{r};{g};{b}m"

    def apply_gradient_to_lines(self, text, color_shift=0):
        lines = text.strip().splitlines()
        gradient_text = ""

        for i, line in enumerate(lines):
            
            r, g, b = self.colors[(i + color_shift) % len(self.colors)]
            gradient_text += f"{self.rgb_to_ansi(r, g, b)}{line}\033[0m\n"
        
        return gradient_text

    def get_terminal_size(self):
        try:
            size = shutil.get_terminal_size()
            return size.columns, size.lines
        except Exception:
            return 80, 24

    def center_text(self, text):
        terminal_width, terminal_height = self.get_terminal_size()
        lines = text.splitlines()
        max_line_length = max(len(line) for line in lines)


        horizontal_padding = (terminal_width - max_line_length) // 2


        vertical_padding = (terminal_height - len(lines)) // 2

        centered_lines = [line.center(max_line_length + horizontal_padding) for line in lines]


        centered_text = "\n" * vertical_padding + "\n".join(centered_lines) + "\n" * vertical_padding

        return centered_text

    def animate_gradient(self, text, delay=0.1, iterations=100):
        for shift in range(iterations):
            os.system('cls' if os.name == 'nt' else 'clear')
            gradient_text = self.apply_gradient_to_lines(text, shift)
            centered_gradient_text = self.center_text(gradient_text)
            print(centered_gradient_text)
            time.sleep(delay)



def get_terminal_size():
    try:
        columns, lines = os.get_terminal_size()
    except OSError:
        columns = 80
        lines = 40
    return columns, lines

def clase_ip(ip):
    primer_octeto = int(ip.split('.')[0])
    if 1 <= primer_octeto <= 126:
        return 'A', 8
    elif 128 <= primer_octeto <= 191:
        return 'B', 16
    elif 192 <= primer_octeto <= 223:
        return 'C', 24
    else:
        return 'Desconocida', 0



def chat_gemini(text: str):
    api_key = "AIzaSyB7tWOl_KAveVNB6vpf2PAgFqWOjCgQsVc"
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={api_key}"   
    headers = {
        "Content-Type": "application/json"
    }
    data = {"contents":[{"parts":[{"text":f"{text}"}]}]}
    response = requests.post(url, headers=headers, json=data)
    response_json = response.json()
    return response_json["candidates"][0]["content"]["parts"][0]["text"]
    

    

hora_actual = datetime.now().strftime("%H:%M:%S")

def main():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

    while True:
        menu = """
 ▄▄▄        ██████  ██▓▒██   ██▒
▒████▄    ▒██    ▒ ▓██▒▒▒ █ █ ▒░
▒██  ▀█▄  ░ ▓██▄   ▒██▒░░  █   ░
░██▄▄▄▄██   ▒   ██▒░██░ ░ █ █ ▒ 
 ▓█   ▓██▒▒██████▒▒░██░▒██▒ ▒██▒
 ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░░▓  ▒▒ ░ ░▓ ░
  ▒   ▒▒ ░░ ░▒  ░ ░ ▒ ░░░   ░▒ ░
  ░   ▒   ░  ░  ░   ▒ ░ ░    ░  
      ░  ░      ░   ░   ░    ░  
                                 
  [1] Convertir Máscara de subred a binario
  [2] Convertir Binario a Decimal
  [3] Convertir Binario a Hexadecimal
  [4] Convertir Hexadecimal a Binario
  [5] Chat con Gemini
  [6] Salir
  CÓDIGO HECHO POR V019 AKA JD
    """
        
        terminal_columns, _ = get_terminal_size()
        ascii_art_lines = menu.strip().split('\n')
        centered_menu_lines = [line.center(terminal_columns) for line in ascii_art_lines]

        full_text = '\n'.join(centered_menu_lines)

        colors = [
            (0, 0, 255),
            (0, 40, 255),
            (0, 80, 255),
            (0, 120, 255),
            (0, 160, 255),
            (0, 180, 255),
            (0, 200, 255),
            (0, 220, 255),
            (0, 240, 255),
        ]
        
        gradient = GradientText(colors)
        gradient_menu = gradient.apply_gradient_to_characters(full_text)

        print(gradient_menu)

        console.print(f"[bold blue][SELECCIÓN][/bold blue] [blue][{hora_actual}][/blue]: [cyan]Seleccione una opción:[/cyan]", end=' ')
        seleccion = input()

        if seleccion == "1":
            mascara = input("Introduzca la máscara: ")
            resultado = convertir_mascara_binario(mascara)
            print(resultado)
        
        if seleccion == "2":
            num_binario = input("Introduce el número binario: ")
            result = convertir_bin_decimal(num_binario)
            print(result)
        
        if seleccion == "3":
            binario = input("Introduce el número binario: ")
            result = convertir_bin_hex(binario)
            print(result)
        
        if seleccion == "4":
            hexadecimal = input("Introduce el hexadecimal: ")
            result = convertir_hex_bin(hexadecimal)
            print(result)
        if seleccion == "5":
            while True:
              text = input("Introduce el texto o pregunta: ")
              result = chat_gemini(text)
              print(f"[{Fore.BLUE}PREGUNTA{Fore.RESET}][{Fore.CYAN}{hora_actual}{Fore.RESET}]: {text}{Style.RESET_ALL}")
              print(f"[{Fore.BLUE}GEMINI AI{Fore.RESET}][{Fore.CYAN}{hora_actual}{Fore.RESET}]: {result}{Style.RESET_ALL}")

              if text.lower() == "salir":
                  break
        
        elif seleccion == "6" or seleccion.lower() == "exit":
            print("Saliendo del programa...")
            break

        if seleccion in ["1", "2", "3", "4", "5"]:
            final = input("¿Quieres continuar usando la herramienta? [s/n]: ")
            if final.lower() != "s":
                break

        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")

if __name__ == "__main__":
    main()
