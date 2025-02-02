#Triangulo
import subprocess
print("Vamos Calcular a Area do Triangulo")
while True:
    print("-+-Digite (voltar) para voltar-+-\n")
    try:
            valores = input("Digite a base e altura do triangulo separados por espaço: ").lower()
            if valores == 'voltar':
                subprocess.run(['python', '/storage/emulated/0/Download/mcm/math/area/form_hub.py'])
                break
            else:
                base, altura = map(float, valores.split())
                area = base * altura / 2
                print(f"A área do triangulo é de {area}\n\n")
    except ValueError:
            print("Erro: Separe os números por espaço e tente novamente.\n\n")