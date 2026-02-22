"""
Test rapido para verificar que todo funcione correctamente
"""
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv(override=True)

# Verificar API key
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    print("ERROR: No se encontro GROQ_API_KEY en el archivo .env")
    print("Por favor, configura tu API key en el archivo .env")
    exit(1)

print("API Key encontrada!")
print(f"Primeros caracteres: {api_key[:10]}...")

# Intentar importar las librerias
try:
    from langchain_groq import ChatGroq
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_core.output_parsers import StrOutputParser
    print("\nTodas las librerias importadas correctamente")
except ImportError as e:
    print(f"\nERROR al importar: {e}")
    print("Ejecuta: pip install -r requirements.txt")
    exit(1)

# Test rapido con el LLM
print("\nProbando conexion con Groq...")
try:
    llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7)
    respuesta = llm.invoke("Di 'Hola, funciona!'")
    print(f"\nRespuesta del LLM: {respuesta.content}")
    print("\nTODO FUNCIONA CORRECTAMENTE!")
except Exception as e:
    print(f"\nERROR al conectar con Groq: {e}")
    print("\nPosibles soluciones:")
    print("1. Verifica que tu API key de Groq sea valida")
    print("2. Obten una API key gratis en: https://console.groq.com")
