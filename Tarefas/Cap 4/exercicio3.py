import numpy as np

def main():
    # cria uma matriz 2x2 só com zeros
    campo_minado = np.zeros((2, 2), dtype=int)

    # sorteia uma posição aleatória para a bomba
    posicao_bomba = tuple(np.random.randint(0, 2, size=2))
    campo_minado[posicao_bomba] = 1  # coloca a bomba

    # variáveis de controle
    tentativas = 3
    jogadas_certas = 0
    total_seguras = 3  # já que é 2x2 com 1 bomba → 3 posições seguras

    print("Bem-vindo ao Mini Campo Minado 2x2!")
    print("Escolha posições no formato: linha,coluna (exemplo: 0,1)\n")

    while tentativas > 0:
        jogada = input(f"Tentativa {4 - tentativas}/3 - Escolha posição: ")
        try:
            linha, coluna = map(int, jogada.split(','))
        except:
            print("Entrada inválida! Use o formato linha,coluna (exemplo: 0,1).")
            continue

        # verifica se dentro da matriz
        if linha not in [0,1] or coluna not in [0,1]:
            print("Posição fora da matriz! Escolha entre 0 e 1.")
            continue

        if (linha, coluna) == posicao_bomba:
            print("Game Over! :( Try Again!")
            return
        else:
            print("Boa! Posição segura.")
            jogadas_certas += 1
            if jogadas_certas == total_seguras:
                print("Congratulations! You beat the game! :)")
                return

        tentativas -= 1

    # se acabarem as 3 tentativas e não venceu
    print("Fim de jogo! Você não conseguiu encontrar todas as posições seguras.")

if __name__ == "__main__":
    main()
