#1 formula pa --- An = A1+(N-1).R
import subprocess
print("Vamos Calcular a P.A")
while True:
    try:
        print("\n-+-Digite (voltar) para voltar-+-\n")
        valores = input("Selecione os termos A1, N, R, respectivamente, separados por espaço: ")
        partes = valores.split()
        if valores == 'voltar':
            subprocess.run(['python', '/storage/emulated/0/Download/mcm/pga_hub.py'])
            continue
        if len(partes) != 3 or not all(val.isdigit() for val in partes):
            print("Por favor, insira exatamente 3 números válidos.")
            continue 
        A1, N, R = map(int, partes)    
        An = A1 + (N - 1) * R
        print()
        print("--An = A1 + (N-1).R")
        print(f"-- A",{N}," é igual a ",An)    
        # 2 formula pa --- Sn = N.(A1 + An) /2
        print()
        print("--Sn = N.(A1 + An) / 2")
        Sn = N * (A1 + An) / 2
        print(f"--Sn é igual a ",Sn)
        continue
    except ValueError:
            print("Erro:digite numeros validos!")