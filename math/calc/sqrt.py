#raiz quadrada
import subprocess
import math
while True:
    print("\nVamos Descobrir a Raiz Quadrada!\n")
    print("-+-Digite (voltar) para voltar-+-\n")
    num = input("- Digite o numero para descobrir sua raiz: ")
    
    if num.lower() == 'voltar':
        subprocess.run(['python', '/storage/emulated/0/Download/mcm/math/calc/calc_hub.py'])
        break 

    try:
        num = float(num)
        raiz = math.sqrt(num)
        print(f'- A raiz quadrada de "{num}" e igual a:{raiz}\n\n')
    except ValueError:
        print("Entrada inválida! Por favor, digite dois números válidos.")