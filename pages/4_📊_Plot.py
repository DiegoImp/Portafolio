import streamlit as st
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['axes.facecolor'] = '#e0f2f1'  # Fondo del área de los ejes
plt.rcParams['figure.facecolor'] = 'gray'  # Fondo de la figura
titulo, frame = st.columns([3, 1])
with titulo:
    st.write("""# :red[En este proyecto vamos a limpiar y visualizar los datos de criptomonedas]:
Utilizando un conjunto de datos del valor diario de :green[Bitcoin] y :blue[Ethereum] que van desde 2017-04 al 2018-04.""")
    st.write("""## :orange[Objetivos]:
1. Dar un :violet[primer vistazo] a los datos
2. Aplicar distintos :blue[metodos] para encontrar :red[invalid data]

    -:green[Buscar] y :blue[arreglar] valores nans(Not a Number).
    
    -:green[Buscar] y :red[analizar] picos.
    
    -:violet[Visualizar] distribuciones bivariadas.
    
    -:red[Analizar] y :blue[resolver] analiticamente.

3. :green[Comparar] el resultado con el original""")
with frame:
    st.write("# :red[Muestra de los datos]:")
    df = pd.read_csv(
        r'./util/data/Plot/btc-eth-prices-outliers.csv',
        index_col=0,
        parse_dates=True
    )
    o_df = df.copy()
    st.dataframe(df.head(10))
    df.info()
st.markdown("---")
primer_vistazo = st.container()
with primer_vistazo:
    st.write("# :violet[Primer vistazo] ")
    fig = df.plot(figsize=(15, 5))
    st.pyplot(fig=plt)
    st.write("""Con el :violet[primer vistazo] uno puede identificar diversas :red[iregularidades] en el grafico.
             
Como por ejemplo:

Los :red[picos] en finales de diciembre 2017 y principios de marzo 2018.Y el espacio :orange[sin datos] a mediados de diciembre 2017.

""")
st.markdown("---")
Nans, code1, code2 = st.columns([3, 1.5, 1])
with Nans:
    st.write("""# :green[Buscando y arreglando valores nans]:
Primero vamos a buscar los valores nans en el DataFrame y luego vamos a arreglarlos.

Hacemos zoom en las fechas donde se encuentran los valores nans y luego los rellenamos con el valor anterior.
""")
    st.write("""#### :orange[Zoom en las fechas]:
Hay varias formas de hacer esto:""")

    st.code("""# 1ra forma(vista general)
df_na = df.loc["2017-12-01":"2017-12-15"]""")
    st.code("""# 2da forma(especifica al problema)
df_na['Ether'].isna().value_counts() # Cuenta la cantidad de nans
df_na.loc[df_na['Ether'].isna()] # Muestra los valores nans en un DataFrame
""")
    st.write("""#### :orange[Rellenando los valores nans]:
Esto se puede hacer utilizando el forward fill o el backward fill.En este ejemplo usare el forward fill.
""")
    st.code("""# Forward fill:
df['Ether'].fillna(method='ffill', inplace=True)
# Backward fill:
df['Ether'].fillna(method='bfill', inplace=True)
""")
with code1:
    st.write("# :red[General]:")
    st.markdown("---")

    df_na = df.loc["2017-12-01":"2017-12-15"]
    st.dataframe(df_na, height=560, use_container_width=True)
with code2:
    st.write("# :red[Especifico]:")
    st.markdown("---")
    nans_count = df_na['Ether'].isna().value_counts()
    nans_count.index = ['No nans', 'Nans']
    nans_count_df = nans_count.to_frame()
    nans_count_df.index.name = 'Condition'
    nans_dataframe = df_na.loc[df_na['Ether'].isna()]
    st.dataframe(nans_count_df, use_container_width=True)
    st.dataframe(nans_dataframe, use_container_width=True)
    st.write("""### :green[Resultado]:""")
    df['Ether'].fillna(method='ffill', inplace=True)
    st.dataframe(df.loc['2017-12-07': '2017-12-11'], use_container_width=True)
st.markdown("---")
Picos, code = st.columns([2, 2])
with Picos:
    st.write("""# :green[Buscando y arreglando picos]:
Ahora revisaremos los :red[picos] en finales de diciembre 2017 y principios de marzo 2018.""")
    st.code("""# Zoom en la localizacion
df['2017-12-25':'2018-01-01'].plot() # 1er pico
df['2018-03-01': '2018-03-09'].plot() # 2do pico
            """)
    st.write(
        "Ahora que tenemos un valor especifico de los picos, podemos eliminarlos.")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")

    st.write(" # :orange[Arreglando los picos]:")
    st.write(
        """Para eliminar los picos, simplemente eliminamos las fechas donde estos se encuentran.""")
    st.code(
        "df_cleaned = df.drop(pd.to_datetime(['2017-12-28', '2018-03-04']))")
    st.write("# :orange[Visualizando el resultado]:")
    st.code("df_cleaned.plot(figsize=(15, 5))")
with code:
    plot1, plot2 = st.columns(2)
    with plot1:
        st.write("""# :red[1er Pico]:""")
        df['2017-12-25':'2018-01-01'].plot(figsize=(7, 5.1))
        st.pyplot(fig=plt)
    with plot2:
        st.write("""# :red[2do Pico]:""")
        df['2018-03-01': '2018-03-09'].plot(figsize=(7, 5))
        st.pyplot(fig=plt)
    st.markdown("---")
    st.write("""### :green[Resultado]:""")
    st.write("Ahora se ve mucho mejor.")
    df_cleaned = df.drop(pd.to_datetime(['2017-12-28', '2018-03-04']))
    df_cleaned.plot(figsize=(15, 5))
    st.pyplot(fig=plt)
st.markdown("---")
Distribucion = st.container()
with Distribucion:
    st.write("""# :red[Visualizando distribuciones bivariadas]:
    Una distribucion bivariada es una distribucion de dos variables aleatorias, en este caso :green[Bitcoin] y :blue[Ether] y el como se relacionan.

    La forma mas comun de visualizar una distribucion bivariada es con un :orange[scatterplot], el :red[jointplot] tambien incluye la distribucion de las variables.
    """)
    plot1, plot2 = st.columns(2)
    with plot1:
        st.write("# :green[Regplot]:")
        st.write("""
    Si solo quieres un scatterplot, puedes usar el metodo regplot, que tambien ajusta un modelo de regresion lineal en la grafica.

    Este modelo sirve para predecir el valor de una variable en base a otra.""")
        st.code("""fig, ax = plt.subplots(figsize=(15, 7))
    sns.regplot(x="Bitcoin", y="Ether", data=df_cleaned, ax=ax)""")
        fig, ax = plt.subplots(figsize=(15, 7))
        sns.regplot(x="Bitcoin", y="Ether", data=df_cleaned, ax=ax)
        st.pyplot(fig=plt)
        st.write("""### :green[Conclusion]:

Los valores de :green[Bitcoin] y :blue[Ether] estan correlacionados positivamente, lo que significa que si uno sube el otro tambien subira.
Aunque tambien se puede ver que hay una gran cantidad de valores que no siguen esta regla y se encuentran dispersos por toda la grafica.""")
    with plot2:
        st.write("# :green[Joinplot]:")
        st.write("""En esta grafica uno puede ver la distribucion de las variables.
                
    sns.jointplot: Crea un gráfico de dispersión de "Bitcoin" vs "Ether" y también muestra las distribuciones marginales de estas variables.""")

        st.code("""sns.jointplot(x="Bitcoin", y="Ether", data=df_cleaned, size=9)""")
        sns.jointplot(x="Bitcoin", y="Ether", data=df_cleaned, size=9)
        st.pyplot(fig=plt)
st.markdown("---")
Analisis, plots = st.columns([2, 2])
with Analisis:
    st.write("""# :red[Analisis y resolucion]:
Vamos a utilizar std: Z score para encontrar los valores atipicos en el DataFrame.""")
    st.code("""# Z score
upper_limit = df['Bitcoin'].mean() + 2 * df['Bitcoin'].std()
lower_limit = df['Bitcoin'].mean() - 2 * df['Bitcoin'].std()
""")
    upper_limit = df['Bitcoin'].mean() + 2 * df['Bitcoin'].std()
    lower_limit = df['Bitcoin'].mean() - 2 * df['Bitcoin'].std()
    st.write("Viendo que el :red[Upper Limit] es: " + str(upper_limit))
    st.write("Viendo que el :blue[Lower Limit] es: " + str(lower_limit))
    st.write("""### :orange[Conclusion]:
Observando la grafica uno puede ver que el limite inferior es inutil siendo que cualquier valor negativo es invalido, pero el limite superior es util para encontrar valores invalidos.
En especial aquellos valores mayores a $27,369.Los cuales se pueden apreciar en el final de la grafica.""")
    st.write("")
    st.write("")

    st.write("""# :red[Limpiando valores invalidos]:""")
    st.code("""df_cleaned = df.drop(df[df['Bitcoin'] > upper_limit].index)
""")
    st.write("# :orange[Visualizando el resultado]:")
    st.code("df_cleaned.plot(figsize=(16,7))")

with plots:
    st.write("# :red[Visualizacion de los limites]")
    fig, ax = plt.subplots(figsize=(15, 7))
    sns.histplot(df['Bitcoin'], ax=ax, kde=True)
    ax.axvline(lower_limit, color='red')
    ax.axvline(upper_limit, color='red')
    st.pyplot(fig=plt)
    st.write("""# :green[Resultado]:""")
    df_cleaned = df.drop(df[df['Bitcoin'] > upper_limit].index)
    df_cleaned.plot(figsize=(16, 7))
    st.pyplot(fig=plt)
st.markdown("---")
Comparacion = st.container()
with Comparacion:
    st.write("""# :green[Comparacion con el original]:""")
    original, cleaned = st.columns(2)
    with original:
        st.write("""## :orange[Original]: """)
        o_df.plot(figsize=(16, 9.1))
        st.pyplot(fig=plt)
    with cleaned:
        st.write("""## :orange[Final]:""")
        df_cleaned.plot(figsize=(16, 10))
        st.pyplot(fig=plt)
st.markdown("---")
Final = st.container()
with Final:
    st.write(
        """Todo el codigo de este ejemplo se encuentra en el siguiente Link
        a mi repositorio en :green[GitHub].""")
    st.link_button(":green[Ir a GitHub]",
                   "https://github.com/DiegoImp/Proyectos-Varios/tree/main/BTC")
