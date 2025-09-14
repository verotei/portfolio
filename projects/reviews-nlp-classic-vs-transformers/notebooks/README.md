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
| Negativa (0)  | 0.77      | 0.91   | 0.83     | 25,138  |
| Positiva (1)  | 0.81      | 0.59   | 0.68     | 16,862  |
| **Accuracy**  |           |        | **0.78** | 42,000  |
| **Macro avg** | 0.79      | 0.75   | 0.76     | 42,000  |
| **Weighted avg** | 0.78   | 0.78   | 0.77     | 42,000  |

## ✅ Conclusión  
- El modelo alcanzó un **accuracy de 77,8%**.  
- Presenta un **alto recall en la clase negativa (0.91)**, lo que indica que identifica muy bien las reseñas negativas.  
- Sin embargo, el **recall de la clase positiva es bajo (0.59)**, lo que significa que deja pasar varias reseñas positivas sin detectarlas.  
- Este comportamiento está asociado al **desbalance de clases** en el dataset, donde predominan las reseñas negativas.  
- Como baseline, Naive Bayes ofrece resultados sólidos con bajo costo computacional.  
- Esta brecha entre clases lo convierte en un buen punto de partida para comparar con modelos más avanzados como Transformers.  

## 🚀 Próximos pasos  
- Comparar desempeño con modelos basados en Transformers (BERT, RoBERTa).  
- Analizar impacto del desbalance de clases.  
- Incorporar representaciones modernas de texto (embeddings contextuales).  
