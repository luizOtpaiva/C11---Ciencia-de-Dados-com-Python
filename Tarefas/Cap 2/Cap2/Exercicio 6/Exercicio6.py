import math

def main():
    numero = float(input("Digite um número decimal: "))

    raiz = math.sqrt(numero) # fazx a raiz quadrado do numero
    teto = math.ceil(numero) # Arredonda x para o menor inteiro acima dele
    chao = math.floor(numero) # Arredonda x para o maior inteiro abaixo dele
    inteiro = math.trunc(numero) # Retorna apenas a parte inteira, ignorando os decimais.

    # print em todas as funçoes usadas
    print("Raiz quadrada:", raiz) 
    print("Função teto:", teto)
    print("Função chão:", chao)
    print("Parte inteira:", inteiro)


if __name__ == '__main__': #para poder mostrar que esse e o programa principal
    main()