import numpy as np # Importando a biblioteca NumPy

# o delimitador do csv e o ponto e virgula
ds = np.loadtxt(r"C:\Users\luizo\OneDrive\Área de Trabalho\Inatel Materias\6 semesntre\C11 - Python\C11 - Ciencia de Dados com Python\Exemplos Aula\space(in).csv", delimiter=';', dtype=str, encoding='utf-8') # Carrega o dataset do arquivo CSV com ponto e vírgula como delimitador
# o dtype=str indica que os dados devem ser tratados como strings
# o encoding="utf-8" garante que os caracteres especiais sejam lidos corretamente, isso depende do arquivo que você esta lendo

print("Dataset carregado:\n", ds)  # Exibe o dataset carregado


# pegando todas as colunas do dataset
colunas = ds[:, 0]  # Extrai todas as colunas do dataset


# calculando a media de uma missao espacial 
#slicing para extrair a coluna custo(cost)

arr_cost = ds[1, 6]  # Extrai a coluna de custo (cost) do dataset apenas da 1 linha
print("Coluna de custo (cost):\n", arr_cost)  # Exibe a coluna de custo

# convertendo a coluna de custo para float
arr_cost_float = arr_cost.astype(float)  # Converte a coluna de custo para float

# agora vendo a media
media_cost = np.mean(arr_cost_float)  # Calcula a média dos custos
print("Média dos custos (cost):", media_cost)  # Exibe a média 




