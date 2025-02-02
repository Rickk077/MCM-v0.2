import subprocess
print("\n" * 100)
while True :
    print("      Tela Inicial mcm      v0.2")
    funcao = str(input("""   Escolha uma função (digite o codigo)
\n----Formulas Matematicas----\n 
- Calculadora basica (CB)
- Calcular P.G / P.A (PGA)
- Calcular area / perimetro de uma forma(AF)
- Teorema de Pitagoras (TP)
- Media (M)
- ####### (##)
- ####### (##)
\n----Formulas de Fisica----\n
- Calcular Energia (CE)
- Calcular Movimento (CM)
- ####### (##)
- ####### (##)
\n----Formulas de Quimica----\n
- ####### (##)
- ####### (##)
\n   Onde deseja ir? """)).strip().lower()
    print("\n" * 100) 
    if funcao == '##' :
        print("Erro:Ops você digitou uma ação que ainda não existe ou esta indisponivel,recarregue o programa e tente novamente.\n\n\n")        
        break
        
#matematica
        
    elif funcao == 'pga' :
        subprocess.run(['python', '/storage/emulated/0/Download/mcm/math/pga/pga_hub.py'])
        break
         
    elif funcao == 'af' :
        subprocess.run(['python', '/storage/emulated/0/Download/mcm/math/area/form_hub.py'])
        break   
        
    elif funcao == 'tp' :
        subprocess.run(['python', '/storage/emulated/0/Download/mcm/math/pit/pit_hub.py'])
        break   
 
    elif funcao == 'm' :
        subprocess.run(['python', '/storage/emulated/0/Download/mcm/math/media.py'])
        break
        
    elif funcao == 'cb' :
        subprocess.run(['python', '/storage/emulated/0/Download/mcm/math/calc/calc_hub.py'])
        break   
        
#fisica
        
    elif funcao == 'ce' :
        subprocess.run(['python', '/storage/emulated/0/Download/mcm/physic/energy/energy_hub.py'])
        break
        
    elif funcao == 'cm' :
        subprocess.run(['python', '/storage/emulated/0/Download/mcm/physic/mov/mov_hub.py'])
        break
        
#quimica
    
    else:
        print("\n== Erro:Função inexistente tente novamente ==\n\n")