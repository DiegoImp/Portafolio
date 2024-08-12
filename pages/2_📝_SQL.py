import streamlit as st
import pandas as pd

st.set_page_config(page_title="Diego's Portafolio",
                   page_icon="📝", layout="wide")
Intro1, Intro2 = st.columns(2)
with Intro1:
    st.write("# :red[SQL]")
    st.write("""En esta seccion se mostraran algunas de las consultas :red[SQL] que he realizado en mis proyectos.
             Las cuales fueron realizadas en una base de datos local publica llamada: <a style="color:red; text-decoration: underline;"
             href="https://en.wikiversity.org/wiki/Database_Examples/Northwind/SQLite" target="_blank">  Northwind</a> en SQLite.""", unsafe_allow_html=True)
    st.write("La base de datos :red[Northwind] simula la operación de una empresa ficticia de importación y exportación de productos. Contiene :blue[tablas] sobre productos, clientes, empleados, pedidos y otros aspectos relevantes para gestionar un negocio.")
with Intro2:
    st.image("./util/data/SQL/Northwind.png")

st.markdown("---")
consulta = st.container()
with consulta:
    st.write("## Consultas :red[SQL]")
    st.write("En este ejemplo, intentaremos extraer de la base de datos 3 cosas, los 10 mejores empleados, los 10 productos mas vendidos y los que tan rentables son cada empleado.")
    st.write(
        "Para ello debemos de importar la libreria sqlite3 y seguir los siguientes pasos.")
imports, conn = st.columns(2)
with imports:
    st.write("""## Importar librerias""")
    st.code("""import sqlite3 as sql
import pandas as pd
import matplotlib.pyplot as plt""")
    st.write("Con esto ya tenemos las librerias necesarias para hacer las consultas,visualizarlas y graficarlas.")
with conn:
    st.write("""## Conexion a la base de datos:""")
    st.code("""with sqlite3.connect("Northwind.db") as conn:""")
    st.write(
        "Con esto ya tenemos la conexion a la :red[base de datos].Ahora podriamos guardar todas las tablas en un :blue[DataFrame] de pandas pero como ya tenemos el diagrama de la base de datos, podemos hacer las consultas directamente.")
st.markdown("---")
select, plot = st.columns(2)
with select:
    st.write("""## :orange[Consulta 1]: Los 10 productos mas rentables""")
    st.code(""" query = '''
        Select ProductName,SUM(Price*Quantity) as Revenue 
        From OrderDetails as od
        JOIN Products as p ON p.ProductID = od.ProductID
        Group By od.ProductID
        Order By Revenue DESC
        Limit 10
        '''""")
    st.write(
        "Con esta consulta obtenemos los 10 productos mas vendidos, junto a sus ganancias, y en orden ascendente.")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")

    st.write("## :red[Plotting]")
    st.code("""top_products = pd.read_sql_query(query, conn)
#List of colours for plotting
colorplot = ['steelblue', 'orange', 'green', 'red',
             'purple', 'blue', 'yellow', 'pink', 'brown', 'gray']
             
top_products.plot(x="ProductName", y="Revenue", kind="bar",
                    figsize=(10, 5), legend=False, color=colorplot)
plt.title("10 Productos mas rentables")
plt.xlabel("Productos")
plt.ylabel("Revenue")
plt.xticks(rotation=90)
plt.gca().invert_xaxis()  # Invert x-axis
plt.show()""")


with plot:
    top_products = pd.read_csv(
        r"./util/data/SQL/Top_Products.csv", index_col=0,)
    top_products.index = pd.Index(range(1, 11))
    st.write("## :blue[Tabla]")
    st.dataframe(top_products, width=800)
    st.write("")
    st.write("")
    st.image(r"./util/data/SQL/Top_Products.png")
    st.write("Con esto ya tenemos el grafico de los 10 productos mas vendidos.")
st.markdown("---")
select2, plot2 = st.columns(2)
with select2:
    st.write("""## :orange[Consulta 2]: Los 10 Empleados mas rentables""")
    st.code("""query2 = '''
        SELECT FirstName || " " || LastName as Employee,COUNT(*) as TOTAL
        FROM Orders o
        JOIN Employees e
        ON e.EmployeeID = o.EmployeeID
        GROUP BY o.EmployeeID
        ORDER BY TOTAL DESC
        Limit 10
        '''""")
    st.write(
        "Con esta consulta obtenemos los 10 empleados mas rentables, junto a sus ventas, y en orden ascendente.")
    st.write("")
    st.write("")
    st.write("")
    st.write("")

    st.write("## :red[Plotting]")
    st.code("""top_Sellers = pd.read_sql_query(query2, conn)
    
    top_Sellers.plot(x="Employee", y="TOTAL", kind="bar",
                     figsize=(10, 5), legend=False, color=colorplot)

    plt.title("10 Empleados mas rentables")
    plt.xlabel("Empleados")
    plt.ylabel("Ordenes")
    plt.xticks(rotation=90)
    plt.gca().invert_xaxis()
    plt.show()""")


with plot2:
    top_employees = pd.read_csv(
        r"./util/data/SQL/Top_Employees.csv", index_col=0,)
    top_employees.index = pd.Index(range(1, 10))
    st.write("## :blue[Tabla]")
    st.dataframe(top_employees, width=800)
    st.write("Muestra unicamente 9 ya que solo hay 9 empleados.")
    st.write("")
    st.write("")
    st.image("./util/data/SQL/Top_Employees.png")
    st.write("Con esto ya tenemos el grafico de los 9 empleados con mas ventas.")
st.markdown("---")
select3, plot3 = st.columns(2)
with select3:
    st.write(
        """## :orange[Consulta 3]: Ganancias de los 9 empleados mas rentables""")
    st.code("""query3 = '''
            SELECT FirstName || " " || LastName as Employee,
            (
            SELECT SUM(p.Price * od.Quantity)
            FROM OrderDetails AS od
            JOIN Products AS p ON p.ProductID = od.ProductID
            JOIN Orders AS o ON o.OrderID = od.OrderID
            WHERE o.EmployeeID = e.EmployeeID
            )AS Ganancias
            FROM 
            Employees AS e;
            '''""")
    st.write(
        "Con esta consulta obtenemos las ventas de los 10 empleados.")
    st.write("## :red[Plotting]")
    st.code("""top_Sellers_Act = pd.read_sql_query(query3, conn)
top_Sellers_Act.plot(x="Employee", y="Ganancias", kind="bar",
                    figsize=(10, 5), legend=False, color=colorplot)
top_Sellers_Act.to_csv("Top_Employees_Sells.csv")
plt.title("10 Empleados mas Exitosos")
plt.xlabel("Empleados")
plt.ylabel("Ganancias")
plt.xticks(rotation=90)
plt.show()""")

with plot3:
    top_employees_Sells = pd.read_csv(
        r"./util/data/SQL/Top_Employees_Sells.csv", index_col=0, nrows=9)
    top_employees_Sells.index = pd.Index(range(1, 10))
    st.write("## :blue[Tabla]")
    st.dataframe(top_employees_Sells, width=800)
    st.write("Muestra unicamente 9 ya que solo hay 9 empleados.")
    st.write("")
    st.write("")
    st.image("./util/data/SQL/Top_Employees_Sells.png")
    st.write("Con esto ya tenemos el grafico de los 9 empleados con mas ventas.")
st.markdown("---")
st.write("## Otras consultas que se pueden realizar")
update, create, insert = st.columns(3)
with update:
    st.write("### :orange[Update]")
    st.write(
        "Con esta consulta podemos :orange[actualizar] los datos de una tabla.")
    st.code("""query4 = '''Update Employees 
            SET FirstName = 'Diego',
            LastName = 'Impriglio' 
            '''
conn.execute(query4)""")
with create:
    st.write("### :blue[Create]")
    st.write("Con esta consulta podemos :blue[crear] una tabla.")
    st.code("""query5 = '''CREATE TABLE IF NOT EXISTS Interns (
            ID INTEGER PRIMARY KEY,
            FirstName TEXT,
            LastName TEXT,
            Age INTEGER,
            Hours INTEGER
            )
            '''
conn.execute(query5)
            """)
with insert:
    st.write("### :red[Insert]")
    st.write("Con esta consulta podemos :red[insertar] datos en una tabla.")
    st.code("""query6 = '''INSERT INTO Interns 
        (FirstName,LastName,Age,Hours)
        VALUES
        ('Pedro','Caballero',24,6),
        ('Juan','Piña',19,5),
        ('Robert','Julians',45,9),
        ('Ana','Sevilla',33,2);
              '''
conn.execute(query6)
        """)
st.write("#### Al final de estas consultas, si se desea guardar los cambios, se debe de hacer un commit.")
st.code("""conn.commit()""")
st.markdown("---")
Final = st.container()
with Final:
    st.write(
        """Todo el codigo de este ejemplo se encuentra en el siguiente Link
        a mi repositorio en :green[GitHub].""")
    st.link_button(":green[Ir a GitHub]",
                   "https://github.com/DiegoImp/Base-de-Datos")
