"""
Ejemplo 3: Chains y Output Parsers con LangChain
Este script demuestra cómo encadenar componentes (chains) y 
parsear las salidas del LLM en formatos estructurados.
"""

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from pydantic import BaseModel, Field

# Cargar variables de entorno
load_dotenv(override=True)


def ejemplo_chain_basico():
    """Demuestra el uso básico de chains con el operador |."""
    
    print("=" * 60)
    print("EJEMPLO 1: CHAIN BÁSICO (PROMPT | LLM | PARSER)")
    print("=" * 60)
    
    # Componentes de la chain
    prompt = ChatPromptTemplate.from_template(
        "Dame {numero} datos curiosos sobre {tema}"
    )
    llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.9)
    output_parser = StrOutputParser()
    
    # Crear la chain usando el operador |
    chain = prompt | llm | output_parser
    
    # Invocar la chain
    resultado = chain.invoke({
        "numero": "3",
        "tema": "Python"
    })
    
    print(f"\nResultado:\n{resultado}\n")


def ejemplo_json_parser():
    """Demuestra el uso de JsonOutputParser para obtener respuestas estructuradas."""
    
    print("=" * 60)
    print("EJEMPLO 2: JSON OUTPUT PARSER")
    print("=" * 60)
    
    # Definir el schema con Pydantic
    class Libro(BaseModel):
        titulo: str = Field(description="Título del libro")
        autor: str = Field(description="Autor del libro")
        año: int = Field(description="Año de publicación")
        genero: str = Field(description="Género literario")
        resumen: str = Field(description="Breve resumen del libro")
    
    # Crear el parser
    parser = JsonOutputParser(pydantic_object=Libro)
    
    # Crear el prompt con instrucciones de formato
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Eres un experto en literatura. Responde en formato JSON."),
        ("human", "{query}\n\n{format_instructions}")
    ])
    
    llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7)
    
    # Crear la chain
    chain = prompt | llm | parser
    
    # Invocar la chain
    resultado = chain.invoke({
        "query": "Dame información sobre el libro '1984' de George Orwell",
        "format_instructions": parser.get_format_instructions()
    })
    
    print(f"\nResultado parseado (tipo: {type(resultado)}):")
    print(f"Título: {resultado['titulo']}")
    print(f"Autor: {resultado['autor']}")
    print(f"Año: {resultado['año']}")
    print(f"Género: {resultado['genero']}")
    print(f"Resumen: {resultado['resumen']}\n")


def ejemplo_chain_secuencial():
    """Demuestra cómo encadenar múltiples chains de forma secuencial."""
    
    print("=" * 60)
    print("EJEMPLO 3: CHAIN SECUENCIAL")
    print("=" * 60)
    
    llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7)
    
    # Primera chain: Genera un concepto técnico
    prompt_concepto = ChatPromptTemplate.from_template(
        "Dame el nombre de un concepto avanzado de {tema}. Responde solo con el nombre del concepto."
    )
    chain_concepto = prompt_concepto | llm | StrOutputParser()
    
    # Segunda chain: Explica el concepto
    prompt_explicacion = ChatPromptTemplate.from_template(
        "Explica el concepto '{concepto}' en 3 líneas."
    )
    chain_explicacion = prompt_explicacion | llm | StrOutputParser()
    
    # Ejecutar las chains secuencialmente
    tema = "machine learning"
    print(f"\nTema seleccionado: {tema}")
    
    concepto = chain_concepto.invoke({"tema": tema})
    print(f"\nConcepto generado: {concepto}")
    
    explicacion = chain_explicacion.invoke({"concepto": concepto})
    print(f"\nExplicación:\n{explicacion}\n")


def ejemplo_chain_con_lista():
    """Demuestra cómo procesar listas de datos con chains."""
    
    print("=" * 60)
    print("EJEMPLO 4: BATCH PROCESSING CON CHAINS")
    print("=" * 60)
    
    prompt = ChatPromptTemplate.from_template(
        "Traduce '{palabra}' del español al inglés. Responde solo con la traducción."
    )
    llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.3)
    chain = prompt | llm | StrOutputParser()
    
    # Procesar múltiples palabras
    palabras = [
        {"palabra": "computadora"},
        {"palabra": "aprendizaje"},
        {"palabra": "inteligencia"},
        {"palabra": "algoritmo"}
    ]
    
    # Batch processing
    traducciones = chain.batch(palabras)
    
    print("\nTraducciones:")
    for i, (original, traduccion) in enumerate(zip(palabras, traducciones), 1):
        print(f"{i}. {original['palabra']} → {traduccion}")
    print()


def ejemplo_chain_con_multiple_parsers():
    """Demuestra el uso de diferentes parsers en una chain."""
    
    print("=" * 60)
    print("EJEMPLO 5: CHAIN CON RESPUESTAS ESTRUCTURADAS")
    print("=" * 60)
    
    # Definir el modelo de datos
    class RecetaCocina(BaseModel):
        nombre: str = Field(description="Nombre de la receta")
        ingredientes: list = Field(description="Lista de ingredientes")
        pasos: list = Field(description="Pasos de preparación")
        tiempo_minutos: int = Field(description="Tiempo de preparación en minutos")
    
    parser = JsonOutputParser(pydantic_object=RecetaCocina)
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Eres un chef profesional. Proporciona recetas en formato JSON."),
        ("human", "Dame una receta simple de {plato}.\n\n{format_instructions}")
    ])
    
    llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7)
    chain = prompt | llm | parser
    
    resultado = chain.invoke({
        "plato": "pasta carbonara",
        "format_instructions": parser.get_format_instructions()
    })
    
    print(f"\n📝 Receta: {resultado['nombre']}")
    print(f"⏱️  Tiempo: {resultado['tiempo_minutos']} minutos")
    print("\nIngredientes:")
    for ing in resultado['ingredientes']:
        print(f"  - {ing}")
    print("\nPasos:")
    for i, paso in enumerate(resultado['pasos'], 1):
        print(f"  {i}. {paso}")
    print()


def main():
    """Ejecuta todos los ejemplos."""
    
    if not os.getenv("GROQ_API_KEY"):
        raise ValueError("Por favor configura GROQ_API_KEY en el archivo .env")
    
    ejemplo_chain_basico()
    ejemplo_json_parser()
    ejemplo_chain_secuencial()
    ejemplo_chain_con_lista()
    ejemplo_chain_con_multiple_parsers()
    
    print("=" * 60)
    print("TODOS LOS EJEMPLOS COMPLETADOS")
    print("=" * 60)


if __name__ == "__main__":
    main()
