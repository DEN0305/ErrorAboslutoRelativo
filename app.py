import sympy as sp
from colorama import Fore, Style, init

init()

def calcular_errores(valor_real, valor_aproximado):
    """
    Calcula el error absoluto y el error relativo
    """
    error_absoluto = abs(valor_real - valor_aproximado)
    error_relativo = error_absoluto / abs(valor_real) if valor_real !=0 else float('inf')

    # Presentacion de resultados con colores y alineacion
    print(Fore.CYAN + "\n" + "="*50)
    print("           CÁLCULO DE ERRORES")
    print("="*50 + Style.RESET_ALL)
    print(Fore.YELLOW + f" Valor real:         {Fore.WHITE}{valor_real}")
    print(Fore.YELLOW + f" Valor aproximado:   {Fore.WHITE}{valor_aproximado}")
    print(Fore.CYAN + "-"*50 + Style.RESET_ALL)
    print(Fore.GREEN + f" Error absoluto:     {Fore.WHITE}{error_absoluto}")
    print(Fore.GREEN + f" Error relativo:     {Fore.WHITE}{error_relativo:.6f}")
    print(Fore.CYAN + "="*50 + Style.RESET_ALL)

if __name__ == "__main__":
    print(Fore.MAGENTA + "\n" + "="*50)
    print("   PROGRAMA DE CÁLCULO DE ERRORES ")
    print("="*50 + Style.RESET_ALL)
    print("Este programa calcula el error absoluto y el error relativo.\n")
    
    valor_real = float(input(Fore.CYAN + "Ingrese el valor real: " + Style.RESET_ALL))
    valor_aproximado = float(input(Fore.CYAN + "Ingrese el valor aproximado: " + Style.RESET_ALL))

    calcular_errores(valor_real, valor_aproximado)