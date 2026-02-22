# Inicio Rapido - LangChain LLM Chain

Esta guia te ayudara a ejecutar el proyecto en menos de 5 minutos.

## Configuracion Rapida

### 1. Instalar Dependencias (1 minuto)

```bash
# Crear entorno virtual (opcional pero recomendado)
python -m venv venv

# Activar entorno virtual
venv\Scripts\activate      # Windows
source venv/bin/activate   # Linux/Mac

# Instalar dependencias
pip install -r requirements.txt
```

### 2. Configurar API Key (1 minuto)

```bash
# Copiar archivo de ejemplo
copy .env.example .env    # Windows
cp .env.example .env      # Linux/Mac
```

Edita `.env` y agrega tu API key de OpenAI:

```
OPENAI_API_KEY=sk-tu-key-aqui
```

**Nota:** Obten una en https://platform.openai.com/api-keys

### 3. Ejecutar (30 segundos)

**Opcion 1: Inicio Interactivo** (Recomendado)

```bash
python start.py
```

**Opcion 2: Ejemplos Individuales**

```bash
python 01_basic_llm.py              # Uso basico de LLM
python 02_prompt_templates.py       # Templates de prompts
python 03_chains_parsers.py         # Chains y parsers
python 04_caso_uso_completo.py      # Caso de uso completo
```

## Requisitos Minimos

- **Python**: 3.8 o superior
- **Internet**: Para conectarse a la API de OpenAI
- **API Key**: De OpenAI (requiere cuenta)

## Que Puedes Hacer

### 1. Preguntar al LLM

```python
llm = ChatOpenAI(model="gpt-3.5-turbo")
respuesta = llm.invoke("Que es LangChain?")
```

### 2. Usar Templates

```python
template = ChatPromptTemplate.from_template(
    "Explica {concepto} en terminos simples"
)
```

### 3. Crear Chains

```python
chain = prompt | llm | output_parser
resultado = chain.invoke({"tema": "Python"})
```

### 4. Analisis de Codigo

```python
analista = AnalistaCodigoLangChain()
analista.analisis_completo(tu_codigo)
```

## Solucion Rapida de Problemas

### Error: "No module named 'langchain'"

```bash
pip install -r requirements.txt
```

### Error: "OpenAI API key not found"

Verifica que `.env` exista y contenga tu API key.

### Error: "Rate limit exceeded"

Espera 1 minuto. Es el limite de la API gratuita de OpenAI.

### Error: "Invalid API key"

Verifica tu API key en https://platform.openai.com/api-keys

## Siguiente Paso

Despues de probar los ejemplos, lee el [README.md](README.md) completo para entender la arquitectura y los conceptos avanzados.

## Consejo

Usa `start.py` para comenzar. Es interactivo y te guiara paso a paso.

```bash
python start.py
```

---

**Necesitas ayuda?** Revisa la documentacion completa en [README.md](README.md)
