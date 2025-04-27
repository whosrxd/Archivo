import streamlit as st

# Configuración para pantalla completa
st.set_page_config(layout="wide")

# --- Aquí empieza el truco del header con audio ---
with st.container():
    col1, col2 = st.columns([8, 2])
    with col1:
        st.title("Feliz Cumpleaños Sofi Bonitaaaa")
    with col2:
        st.audio("audio/Til Kingdom Come.mp3", format="audio/mpeg", autoplay=True, start_time=0)
# --- Aquí termina el header con audio ---

# Lógica para navegar entre páginas
if "pagina" not in st.session_state:
    st.session_state.pagina = "inicio"  # Página inicial por defecto

# Página 1
if st.session_state.pagina == "inicio":
    col1, col2, col3 = st.columns([1, 3, 1])

    with col2:
        st.image("imgs/imagen01.jpeg", caption="17 de diciembre de 2024. Amo hacer FaceTime contigo")
        st.markdown("<h2 style='text-align: center; color: white;'>Te quiero mucho mucho mucho</h2>", unsafe_allow_html=True)
        
        # Botón para resolver (habilitado solo si los datos están completos)
        if st.button("Comencemos jiji", use_container_width=True):
            st.session_state.pagina = "Pagina2"
            st.rerun()
            
# Página 2
elif st.session_state.pagina == "Pagina2":
    col1, col2, col3 = st.columns([1, 3, 1])

    with col2:
        st.title("Holaaaa mi sofi bonita <3")
        st.text("Me da muchisima alegría que hayas logrado encontrar la página jiji")

        st.text("Quizá esto sea muy ñoño o no sé que sea, pero queria demostrarte que hasta programando me tomaría el tiempo para hacerte algo especial (así como tú lo eres).")
        st.text("Estoy tan contento de estar para ti en otro añito de tu vida, sé que estos mesesitos han sido algo dificiles por el hecho de estudiar fuera y tener que acostumbrarte, pero creeme cuando te digo que lo estás haciendo muy bien <3")
        st.text("De verdad espero estar para ti y estar presente en los años que vengan porque amo estar contigo.")

        st.image("imgs/imagen02.jpeg", caption = "10 de diciembre de 2024. Ese día me puse muy nervioso porque jamás había metido una niña a mi salón jiji (perdon x la cara fea)")

        st.text("Quizá esto no sea el gran regalo así que digas guaooo, pero te lo hago con mucho cariño, oki?")

        st.markdown("""
            <style>
                .hidden-word {
                    color: white;
                    font-size: 18px;
                    transition: color 0.3s ease-in-out;
                }
                .hidden-word:hover {
                    color: transparent;
                }
                .hidden-word:hover::after {
                    content: '12/07/22'; /* Aquí va la contraseña */
                    color: #Ca80E9; /* Puedes cambiar el color si quieres */
                    font-weight: bold;
                }
            </style>
            
            <p><span class="hidden-word"> Te quiero muchísimo <3 </span></p>
        """, unsafe_allow_html=True)

        st.text("Aún te tengo una última sopresita jiji (aunque no sé si la verás antes que esto o después, ya veremos bonita <3")

        st.divider()

        st.title("contraseña 🔒")

        # Inicializar variable en session_state
        if "acceso_permitido" not in st.session_state:
            st.session_state.acceso_permitido = False

        # Si la contraseña aún no es correcta
        if not st.session_state.acceso_permitido:
            contraseña_fridita = st.text_input("Ingresa la contraseña mi mar:", type="password")
            st.write("Es una fecha importante jiji")
            st.write("??/??/??")

            if contraseña_fridita == "12/07/22":
                st.session_state.acceso_permitido = True
                st.rerun()  # Recarga la app para actualizar la interfaz
            elif contraseña_fridita:  # Solo mostrar mensaje si el usuario escribió algo
                st.error("Ayy sofi, quizá deberías buscar en el texto anterior jiji")
                
        # Si la contraseña es correcta, mostrar el acceso
        if st.session_state.acceso_permitido:
            st.success("Yeiii, por fin mi bonita <3")
             # Botón para resolver (habilitado solo si los datos están completos)
            if st.button("💖", use_container_width=True):
                st.session_state.pagina = "Pagina3"
                st.rerun()

# Página 4
elif st.session_state.pagina == "Pagina3":        
    
    col1, col2, col3 = st.columns([1, 3, 1])
     
    with col2:
        st.title("Haces mis días más bonitos sofi")

        st.image("imgs/imagen03.jpeg", caption = "27 de diciembre de 2024. Ese día te veías muy bonita jiji")

        st.text("Gracias por todo mi sofi bonita, de verdad estoy muy agradecido con dios y con la vida de poder ser parte de lo que haces, te quiero mil ocho mil millones, con toda mi alma y con todo mi corazoncito, eres increible y eres la mejor <3, la mejor en cada cosa que haces, creeme que me fascinas en cada cosa que haces, en cada cosa que dices, en cada cosa que piensas, en cada cosa que sientes. Me fascina como eres <3")

        st.divider()

        st.title("Canciones que ya te pertenecen <3")

        st.subheader("Quizá si el mundo gira más despacio 🤍")
        st.markdown("""
                    <iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/6P70hz3JRyFLp0tL4HWrZD?utm_source=generator" width="100%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
        """, unsafe_allow_html=True)
        
        st.subheader("No dejes nunca de pensar en mi")
        st.markdown("""
                    <iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/00YJ1m8El41cHi3airbL0c?utm_source=generator" width="100%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>            
        """, unsafe_allow_html=True)

        st.subheader("When I'm with you everything goes slow") 
        st.markdown("""
                    <iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/45J4avUb9Ni0bnETYaYFVJ?utm_source=generator" width="100%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
        """, unsafe_allow_html=True)

        st.subheader("I wouldn't change a single thing")
        st.markdown("""
                    <iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/1wQXj5bgxyZQ2XmE2X9s6n?utm_source=generator" width="100%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
        """, unsafe_allow_html=True)

        st.subheader("Cuéntame siquiera que animales viste en las nubes")
        st.markdown("""
                    <iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/6EjBcoyPVn99cpRfoDiuRf?utm_source=generator" width="100%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
        """, unsafe_allow_html=True)

        st.write("Espero que te guste la cancioncita, la elegí con mucho cariño <3")
        
        st.header("Feliz vida mi bonita, te quiero tanto <3")
        st.write("Pausa la música de fondo para escuchar un audio q grabé para ti jiji (o igual hasta este punto ya no hay música de fondo)")
        st.audio("audio/audio_sofi.mp3", format="audio/mpeg", start_time=0)
        
        if st.button("Volver al inicio"):
            st.session_state.pagina = "inicio"
            st.rerun()
