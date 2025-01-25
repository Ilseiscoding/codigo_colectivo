def crear_historia():
    """
    Esta función genera y RETORNA una historia personalizada basada en la información
    que ingresa el usuario:
      - Nombre
      - Edad
      - Estado de ánimo
      - Clase que está tomando
      - Profesión
    """

    # Solicitar datos al usuario
    nombre = input("¿Cuál es tu nombre? ")
    
    # Conversión segura de edad
    edad_str = input("¿Cuál es tu edad? ")
    try:
        edad = int(edad_str)
    except ValueError:
        edad = 0  # Valor por defecto si no se logra convertir
        print("No ingresaste un número válido, usaremos 0 como edad.\n")
    
    estado_animo = input("¿Cómo te sientes hoy? (ej. feliz, cansado, emocionado) ")
    clase = input("¿Qué clase estás tomando actualmente? ")
    profesion = input("¿A qué te dedicas o cuál es tu profesión? ")
    
    # Construir la historia en una variable de tipo string
    historia = "\n===== HISTORIA PERSONALIZADA =====\n\n"
    historia += f"Un día, {nombre}, de {edad} años de edad, se levantó sintiéndose {estado_animo}.\n"
    historia += f"Con mucha motivación, se preparó para asistir a la clase de {clase}.\n"
    historia += f"Como {profesion}, {nombre} siempre busca expandir sus conocimientos y habilidades.\n"

    # Lógica opcional según la edad
    if edad < 18:
        historia += f"¡Y eso es sorprendente, porque tener solo {edad} años y estudiar {clase} demuestra mucha dedicación!\n"
    elif 18 <= edad < 30:
        historia += f"A la edad de {edad}, la curiosidad de {nombre} por aprender {clase} es un gran impulso profesional.\n"
    else:
        historia += f"Con {edad} años, {nombre} demuestra que nunca es tarde para aprender algo nuevo, como {clase}.\n"

    # Comentario según el estado de ánimo
    estado_animo_lower = estado_animo.lower()
    if "feliz" in estado_animo_lower or "emocionad" in estado_animo_lower:
        historia += f"¡Se nota su entusiasmo al entrar al salón con una gran sonrisa en el rostro!\n"
    elif "cansad" in estado_animo_lower:
        historia += f"Aunque {nombre} se siente algo cansado, la pasión por seguir aprendiendo lo mantiene en marcha.\n"
    else:
        historia += f"En un estado de ánimo curioso, {nombre} afronta cada reto con determinación.\n"

    # Cierre de la historia
    historia += f"\nDe esta forma, {nombre} comenzó una nueva aventura en el mundo de {clase}, "
    historia += f"donde cada día es una oportunidad para crecer como {profesion}.\n"
    historia += "\n===== FIN DE LA HISTORIA =====\n"

    # RETORNAR la historia en lugar de imprimirla
    return historia
