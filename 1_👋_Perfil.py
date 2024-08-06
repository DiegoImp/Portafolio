import streamlit as st

st.set_page_config(page_title="Diego's Portafolio",
                   page_icon="👋", layout="wide")

st.sidebar.markdown("### Contactos")
side_col1, side_col2 = st.sidebar.columns([1, 3])
with side_col1:
    st.write("")
    st.image(
        r'util\data\sidebar_logos\gmail1.png')
    st.write("")
    st.image(
        'util\data\sidebar_logos\celular.png')
    st.write("")
    st.image(
        r"util\data\sidebar_logos\googlemaps.png")
    st.image(
        r"util\data\sidebar_logos\github_logo.png", caption="Github")
    st.image(r"util\data\sidebar_logos\BBVA.jpeg")
with side_col2:
    st.write("""#### :red[Correo]:
                        """)
    st.write("diegoimptrabajo@gmail.com")
    st.write("#### :orange[Celular]:")
    st.write("261-659-7552")
    st.write("#### :rainbow[Ubicacion]:")
    st.write("Argentina, Mendoza, Godoy Cruz")
    st.write("""<a style="color:#009846; text-decoration: underline;" href="https://github.com/DiegoImp?tab=repositories" target="_blank">Mi Repositorio</a>""", unsafe_allow_html=True)
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write(""":blue[CBU]: 0170240040000032756588""")
# ---------------------------------------------------------------------------------------------------------
# Intro
col1, col2 = st.columns(2, gap='large')
with col1:
    st.write("# Bienvenidos a mi pagina personal")
    st.write("""Hola, soy Diego, un apasionado por la tecnología y la programación.\n
Esta es una página creada por mí para mostrar mis habilidades y proyectos.\n
Espero que les muestre quién soy y qué puedo aportar a su equipo.""")
with col2:
    st.image(
        r'util\data\home\Yo.jpg', width=300)
st.markdown("---")
# ---------------------------------------------------------------------------------------------------------
# About me
Me_col1, Me_col2 = st.columns(2, gap='large')
with Me_col1:
    st.write("# Acerca de mí")
    st.write(
        """Estoy buscando oportunidades para aplicar mis habilidades y conocimientos en Data Science, y estoy comprometido a contribuir de manera significativa al éxito de cualquier proyecto en el que participe.""")

    st.markdown(
        """
    #### Algunas de mis habilidades incluyen:
    - :blue[Python]
    - :red[SQL]
    - :orange[Machine Learning]
    - :blue[Pandas]
    - :blue[Matplotlib]
    - :blue[Seaborn]
    - :green[Streamlit]
    - :gray[Git]
    - :blue[Visual Studio Code]
    - :orange[Jupyter Notebook]
    - :green[PyCharm]
    """
    )
with Me_col2:
    st.write("# Metas")
    st.write("Estoy ansioso por aprender de primera mano cómo es trabajar en un campo dinámico y en constante evolución.Donde pueda tomar desafios que me ayuden a crecer tanto personal como profesionalmente.Ademas otra de mis principales metas es seguir avanzando en mi educación y aplicación práctica de Machine Learning en casos reales.")
    st.markdown(
        """
        #### Algunas de mis metas son:
- :green[Desarrollar habilidades en un entorno dinámico.]
- :orange[Dominar Machine Learning en proyectos reales.]
- :red[Liderar equipos hacia soluciones innovadoras.]
- :blue[Impactar positivamente en la comunidad.]
- :orange[Actualizarme constantemente en mi campo.]
- :blue[Aceptar y superar desafíos complejos en análisis de datos.]
        """
    )
st.markdown("---")
# ---------------------------------------------------------------------------------------------------------
# Educacion
Edu_col1, Edu_col2 = st.columns(2)
with Edu_col1:
    st.write("# Educación")
    Edu_img, Edu_text = st.columns([1, 3])
    with Edu_img:
        st.image(r"util\data\home\UTN_logo.jpg",
                 caption="Universidad Tecnológica Nacional")

        st.image(r"util\data\home\CdM_logo.jpeg",
                 caption="Compañia de Maria")
        st.image(r"util\data\home\Master_logo.png",
                 caption="Master English Center")
    with Edu_text:
        st.write(
            "Gracias a mi Universidad eh sido capaz de comprender importantes aspectos de la computacion,y Matematicas, ademas de programas como :orange[java] y :green[c++] , :red[bases de datos] y algoritmos,pero lo que mas me apasiono fue el mundo del :blue[Data Science] y el :rainbow[machine learning],por lo que decidi seguir aprendiendo por mi cuenta y aplicando mis conocimientos en proyectos reales.")
        st.write("")
        st.write("")
        st.write(
            "Durante mi educación secundaria en una institución de orientación :orange[económica], desarrollé una sólida comprensión de los principios fundamentales de la :orange[economía] y las finanzas. Esta formación me proporcionó una base sólida para entender conceptos complejos y analizar :orange[datos económicos] de manera efectiva.")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("""Graduado del <a style="color:blue; text-decoration: underline;" href="https://www.facebook.com/inglesmaster.arg/" target="_blank">Instituto Master</a> en Mendoza, Argentina. Gracias a este instituto soy capaz de comunicarme con fluidez y precisión en inglés, lo que facilita la interacción efectiva en entornos profesionales y personales.""", unsafe_allow_html=True)
with Edu_col2:
    st.write("# Cursos")
    st.write("En la sección de cursos, presento una selección de capacitaciones que he completado para fortalecer mis habilidades y conocimientos en áreas específicas.")
    Curs_text, Curs_img = st.columns(2)
    with Curs_text:

        st.markdown(
            """
    #### <a style="color:#00FFFF; text-decoration: underline;" href="https://www.freecodecamp.org/learn" target="_blank">freecodecamp</a>:
    - :blue[Data Analysis with Python]
    - :orange[Machine Learning with Python(in progress)]
    - :red[Relational Database(in progress)]
    - :green[Back End Development and APIs(in progress)]
    """, unsafe_allow_html=True)
        st.markdown(
            """
    #### Youtube:
    - <a style="color:blue; text-decoration: underline;" href="https://www.youtube.com/watch?v=nKPbfIU442g&t=20074s" target="_blank">Python</a>
    - <a style="color:red; text-decoration: underline;" href="https://www.youtube.com/watch?v=DFg1V-rO6Pg" target="_blank">SQL</a>
    - <a style="color:gray; text-decoration: underline;" href="https://youtu.be/9ZJ-K-zk_Go" target="_blank">Git</a>
        """, unsafe_allow_html=True)
    with Curs_img:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.image(
            r"util\data\home\freecodecamp_logo.png")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.image(
            r"util\data\home\Youtube_logo.png")
st.markdown("---")
# ---------------------------------------------------------------------------------------------------------
# Hobbies
st.write("# Hobbies")
st.write("En mi tiempo libre, disfruto de actividades como escuchar música,ver anime y manga, y jugar videojuegos.")
Casual, Multip = st.columns(2)
with Casual:
    st.write("## Videojuegos")
    st.write(
        """Gracias a mis ahorros y a un trabajo de medio tiempo, pude comprar una excelente computadora que me permitio jugar a juegos como :orange[The Witcher 3], :red[Saga Souls],:green[Saga Assasins Creed], y :blue[Overwatch 2], donde cada uno me enseño cosas distintas.""")
    imagenes1 = ["util/data/home/Witcher3.jpeg",
                 "util/data/home/overwatch.png"]
    imagenes2 = ["util/data/home/Creed.png", "util/data/home/Souls.webp"]
    im1, im2 = st.columns(2)
    im1.image(imagenes1, caption=[
              "The Witcher 3: Explorar todas las posibilidades", "Overwatch 2: Comunicacion y Trabajo en Equipo"], width=200)
    im2.image(imagenes2, caption=["Assasins Creed: Historia y Mentalidad Abierta",
              "Saga Souls: Paciencia y Perseverancia."], width=220)
with Multip:
    st.write("## Series y Anime")
    st.write(
        """Soy muy fan del anime y las series aunque no le dedico tiempo apenas,el unico que sigo al dia desde hace años es :red[One piece] y :blue[Fate/Grand Order] , series que me encantan son :orange[the office] y :green[How i met your mother].""")
    imagenes3 = ["util/data/home/OnePiece.png",
                 "util/data/home/office.png"]
    imagenes4 = ["util/data/home/HIMYM.jpeg",
                 "util/data/home/fate.jpeg"]
    im3, im4 = st.columns(2)
    im3.image(imagenes3, caption=["One Piece", "The Office"], width=210)
    im4.image(imagenes4, caption=[
              "How I Met Your Mother", "Fate/Grand Order"], width=175)
