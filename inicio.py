import streamlit as st

## VARIABLES
page_title = "Inicio"
page_icon = ":house:"
layout="wide"

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)

st.title("Sobre Nosotros")
# Imagen del salón (si tienes alguna imagen puedes incluirla)
st.image("assets/salon_masajes_2.jpg", caption="Nuestro acogedor salón de masajes")

# Descripción del salón de masajes
st.header("Bienvenido a Nuestro Salón de Masajes")
st.write("""
En nuestro salón de masajes, nos dedicamos a ofrecer una experiencia de relajación y bienestar
personalizada para cada uno de nuestros clientes. Nuestro equipo de masajistas profesionales está
comprometido en brindar servicios de alta calidad que te ayudarán a aliviar el estrés y mejorar tu salud física y mental.
""")

# Misión y Visión
st.header("Nuestra Misión y Visión")
st.write("""
**Misión:** Nuestra misión es proporcionar un refugio de tranquilidad y rejuvenecimiento en el que nuestros clientes puedan
escapar del estrés diario y encontrar paz y equilibrio a través de nuestros tratamientos de masaje y bienestar.

**Visión:** Aspiramos a ser el salón de masajes líder en nuestra comunidad, reconocido por nuestra dedicación a la excelencia,
la innovación en tratamientos y un servicio al cliente excepcional.
""")

# Servicios ofrecidos
st.header("Nuestros Servicios")
st.write("""
Ofrecemos una variedad de servicios de masaje adaptados a tus necesidades específicas:
- **Masaje Relajante:** Ideal para reducir el estrés y la tensión.
- **Masaje Deportivo:** Perfecto para los atletas que necesitan recuperar sus músculos después de un entrenamiento intenso.
- **Masaje Terapéutico:** Diseñado para tratar dolores y molestias crónicas.
- **Masaje de Tejido Profundo:** Enfocado en las capas más profundas de los músculos para aliviar tensiones.
""")

# Nuestro Equipo
st.header("Conoce a Nuestro Equipo")
st.write("""
Contamos con un equipo de masajistas altamente cualificados y apasionados por su trabajo:
- **Luis:** Especialista en masajes deportivos y de tejido profundo.
- **David:** Experto en masajes relajantes y terapéuticos.
- **Noelia:** Masajista versátil con experiencia en diversas técnicas de masaje.
- **Maria:** Especialista en masajes relajantes y tratamientos holísticos.
""")

# Testimonios de Clientes
st.header("Testimonios de Nuestros Clientes")
st.write("""
_"El mejor lugar para relajarse. El personal es increíblemente profesional y siempre me siento renovado después de cada visita."_
- **Juan Pérez**

_"Un ambiente perfecto y un servicio excepcional. No puedo recomendarlo lo suficiente."_
- **Ana Gómez**
""")

# Ubicación y Contacto
st.header("Ubicación y Contacto")


st.write("""
Nos encontramos en el corazón de la ciudad, fácilmente accesibles para todos nuestros clientes.

**Dirección:** Calle Falsa, 123, Ciudad Ejemplo

**Teléfono:** +34 123 456 789

**Correo Electrónico:** info@salondemasajes.com
""")




# Mapa de ubicación (si tienes coordenadas puedes usar el componente de mapa de Streamlit)
st.subheader("Ubicación")
st.markdown("""<iframe src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d1227.5487766992082!2d-4.8053174!3d37.9124114!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0xd6cdf2e179aba81%3A0x6eb276d3beff43c5!2sEscuder%C3%ADa%20Alba%20de%20C%C3%B3rdoba!5e1!3m2!1ses-419!2ses!4v1719469549986!5m2!1ses-419!2ses" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>""", unsafe_allow_html=True)



