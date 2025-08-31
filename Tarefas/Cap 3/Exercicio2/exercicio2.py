def main():

    # Conjunto com os modelos vendidos pela Loja 1
    loja1 = {"iPhone 14", "Samsung S23", "Motorola Edge 40", "Xiaomi 13"}
    # Conjunto com os modelos vendidos pela Loja 2
    loja2 = {"Samsung S23", "Xiaomi 13", "Asus ROG Phone 7", "Google Pixel 7"}

    # Exibindo os modelos disponíveis em cada loja
    print("Modelos disponíveis na Loja 1: {} ".format(loja1))
    print("Modelos disponíveis na Loja 2: {} ".format(loja2))

    # Modelos que posso comprar visitando as duas lojas (união dos conjuntos)
    todos_modelos = loja1.union(loja2)  # ou loja1 | loja2 mostra todos os modelos da loja 1 e loja 2
    print("\nTodos os modelos disponíveis somando as duas lojas:")
    print(todos_modelos)

    # Modelos que estão disponíveis em ambas as lojas (interseção dos conjuntos)
    modelos_em_ambas = loja1.intersection(loja2)  # ou loja1 & loja2
    print("\nModelos disponíveis em ambas as lojas:")
    print(modelos_em_ambas)


if __name__ == '__main__':  # para mostrar que esse é o programa principal
    main()
