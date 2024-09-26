# Importa a biblioteca pandas, que é usada para manipular dados
import pandas as pd

# Define a função calculate_demographic_data
def calculate_demographic_data(print_data=True):
    # Lê o arquivo CSV que contém os dados demográficos
    df = pd.read_csv('adult.data.csv')

    # Conta quantas pessoas de cada raça estão no conjunto de dados
    race_count = df['race'].value_counts()

    # Calcula a média de idade dos homens
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # Calcula a porcentagem de pessoas que têm um diploma de bacharel
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # Verifica quem tem formação avançada (Bacharelado, Mestrado ou Doutorado)
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_education = ~higher_education  # As pessoas que não têm formação avançada

    # Calcula a porcentagem de pessoas com formação avançada que ganham mais de 50K
    higher_education_rich = round((df[higher_education]['salary'] == '>50K').mean() * 100, 1)

    # Calcula a porcentagem de pessoas sem formação avançada que ganham mais de 50K
    lower_education_rich = round((df[lower_education & (df['salary'] == '>50K')].shape[0] / df[lower_education].shape[0]) * 100, 1)

    # Encontra o número mínimo de horas que alguém trabalha por semana
    min_work_hours = df['hours-per-week'].min()

    # Filtra as pessoas que trabalham o número mínimo de horas e conta quantas ganham mais de 50K
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((num_min_workers[num_min_workers['salary'] == '>50K'].shape[0] / num_min_workers.shape[0]) * 100, 1)

    # Agrupa os dados por país e calcula a porcentagem de pessoas que ganham mais de 50K em cada país
    countries = df.groupby('native-country')
    rich_countries = countries['salary'].apply(lambda x: (x == '>50K').mean())
    
    # Encontra o país onde a maior porcentagem de pessoas ganham mais de 50K
    highest_earning_country = rich_countries.idxmax()
    highest_earning_country_percentage = round(rich_countries.max() * 100, 1)

    # Descobre qual é a profissão mais comum que ganha mais de 50K na Índia
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