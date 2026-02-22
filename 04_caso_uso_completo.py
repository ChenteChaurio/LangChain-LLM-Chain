"""
Ejemplo 4: Caso de Uso Completo - Asistente de Análisis de Código
Este script demuestra un caso de uso práctico que combina todos los conceptos:
prompts, chains, y output parsers para crear un asistente de análisis de código.
"""

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field

# Cargar variables de entorno
load_dotenv(override=True)


# Modelos de datos para el análisis
class AnalisisCalidad(BaseModel):
    """Modelo para el análisis de calidad del código."""
    puntuacion: int = Field(description="Puntuación de calidad del código (0-10)")
    puntos_fuertes: list = Field(description="Aspectos positivos del código")
    puntos_mejora: list = Field(description="Aspectos que se pueden mejorar")
    complejidad: str = Field(description="Nivel de complejidad: Baja, Media, Alta")


class SugerenciaMejora(BaseModel):
    """Modelo para sugerencias de mejora del código."""
    problema: str = Field(description="Problema identificado")
    solucion: str = Field(description="Solución propuesta")
    codigo_mejorado: str = Field(description="Fragmento de código mejorado")


class AnalistaCodigoLangChain:
    """Asistente de análisis de código usando LangChain."""
    
    def __init__(self):
        """Inicializa el analista con el LLM y las chains necesarias."""
        
        if not os.getenv("GROQ_API_KEY"):
            raise ValueError("Por favor configura GROQ_API_KEY en el archivo .env")
        
        self.llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.3)
        
        # Chain para análisis de calidad
        self.parser_calidad = JsonOutputParser(pydantic_object=AnalisisCalidad)
        self.prompt_calidad = ChatPromptTemplate.from_messages([
            ("system", """Eres un experto revisor de código. 
            Analiza el código proporcionado y evalúa su calidad.
            Responde en formato JSON."""),
            ("human", "{codigo}\n\n{format_instructions}")
        ])
        self.chain_calidad = self.prompt_calidad | self.llm | self.parser_calidad
        
        # Chain para generar sugerencias
        self.parser_sugerencias = JsonOutputParser(pydantic_object=SugerenciaMejora)
        self.prompt_sugerencias = ChatPromptTemplate.from_messages([
            ("system", """Eres un mentor de programación experto.
            Identifica UN problema principal en el código y proporciona una solución.
            Responde en formato JSON."""),
            ("human", "{codigo}\n\n{format_instructions}")
        ])
        self.chain_sugerencias = self.prompt_sugerencias | self.llm | self.parser_sugerencias
        
        # Chain para documentación
        self.prompt_documentacion = ChatPromptTemplate.from_template(
            """Genera una documentación completa para el siguiente código.
            Incluye:
            - Descripción general
            - Parámetros (si aplica)
            - Valor de retorno (si aplica)
            - Ejemplo de uso
            
            Código:
            {codigo}
            """
        )
        from langchain_core.output_parsers import StrOutputParser
        self.chain_documentacion = self.prompt_documentacion | self.llm | StrOutputParser()
    
    def analizar_calidad(self, codigo: str) -> dict:
        """
        Analiza la calidad del código proporcionado.
        
        Args:
            codigo: Código fuente a analizar
            
        Returns:
            Diccionario con el análisis de calidad
        """
        return self.chain_calidad.invoke({
            "codigo": codigo,
            "format_instructions": self.parser_calidad.get_format_instructions()
        })
    
    def obtener_sugerencias(self, codigo: str) -> dict:
        """
        Obtiene sugerencias de mejora para el código.
        
        Args:
            codigo: Código fuente a mejorar
            
        Returns:
            Diccionario con sugerencias de mejora
        """
        return self.chain_sugerencias.invoke({
            "codigo": codigo,
            "format_instructions": self.parser_sugerencias.get_format_instructions()
        })
    
    def generar_documentacion(self, codigo: str) -> str:
        """
        Genera documentación para el código proporcionado.
        
        Args:
            codigo: Código fuente a documentar
            
        Returns:
            Documentación generada
        """
        return self.chain_documentacion.invoke({"codigo": codigo})
    
    def analisis_completo(self, codigo: str):
        """
        Realiza un análisis completo del código.
        
        Args:
            codigo: Código fuente a analizar
        """
        print("=" * 70)
        print("🔍 ANÁLISIS COMPLETO DE CÓDIGO")
        print("=" * 70)
        print(f"\nCódigo a analizar:\n{'-' * 70}")
        print(codigo)
        print("-" * 70)
        
        # 1. Análisis de calidad
        print("\n📊 ANÁLISIS DE CALIDAD")
        print("-" * 70)
        calidad = self.analizar_calidad(codigo)
        print(f"Puntuación: {calidad['puntuacion']}/10")
        print(f"Complejidad: {calidad['complejidad']}")
        print("\nPuntos Fuertes:")
        for punto in calidad['puntos_fuertes']:
            print(f"   - {punto}")
        print("\nPuntos de Mejora:")
        for punto in calidad['puntos_mejora']:
            print(f"   • {punto}")
        
        # 2. Sugerencias de mejora
        print("\n" + "-" * 70)
        print("💡 SUGERENCIAS DE MEJORA")
        print("-" * 70)
        sugerencia = self.obtener_sugerencias(codigo)
        print(f"Problema: {sugerencia['problema']}")
        print(f"Solución: {sugerencia['solucion']}")
        print("\nCodigo Mejorado:")
        print(sugerencia['codigo_mejorado'])
        
        # 3. Documentación
        print("\n" + "-" * 70)
        print("📚 DOCUMENTACIÓN GENERADA")
        print("-" * 70)
        documentacion = self.generar_documentacion(codigo)
        print(documentacion)
        
        print("\n" + "=" * 70)
        print("✨ ANÁLISIS COMPLETADO")
        print("=" * 70)


def ejemplo_codigo_simple():
    """Analiza un ejemplo de código simple."""
    
    codigo = """
def calcular(a, b):
    return a + b
    """
    
    analista = AnalistaCodigoLangChain()
    analista.analisis_completo(codigo)


def ejemplo_codigo_complejo():
    """Analiza un ejemplo de código más complejo."""
    
    codigo = """
def procesar_usuarios(usuarios):
    resultado = []
    for i in range(len(usuarios)):
        if usuarios[i]['edad'] >= 18:
            nombre = usuarios[i]['nombre']
            email = usuarios[i]['email']
            resultado.append({'nombre': nombre, 'email': email})
    return resultado
    """
    
    print("\n\n")
    analista = AnalistaCodigoLangChain()
    analista.analisis_completo(codigo)


def main():
    """Ejecuta los ejemplos de análisis de código."""
    
    print("╔" + "=" * 68 + "╗")
    print("║" + " " * 10 + "ASISTENTE DE ANÁLISIS DE CÓDIGO CON LANGCHAIN" + " " * 12 + "║")
    print("╚" + "=" * 68 + "╝")
    print()
    
    # Ejemplo 1: Código simple
    ejemplo_codigo_simple()
    
    # Ejemplo 2: Código más complejo
    ejemplo_codigo_complejo()


if __name__ == "__main__":
    main()
