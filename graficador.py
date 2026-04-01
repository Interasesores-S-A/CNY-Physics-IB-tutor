

import numpy as np
import matplotlib.pyplot as plt
from ecuaciones_ib import ecuaciones_ib


def obtener_ecuaciones_graficables():
    """
    Devuelve todas las ecuaciones graficables del Data Booklet
    """
    lista = []

    for tema, ecuaciones in ecuaciones_ib.items():
        for eq in ecuaciones:
            if eq["graficable"]:
                lista.append(eq)

    return lista


def filtrar_ecuaciones_por_pregunta(pregunta):
    """
    Filtra ecuaciones relevantes según la pregunta
    """
    resultados = []

    for tema, ecuaciones in ecuaciones_ib.items():
        for eq in ecuaciones:
            if eq["graficable"]:
                for var in eq["variables"]:
                    if var.lower() in pregunta.lower():
                        resultados.append(eq)

    return resultados


def graficar_desde_ecuacion(eq_dict, variable_x, parametros):
    """
    Grafica usando directamente una ecuación del archivo ecuaciones_ib
    """

    ecuacion = eq_dict["eq"]

    # Separar ecuación
    izquierda, derecha = ecuacion.split("=")

    # Crear valores para eje x
    x_vals = np.linspace(0, 10, 100)

    # Entorno de variables
    entorno = {variable_x: x_vals}
    entorno.update(parametros)

    try:
        y_vals = eval(derecha, {}, entorno)

        plt.figure()
        plt.plot(x_vals, y_vals)
        plt.xlabel(variable_x)
        plt.ylabel(izquierda.strip())
        plt.title(ecuacion)
        plt.grid()
        plt.show()

    except Exception as e:
        print("Error al graficar:", e)


def interfaz_grafica_basica(pregunta):
    """
    Flujo interactivo simple para el estudiante
    """

    ecuaciones = filtrar_ecuaciones_por_pregunta(pregunta)

    if not ecuaciones:
        print("No se encontraron ecuaciones graficables.")
        return

    print("\nEcuaciones disponibles:\n")

    for i, eq in enumerate(ecuaciones):
        print(f"{i}: {eq['eq']} | variables: {eq['variables']}")

    # Selección
    idx = int(input("\nSelecciona el número de la ecuación: "))
    eq_sel = ecuaciones[idx]

    # Variable independiente
    variable_x = input("¿Qué variable deseas graficar en el eje x?: ")

    # Pedir valores de parámetros
    parametros = {}

    for var in eq_sel["variables"]:
        if var != variable_x:
            valor = float(input(f"Valor para {var}: "))
            parametros[var] = valor

    graficar_desde_ecuacion(eq_sel, variable_x, parametros)
