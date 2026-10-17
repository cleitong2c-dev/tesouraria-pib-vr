import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(
    page_title="Tesouraria - PIB Volta Redonda",
    page_icon="⛪",
    layout="wide"
)

# Gestão de Sessão / Login
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
    st.session_state["user_role"] = None

def login():
    st.image("https://i.imgur.com/v8ZpM9k.jpg", width=120)  # Logomarca PIB
    st.title("⛪ Sistema de Gestão Financeira - PIB Volta Redonda")
    st.subheader("Acesso Restrito")
    
    username = st.text_input("Utilizador")
    password = st.text_input("Palavra-passe", type="password")
    
    if st.button("Entrar"):
        if username == "tesoureiro" and password == "tesouraria2026":
            st.session_state["logged_in"] = True
            st.session_state["user_role"] = "Tesouraria"
            st.success("Login efetuado com sucesso!")
            st.rerun()
        elif username == "conselho" and password == "conselho2026":
            st.session_state["logged_in"] = True
            st.session_state["user_role"] = "Conselho"
            st.success("Login efetuado com sucesso!")
            st.rerun()
        else:
            st.error("Utilizador ou palavra-passe incorretos.")

if not st.session_state["logged_in"]:
    login()
else:
    # Sidebar
    st.sidebar.image("https://i.imgur.com/v8ZpM9k.jpg", width=100)
    st.sidebar.title("PIB Volta Redonda")
    st.sidebar.write(f"**Perfil:** {st.session_state['user_role']}")
    
    if st.sidebar.button("Sair / Logout"):
        st.session_state["logged_in"] = False
        st.session_state["user_role"] = None
        st.rerun()

    # Menu Navegação
    menu = st.sidebar.radio("Navegação", [
        "Dashboard / Início", 
        "Carregamento Atos 6", 
        "Entradas & Saídas", 
        "Bancos & Cofre", 
        "Controle Gerencial", 
        "Assistente Farol"
    ])

    st.title(f"📌 {menu}")
    st.info("Sistema ativo e pronto para operacionalização da tesouraria.")
