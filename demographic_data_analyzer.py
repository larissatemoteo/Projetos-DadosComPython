#Importa a biblioteca pandas
import pandas as pd

# Define a função calculate_demographic_data que recebe um argumento print_data
def calculate_demographic_data(print_data=True):
    # Leitura do arquivo csv
    df = pd.read_csv('adult.data.csv')

    # Quantidade de cada raça no dataset
    race_count = df['race'].value_counts() # Conta a quantidade de cada raça

    # Média de idade dos homens
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1) # Filtra os homens e calcula a média de idade

    # Porcentagem de pessoas que possuem bacharelado
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)#Conta o numero de linhas com bacharelado e divide pelo total de linhas

    # Qual a percentagem de pessoas com formação avançada (`Bacharelado`, `Mestrado` ou `Doutorado`) que ganham mais de 50 mil?
    # Qual é a porcentagem de pessoas sem educação avançada que ganham mais de 50 mil?

    # Com e sem `Bacharelado`, `Mestrado` ou `Doutorado`
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_education = ~higher_education

    # Porcentagem de pessoas com formação avançada que ganham mais de 50K
    higher_education_rich = round((df[higher_education]['salary'] == '>50K').shape[0]/df[higher_education].shape[0] * 100, 1)
    lower_education_rich = round((df[lower_education & (df['salary'] == '>50K')].shape[0] / df[lower_education].shape[0]) * 100, 1)

    # Numero mínimo de horas trabalhadas por semana
    min_work_hours = df['hours-per-week'].min() # Encontra o menor valor da coluna 'horas por semana'

    # Porcentagem de pessoas que trabalham o número mínimo de horas por semana e ganham mais de 50K
    num_min_workers = df[df['hours-per-week'] == min_work_hours] # Filtra as pessoas que trabalham o número mínimo de horas
    rich_percentage = round((num_min_workers[num_min_workers['salary'] == '>50K'].shape[0] / num_min_workers.shape[]) * 100, 1) #'

    # País com a maior porcentagem de pessoas que ganham mais de 50K
    countries = df.groupby('native-country') # Agrupa os dados por país
    rich_countries = countries['salary'].apply(lambda x: (x == '>50k').mean())[:, '>50K'] # Calcula a porcentagem de pessoas que ganham mais de 50k em cada país
    highest_earning_country = rich_countries.idxmax() # Encontra o país com a maior porcentagem de pessoas que ganham mais de 50k
    highest_earning_country_percentage = round(rich_countries.max() * 100, 1) # Calcula a porcentagem de pessoas que ganham mais de 50k no país com a maior porcentagem

    # Profissão mais comum que recebe mais de 50k na Índia
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }