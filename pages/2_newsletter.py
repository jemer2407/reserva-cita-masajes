import streamlit as st
import re
import uuid
from datetime import datetime
from google_sheets import GoogleSheets # type: ignore


# -------- FUNCIONES --------
# funcion para validar formato del email
def formatocorreo(correo):
    patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(patron, correo):
        return True
    else:
        return False


def generate_uid():
    return str(uuid.uuid4())

def hoy():

	hoy=datetime.today()
	return str(hoy)

# VARIABLES
# ---- credenciales, nombre del documento de hoja de calculo y nombre de la hoja ----
credentials = st.secrets["google"]["credentials_google"]
document_name = "bbdd-citas-masajes"
sheet_name = "contactos"
# ---------------------------------

# ---- datos de la pagina: título, icono, centrado en la página ----
page_title = "Salón de masajes"
page_icon = "assets/logo.ico"
layout="centered"
# ---------------------------------
# FIN VARIABLES ------------------
# INICIO FRONT-END
st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)

st.write("##")
st.title("¡Únete a nuestra newsletter :massage:!")
st.write("##")

c1,c2 = st.columns(2)

with c1:
    st.image("assets/logo.png")
with c2:
   
    nombre = st.text_input("Nombre*", placeholder="Tu nombre")
    email = st.text_input("Email*", placeholder="Tu mejor email")
    fecha_nac = st.date_input("Fecha de Nacimiento",
                              help="Tu cumpleaños es importante para nosotros. Te enviaremos un regalo especial!",
                              value=None,
                              format='DD/MM/YYYY')
    policy = st.checkbox("Acepto recibir emails por parte de la empresa")
    enviar = st.button("Enviar")

    st.write("##")
    st.caption("© 2024 Salón de masajes de Córdoba. Todos los derechos reservados")

    if enviar:
        if not nombre:
            st.warning("Por favor, completa el campo del nombre")
        elif not email:
            st.warning("Por favor, completa el campo del email")
        elif not formatocorreo(email):
            st.warning("Formato de email incorrecto")
        elif not policy:
            st.warning("Por favor, acepta recibir email por parte de la empresa")
        elif fecha_nac != None and fecha_nac > datetime.now().date():
            st.error("Por favor, introduce una fecha de nacimiento válida")
        
        else:
            # implementar la logica para guardar el usuario en la bbdd
            try:
                with st.spinner("Enviando información...."):
                    uid = generate_uid()    # creamos un identificador unico
                    timestap = hoy()  # creamos la fecha de hoy
                    values = [[uid,nombre,email,str(fecha_nac),timestap]] # valores que vamos a enviar a la bbdd
                    gsheet = GoogleSheets(credentials,document_name,sheet_name) # creamos el objeto de nuestro google sheets
                    range = gsheet.get_last_row_range() # obtenemos el rango donde vamos a escribir un registro
                    gsheet.write_data(range,values)
                    st.success("¡Gracias por unirte a nuestra newsletter!")
            except Exception as e:
                st.error(f"Ocurrió un error al enviar su información")