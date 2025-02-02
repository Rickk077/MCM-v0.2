import subprocess

while True:
    print("-+-Digite (voltar) para voltar-+-\n")
    print("      CALCULAR MOVIMENTO      ")
    funcao = str(input("""   Escolha uma função\n
- Movimento Uniforme (MU)\n- Movimento Uniforme Variado(MUV)\n- Aceleração Media (AM)\n- Velocidade Media (VM) """)).strip().lower()
    
    if funcao == 'voltar':
        subprocess.run(['python', '/storage/emulated/0/Download/mcm/main.py'])
        break
        

    elif funcao == 'mu':
        subprocess.run(['python', '/storage/emulated/0/Download/mcm/physic/mov/mu.py'])
        break

    
    elif funcao == 'muv':
        subprocess.run(['python', '/storage/emulated/0/Download/mcm/physic/mov/muv.py'])
        break

    
    elif funcao == 'am':
        subprocess.run(['python', '/storage/emulated/0/Download/mcm/physic/mov/acel_media.py'])
        break

   
    elif funcao == 'vm':
        subprocess.run(['python', '/storage/emulated/0/Download/mcm/physic/mov/velo_media.py'])
        break

    else:
        print("\n"*100)
        print("\n== Erro:Função inexistente tente novamente ==\n\n")