def main():

    # Lista para guardar os dados das pessoas
    pessoas = []

    # ler os dados de 3 pessoas
    for i in range(3):
        nome = input(f"Digite o nome da {i+1} pessoa: ")
        peso = float(input(f"Digite o peso de {nome} (kg): "))
        pessoas.append({f"nome": nome, "peso": peso}) # para colocar os dados na lista

    # Inicializar variáveis para encontrar a pessoa mais pesada e a mais leve
    mais_pesada = pessoas[0]
    mais_leve = pessoas[0]

    # Encontrar a pessoa mais pesada e a mais leve
    for pessoa in pessoas[1:]:
        if pessoa["peso"] > mais_pesada["peso"]:
            mais_pesada = pessoa
        if pessoa["peso"] < mais_leve["peso"]:
            mais_leve = pessoa

    # Exibir os resultados
    print(f"\nA pessoa mais pesada é {mais_pesada['nome']} com {mais_pesada['peso']} kg.")
    print(f"A pessoa mais leve é {mais_leve['nome']} com {mais_leve['peso']} kg.")

if __name__ == '__main__':  # para mostrar que esse é o programa principal
    main()