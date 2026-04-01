
import ipywidgets as widgets
from IPython.display import display, clear_output

from tutor_ib import tutor_ib_fisica
from graficador_ui import crear_interfaz_grafica
from simulador_fisica import simulacion_movimiento
from cliente_openai import preguntar_chatgpt


# =========================
# 🧠 TAB 1: TUTOR IB
# =========================

def tab_tutor():

    pregunta = widgets.Textarea(
        placeholder="Escribe tu pregunta de Física IB...",
        layout=widgets.Layout(width='100%', height='100px')
    )

    boton = widgets.Button(description="Analizar", button_style='success')
    salida = widgets.Output()

    def ejecutar(b):
        with salida:
            clear_output()

            if not pregunta.value.strip():
                print("⚠️ Escribe una pregunta.")
                return

            print("🧠 Analizando...\n")
            print(tutor_ib_fisica(pregunta.value))

    boton.on_click(ejecutar)

    return widgets.VBox([
        widgets.HTML("<h3>🧠 Tutor IB</h3>"),
        pregunta,
        boton,
        salida
    ])


# =========================
# 📊 TAB 2: GRAFICADOR
# =========================

def tab_grafica():

    pregunta = widgets.Textarea(
        placeholder="Ej: movimiento con aceleración constante",
        layout=widgets.Layout(width='100%', height='80px')
    )

    boton = widgets.Button(description="Generar graficador", button_style='info')
    salida = widgets.Output()

    def ejecutar(b):
        with salida:
            clear_output()
            crear_interfaz_grafica(pregunta.value)

    boton.on_click(ejecutar)

    return widgets.VBox([
        widgets.HTML("<h3>📊 Graficador</h3>"),
        pregunta,
        boton,
        salida
    ])


# =========================
# 🎛️ TAB 3: SIMULADOR
# =========================

def tab_simulador():

    contenedor = widgets.Output()

    with contenedor:
        simulacion_movimiento()

    return widgets.VBox([
        widgets.HTML("<h3>🎛️ Simulación Física</h3>"),
        contenedor
    ])


# =========================
# 🧪 TAB 4: GENERADOR IB
# =========================

def tab_generador():

    tema = widgets.Text(
        placeholder="Ej: cinemática, energía...",
        layout=widgets.Layout(width='100%')
    )

    boton = widgets.Button(description="Generar pregunta", button_style='warning')
    salida = widgets.Output()

    def ejecutar(b):
        with salida:
            clear_output()

            if not tema.value.strip():
                print("⚠️ Escribe un tema.")
                return

            prompt = f"""
Genera una pregunta tipo examen de Física IB sobre el tema: {tema.value}.
Incluye:
- Enunciado
- Tipo (Paper 1 o Paper 2)
- Nivel de dificultad
NO incluyas solución.
"""
            print(preguntar_chatgpt(prompt))

    boton.on_click(ejecutar)

    return widgets.VBox([
        widgets.HTML("<h3>🧪 Generador IB</h3>"),
        tema,
        boton,
        salida
    ])


# =========================
# 🚀 APP PRINCIPAL
# =========================

def lanzar_app():

    tabs = widgets.Tab()

    tab1 = tab_tutor()
    tab2 = tab_grafica()
    tab3 = tab_simulador()
    tab4 = tab_generador()

    tabs.children = [tab1, tab2, tab3, tab4]

    tabs.set_title(0, "Tutor")
    tabs.set_title(1, "Graficador")
    tabs.set_title(2, "Simulador")
    tabs.set_title(3, "Generador")

    display(widgets.HTML("<h2>🚀 Plataforma IB de Física</h2>"))
    display(tabs)
