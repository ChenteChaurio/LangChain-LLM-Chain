# Arquitectura y Componentes - LangChain LLM Chain

## Arquitectura General

```
┌───────────────────────────────────────────────────────────────┐
│                     APLICACION PYTHON                          │
│                                                                │
│  ┌─────────────────────────────────────────────────────────┐  │
│  │                    LANGCHAIN FRAMEWORK                   │  │
│  │                                                          │  │
│  │  ┌─────────────┐      ┌─────────────┐      ┌─────────┐ │  │
│  │  │   PROMPT    │  →   │    CHAIN    │  →   │ PARSER  │ │  │
│  │  │  TEMPLATE   │      │             │      │         │ │  │
│  │  └─────────────┘      └─────────────┘      └─────────┘ │  │
│  │         │                     │                   │     │  │
│  │         └─────────────────────┼───────────────────┘     │  │
│  │                               ▼                         │  │
│  │                        ┌──────────────┐                 │  │
│  │                        │  LLM MODEL   │                 │  │
│  │                        │  (GPT-3.5)   │                 │  │
│  │                        └──────────────┘                 │  │
│  └─────────────────────────────────────────────────────────┘  │
│                               │                               │
│                               ▼                               │
│                    ┌─────────────────────┐                    │
│                    │    OPENAI API       │                    │
│                    └─────────────────────┘                    │
└───────────────────────────────────────────────────────────────┘
```

## Componentes Principales

### 1. Prompt Templates

**Proposito**: Estructurar y formatear consultas al LLM

```python
ChatPromptTemplate.from_messages([
    ("system", "Eres un {profesion}"),
    ("human", "{pregunta}")
])
```

**Ventajas:**

- Reutilizacion de prompts
- Separacion de logica y contenido
- Variables dinamicas
- Facil mantenimiento

### 2. LLM (Large Language Model)

**Proposito**: Procesar lenguaje natural y generar respuestas

```python
ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.7
)
```

**Parametros importantes:**

- `model`: Modelo a usar (gpt-3.5-turbo, gpt-4, etc.)
- `temperature`: Creatividad (0 = determinista, 1 = creativo)
- `max_tokens`: Longitud maxima de respuesta

### 3. Output Parsers

**Proposito**: Estructurar la salida del LLM

```python
# String Parser
StrOutputParser()

# JSON Parser
JsonOutputParser(pydantic_object=MiModelo)
```

**Tipos de parsers:**

- `StrOutputParser`: Texto plano
- `JsonOutputParser`: Datos estructurados en JSON
- `ListOutputParser`: Listas
- `DatetimeOutputParser`: Fechas

### 4. Chains

**Proposito**: Conectar componentes en flujos de trabajo

```python
chain = prompt | llm | parser
resultado = chain.invoke({"variable": "valor"})
```

**Operador `|` (pipe):**

- Conecta componentes secuencialmente
- La salida de uno es la entrada del siguiente
- Similar a pipes en Unix/Linux

## Flujo de Datos Detallado

```
1. ENTRADA DEL USUARIO
   ↓
2. PROMPT TEMPLATE
   - Formatea la entrada con variables
   - Agrega contexto del sistema
   - Estructura el mensaje
   ↓
3. LLM (GPT-3.5)
   - Procesa el prompt
   - Genera respuesta
   - Usa el modelo de lenguaje
   ↓
4. OUTPUT PARSER
   - Extrae informacion relevante
   - Convierte a formato deseado
   - Valida la estructura
   ↓
5. RESULTADO FINAL
   - Texto estructurado
   - JSON validado
   - Lista procesada
```

## Ejemplos de Uso por Componente

### Ejemplo 1: Solo LLM (Simple)

```python
llm = ChatOpenAI()
respuesta = llm.invoke("Hola")
# Input: string
# Output: AIMessage
```

### Ejemplo 2: LLM + Parser

```python
chain = llm | StrOutputParser()
respuesta = chain.invoke("Hola")
# Input: string
# Output: string (contenido extraido)
```

### Ejemplo 3: Prompt + LLM + Parser

```python
prompt = ChatPromptTemplate.from_template("Di {frase}")
chain = prompt | llm | StrOutputParser()
respuesta = chain.invoke({"frase": "hola"})
# Input: dict
# Output: string
```

### Ejemplo 4: Chain Completa con JSON

```python
prompt = ChatPromptTemplate.from_template("Info de {tema}")
parser = JsonOutputParser(pydantic_object=MiModelo)
chain = prompt | llm | parser
respuesta = chain.invoke({"tema": "Python"})
# Input: dict
# Output: dict (JSON validado)
```

## Patrones de Diseno Utilizados

### 1. Chain of Responsibility

Los componentes procesan la informacion secuencialmente.

### 2. Template Method

Los prompt templates definen la estructura, los datos la completan.

### 3. Strategy

Diferentes parsers para diferentes estrategias de salida.

### 4. Builder

Construccion fluida de chains con el operador `|`.

## Best Practices

### DO (Hacer)

```python
# Usar templates para reutilizacion
template = ChatPromptTemplate.from_template("...")

# Chains simples y composables
chain = prompt | llm | parser

# Validar salidas con Pydantic
class MiModelo(BaseModel):
    campo: str
```

### DON'T (No hacer)

```python
# Hardcodear prompts
llm.invoke("Eres un experto en...")  # No recomendado

# Chains muy complejas
chain = a | b | c | d | e | f | g  # Dificil de mantener

# Ignorar validacion
resultado = llm.invoke(...)  # Sin parsear
```

## Seguridad y Variables de Entorno

### Gestion de API Keys

```python
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
```

### Estructura del .env

```bash
# OpenAI
OPENAI_API_KEY=sk-...

# Opcional: Configuracion adicional
OPENAI_ORGANIZATION=org-...
```

### .gitignore

```
.env          # NUNCA commitear
.env.local
*.key
```

## Escalabilidad

### Procesamiento por Lotes

```python
# Procesar multiples inputs eficientemente
inputs = [{"tema": "Python"}, {"tema": "JavaScript"}]
results = chain.batch(inputs)
```

### Streaming

```python
# Para respuestas largas
for chunk in chain.stream({"pregunta": "..."}):
    print(chunk, end="", flush=True)
```

### Async/Await

```python
# Procesamiento asincrono
async def procesar():
    resultado = await chain.ainvoke({"tema": "..."})
    return resultado
```

## Testing

### Unit Tests

```python
def test_chain():
    chain = prompt | llm | parser
    resultado = chain.invoke({"input": "test"})
    assert isinstance(resultado, dict)
    assert "campo" in resultado
```

### Mocking

```python
from unittest.mock import Mock

llm_mock = Mock()
llm_mock.invoke.return_value = "respuesta"
chain = prompt | llm_mock | parser
```

## Recursos de Aprendizaje

### Documentacion Oficial

- [LangChain Docs](https://python.langchain.com/docs/)
- [OpenAI API Reference](https://platform.openai.com/docs/)

### Conceptos Clave

1. **Prompts**: Como formular consultas efectivas
2. **LLMs**: Modelos de lenguaje y sus capacidades
3. **Chains**: Composicion de flujos de trabajo
4. **Parsers**: Estructuracion de salidas

### Proximos Pasos

- Completado: LangChain LLM Chain (este proyecto)
- Siguiente: RAG (Retrieval Augmented Generation)
- Siguiente: Vector Stores (Pinecone)
- Siguiente: Embeddings y Busqueda Semantica

---

Este documento forma parte del **Repositorio 1: LangChain LLM Chain**
