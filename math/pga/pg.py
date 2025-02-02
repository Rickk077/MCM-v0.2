#pg  Sn=A1.(Q**n-1)
import subprocess
print("Vamos Calcular a P.G")
while True:
    try:
        print("\n-+-Digite (voltar) para voltar-+-\n")
        valores = input("Digite o valor de:\n\n A1 (primeiro numero da sequencia).\n Q (a razao da sequencia).\n N(numero de elementos na sequencia).\n-Respectivamente separados por espaço ")
        if valores == 'voltar':
            print()
            print()
            subprocess.run(['python', '/storage/emulated/0/Download/mcm/pga_hub.py'])
            continue
        a1,q,n = map(float, valores.split())
        Sn = a1*(q**n-1)
        print()
        print(f"O valor de Sn dessa P.G e de: ",Sn)
        print()
    except ValueError:
            print("Erro:digite numeros validos!")