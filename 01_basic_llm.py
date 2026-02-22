"""
Ejemplo 1: Uso básico de LLM con LangChain
Este script demuestra cómo usar un modelo de lenguaje (LLM) con LangChain y Groq.
"""

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Cargar variables de entorno desde .env
load_dotenv(override=True)

# Verificar que la API key esté configurada
if not os.getenv("GROQ_API_KEY"):
    raise ValueError("Por favor configura GROQ_API_KEY en el archivo .env")

def main():
    """Función principal que demuestra el uso básico de un LLM."""
    
    # Inicializar el modelo de lenguaje
    # temperature=0.7 controla la aleatoriedad (0=determinista, 1=muy creativo)
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.7
    )
    
    # Ejemplo 1: Invocación simple
    print("=" * 60)
    print("EJEMPLO 1: INVOCACIÓN SIMPLE")
    print("=" * 60)
    
    mensaje = "¿Qué es LangChain y para qué se utiliza?"
    respuesta = llm.invoke(mensaje)
    
    print(f"\nPregunta: {mensaje}")
    print(f"\nRespuesta: {respuesta.content}")
    
    # Ejemplo 2: Múltiples mensajes
    print("\n" + "=" * 60)
    print("EJEMPLO 2: CONVERSACIÓN CON MÚLTIPLES MENSAJES")
    print("=" * 60)
    
    from langchain_core.messages import HumanMessage, SystemMessage
    
    mensajes = [
        SystemMessage(content="Eres un asistente experto en Python y desarrollo de software."),
        HumanMessage(content="Explícame qué es una función lambda en Python en 2 líneas.")
    ]
    
    respuesta = llm.invoke(mensajes)
    print(f"\nRespuesta: {respuesta.content}")
    
    # Ejemplo 3: Streaming de respuestas
    print("\n" + "=" * 60)
    print("EJEMPLO 3: STREAMING DE RESPUESTAS")
    print("=" * 60)
    
    pregunta = "Dame 3 beneficios de usar LangChain"
    print(f"\nPregunta: {pregunta}")
    print("\nRespuesta (streaming): ", end="", flush=True)
    
    for chunk in llm.stream(pregunta):
        print(chunk.content, end="", flush=True)
    
    print("\n")

if __name__ == "__main__":
    main()
