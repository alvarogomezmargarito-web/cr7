import streamlit as st

# 1. EL ARCHIVADOR (Base de datos de preguntas)
preguntas = [
    {
        "texto": "¿En qué club debutó Cristiano Ronaldo?",
        "opciones": ["Sporting CP", "Manchester United", "Real Madrid", "Juventus"],
        "correcta": "Sporting CP"
    },
    {
        "texto": "¿Cuántos Balones de Oro ha ganado Cristiano Ronaldo?",
        "opciones": ["3", "4", "5", "6"],
        "correcta": "5"
    },
    {
        "texto": "¿Con qué selección ganó la Eurocopa en 2016?",
        "opciones": ["España", "Brasil", "Portugal", "Francia"],
        "correcta": "Portugal"
    },
    {
        "texto": "¿En qué club marcó más goles Cristiano Ronaldo?",
        "opciones": ["Manchester United", "Real Madrid", "Juventus", "Al Nassr"],
        "correcta": "Real Madrid"
    },
    {
        "texto": "¿En qué año nació Cristiano Ronaldo?",
        "opciones": ["1983", "1985", "1987", "1989"],
        "correcta": "1985"
    },
    {
        "texto": "¿Qué dorsal le representa?",
        "opciones": ["7", "9", "10", "11"],
        "correcta": "7"
    },
    {
        "texto": "¿Cuántas Champions ha ganado en su carrera?",
        "opciones": ["3", "4", "5", "6"],
        "correcta": "5"
    },
    {
        "texto": "¿En qué pais juega actualmente?",
        "opciones": ["España", "Italia", "Arabia Saudita", "Inglaterra"],
        "correcta": "Arabia Saudita"
    },
    {
        "texto": "¿Contra qué equipo marcó su famosa chilena en Champions con la Juventus?",
        "opciones": ["Barcelona", "Atlético de Madrid", "PSG", "Juventus"],
        "correcta": "Juventus"
    },
    {
        "texto": "¿Qué apodo tiene?",
        "opciones": ["El crack", "CR7", "La Pulga", "El Tigre"],
        "correcta": "CR7"
    }
]

# Configuración visual
st.title("preguntas dificiles de cr7")
st.write("Responde las preguntas y pulsa el botón para descubrir si eres una verdadera leyenda.")

with st.form("quiz_form"):

    respuestas_usuario = []
    
    for pregunta in preguntas:
        st.subheader(pregunta["texto"])
        eleccion = st.radio("Elige una opción:", pregunta["opciones"], key=pregunta["texto"])
        respuestas_usuario.append(eleccion)
        st.write("---")

    boton_enviar = st.form_submit_button("Ver resultado")

# Corrección
if boton_enviar:
    aciertos = 0
    total = len(preguntas)

    for i in range(total):
        if respuestas_usuario[i] == preguntas[i]["correcta"]:
            aciertos += 1

    st.divider()
    st.header(f"Resultado final: {aciertos} / {total}")

    if aciertos <= 4:
        st.error("Sigue entrenando ")
    elif 5 <= aciertos <= 7:
        st.warning("Buen fan ")
    else:
        st.success("Leyenda CR7")
        st.balloons()
