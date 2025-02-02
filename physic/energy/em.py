#energia mecanica
#em = ep + ec
import time
import subprocess
while True:
    print("-+-Digite (voltar) para voltar-+-\n")
    print("Vamos Calculcar Energia Mecanica!")
    time.sleep(0.5)
    valores =  input("Qual a energia potencial e energia cinetica desse objeto?\n(escreva respectivamente separados por espaço).").lower()
    if valores == 'voltar':
        subprocess.run(['python', '/storage/emulated/0/Download/mcm/physic/energy/energy_hub.py'])
        continue
    ep, ec = map(float, valores.split())
    em = ep + ec
    print()
    print(f"A energia mecanica desse objeto e: ",em,"N")
    print()