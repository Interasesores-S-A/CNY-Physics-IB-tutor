
import numpy as np
import matplotlib.pyplot as plt
from ecuaciones_ib import ecuaciones_ib
import ipywidgets as widgets
from IPython.display import display, clear_output


def obtener_ecuaciones_graficables(pregunta):
    resultados = []

    for tema, ecuaciones in ecuaciones_ib.items():
        for eq in ecuaciones:
            if eq["graficable"]:
                for var in eq["variables"]:
                    if var.lower() in pregunta.lower():
                        resultados.append(eq)

    return resultados


def variables_validas(eq):
    izquierda, derecha = eq["eq"].split("=")
    return [var for var in eq["variables"] if var in derecha]


def crear_interfaz_grafica(pregunta):

    ecuaciones = obtener_ecuaciones_graficables(pregunta)

    if not ecuaciones:
        display(widgets.HTML("<b>No hay ecuaciones graficables.</b>"))
        return

    dropdown_eq = widgets.Dropdown(
        options=[(eq["eq"], i) for i, eq in enumerate(ecuaciones)],
        description="Ecuación:",
        layout=widgets.Layout(width='80%')
    )

    dropdown_x = widgets.Dropdown(description="Eje x:")
    sliders_box = widgets.VBox()
    output = widgets.Output()

    def actualizar_sliders(change=None):
        eq = ecuaciones[dropdown_eq.value]

        vars_validas = variables_validas(eq)
        if not vars_validas:
            vars_validas = eq["variables"]

        dropdown_x.options = vars_validas

        sliders = []
        for var in eq["variables"]:
            slider = widgets.FloatSlider(
                value=1,
                min=-10,
                max=10,
                step=0.5,
                description=var,
                continuous_update=False
            )
            sliders.append(slider)

        sliders_box.children = sliders

        for slider in sliders:
            slider.observe(actualizar_grafica, names='value')

        actualizar_grafica()

    def actualizar_grafica(*args):

        output.clear_output(wait=True)

        with output:

            eq = ecuaciones[dropdown_eq.value]
            izquierda, derecha = eq["eq"].split("=")
            var_x = dropdown_x.value

            if var_x not in derecha:
                print(f"⚠️ '{var_x}' no es variable independiente válida.")
                return

            x_vals = np.linspace(0, 10, 100)

            entorno = {var_x: x_vals}

            for slider in sliders_box.children:
                if slider.description != var_x:
                    entorno[slider.description] = slider.value

            try:
                y_vals = eval(derecha, {"np": np}, entorno)

                # 🔥 FIX DEFINITIVO dimensiones
                if np.isscalar(y_vals):
                    y_vals = np.full_like(x_vals, y_vals)
                elif len(np.atleast_1d(y_vals)) != len(x_vals):
                    y_vals = np.full_like(x_vals, np.atleast_1d(y_vals)[0])

                # 🔥 SOLO UNA FIGURA (sin display manual)
                plt.plot(x_vals, y_vals)
                plt.xlabel(var_x)
                plt.ylabel(izquierda.strip())
                plt.title(eq["eq"])
                plt.grid()

                plt.show()
                plt.clf()  # limpia la figura después de mostrar

            except Exception as e:
                print("Error al graficar:", e)

    dropdown_eq.observe(actualizar_sliders, names='value')
    dropdown_x.observe(actualizar_grafica, names='value')

    actualizar_sliders()

    ui = widgets.VBox([
        widgets.HTML("<h3>📊 Graficador IB Interactivo</h3>"),
        dropdown_eq,
        dropdown_x,
        sliders_box,
        output
    ])

    display(ui)
