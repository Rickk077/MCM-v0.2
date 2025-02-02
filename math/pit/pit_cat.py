#import math
import time
import subprocess
import math
#calcular cateto
print("\n-+-Digite (voltar) para voltar-+-\n")
print("Vamos descobrir o valor do cateto!")
while True:
    try:
        time.sleep(0.5)
        valores = input("Qual o valor do cateto e da hipotenusa? \n(escreva respectivamente e separe com espaço): ")      
        if valores == 'voltar':
            print()
            print()
            subprocess.run(['python', '/storage/emulated/0/Download/mcm/pit_hub.py']) 
            continue
        c1, h = map(float, valores.split())
        
        if h > c1:  
            c22 = h**2 - c1**2
            cateto2 = math.sqrt(c22)
            print()
            print(f"O valor do outro cateto é: ", cateto2)
            print()
        else:
            print("Erro: O valor da hipotenusa deve ser maior que o do cateto.\n")
    except ValueError:
        print("\nErro:digite numeros validos!\n")