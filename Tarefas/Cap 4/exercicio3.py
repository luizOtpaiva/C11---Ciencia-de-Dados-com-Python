import numpy as np # Importando a biblioteca NumPy

# fazendo um mini campo minado com a biblioteca NumPy

def main():
    # criaando uma matriz 2x2 formado apenas por 0's
    campo_minado = np.zeros((2, 2))
    print("Campo minado inicial:", campo_minado)

    # adicionado um numero aleatorio em uma das posiçoes da matriz
    posicao_aleatoria = np.random.randint(0, 2, size=2)  # Gera uma posição aleatória (linha, coluna)
    campo_minado[tuple(posicao_aleatoria)] = np.random.randint(1, 2)  # Atribui um número aleatório entre 1 e 9
    print("Posição aleatória escolhida:", posicao_aleatoria) # mostra a posiçao aleatoria escolhida
    print("Campo minado após adição de número aleatório:", campo_minado) # mostra o campo minado após a adição do número aleatório

    # usuario faz uma entrada de dados para solicitar o usuário que faça uma jogada (selecione uma posição da matriz)
    jogada = input("Escolha uma posição no campo minado (ex: 0,0 para linha 0 e coluna 0): ")
    linha, coluna = map(int, jogada.split(','))  # Divide a entrada e converte para inteiros
    print("Jogada escolhida:", (linha, coluna))  # mostra a jogada escolhida
    # mostra o campo minado após a jogada do usuário
    print("Campo minado após a jogada do usuário:", campo_minado)


    if campo_minado[linha, coluna] == 0:
        print("Parabéns! Você acertou uma posição sem bomba!")
    else:
        print("Você perdeu! A posição escolhida tinha uma bomba!")

   # caso contrario dentro das 3 primeiras jogadas o usuário não tenha acertado, ele perde o jogo
    tentativas = 3
    while tentativas > 0:
        jogada = input(f"Você ainda tem {tentativas} tentativas. Escolha uma posição (ex: 0,1): ")
        linha, coluna = map(int, jogada.split(','))
        
        if campo_minado[linha, coluna] == 0:
            print("Parabéns! Você acertou uma posição sem bomba!")
            break
        else:
            print("Você perdeu! A posição escolhida tinha uma bomba!")
        
        tentativas -= 1

        if tentativas == 0:
            print("Você perdeu o jogo! Não sobrou mais tentativas.")


if __name__ == '__main__':  # para poder mostrar que esse é o programa principal
    main()