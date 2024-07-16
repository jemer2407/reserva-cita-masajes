import streamlit as st
import re
import uuid
import datetime as dt
import numpy as np
from datetime import datetime
from app.google_sheets import GoogleSheets
from app.google_calendar import GoogleCalendar
from app.send_email import send_email

## FUNCIONES
def sumar_una_hora(hora_str):
    # Convertir la cadena de hora a un objeto datetime
    hora = dt.datetime.strptime(hora_str, '%H:%M')
    
    # Sumar minutos
    nueva_hora = hora + dt.timedelta(hours=1)
    
    # Convertir el objeto datetime de nuevo a una cadena con el mismo formato
    return nueva_hora.strftime('%H:%M')


def generate_uid():
    return str(uuid.uuid4())

def formatocorreo(correo):
    patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(patron, correo):
        return True
    else:
        return False

# ---------------------------------------------------

## VARIABLES
document = "bbdd-citas-masajes"
sheet_citas = "citas"
sheet_masajistas = "masajistas"
sheet_servicios = "servicios"
sheet_horario = "horario"
credentials = st.secrets["google"]["credentials_google"]

idcalendar1 = 'jesusmerc2407@gmail.com'
idcalendar2 = '53978dab6147b9235455f7ce6974542f8e6a0f27c3b0c0ae281d551664d7e076@group.calendar.google.com'
idcalendar3 = '318f21263fc6924256968123a17948542133c35b960ca936de554b62be10df2e@group.calendar.google.com'
idcalendar4 = '84fdd677cad978da651079dfe1202ee835d583ec422cdcd80b30f3b831f702af@group.calendar.google.com'
time_zone = 'Europe/Madrid'

st.title("Pedir Cita")

horas = ["09:00","10:00","11:00","12:00","13:00","17:00","18:00","19:00"]
masajistas = ["Luis","David","Noelia","Maria"]
servicios = ["Masaje relajante",
             "Masaje craneofacial",
             "Masaje circulatorio",
             "Masaje descontracturante y deportivo",
             "Masaje de drenaje linfático"]

# formulario solicitud de cita de masaje

nombre = st.text_input("Tu nombre*")
email = st.text_input("Tu email*")
fecha = st.date_input("Fecha", format="DD/MM/YYYY", min_value=datetime.now())
servicio = st.selectbox("Servicio", servicios)
masajista = st.selectbox("Masajista",masajistas)
# una vez seleccionada la fecha guardamos en id el id de calendario del masajista seleccionado
if fecha:
    if masajista == "Luis":
        id = idcalendar1
    elif masajista == "David":
        id = idcalendar2
    elif masajista == "Maria":
        id = idcalendar3
    elif masajista == "Noelia":
        id = idcalendar4
   


    calendar = GoogleCalendar(credentials, id)  # nos autenticamos
    hours_blocked = calendar.get_events_start_time(str(fecha))  # obtenemos las horas reservadas de la fecha seleccionada
    result_hours = np.setdiff1d(horas, hours_blocked)   # comparamos las listas horas y hours_blocked y obtenemos una lista con las horas libres
    


hora = st.selectbox("horas",result_hours)

enviar = st.button("Enviar")

if enviar:
    with st.spinner("Cargando..."):

            if nombre == "":
                st.warning("Introduzca el nombre")
            elif email == "":
                st.warning("Introduzca el email")
            elif not formatocorreo(email):
                st.warning("Formato de email incorrecto")              
            else:
                # Crear evento en google calendar
                parsed_time = dt.datetime.strptime(hora, "%H:%M").time()
                hours1 = parsed_time.hour
                minutes1 = parsed_time.minute


                
                end_hours = sumar_una_hora(hora)

                parsed_time2 = dt.datetime.strptime(end_hours, "%H:%M").time()
                hours2 = parsed_time2.hour
                minutes2 = parsed_time2.minute

                start_time = dt.datetime(fecha.year,fecha.month,fecha.day,hours1,minutes1).astimezone(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
                end_time = dt.datetime(fecha.year,fecha.month,fecha.day,hours2,minutes2).astimezone(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
                calendar = GoogleCalendar(credentials, id)  # nos autenticamos
                calendar.create_event(nombre, start_time, end_time, time_zone)


                # Crear registro en google sheets
                uid = generate_uid()
                data = [[uid,nombre,email,masajista,servicio,str(fecha),hora]]
                gs = GoogleSheets(credentials, document, sheet_citas)
                range = gs.get_last_row_range()
                gs.write_data(range,data)

                # enviar email al usuario
                send_email(email,nombre,fecha,hora,masajista,servicio)
                st.success("Su cita ha sido reservada con éxito")




