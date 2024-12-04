import streamlit as st
import streamlit_authenticator as stauth
from streamlit_option_menu import option_menu

lesDonneesDesComptes = {'usernames': {'utilisateur': {'name': 'utilisateur',
   'password': 'utilisateurMDP',
   'email': 'utilisateur@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'utilisateur'},
   'root': {'name': 'root',
   'password': 'rootMDP',
   'email': 'admin@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'administrateur'}}}

authenticator = stauth.Authenticate(
    lesDonneesDesComptes, # Les données des comptes
    "cookie name", # Le nom du cookie, un str quelconque
    "cookie key", # La clé du cookie, un str quelconque
    30, # Le nombre de jours avant que le cookie expire 
)


authenticator.login()



def page():
    if selection == "Accueil":
        st.title("Bienvenidos Compañero")
        st.image("deguisement-de-mexicain-poncho.jpg")
    
    elif selection == "Photos":
        st.title("Mexico es un guapo pays !!")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image("mexico-city-1280x800.jpeg")
        with col2:
            st.image("burritos_0536-500x500.jpg")
        with col3:
            st.image("tabasco_6-min_05b50b82-582f-4865-aa8f-166758c34e10_900x.webp")
   

if st.session_state["authentication_status"]:
    with st.sidebar:
        selection = option_menu(
                    menu_title=None,
                    options = ["Accueil", "Photos"]
        )
        authenticator.logout("Déconnexion")

    page()
  

elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')