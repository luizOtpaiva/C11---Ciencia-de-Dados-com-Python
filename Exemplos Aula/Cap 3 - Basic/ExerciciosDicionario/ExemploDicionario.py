# Trabalhamos com um dicionário no formato chave:valor (key:value)
# A chave pode ser qualquer identificador (como 'nome', 'idade', etc.)

# Criando um dicionário com três pares chave:valor
pessoas = {
    'nome': 'Goku',           # chave 'nome' com valor 'Goku'
    'idade': 43,              # chave 'idade' com valor numérico 43
    'sexo': 'Nao Binarie'     # chave 'sexo' com valor 'Nao Binarie'
}

# Imprimindo o dicionário completo
print(pessoas)  # Exibe: {'nome': 'Goku', 'idade': 43, 'sexo': 'Nao Binarie'}

#adicionando
pessoas["raca"] = "sayajin"
pessoas["familia"] = ["Gohan", "Goten", "Chichi", "Pan" ]
print(pessoas)

# dando update em algum valor

pessoas["idade"] = 45
print(pessoas)

# Excluindo algum valor

del pessoas["sexo"]
print(pessoas)


# acessando algo dentro do dicionario, nesse caso a Chichi

print(pessoas["familia"][2])