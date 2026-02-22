# LangChain LLM Chain - Tutorial Basico

![LangChain](https://img.shields.io/badge/LangChain-0.1.0-blue)
![Groq](https://img.shields.io/badge/Groq-LLaMA3-orange)
![Python](https://img.shields.io/badge/Python-3.8%2B-yellow)

## Descripcion

Este repositorio contiene una implementacion completa del tutorial basico de **LangChain LLM Chain**, desarrollado como parte del laboratorio de introduccion a Generadores de Recuperacion Aumentada (RAG). El proyecto demuestra los conceptos fundamentales de LangChain, incluyendo el uso de modelos de lenguaje (LLM), prompt templates, chains y output parsers.

## Arquitectura del Proyecto

### Componentes Principales

```
LangChain-LLM-Chain/
│
├── 01_basic_llm.py              # Uso basico de LLM con Groq
├── 02_prompt_templates.py       # Templates de prompts y formateo
├── 03_chains_parsers.py         # Chains y parsers de salida
├── 04_caso_uso_completo.py      # Caso de uso completo: Analizador de codigo
├── requirements.txt             # Dependencias del proyecto
├── .env.example                 # Ejemplo de variables de entorno
├── .gitignore                   # Archivos ignorados por git
└── README.md                    # Este archivo
```

### Arquitectura de Componentes

```
┌─────────────────────────────────────────────────────────┐
│                    Aplicacion Python                     │
└─────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────┐
│                      LangChain                           │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │   Prompts    │→ │    Chains    │→ │   Parsers    │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
└─────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────┐
│                  Groq API (LLaMA-3.3-70b)               │
└─────────────────────────────────────────────────────────┘
```

### Flujo de Datos

1. **Prompt Template**: Define la estructura de la consulta
2. **LLM (Large Language Model)**: Procesa la consulta con LLaMA-3.3-70b via Groq
3. **Output Parser**: Estructura la respuesta en el formato deseado
4. **Chain**: Conecta todos los componentes en un flujo unificado

## Instalacion y Configuracion

### Prerrequisitos

- Python 3.8 o superior
- Una cuenta de Groq con API key (gratuita en https://console.groq.com)
- Git (para clonar el repositorio)

### Paso 1: Clonar el Repositorio

```bash
git clone https://github.com/TU-USUARIO/LangChain-LLM-Chain.git
cd LangChain-LLM-Chain
```

### Paso 2: Crear un Entorno Virtual (Recomendado)

**En Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**En Linux/Mac:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### Paso 3: Instalar Dependencias

```bash
pip install -r requirements.txt
```

### Paso 4: Configurar Variables de Entorno

1. Copia el archivo `.env.example` a `.env`:

   ```bash
   copy .env.example .env    # Windows
   cp .env.example .env      # Linux/Mac
   ```

2. Edita el archivo `.env` y agrega tu API key de Groq:

   ```
   GROQ_API_KEY=gsk-tu-api-key-aqui
   ```

3. Para obtener tu API key:
   - Ve a https://console.groq.com
   - Inicia sesion o crea una cuenta (es gratuita)
   - En API Keys, crea una nueva key
   - Copia y pega la key en el archivo `.env`

## Ejemplos y Uso

### Ejemplo 1: Uso Basico de LLM

Este ejemplo demuestra como interactuar con un modelo de lenguaje de Groq (LLaMA).

```bash
python 01_basic_llm.py
```

**Caracteristicas:**

- Invocacion simple del LLM
- Conversaciones con multiples mensajes
- Streaming de respuestas en tiempo real

**Codigo de ejemplo:**

```python
from langchain_groq import ChatGroq

llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7)
respuesta = llm.invoke("¿Que es LangChain?")
print(respuesta.content)
```

### Ejemplo 2: Prompt Templates

Este ejemplo muestra como crear templates reutilizables para prompts.

```bash
python 02_prompt_templates.py
```

**Caracteristicas:**

- Templates simples con variables
- Chat prompt templates con contexto
- Templates reutilizables para multiples casos
- Generacion de codigo con templates

### Ejemplo 3: Chains y Output Parsers

Este ejemplo demuestra como encadenar componentes y parsear salidas estructuradas.

```bash
python 03_chains_parsers.py
```

**Caracteristicas:**

- Chains basicas con el operador `|`
- JSON output parsers con Pydantic
- Chains secuenciales
- Batch processing
- Respuestas estructuradas

### Ejemplo 4: Caso de Uso Completo - Asistente de Analisis de Codigo

Este ejemplo integra todos los conceptos en un asistente practico.

```bash
python 04_caso_uso_completo.py
```

**Caracteristicas:**

- Analisis de calidad de codigo
- Sugerencias de mejora automatizadas
- Generacion de documentacion
- Multiples chains trabajando en conjunto

## Conceptos Clave Aprendidos

### 1. LLM (Large Language Model)

- Uso de modelos de Groq (LLaMA-3.3-70b)
- Configuracion de temperatura y parametros
- Invocacion simple y streaming

### 2. Prompt Templates

- Creacion de templates reutilizables
- Variables dinamicas en prompts
- System y Human messages
- Formateo de conversaciones

### 3. Chains

- Encadenamiento con operador `|`
- Chains secuenciales
- Batch processing
- Composicion de multiples chains

### 4. Output Parsers

- String output parser
- JSON output parser
- Pydantic models para validacion
- Respuestas estructuradas

### 5. Integracion

- Combinacion de todos los componentes
- Casos de uso practicos
- Manejo de errores
- Best practices

## Estructura de Dependencias

```
langchain>=0.1.0              # Framework principal
langchain-groq>=1.1.0         # Integracion con Groq
langchain-core>=0.1.10        # Componentes core de LangChain
python-dotenv>=1.0.0          # Manejo de variables de entorno
```

## Solucion de Problemas

### Error: "No module named 'langchain'"

**Solucion:** Asegurate de haber activado el entorno virtual e instalado las dependencias:

```bash
pip install -r requirements.txt
```

### Error: "Groq API key not found"

**Solucion:** Verifica que el archivo `.env` exista y contenga tu API key:

```bash
GROQ_API_KEY=gsk-tu-key-aqui
```

### Error: "Rate limit exceeded"

**Solucion:** Has excedido el limite de la API de Groq. Espera unos minutos (el tier gratuito tiene limites por minuto).

### Error: "Invalid API key"

**Solucion:** Verifica que tu API key sea correcta y este activa en https://console.groq.com

## Recursos Adicionales

- [Documentacion oficial de LangChain](https://python.langchain.com/docs/)
- [LangChain LLM Chain Tutorial](https://docs.langchain.com/oss/python/langchain/quickstart)
- [Groq API Documentation](https://console.groq.com/docs)
- [Pydantic Documentation](https://docs.pydantic.dev/)

## Proximos Pasos

Este repositorio es la **Parte 1** del laboratorio. La **Parte 2** incluira:

1. **RAG (Retrieval Augmented Generation)** con LangChain
2. **Pinecone** como base de datos vectorial
3. **Embeddings** para vectorizacion de documentos
4. **Busqueda semantica** y recuperacion de documentos
5. Integracion completa de RAG

## Autor

Desarrollado como parte del laboratorio de AREP - Introduccion a RAG con LangChain y Groq

## Licencia

Este proyecto es de codigo abierto y esta disponible para fines educativos.

---

Si este repositorio te fue util, no olvides darle una estrella en GitHub!
