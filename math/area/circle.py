#Circulo
import subprocess
print("Vamos Calcular a Area e Perimetro do Circulo!")
while True:
    print("-+-Digite (voltar) para voltar-+-\n")
    try:
            r = input("Digite o raio da circunferencia: ").lower()
            if r.lower( ) == 'voltar':
                subprocess.run(['python', '/storage/emulated/0/Download/mcm/math/area/form_hub.py'])
                break
            else:
                r = float(r)
                area = 3.14 * r**2
                perimetro = 2*3.14*r
                
                print(f"A area da circunferencia e de:{area}\ne seu perimetro e de:{perimetro}\n\n")
            
    except ValueError:

            print("Erro: Separe os números por espaço e tente novamente.\n\n")   