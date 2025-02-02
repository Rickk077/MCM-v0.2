import subprocess

while True:
    print("-+-Digite (voltar) para voltar-+-\n")
    print("      CALCULAR ENERGIA      ")
    funcao = str(input("""   Escolha uma função\n
--Energia Cinetica (EC)\n--Energia Mecanica (EM)\n--Energia Potencial Gravitacional (EPG)\n--Energia Potencial Elastica (EPE) """)).strip().lower()
    #voltar
    if funcao == 'voltar':
        subprocess.run(['python', '/storage/emulated/0/Download/mcm/main.py'])
        break
        
    # energia cinetica
    elif funcao == 'ec':
        subprocess.run(['python', '/storage/emulated/0/Download/mcm/physic/energy/ec.py'])
        break

    # energia mecanica
    elif funcao == 'em':
        subprocess.run(['python', '/storage/emulated/0/Download/mcm/physic/energy/em.py'])
        break

    # energia gravitacional
    elif funcao == 'epg':
        subprocess.run(['python', '/storage/emulated/0/Download/mcm/physic/energy/epg.py'])
        break

    # energia elastica
    elif funcao == 'epe':
        subprocess.run(['python', '/storage/emulated/0/Download/mcm/physic/energy/epe.py'])
        break

    else:
        print("\n"*100)
        print("\n== Erro:Função inexistente tente novamente ==\n\n")