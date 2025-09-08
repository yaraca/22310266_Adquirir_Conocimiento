# 22310266_Adquirir_Conocimiento

# 🤖 Chatbot con Adquisición de Conocimiento

## Descripción
Este proyecto implementa un **chatbot sencillo en Python** que incluye un **módulo de adquisición de conocimiento**.  
El chatbot comienza con una base de datos de respuestas precargadas y, cuando se le hace una pregunta que no reconoce, solicita al usuario que le enseñe la respuesta.  
La nueva información se almacena en un archivo JSON, lo que permite al bot **aprender de manera incremental**.  

Este tipo de práctica está relacionada con los **sistemas expertos** y el **manejo de bases de conocimiento**, áreas clave en la Inteligencia Artificial.  

---

## Características
- Base de conocimiento inicial con 3 frases precargadas.  
- Aprendizaje interactivo: si no conoce la respuesta, pide al usuario que lo enseñe.  
- Persistencia: la información nueva se guarda en `conocimiento.json` y se reutiliza en futuras ejecuciones.  
- Ejemplo sencillo del **módulo de adquisición de conocimiento** en sistemas expertos.  

---

## Librerías utilizadas

| Librería  | Uso en el proyecto |
|-----------|--------------------|
| `json`    | Guardar y cargar la base de conocimiento en un archivo `.json` (persistencia de datos). |
| `os`      | Verificar si el archivo de conocimiento existe antes de cargarlo. |