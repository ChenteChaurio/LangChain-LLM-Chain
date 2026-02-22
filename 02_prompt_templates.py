"""
Ejemplo 2: Prompt Templates con LangChain
Este script demuestra cómo usar templates de prompts para crear 
interacciones más estructuradas con el LLM.
"""

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate

# Cargar variables de entorno
load_dotenv(override=True)

def ejemplo_prompt_simple():
    """Demuestra el uso de un prompt template simple."""
    
    print("=" * 60)
    print("EJEMPLO 1: PROMPT TEMPLATE SIMPLE")
    print("=" * 60)
    
    # Crear un template simple
    template = PromptTemplate.from_template(
        "Eres un experto en {tema}. Explica {concepto} en términos simples."
    )
    
    # Formatear el prompt con valores específicos
    prompt_formateado = template.format(
        tema="inteligencia artificial",
        concepto="redes neuronales"
    )
    
    print(f"\nPrompt formateado:\n{prompt_formateado}\n")
    
    # Usar el prompt con el LLM
    llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7)
    respuesta = llm.invoke(prompt_formateado)
    
    print(f"Respuesta:\n{respuesta.content}\n")


def ejemplo_chat_prompt_template():
    """Demuestra el uso de ChatPromptTemplate para conversaciones estructuradas."""
    
    print("=" * 60)
    print("EJEMPLO 2: CHAT PROMPT TEMPLATE")
    print("=" * 60)
    
    # Crear un template de chat con múltiples mensajes
    template_chat = ChatPromptTemplate.from_messages([
        ("system", "Eres un {profesion} muy experimentado y amigable."),
        ("human", "Tengo una pregunta sobre {tema}"),
        ("human", "{pregunta}")
    ])
    
    # Formatear los mensajes
    mensajes = template_chat.format_messages(
        profesion="desarrollador de software senior",
        tema="patrones de diseño",
        pregunta="¿Cuál es la diferencia entre Factory y Abstract Factory?"
    )
    
    print("\nMensajes formateados:")
    for msg in mensajes:
        print(f"{msg.__class__.__name__}: {msg.content}")
    
    # Invocar el LLM
    llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7)
    respuesta = llm.invoke(mensajes)
    
    print(f"\nRespuesta:\n{respuesta.content}\n")


def ejemplo_prompt_con_variables_multiples():
    """Demuestra el uso de templates con múltiples variables."""
    
    print("=" * 60)
    print("EJEMPLO 3: TEMPLATE CON VARIABLES MÚLTIPLES")
    print("=" * 60)
    
    # Template para generar código
    template_codigo = ChatPromptTemplate.from_messages([
        ("system", "Eres un experto programador en {lenguaje}."),
        ("human", """Genera una función {tipo_funcion} que:
        - Nombre: {nombre_funcion}
        - Propósito: {proposito}
        - Debe incluir comentarios y seguir las mejores prácticas.
        """)
    ])
    
    # Formatear el template
    prompt = template_codigo.format_messages(
        lenguaje="Python",
        tipo_funcion="recursiva",
        nombre_funcion="fibonacci",
        proposito="calcular el n-ésimo número de la secuencia de Fibonacci"
    )
    
    # Invocar el LLM
    llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.3)
    respuesta = llm.invoke(prompt)
    
    print(f"\nCódigo generado:\n{respuesta.content}\n")


def ejemplo_prompt_reutilizable():
    """Demuestra cómo crear y reutilizar un prompt template."""
    
    print("=" * 60)
    print("EJEMPLO 4: PROMPT REUTILIZABLE")
    print("=" * 60)
    
    # Crear un template reutilizable para traducción
    template_traduccion = ChatPromptTemplate.from_messages([
        ("system", "Eres un traductor profesional."),
        ("human", "Traduce el siguiente texto de {idioma_origen} a {idioma_destino}:\n\n{texto}")
    ])
    
    llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.3)
    
    # Usar el mismo template para diferentes traducciones
    traducciones = [
        {
            "idioma_origen": "español",
            "idioma_destino": "inglés",
            "texto": "La inteligencia artificial está transformando el mundo."
        },
        {
            "idioma_origen": "inglés",
            "idioma_destino": "francés",
            "texto": "Machine learning is a subset of artificial intelligence."
        }
    ]
    
    for i, params in enumerate(traducciones, 1):
        print(f"\n--- Traducción {i} ---")
        print(f"Original ({params['idioma_origen']}): {params['texto']}")
        
        mensajes = template_traduccion.format_messages(**params)
        respuesta = llm.invoke(mensajes)
        
        print(f"Traducido ({params['idioma_destino']}): {respuesta.content}")


def main():
    """Ejecuta todos los ejemplos."""
    
    if not os.getenv("GROQ_API_KEY"):
        raise ValueError("Por favor configura GROQ_API_KEY en el archivo .env")
    
    ejemplo_prompt_simple()
    ejemplo_chat_prompt_template()
    ejemplo_prompt_con_variables_multiples()
    ejemplo_prompt_reutilizable()
    
    print("\n" + "=" * 60)
    print("EJEMPLOS COMPLETADOS")
    print("=" * 60)


if __name__ == "__main__":
    main()
