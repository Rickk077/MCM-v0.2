import subprocess
while True:
    print("-+-Digite (voltar) para voltar-+-\n")
    i= input("Oque deseja descobrir?\n-O valor da hipotenusa (H)\n-O valor do cateto(C)\n").lower()
    print("\n" * 100)
    if i == 'voltar':
        subprocess.run(['python', '/storage/emulated/0/Download/mcm/main.py'])
    elif i == 'h':
        subprocess.run(['python', '/storage/emulated/0/Download/mcm/math/pit/pit_hipo.py'])
        break
    elif i == 'c':
        subprocess.run(['python', '/storage/emulated/0/Download/mcm/math/pit/pit_cat.py'])
        break
    else:
        print("\n== Erro:Função inexistente tente novamente ==\n\n")