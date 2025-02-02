import subprocess
while True:

    print("-+-Digite (voltar) para voltar-+-\n")
    print("Calculadora Basica\n\n")
    print("- Adição (A)")
    print("- Subtração (S)")
    print("- Multiplicação (M)")
    print("- Divisão (D)")
    print("- Raiz Quadrada(SQRT)")
    act = input("\nQual operação deseja realizar? ").lower()
    print("\n" * 100)
    if act == 'voltar':
        subprocess.run(['python', '/storage/emulated/0/Download/mcm/main.py'])
        
    elif act not in  ['a' ,'s' ,'m' ,'d' ,'sqrt']:
        print("\nErro:Ação inexistente,digite uma ação valida!\n\n")

    elif act == 'a':
        subprocess.run(['python', '/storage/emulated/0/Download/mcm/math/calc/addition.py'])
        
    elif act == 's':
        subprocess.run(['python', '/storage/emulated/0/Download/mcm/math/calc/subtraction.py'])
        
    elif act == 'm':
        subprocess.run(['python', '/storage/emulated/0/Download/mcm/math/calc/multiply.py'])
        
    elif act == 'd':
        subprocess.run(['python', '/storage/emulated/0/Download/mcm/math/calc/division.py'])

     
    elif act == 'sqrt':
        subprocess.run(['python', '/storage/emulated/0/Download/mcm/math/calc/sqrt.py'])
    else:
        print("\n== Erro:Função inexistente tente novamente ==\n\n")