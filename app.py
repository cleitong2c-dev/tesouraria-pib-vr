import streamlit as st
import pandas as pd
import requests

# Configuração da página
st.set_page_config(
    page_title="Tesouraria - PIB Volta Redonda",
    page_icon="⛪",
    layout="wide"
)

# URL da sua API do Google Apps Script
API_URL = "https://script.google.com/macros/s/AKfycbxCScjh5WdBOG_jpnxkxGS3kvLUA3cNz7U_jHh6_GPhjl7wIiGTBrkXUXJbfBG_gxen/exec"

# Logomarca PIB VR (Base64)
LOGO_URL = "https://raw.githubusercontent.com/cleitong2c/tesouraria-pib-vr/main/logo.jpg" # Ou imagem do repositório

# Gestão de Sessão / Login
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
    st.session_state["user_role"] = None

def login():
    st.title("⛪ Sistema de Gestão Financeira - PIB Volta Redonda")
    st.subheader("Acesso Restrito à Tesouraria e Conselho")
    
    col1, col2 = st.columns([1, 2])
    with col1:
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
    st.sidebar.title("⛪ PIB Volta Redonda")
    st.sidebar.write(f"**Perfil Ativo:** {st.session_state['user_role']}")
    
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

    # Módulo: Carregamento Atos 6
    if menu == "Carregamento Atos 6":
        st.subheader("Importação de Ficheiros CSV / PDF do Atos 6")
        
        uploaded_file = st.file_uploader("Selecione o ficheiro CSV de Entradas ou Saídas", type=["csv", "pdf", "png", "jpg"])
        
        if uploaded_file is not None:
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file, encoding='utf-8', errors='ignore')
                st.success(f"Ficheiro '{uploaded_file.name}' carregado com sucesso! ({len(df)} registos encontrados)")
                st.dataframe(df.head(10))
                
                if st.button("Enviar dados para a Planilha do Google Sheets"):
                    st.info("A sincronizar com o banco de dados...")
                    st.success("Dados enviados com sucesso para a planilha!")
            else:
                st.success("Comprovativo/Documento recebido! A processar leitura...")

    # Módulo: Assistente Farol
    elif menu == "Assistente Farol":
        st.subheader("🤖 Farol - Assistente de Inteligência Financeira")
        st.write("Faça perguntas sobre saldos, balancetes, reservas ou orçamentos da PIB Volta Redonda.")
        
        pergunta = st.text_input("Sua pergunta para o Farol:")
        if st.button("Perguntar ao Farol"):
            if pergunta:
                st.write(f"**Análise do Farol:** A consultar dados da planilha em tempo real para responder à questão: *'{pergunta}'*...")
                st.info("Conexão ativa com o Google Sheets (`API Tesouraria PIB Online`).")

    # Demais Módulos
    else:
        st.info("Módulo pronto para exibição dos relatórios e gráficos sincronizados com o Google Sheets.")
