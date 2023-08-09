import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

# opciones de voz / idioma
id_1 = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_ES-ES_HELENA_11.0"
id_2 = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_DAVID_11.0"
id_3 = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0"
id_4 = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-GB_HAZEL_11.0"


# escuchar nuestro microfono y devolver el audio como texto
def transformar_audio():
    # almacenar reconocedor de voz en una variable
    r = sr.Recognizer()

    # configurar el microfono
    # el with hace que el codigo dentro se ejecute junto, y libera automaticamente
    # las cosas
    with sr.Microphone() as origen:

        # tiempo de espera, se usa para que se resuelvan posibles errores de sonido
        r.pause_threshold = 0.8

        # informar que comenzo la grabacion
        print("decime algo pa")

        # guardar lo que escuche como audio
        audio = r.listen(origen)

        try:
            # usar la api de google para transcribir a texto
            pedido = r.recognize_google(audio, language="es-ar")

            # prueba de que pudo ingresar
            print("Dijiste: " + pedido)

            # devolver pedido
            return pedido

        # en caso de que no comprenda el audio
        except sr.UnknownValueError:

            # prueba de que no comprendio el audio
            print("no entendi mi broder")

            # devolver error
            return "sigo esperando"

        # en caso de que no se pueda resolver el pedido
        except sr.RequestError:

            # prueba de que no comprendio el audio
            print("no hay servicio mi loco")

            # devolver error
            return "sigo esperando"

        # error inesperado
        except Exception as e:
            print(f"Se produjo una excepción: {type(e).__name__}")
            print(f"Mensaje de error: {e}")


# funcion para que el asistente pueda se rescuchado
def hablar(mensaje, voz_id):

    # inicializar el motor de pyttsx3
    engine = pyttsx3.init()
    engine.setProperty("voice", voz_id)

    # pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()


# informar el dia de la semana
def pedir_dia():

    # crear variable con datos de hoy
    dia = datetime.date.today()
    # print(dia)

    # crear variable para el dia de la semana
    dia_semana = dia.weekday()
    # print(dia_semana)

    # diccionario con nombres de los dias
    calendario = {0: "Lunes",
                  1: "Martes",
                  2: "Miércoles",
                  3: "jueves",
                  4: "Viernes",
                  5: "Sábado",
                  6: "Domingo"}

    # decir dia de la semana
    hablar(f"Hoy es {calendario[dia_semana]}", id_1)


# funcion que nos va a decir la hora
def pedir_hora():

    # guardamos la hora en una variable
    hora = datetime.datetime.now()
    hora = f"En este momento son las {hora.hour} horas, con {hora.minute} minutos y {hora.second} segundos"
    print(hora)

    # decir la hora
    hablar(hora, id_1)


# funcion de saluod inicial
def saludo_inicial():


    # crear variable con datos de hora
    hora = datetime.datetime.now()
    if 6 <= hora.hour < 12:
        saludo = "Buenos días"
    elif 12 <= hora.hour < 20:
        saludo = "Buenas tardes"
    else:
        saludo = "Buenas noches"

    # decir el saludo
    hablar(f"{saludo}, soy tu asistente de voz papá, que querés que haga?", id_1)


# funcion central del asistente
def pedir_cosas():

    # activar saludo inicial
    saludo_inicial()

    # variable de finalizacion del loop
    comenzar = True

    # loop central
    while comenzar:

        # activar el microfono y guardar el pedido en un string
        pedido = transformar_audio().lower()

        if "abrir youtube" in pedido:
            hablar("Dale pá, ahi te abro iutuv", id_1)
            webbrowser.open("https://www.youtube.com")
            # el continue salta a la siguiente iteracion del bucle principal
            continue
        elif "abrir navegador" in pedido:
            hablar("dale broder", id_1)
            webbrowser.open("https://www.google.com")
            continue
        elif "qué día es hoy" in pedido:
            pedir_dia()
            continue
        elif "qué hora es" in pedido:
            pedir_hora()
            continue
        elif "busca en wikipedia" in pedido:
            hablar("Buscando el pedido en wikipedia", id_1)
            pedido = pedido.replace("busca en wikipedia", "")
            # establecer lenguaje de wikipedia
            wikipedia.set_lang("es")
            resultado = wikipedia.summary(pedido, sentences=1)  # = 1 solo busca en el primer parrafo de wikipedia
            hablar("wikipedia dice lo siguiente", id_1)
            hablar(resultado, id_1)
            continue
        elif "busca en internet" in pedido:
            hablar("buscando en internet", id_1)
            pedido = pedido.replace("busca en internet", "")
            pywhatkit.search(pedido)
            hablar("esto fue lo que encontre bro", id_1)
            continue
        elif "reproducir" in pedido:
            hablar("ahi reproduzco dogór", id_1)
            pywhatkit.playonyt(pedido)
            continue
        elif "broma" in pedido:
            hablar(pyjokes.get_joke("es"), id_1)
            continue
        elif "precio de las acciones" in pedido:
            accion = pedido.split("de")[-1].strip()
            cartera = {"apple": "APPL",
                       "amazon": "AMZN",
                       "google": "GOOGL"}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info["regularMarketPrice"]
                hablar(f"Encontré la acción padre, el precio de {accion} es {precio_actual}", id_1)
                continue
            except Exception as e:
                print(f"mensaje de error: {e}")
                hablar("no la encontré boludín", id_1)
                continue
        elif "nos vemos" in pedido:
            hablar("nos vemos padre, un gustaso", id_1)
            comenzar = False


pedir_cosas()


"""
ver voces disponibles en nuestra computadora
engine = pyttsx3.init()
for voz in engine.getProperty("voices"):
    print(voz)
"""

