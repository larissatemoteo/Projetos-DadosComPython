#Importa a biblioteca pandas
import pandas as pd

#Função que analisa dados demográficos
def demographic_data_analyzer():
    # Carregar o dataset a partir de um arquivo CSV (ajuste o caminho conforme necessário)
    df = pd.read_csv('adult.data.csv')

    # 1. Quantas pessoas de cada raça estão representadas neste conjunto de dados?
    race_count = df['race'].value_counts()

    # 2. Qual é a idade média dos homens?
    average_age_men = df[df['sex'] == 'Male']['age'].mean()

    # 3. Qual é a porcentagem de pessoas que possuem diploma de bacharel?
    percentage_bachelors = (df['education'] == 'Bachelors').mean() * 100

    # 4. Qual a porcentagem de pessoas com educação avançada (Bachelors, Masters, Doctorate) que ganham mais de 50 mil?
    advanced_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    percentage_advanced_education_rich = (df[advanced_education & (df['salary'] == '>50K')].shape[0] / df[advanced_education].shape[0]) * 100

    # 5. Qual a porcentagem de pessoas sem educação avançada que ganham mais de 50 mil?
    no_advanced_education = ~advanced_education
    percentage_non_advanced_education_rich = (df[no_advanced_education & (df['salary'] == '>50K')].shape[0] / df[no_advanced_education].shape[0]) * 100

    # 6. Qual é o número mínimo de horas que uma pessoa trabalha por semana?
    min_hours_per_week = df['hours-per-week'].min()

    # 7. Qual a porcentagem de pessoas que trabalham o número mínimo de horas por semana e têm um salário de mais de 50 mil?
    min_workers = df[df['hours-per-week'] == min_hours_per_week]
    percentage_min_workers_rich = (min_workers[min_workers['salary'] == '>50K'].shape[0] / min_workers.shape[0]) * 100

    # 8. Qual país tem a maior porcentagem de pessoas que ganham >50 mil e qual é essa porcentagem?
    rich_by_country = df[df['salary'] == '>50K']['native-country'].value_counts()
    total_by_country = df['native-country'].value_counts()
    highest_earning_country = (rich_by_country / total_by_country).idxmax()
    highest_earning_country_percentage = (rich_by_country / total_by_country).max() * 100

    # 9. Identifique a ocupação mais popular para aqueles que ganham >50 mil na Índia.
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

    # Dicionário com os resultados
    results = {
        'race_count': race_count,
        'average_age_men': round(average_age_men, 1),
        'percentage_bachelors': round(percentage_bachelors, 1),
        'percentage_advanced_education_rich': round(percentage_advanced_education_rich, 1),
        'percentage_non_advanced_education_rich': round(percentage_non_advanced_education_rich, 1),
        'min_hours_per_week': min_hours_per_week,
        'percentage_min_workers_rich': round(percentage_min_workers_rich, 1),
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': round(highest_earning_country_percentage, 1),
        'top_IN_occupation': top_IN_occupation
    }

    return results
