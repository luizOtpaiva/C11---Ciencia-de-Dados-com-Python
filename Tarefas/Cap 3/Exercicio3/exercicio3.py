def main():
    # Criando um dicionário vazio
    aluno = {}

    # Lendo nome e média do aluno
    aluno["nome"] = input("Digite o nome do aluno: ")
    aluno["media"] = float(input("Digite a média do aluno: "))

    # Determinando a situação do aluno
    if aluno["media"] >= 50:
        aluno["situacao"] = "AP"  # Aprovado
    else:
        aluno["situacao"] = "RP"  # Reprovado

    # Mostrando todo o conteúdo do dicionário
    print("\nDados do aluno:")
    print(aluno)


if __name__ == '__main__':  # para mostrar que esse é o programa principal
    main()