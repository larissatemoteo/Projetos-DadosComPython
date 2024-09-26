import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Carregar os dados do arquivo csv
    df = pd.read_csv('epa-sea-level.csv')

    # Plota um gráfico de dispersão
    # Usamos os anos como eixo x e os níveis do mar ajustados como eixo y
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Cria a linha de melhor ajuste
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Cria uma lista de anos de 1880 a 2051 para que possamos prever os níveis do mar
    years_extended = list(range(1880, 2051))

    # Calcula os níveis do mar previstos
    sea_level_predicted = intercept + slope * years_extended

    # Plota a linha de melhor ajuste
    plt.plot(years_extended, sea_level_predicted, 'r', label='Best Fit Line 1')


    # Cria uma nova linha de melhor ajuste para os dados após o ano 2000
    # Filtra os dados para incluir apenas os anos a partir de 2000
    df_2000 = df[df['Year'] >= 2000]

    # Calcula a linha de melhor ajuste
    slope_2000, intercept_2000, r_value_2000, p_value_2000, std_err_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])

    # Cria uma lista de anos de 2000 a 2051 para que possamos prever os níveis do mar
    years_extended_2000 = list(range(2000, 2051))

    # Calcula os níveis do mar previstos
    sea_level_predicted_2000 = intercept_2000 + slope_2000 * years_extended_2000

    # Plota a linha de melhor ajuste
    plt.plot(years_extended_2000, sea_level_predicted_2000, 'g', label='Best Fit Line (2000)')	

    # Adiciona rótulos e título
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Salva o gráfico como uma imagem
    plt.savefig('sea_level_plot.png')
    return plt.gca()