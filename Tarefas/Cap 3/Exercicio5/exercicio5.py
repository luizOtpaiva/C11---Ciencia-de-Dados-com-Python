def main():

    n = int(input("Quantas pessoas serão cadastradas? "))

    pessoas = []

    for i in range(n):
        print(f"\nPessoa {i+1}:")
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        sexo = input("Sexo (M/F): ").strip().upper()# remove os espaços e converte para maiúsculas
        pessoas.append({"nome": nome, "idade": idade, "sexo": sexo})

    # Calcular a média de idade
    total_idade = sum(p["idade"] for p in pessoas) #  percorre a lista pessoas, pega a idade de cada uma (p["idade"]), e soma todas essas idades.
    media_idade = total_idade / n if n > 0 else 0 

    # Contar mulheres com menos de 20 anos
    contador_mulheres_menos_20 = sum(1 for p in pessoas if p["sexo"] == "F" and p["idade"] < 20)

    print(f"\nA média de idade do grupo é: {media_idade:.2f} anos.")
    print(f"Quantidade de mulheres com menos de 20 anos: {contador_mulheres_menos_20}")


if __name__ == '__main__':  # para mostrar que esse é o programa principal
    main()  

