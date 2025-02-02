##Losango
import subprocess
import math
print("Vamos Calcular a Area e Perimetro do Losango!")
while True:
    print("-+-Digite (voltar) para voltar-+-\n")
    try:
            valores = input("Digite o Diametro maior e o Diametro menor do losango separados por espaço: ")
            if valores == 'voltar':
                subprocess.run(['python', '/storage/emulated/0/Download/mcm/math/area/form_hub.py'])
                break
            else:
                D,d = map(float, valores.split())
                area = D*d / 2
                percat1 = D / 2
                percat2 = d / 2
                ladoC = D**2 + d**2
                lado = math.sqrt(ladoC)
                perimetro = lado * 2
                print(f"A área do losango é de {area}\ne seu perimetro e de {perimetro}\n\n")
    except ValueError:
            print("Erro: Separe os números por espaço e tente novamente.\n\n")