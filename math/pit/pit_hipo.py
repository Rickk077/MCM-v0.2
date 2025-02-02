#calcular hipotenusa
import math
import subprocess

print("\n-+-Digite (voltar) para voltar-+-\n")
print("Vamos descobrir a hipotenusa!")

while True:
    valores = input("Qual o valor dos catetos? (separe com espaço): ")
    
    if valores.lower() == 'voltar':
        print()
        subprocess.run(['python', '/storage/emulated/0/Download/mcm/pit_hub.py']) 
        break
    
    try:
        c1, c2 = map(float, valores.split())
    except ValueError:
        print("Erro: Por favor, insira dois números separados por espaço.")
        continue

    h2 = c1**2 + c2**2
    hipo = math.sqrt(h2)
    print()
    print(f"O valor da hipotenusa é: {hipo}") 
    print()