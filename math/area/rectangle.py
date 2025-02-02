#Retangulo
import subprocess
print("Vamos Calcular a Area do Retangulo!")
while True:
    print("-+-Digite (voltar) para voltar-+-\n")
    try:
            valores = input("Digite a base e altura do retângulo separados por espaço: ")
            if valores == 'voltar':
                subprocess.run(['python', '/storage/emulated/0/Download/mcm/math/area/form_hub.py'])
                break
            else:
                base, altura = map(float, valores.split())
                area = base * altura
                perimetro = 2 * (base + altura)
                print(f"A área do retângulo é de {area}\nE seu perímetro é de {perimetro}\n\n")
    except ValueError:
            print("Erro: Separe os números por espaço e tente novamente.\n\n")