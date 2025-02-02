#forma hub
import subprocess
print("Vamos Calcular Área e Perímetro!")
while True:
    print("-+-Digite (voltar) para voltar-+-")
    form = input("Qual a forma que deseja calcular?\nQuadrado (Q)\nRetângulo (R)\nTriângulo (T)\nLosango (L)\nCírculo (C)\n").lower()
    print("\n" * 100)
    if form == 'voltar':
        subprocess.run(['python', '/storage/emulated/0/Download/mcm/main.py'])
   
    elif form == 'q':
        subprocess.run(['python', '/storage/emulated/0/Download/mcm/math/area/square.py'])
        
    elif form == 'r':
        subprocess.run(['python', '/storage/emulated/0/Download/mcm/math/area/rectangle.py'])
        
    elif form == 't':
        subprocess.run(['python', '/storage/emulated/0/Download/mcm/math/area/triangle.py']) 
        
    elif form == 'l':
        subprocess.run(['python', '/storage/emulated/0/Download/mcm/math/area/diamond.py'])
        
    elif form == 'c':
        subprocess.run(['python', '/storage/emulated/0/Download/mcm/math/area/circle.py'])
        
    else:
        print("\n== Erro:Função inexistente tente novamente ==\n\n")