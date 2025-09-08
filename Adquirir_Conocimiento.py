#En esta práctica, vamos a crear un chatbot sencillo que pueda adquirir conocimiento de las interacciones con el usuario.
#El chatbot responderá a preguntas basadas en una base de conocimiento inicial y, si no sabe la respuesta, le pedirá al usuario que le enseñe.
#El conocimiento adquirido se guardará en un archivo para futuras interacciones.
#Este es un ejemplo básico y puede ser expandido con técnicas más avanzadas de procesamiento de lenguaje natural y aprendizaje automático.
#Nos ayuda a entender cómo los sistemas pueden aprender de la experiencia y mejorar sus respuestas con el tiempo.

#Librerías necesarias
import json #para manejar archivos JSON y estructuras de datos
#JSON es un formato ligero de intercambio de datos que es fácil de leer y escribir para los humanos, y fácil de parsear y generar para las máquinas.
import os #para manejar operaciones del sistema como verificar la existencia de archivos
#OS proporciona una manera portátil de usar funcionalidades dependientes del sistema operativo, como leer o escribir archivos.

#Archivo donde se guarda el conocimiento
BASE_CONOCIMIENTO = "conocimiento.json" #archivo JSON para almacenar el conocimiento del chatbot

#cargar base de conocimiento si existe, sino crear una nueva
if os.path.exists(BASE_CONOCIMIENTO): #si el archivo de base de conocimiento existe
    with open(BASE_CONOCIMIENTO, "r", encoding="utf-8") as f: #abrir el archivo en modo lectura con codificación UTF-8
        #UTF-8 es una codificación de caracteres que puede representar todos los caracteres en el estándar Unicode, lo que la hace ideal para manejar texto en múltiples idiomas.
        conocimiento = json.load(f) #cargar el contenido del archivo JSON en un diccionario de Python
else: #si el archivo no existe, inicializar con conocimiento básico
    conocimiento = {
        "hola": "¡Hola! ¿Cómo estás?", #respuesta predeterminada para "hola"
        "cómo estás": "Muy bien, gracias. ¿Y tú?", #respuesta predeterminada para "cómo estás"
        "qué haces": "Estoy aquí para platicar contigo." #respuesta predeterminada para "qué haces"
    }

print("🤖Chatbot: Hola, soy tu asistente virtual. Escribe 'salir' para terminar.\n") 

#Bucle principal del chat
while True: #bucle infinito para mantener la conversación hasta que el usuario decida salir
    pregunta = input("Tú: ").strip().lower() #leer la entrada del usuario, eliminar espacios en blanco y convertir a minúsculas

    if pregunta == "salir": #si el usuario escribe "salir", terminar la conversación
        print("🤖 Chatbot: ¡Hasta pronto!")
        break

    #buscar coincidencia exacta en la base de conocimiento
    if pregunta in conocimiento: #si la pregunta del usuario está en el diccionario de conocimiento
        print("🤖 Chatbot:", conocimiento[pregunta]) #el chatbot da la respuesta de la base del conocimiento
    else: #si no se encuentra la pregunta en el conocimiento
        print("🤖 Chatbot: No sé qué responder a eso.") #el chatbot responde que no tiene esa informacion
        nueva_respuesta = input("¿Qué debería responder cuando digas eso?: ") #pedir al usuario que proporcione una respuesta para esa pregunta

        #Guardar nuevo conocimiento
        conocimiento[pregunta] = nueva_respuesta #agregar la nueva pregunta y respuesta al diccionario de conocimiento
        with open(BASE_CONOCIMIENTO, "w", encoding="utf-8") as f: #abrir el archivo de base de conocimiento en modo escritura con codificación UTF-8
            json.dump(conocimiento, f, ensure_ascii=False, indent=4) #guardar el diccionario actualizado en el archivo JSON

        print("🤖 Chatbot: ¡Gracias! Aprendí algo nuevo.") 