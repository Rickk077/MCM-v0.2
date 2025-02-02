#energia potencial gravitacional
#epg = m.g.h
import time
import subprocess
while True:
    print("-+-Digite (voltar) para voltar-+-\n")
    print("Vamos Calculcar Energia Potencial Gravitacional!")
    time.sleep(0.5)
    valores =  input("Qual a massa (Kg), aceleraçao gravitacional (m/s²) e altura (m) desse objeto?\n (escreva respectivamente separados por espaço).").lower()
    if valores == 'voltar':
        subprocess.run(['python', '/storage/emulated/0/Download/mcm/physic/energy/energy_hub.py'])
        continue
    m,g,h = map(float, valores.split())
    epg = m*g*h
    print()
    print(f"A energia potencial deste objeto e: ",epg,"N")
    print()