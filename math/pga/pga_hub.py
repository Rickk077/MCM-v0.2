import subprocess
while True:
        print("-+-Digite (voltar) para voltar-+-\n")
        i= input("Oque deseja descobrir?\n-Progressão Geometrica (PG)\n-Progressão Aritimetica (PA)").lower()
        
        print("\n" * 100)

        if i == 'voltar':
            subprocess.run(['python', '/storage/emulated/0/Download/mcm/main.py'])
        elif i == 'pa':
            subprocess.run(['python', '/storage/emulated/0/Download/mcm/math/pga/pa.py'])
            break
        elif i == 'pg':
            subprocess.run(['python', '/storage/emulated/0/Download/mcm/math/pga/pg.py'])
            break
        else:
            print("\n== Erro:Função inexistente tente novamente ==\n\n")