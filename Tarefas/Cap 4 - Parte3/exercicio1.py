import numpy as np 

def main():
    ds = np.loadtxt(
        r"C:\Users\luizo\OneDrive\Área de Trabalho\Inatel Materias\6 semesntre\C11 - Python\C11 - Ciencia de Dados com Python\Exemplos Aula\space(in).csv", 
        delimiter=';', dtype=str, encoding='utf-8'
    )

    print("Dataset carregado:\n", ds)

    # Extrair coluna de status (sem cabeçalho)
    arr_status = ds[1:, 7]

    # Limpar espaços e vírgulas extras
    arr_status = np.char.strip(arr_status)           # tira espaços
    arr_status = np.char.replace(arr_status, ",", "") # tira vírgulas

    # Contar sucessos
    count_success = np.sum(arr_status == 'Success')
    print("Número de missões com status 'Success':", count_success)

    # mostranddo a porcentagem de missoes bem sucedidas
    total_missions = arr_status.shape[0]
    success_percentage = (count_success / total_missions) * 100
    print("Porcentagem de missões bem-sucedidas: ", success_percentage, "%")

if __name__ == '__main__':  
    main()
