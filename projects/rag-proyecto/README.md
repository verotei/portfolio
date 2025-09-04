# 🚀 Retrieval Augmented Generation (RAG): validación inicial y potencial

Este proyecto surge de lo aprendido en la materia **Minería de Textos** de la **Especialización en Inteligencia de Datos orientada a Big Data** (UNLP), con el profesor **Marcelo Errecalde**.  
Ahí conocí en detalle los **Transformers**, una arquitectura que me voló la cabeza y me inspiró a armar este prototipo de RAG.

---

## ✨ ¿De qué se trata?
La idea es simple, en vez de que un modelo de lenguaje responda solo con lo que aprendió en su entrenamiento, le damos **contexto extra** conectándolo a una base vectorial con documentos propios.  
Así, el modelo puede responder preguntas con información contextualizada y relevante.

---

## 🛠️ Tecnologías usadas
- Python 
- LangChain
- ChromaDB
- OpenAI API
- Jupyter Notebook

---

## 📂 Estructura del repo
- `notebook/` → notebook principal con la demo (incluye outputs ejecutados)  
- `data/` → documentos de ejemplo (en este caso un PDF)
- `outputs/` → ejemplos de respuestas generadas (capturas de pantalla)
- `requirements.txt` → librerías necesarias  
- `README.md` → esta explicación  

---

## ⚡ Cómo correrlo
1. Cloná el repo o bajate la carpeta.  
2. Instalá dependencias:  
   ```bash
   pip install -r requirements.txt
