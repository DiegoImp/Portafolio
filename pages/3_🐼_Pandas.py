import streamlit as st
import pandas as pd
import io
st.set_page_config(page_title="Diego's Portafolio",
                   page_icon="👋", layout="wide")

df = pd.read_csv(
    r'util\data\Pandas\adult.data.csv')
Muestra = df.head(10)
Intro, Info = st.columns([2, 1])
with Intro:
    st.write("""# :red[Extracción de datos]: 
En este ejemplo, extraeremos diversos datos de un dataset que cuenta con 32.561 filas y 15 columnas:
    
1. A Pandas series with race names as the index labels, representing the :violet[count] of people of each race in the dataset.
2. The :red[average] age of men in the dataset.
3. The :green[percentage] of people who have a Bachelor's degree.
4. The :green[percentage] of people with advanced education (Bachelors, Masters, or Doctorate) who make more than 50K.
5. The :green[percentage] of people without advanced education who make more than 50K.
6. The :blue[minimum] number of hours a person works per week.
7. The :green[percentage] of people who work the minimum number of hours per week and have a salary of more than 50K.
8. The country with the :green[highest percentage] of people who earn more than 50K, and the corresponding percentage.
9. The :orange[most popular] occupation for those who earn more than 50K in India.""")
with Info:
    st.write("## :red[Información del dataset]:")
    buffer = io.StringIO()
    df.info(buf=buffer)
    s = buffer.getvalue()
    st.text(s)
st.markdown("---")
MuestraData = st.container()
with MuestraData:
    st.write("## :red[Muestra de las primeras 10 filas del dataset]:")
    st.dataframe(Muestra)
st.markdown("---")
consulta1, resultado = st.columns([2, 1])
with consulta1:
    st.write("#### :green[1° Consulta]:")
    st.write(
        "A Pandas series with race names as the index labels, representing the :violet[count] of people of each race in the dataset.")
    st.code("df['race'].value_counts()")
with resultado:
    race_counts = df['race'].value_counts()
    st.write(race_counts)
st.markdown("---")
consulta2, resultado = st.columns([2, 1])
with consulta2:
    st.write("#### :green[2° Consulta]:")
    st.write("The :red[average] age of men in the dataset.")
    st.code("average_age_of_men = df[df['sex'] == 'Male']['age'].mean()")
with resultado:
    average_age_of_men = df[df['sex'] == 'Male']['age'].mean()
    st.write("# ")
    st.write("# ")
    st.write("# =", average_age_of_men)
st.markdown("---")
consulta3, resultado = st.columns([2, 1])
with consulta3:
    st.write("#### :green[3° Consulta]:")
    st.write("The :green[percentage] of people who have a Bachelor's degree.")
    st.code(
        "percentage_bachelors_degree = (df['education'] == 'Bachelors').mean() * 100")
with resultado:
    percentage_bachelors_degree = (
        df['education'] == 'Bachelors').mean() * 100
    st.write("# ")
    st.write("# ")
    st.write("# =", percentage_bachelors_degree, "%")
st.markdown("---")
consulta4 = st.container()
with consulta4:
    st.write("#### :green[4° Consulta]:")
    st.write(
        "The :green[percentage] of people :red[with] advanced education (Bachelors, Masters, or Doctorate) who make more than 50K.")
    st.code("""# Filtramos las filas que tienen una educación avanzada y un salario >50K
    advanced_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])

    high_salary = df['salary'] == '>50K'

    # Calculamos el porcentaje de personas con educación avanzada que tienen un salario >50K

    percentage_advanced_education = df[advanced_education & high_salary].shape[0] / df[advanced_education].shape[0] * 100""")
    # Filtramos las filas que tienen una educación avanzada y un salario >50K
    advanced_education = df['education'].isin(
        ['Bachelors', 'Masters', 'Doctorate'])
    high_salary = df['salary'] == '>50K'

    # Calculamos el porcentaje de personas con educación avanzada que tienen un salario >50K
    percentage_advanced_education = df[advanced_education &
                                       high_salary].shape[0] / df[advanced_education].shape[0] * 100

    st.write("#### :green[Resultado] = ", percentage_advanced_education, "%")
st.markdown("---")
consulta5 = st.container()
with consulta5:
    st.write("#### :green[5° Consulta]:")
    st.write(
        "The :green[percentage] of people :red[without] advanced education who make more than 50K.")
    st.code(
        """
        # Podemos negar una condicion con el simbolo '~'.
        no_advanced_education = ~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
        
        percentage_no_advanced_education = df[no_advanced_education & high_salary].shape[0] / df[no_advanced_education].shape[0] * 100""")

    no_advanced_education = ~df['education'].isin(
        ['Bachelors', 'Masters', 'Doctorate'])

    percentage_no_advanced_education = df[no_advanced_education &
                                          high_salary].shape[0] / df[no_advanced_education].shape[0] * 100
    st.write("#### :green[Resultado] = ",
             percentage_no_advanced_education, "%")
st.markdown("---")
consulta, resultado = st.columns([2, 1])
with consulta:
    st.write("#### :green[6° Consulta]:")
    st.write("The :blue[minimum] number of hours a person works per week.")
    st.code("min_hours_per_week = df['hours-per-week'].min()")
with resultado:
    min_hours_per_week = df['hours-per-week'].min()
    st.write("# ")
    st.write("# ")
    st.write("# =", min_hours_per_week)
st.markdown("---")
consulta7 = st.container()
with consulta7:
    st.write("#### :green[7° Consulta]:")
    st.write(
        "The :green[percentage] of people who work the :blue[minimum] number of hours per week and have a salary of more than 50K.")
    st.code(
        """# Encontramos el mínimo número de horas trabajadas por semana
    min_hours_per_week_df = df['hours-per-week'] == min_hours_per_week

    # Calculamos el porcentaje de personas que trabajan el número mínimo de horas por semana y tienen un salario >50K
    min_hours_high_salary = df[(min_hours_per_week_df) & high_salary].shape[0] / df[min_hours_per_week_df].shape[0] * 100
    """)
    min_hours_per_week_df = df['hours-per-week'] == min_hours_per_week

    min_hours_high_salary = df[(min_hours_per_week_df) &
                               high_salary].shape[0] / df[min_hours_per_week_df].shape[0] * 100
    st.write("#### :green[Resultado] = ", min_hours_high_salary, "%")
st.markdown("---")
consulta8 = st.container()
with consulta8:
    st.write("#### :green[8° Consulta]:")
    st.write(
        "The :red[country] with the :green[highest percentage] of people who earn more than 50K, and the corresponding percentage.")
    st.code(
        """country_highest_percentage_gt_50K = (df[high_salary]['native-country'].value_counts() / df['native-country'].value_counts() * 100).idxmax()""")
    country_highest_percentage_gt_50K = (
        df[high_salary]['native-country'].value_counts() / df['native-country'].value_counts() * 100).idxmax()
    percentage_highest_percentage_gt_50K = (
        df[high_salary]['native-country'].value_counts() / df['native-country'].value_counts() * 100).max()
    st.write("#### :green[Resultado] = ", country_highest_percentage_gt_50K)
    st.write("##### Con un porcentaje del: ",
             percentage_highest_percentage_gt_50K, "%")
    st.write("")
st.markdown("---")
consulta9 = st.container()
with consulta9:
    st.write("#### :green[9° Consulta]:")
    st.write(
        "The :orange[most popular] occupation for those who earn more than 50K in India.")
    st.code(
        """most_popular_occupation_india = df[(df['native-country'] == 'India') & high_salary]['occupation'].value_counts().idxmax()""")
    most_popular_occupation_india = df[(
        df['native-country'] == 'India') & high_salary]['occupation'].value_counts().idxmax()
    st.write("#### :green[Resultado] = ", most_popular_occupation_india)
st.markdown("---")
Final = st.container()
with Final:
    st.write(
        """Todo el codigo de este ejemplo se encuentra en el siguiente Link
        a mi repositorio en :green[GitHub].""")
    st.link_button(":green[Ir a GitHub]",
                   "https://github.com/DiegoImp/Demographic-Data-Analyzer-project")
