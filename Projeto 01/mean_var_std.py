#Importa a biblioteca numpy
import numpy as np

#Função que calcula a média, variância, desvio padrão, máximo, mínimo e soma de uma matriz 3x3
def calculate(list):
    #O script recebe uma lista de 9 números e retorna um dicionário contendo as estatísticas.
    # Verifica se a lista contém exatamente 9 números
    if len(list) != 9:
        raise ValueError("A lista deve conter nove números")
    
    # Converte a lista em uma matriz 3x3
    matriz = np.array(list).reshape(3, 3)

    # Função que calcula as estatísticas
    # Cada estatística é uma lista com o cálculo feito ao longo das linhas, colunas e de toda a matriz
    def estatisticas(op, arr):
        # A função recebe uma operação (op) e um array (arr)
        # Retorna a operação aplicada ao longo das linhas, colunas e de toda a matriz
        return [op(arr, axis=0).tolist(), op(arr, axis=1).tolist(), op(arr).item()]
          # O método tolist() é usado para converter o array numpy em uma lista
          # # O método item() é usado para obter o valor escalar de um array numpy de um único elemento

    # Cria um dicionário contendo as operações
    calculations = {
        'mean': estatisticas(np.mean, matriz),
        'variance': estatisticas(np.var, matriz),
        'standard deviation': estatisticas(np.std, matriz),
        'max': estatisticas(np.max, matriz),
        'min': estatisticas(np.min, matriz),
        'sum': estatisticas(np.sum, matriz)
    }    

    return calculations

print(calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]))
# Saída esperada: 
# {'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0], 
#  'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667], 
#  'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
#  'max': [[6, 7, 8], [2, 5, 8], 8], 
#  'min': [[0, 1, 2], [0, 3, 6], 0], 
#  'sum': [[9, 12, 15], [3, 12, 21], 36]}

print(calculate([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])) 
# Saída esperada: ValueError: A lista deve conter nove números