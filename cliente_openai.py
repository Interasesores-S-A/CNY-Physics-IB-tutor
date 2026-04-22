from openai import OpenAI
import os
import streamlit as st

# Prioridad 1: Secretos de Streamlit (App settings)
# Prioridad 2: Variable de entorno del sistema
api_key = st.secrets.get("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

def preguntar_chatgpt(mensaje_usuario, modelo="gpt-4o-mini"):
    if not api_key:
        return "⚠️ Error: No se encontró la API KEY de OpenAI. Asegúrate de configurarla en los 'Secrets' de la App."
    
    try:
        response = client.chat.completions.create(
            model=modelo,
            messages=[
                {"role": "user", "content": mensaje_usuario}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Error al consultar ChatGPT: {str(e)}"
