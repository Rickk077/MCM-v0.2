#energia potencial elastica
#epe= k.x2 /2
import time
import subprocess

while True:
    print("-+-Digite (voltar) para voltar-+-\n")
    print("Vamos Calculcar Energia Potencial Elastica!")
    time.sleep(0.5)
    valores =  input("Qual a constante elastica e a deformaçao desse objeto?\n (escreva respectivamente separados por espaço).").lower()
    if valores == 'voltar':
        subprocess.run(['python', '/storage/emulated/0/Download/mcm/physic/energy/energy_hub.py'])
        continue
    k, x = map(float, valores.split())
    x2 = x**2
    epe= k*x2 /2
    print()
    print("A constante elastica desse objeto e de: ",epe,"N")
    print()