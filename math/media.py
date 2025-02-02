from collections import Counter
import subprocess

def calcular_mediana(lista):
    lista.sort()
    quantidade = len(lista)
    
    if quantidade % 2 == 0:
        mediana = (lista[quantidade // 2 - 1] + lista[quantidade // 2]) / 2
    else:
        mediana = lista[quantidade // 2]
        
    return mediana

def calcular_moda(lista):
    contador = Counter(lista)
    moda = contador.most_common(1)[0] 
    return moda[0], moda[1] 

while True:
    print("   Bem vindo a média")
    print("-+-Digite (voltar) para voltar-+-\n")
    try:
        entrada = input("      Digite sua lista separada por espaço.\n").split()
        
        if entrada == ['voltar']:
            subprocess.run(['python', '/storage/emulated/0/Download/mcm/main.py'])
            continue
        
        if len(entrada) == 0:
            print("Erro: lista vazia.")
            continue
            
        lista = [float(num) for num in entrada]
        
        # calcular elementos da lista
        quantidade = len(lista)
        
        # calcular a soma dos elementos
        soma = sum(lista)
        
        # calcular a média
        media = soma / quantidade
        
        # calcular a mediana
        mediana = calcular_mediana(lista)
        
        # calcular moda
        moda_valor, moda_contagem = calcular_moda(lista)
        
        # resultados para o usuário
        print(f"A sua média é: {media}")
        print(f"A sua lista em ordem crescente é: {sorted(lista)}")
        print(f"A sua mediana é: {mediana}")
        print(f"O número que mais se repete (moda) é: {moda_valor} (repetido {moda_contagem} vezes)")
        print("\n\n\n")
        
    except ValueError:
        print("Erro: digite um número (letras não são suportadas).\n")