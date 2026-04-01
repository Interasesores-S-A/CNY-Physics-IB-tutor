
from cliente_openai import preguntar_chatgpt
from ecuaciones_ib import ecuaciones_ib
from graficador import interfaz_grafica_basica


def buscar_ecuaciones_relacionadas(pregunta):
    resultados = []

    for tema, lista in ecuaciones_ib.items():
        for eq in lista:
            for var in eq["variables"]:
                if var.lower() in pregunta.lower():
                    resultados.append(eq["eq"])

    return list(set(resultados))


def tutor_ib_fisica(pregunta):
    """
    Tutor IB con estructura completa de análisis tipo examen
    """

    ecuaciones = buscar_ecuaciones_relacionadas(pregunta)

    contexto_ecuaciones = ""
    if ecuaciones:
        contexto_ecuaciones = "Ecuaciones del Data Booklet potencialmente relevantes:\n"
        contexto_ecuaciones += "\n".join(ecuaciones)

    prompt = f"""
Eres un tutor experto en Física del Bachillerato Internacional (IB).

Cuando recibas una pregunta debes responder EXACTAMENTE con la siguiente estructura:

1. Clasificación de la pregunta
   - problema cuantitativo
   - pregunta conceptual
   - definición

2. Identificación del término de instrucción (command term IB).

3. Significado práctico del término de instrucción.

4. Identificación del tema del programa IB usando SOLO estas categorías:

A. Space, time and motion
A.1 Kinematics
A.2 Forces and momentum
A.3 Work, energy and power
A.4 Rigid body mechanics (HL)
A.5 Relativity (HL)

B. The particulate nature of matter
B.1 Thermal energy transfers
B.2 Greenhouse effect
B.3 Gas laws
B.4 Thermodynamics (HL)
B.5 Current and circuits

C. Wave behaviour
C.1 Simple harmonic motion
C.2 Wave model
C.3 Wave phenomena
C.4 Standing waves and resonance
C.5 Doppler effect

D. Fields
D.1 Gravitational fields
D.2 Electric and magnetic fields
D.3 Motion in electromagnetic fields
D.4 Induction (HL)

E. Nuclear and quantum
E.1 Structure of the atom
E.2 Quantum physics (HL)
E.3 Radioactive decay
E.4 Fission
E.5 Fusion and stars

5. Identifica qué ecuación del Data Booklet es relevante.

6. Estrategia general de resolución.

Pregunta:
{pregunta}

{contexto_ecuaciones}

Reglas:
- NO omitir ningún punto
- Mantener formato numerado
- Usar lenguaje claro tipo IB
- Si no hay ecuación clara, indicarlo explícitamente
"""

    respuesta = preguntar_chatgpt(prompt)

    return respuesta


def tutor_con_grafica(pregunta):
    """
    Tutor completo con opción de graficación
    """

    print("\n==============================")
    print("      TUTOR IB DE FÍSICA")
    print("==============================\n")

    respuesta = tutor_ib_fisica(pregunta)
    print(respuesta)

    opcion = input("\n¿Deseas graficar una ecuación relacionada? (si/no): ")

    if opcion.lower() == "si":
        interfaz_grafica_basica(pregunta)
