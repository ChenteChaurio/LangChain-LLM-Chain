"""
Script de Inicio Rápido - LangChain LLM Chain
Este script te permite probar rápidamente LangChain con un ejemplo interactivo.
"""

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

def verificar_configuracion():
    """Verifica que todo esté configurado correctamente."""
    
    load_dotenv(override=True)
    
    if not os.getenv("GROQ_API_KEY"):
        print("ERROR: No se encontro GROQ_API_KEY")
        print("\nPara configurar:")
        print("1. Copia .env.example a .env")
        print("2. Agrega tu API key de Groq en el archivo .env")
        print("3. Obten tu API key GRATIS en: https://console.groq.com")
        return False
    
    print("Configuracion correcta\n")
    return True


def ejemplo_interactivo():
    """Ejemplo interactivo de LangChain."""
    
    print("=" * 60)
    print("🤖 ASISTENTE LANGCHAIN - EJEMPLO INTERACTIVO")
    print("=" * 60)
    print("\nEste es un ejemplo básico de cómo funciona LangChain.")
    print("El asistente responderá tus preguntas sobre programación.\n")
    
    # Crear la chain
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Eres un asistente experto en programación que explica conceptos de forma clara y concisa."),
        ("human", "{pregunta}")
    ])
    
    llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7)
    output_parser = StrOutputParser()
    
    chain = prompt | llm | output_parser
    
    # Preguntas de ejemplo
    preguntas_ejemplo = [
        "¿Qué es una API REST?",
        "Explica qué es recursividad con un ejemplo simple",
        "¿Cuál es la diferencia entre una lista y una tupla en Python?"
    ]
    
    print("Preguntas de ejemplo:")
    for i, p in enumerate(preguntas_ejemplo, 1):
        print(f"{i}. {p}")
    
    print("\nOpciones:")
    print("- Escribe el número (1-3) para usar una pregunta de ejemplo")
    print("- Escribe tu propia pregunta")
    print("- Escribe 'salir' para terminar\n")
    
    while True:
        pregunta_usuario = input("Tu pregunta: ").strip()
        
        if pregunta_usuario.lower() in ['salir', 'exit', 'quit']:
            print("\n👋 ¡Hasta luego!")
            break
        
        # Verificar si es un número de ejemplo
        if pregunta_usuario in ['1', '2', '3']:
            pregunta = preguntas_ejemplo[int(pregunta_usuario) - 1]
            print(f"\nPregunta seleccionada: {pregunta}")
        else:
            pregunta = pregunta_usuario
        
        if not pregunta:
            continue
        
        print("\n🤔 Pensando...\n")
        
        try:
            # Invocar la chain
            respuesta = chain.invoke({"pregunta": pregunta})
            
            print("💡 Respuesta:")
            print("-" * 60)
            print(respuesta)
            print("-" * 60)
            print()
            
        except Exception as e:
            print(f"❌ Error: {e}\n")
            print("Verifica tu conexión y API key.\n")


def main():
    """Función principal."""
    
    print("\n" + "╔" + "=" * 58 + "╗")
    print("║" + " " * 15 + "LANGCHAIN - INICIO RÁPIDO" + " " * 18 + "║")
    print("╚" + "=" * 58 + "╝\n")
    
    if not verificar_configuracion():
        return
    
    print("Selecciona una opción:")
    print("1. Ejemplo interactivo (recomendado)")
    print("2. Ejecutar todos los ejemplos del tutorial")
    print("3. Salir\n")
    
    opcion = input("Opción (1-3): ").strip()
    
    if opcion == "1":
        print()
        ejemplo_interactivo()
    
    elif opcion == "2":
        print("\n📚 Ejecutando todos los ejemplos...\n")
        print("Consejo: Puedes ejecutar cada ejemplo individualmente:")
        print("  • python 01_basic_llm.py")
        print("  • python 02_prompt_templates.py")
        print("  • python 03_chains_parsers.py")
        print("  • python 04_caso_uso_completo.py\n")
        
        respuesta = input("¿Continuar? (s/n): ").strip().lower()
        if respuesta == 's':
            import subprocess
            ejemplos = [
                "01_basic_llm.py",
                "02_prompt_templates.py",
                "03_chains_parsers.py",
                "04_caso_uso_completo.py"
            ]
            for ejemplo in ejemplos:
                print(f"\n{'='*60}")
                print(f"Ejecutando: {ejemplo}")
                print('='*60)
                subprocess.run(["python", ejemplo])
                input("\nPresiona Enter para continuar al siguiente ejemplo...")
    
    elif opcion == "3":
        print("\n👋 ¡Hasta luego!")
    
    else:
        print("\n❌ Opción no válida")


if __name__ == "__main__":
    main()
