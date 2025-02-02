#subtracao
import subprocess

while True:
    print("\nVamos Realizar a Subtração!\n")
    print("-+-Digite (voltar) para voltar-+-\n")
    nums = input("- Digite os numeros a serem subtraidos: ")
    
    if nums.lower() == 'voltar':
        subprocess.run(['python', '/storage/emulated/0/Download/mcm/math/calc/calc_hub.py'])
        break 

    try:
        num1, num2 = map(float, nums.split())
        subtracao = num1 - num2
        print()
        print(f"Resultado da subtração: {subtracao}\n\n")
    except ValueError:
        print("Entrada inválida! Por favor, digite dois números válidos.")