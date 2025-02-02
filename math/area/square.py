#Quadrado
import subprocess
print("Vamos Calcular a Area do Quadrado!")
while True:
    print("-+-Digite (voltar) para voltar-+-\n")
    try:
        lado = input("Qual o tamanho do lado do quadrado?  ")
        if lado == 'voltar':
            subprocess.run(['python', '/storage/emulated/0/Download/mcm/math/area/form_hub.py'])
            break
        else:
              lado = float(lado)
              area = lado * lado
              perimetro = lado * 4
              print(f"A área do quadrado é de: {area}\nE seu perímetro é de: {perimetro}\n\n")
    except ValueError:      
            print("Erro:Digite a base do quadrado corretamente")