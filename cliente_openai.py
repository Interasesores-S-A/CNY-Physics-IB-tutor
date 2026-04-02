from openai import OpenAI
import os

# Correcto: obtiene la variable de entorno
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def preguntar_chatgpt(mensaje_usuario, modelo="gpt-4o-mini"):
    response = client.chat.completions.create(
        model=modelo,
        messages=[
            {"role": "user", "content": mensaje_usuario}
        ]
    )
    return response.choices[0].message.content
