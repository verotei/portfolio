# Clasificación de Reseñas con Naive Bayes  

⚠️ Proyecto en construcción. Próximamente se agregarán comparaciones con otros modelos de NLP.  

## 📌 Objetivo  
Explorar un método clásico de Machine Learning (Naive Bayes) para clasificar reseñas de productos en positivas o negativas.  

## 🧩 Contenido  
- Limpieza y preprocesamiento de texto  
- Representación con Bag-of-Words / TF-IDF  
- Entrenamiento del modelo Naive Bayes  
- Evaluación de métricas (accuracy, precision, recall, f1-score)  
- Ejemplos prácticos de clasificación de nuevas reseñas  

## 📊 Resultados principales  

| Clase         | Precision | Recall | F1-score | Soporte |
|---------------|-----------|--------|----------|---------|
| Negativa (0)  | 0.83      | 0.81   | 0.82     | 25,138  |
| Positiva (1)  | 0.73      | 0.75   | 0.74     | 16,862  |
| **Accuracy**  |           |        | **0.785**| 42,000  |
| **Macro avg** | 0.78      | 0.78   | 0.78     | 42,000  |
| **Weighted avg** | 0.79   | 0.79   | 0.79     | 42,000  |

## ✅ Conclusión  
- El modelo alcanzó un **accuracy del 78,5%**.  
- La clase negativa mantiene un alto nivel de desempeño (f1-score 0.82).  
- La clase positiva también logra métricas consistentes (f1-score 0.74), mostrando que el modelo reconoce adecuadamente ambas categorías.  
- El macro promedio (0.78) confirma que el rendimiento es equilibrado entre clases.  
- Naive Bayes ofrece una solución simple y efectiva como baseline, con bajo costo computacional y resultados competitivos.  

## 🚀 Próximos pasos  
- Comparar desempeño con modelos basados en Transformers (BERT, RoBERTa).  
- Incorporar representaciones modernas de texto (embeddings contextuales). 

