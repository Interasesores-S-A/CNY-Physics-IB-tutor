
import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display, clear_output
import time


def simulacion_movimiento():

    u_slider = widgets.FloatSlider(value=0, min=-10, max=20, step=0.5, description='u')
    a_slider = widgets.FloatSlider(value=1, min=-10, max=10, step=0.5, description='a')
    t_max_slider = widgets.FloatSlider(value=10, min=1, max=20, step=1, description='t max')

    boton = widgets.Button(description="▶ Ejecutar simulación", button_style='success')
    output = widgets.Output()

    def ejecutar(b):

        with output:
            clear_output(wait=True)

            u = u_slider.value
            a = a_slider.value
            t_max = t_max_slider.value

            t_vals = np.linspace(0, t_max, 100)
            s_vals = u * t_vals + 0.5 * a * t_vals**2

            fig, ax = plt.subplots()

            ax.set_xlim(0, t_max)
            ax.set_ylim(min(0, np.min(s_vals)), max(1, np.max(s_vals)))
            ax.set_xlabel("Tiempo (s)")
            ax.set_ylabel("Posición (m)")
            ax.set_title("Movimiento Uniformemente Acelerado")
            ax.grid()

            ax.plot(t_vals, s_vals, '--', alpha=0.5)

            punto, = ax.plot([], [], 'ro')

            for i in range(len(t_vals)):

                t = t_vals[i]
                s = s_vals[i]

                # 🔥 CORRECCIÓN REAL
                punto.set_data([t], [s])

                clear_output(wait=True)
                display(fig)

                time.sleep(0.03)

            plt.close(fig)

    boton.on_click(ejecutar)

    ui = widgets.VBox([
        widgets.HTML("<h3>Simulación MUA</h3>"),
        u_slider,
        a_slider,
        t_max_slider,
        boton,
        output
    ])

    display(ui)
