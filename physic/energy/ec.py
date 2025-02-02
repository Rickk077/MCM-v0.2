#energia cinetica
#ec = m.v2 /2
import time
import subprocess
while True:
    print("-+-Digite (voltar) para voltar-+-\n")
    print("Vamos Calcular Energia Cinetica!")
    time.sleep(0.5)
    valores = input("Qual a massa e velocidade (m/s) do objeto?\n(escreva respectivamente dividido por espaço)").lower()
    if valores == 'voltar':
        subprocess.run(['python', '/storage/emulated/0/Download/mcm/physic/energy/energy_hub.py'])
        continue
    m, v = map(float, valores.split())
    v2 = v**2
    ec =m*v2 /2
    print()
    print(f"-A energia cinetica deste objeto e de ",ec,"N")
    print()