import streamlit as st
import time

# Configuração da Página
st.set_page_config(page_title="Portal RH", layout="wide", initial_sidebar_state="collapsed")

# --- SISTEMA DE LOGIN ---
def verificar_login():
    # Dicionário de usuários (Em produção, use banco de dados ou variáveis de ambiente)
    USUARIOS = {
        "admin": "admin123",
        "gerente": "rh2024",
        "recrutador": "vagas24"
    }

    if 'logado' not in st.session_state:
        st.session_state['logado'] = False
        st.session_state['usuario_atual'] = ""

    if not st.session_state['logado']:
        # Tela de Login Centralizada
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown("## 🔐 Acesso Restrito - RH")
            usuario = st.text_input("Usuário")
            senha = st.text_input("Senha", type="password")
            
            if st.button("Entrar", type="primary"):
                if usuario in USUARIOS and USUARIOS[usuario] == senha:
                    st.session_state['logado'] = True
                    st.session_state['usuario_atual'] = usuario
                    st.toast("Login realizado com sucesso!")
                    time.sleep(0.5)
                    st.rerun()
                else:
                    st.error("Usuário ou senha incorretos.")
        return False
    return True

# --- APLICAÇÃO PRINCIPAL ---
def main():
    # Sidebar só aparece depois de logar
    with st.sidebar:
        st.write(f"👤 Olá, **{st.session_state['usuario_atual'].upper()}**")
        st.markdown("---")
        menu = st.radio("Menu", ["🏠 Dashboard", "👥 Funcionários", "💰 Folha de Pagamento", "📄 Documentos"])
        st.markdown("---")
        if st.button("Sair / Logout"):
            st.session_state['logado'] = False
            st.rerun()

    # Conteúdo das Páginas
    if menu == "🏠 Dashboard":
        st.title("Visão Geral da Empresa")
        col1, col2, col3 = st.columns(3)
        col1.metric("Funcionários Ativos", "142", "+2")
        col2.metric("Folha Mensal", "R$ 450k", "Dentro do orçamento")
        col3.metric("Vagas Abertas", "5", "Urgente")

    elif menu == "👥 Funcionários":
        st.title("Gestão de Colaboradores")
        st.dataframe({"Nome": ["Ana", "Carlos"], "Cargo": ["Analista", "Gerente"]}, use_container_width=True)

    elif menu == "💰 Folha de Pagamento":
        st.title("Processamento de Folha")
        st.warning("Área restrita a Gerentes.")

    elif menu == "📄 Documentos":
        st.title("Repositório de Contratos")
        st.file_uploader("Upload de Contrato (PDF)", type="pdf")

# Execução
if verificar_login():
    main()