#divisao
import subprocess

while True:
    print("\nVamos Realizar a Divisão!\n")
    print("-+-Digite (voltar) para voltar-+-\n")
    nums = input("- Digite os numeros a serem divididos: ")
    
    if nums.lower() == 'voltar':
        subprocess.run(['python', '/storage/emulated/0/Download/mcm/math/calc/calc_hub.py'])
        break 

    try:
        num1, num2 = map(float, nums.split())
        if num2 == 0:
            print("Divisão por zero é impossível.")
            print("\n\n")
        else:
            print("Resultado da divisão:", num1 / num2)
            print("\n\n")
    except ValueError:
        print("Entrada inválida! Por favor, digite dois números válidos.")