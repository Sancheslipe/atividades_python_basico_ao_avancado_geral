from colorama import init as colorama_init
from colorama import Fore, Back, Style
colorama_init(autoreset=True)


s = 0 
numerador = 1
denominador = 2

for n in range(1, 5 +1 ):
    s = s + (numerador * n) / (denominador * n )
    
print(f'{Fore.RED}o resultado {s}')