# 🚀 Retrieval Augmented Generation (RAG): validación inicial y potencial [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

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
- `README.md` → documentación principal del proyecto

---

## ☁️ Entorno de ejecución en Google Colab

El proyecto está diseñado para correrse en **Google Colab**, con los documentos almacenados en **Google Drive**.

Pasos básicos:
1. Abrí el notebook en Colab.  
2. En tu Drive creá la carpeta "Proyecto RAG"
3. Subí en esa carpeta los documentos PDFs con los que vas a trabajar o usá el de este proyecto que vas a encontrar dentro de la carpeta data.
4. La ruta por defecto del notebook ya apunta a: `ruta_directorio = "/content/drive/MyDrive/Proyecto RAG"`
5. Ejecutá el notebook: cargará automáticamente todos los PDFs guardados en esa carpeta.

   

