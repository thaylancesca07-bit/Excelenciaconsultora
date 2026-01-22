import streamlit as st
import pandas as pd
from supabase import create_client, Client
import time
from datetime import datetime

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="RRHH Excelencia", layout="centered", page_icon="👔")

# --- CONEXIÓN BASE DE DATOS (SEGURA) ---
# Intenta leer las claves desde los "Secretos" del servidor
try:
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    supabase: Client = create_client(url, key)
    DB_ONLINE = True
except:
    st.warning("⚠️ Modo Offline: No se detectó conexión a Base de Datos.")
    DB_ONLINE = False

# --- ESTILOS CSS ---
st.markdown("""
<style>
    .stApp { background-color: #F0F2F5; }
    h1, h2, h3 { color: #003366; }
    div.stButton > button {
        width: 100%; height: 60px;
        background-color: white; color: #003366;
        border: 1px solid #003366; border-radius: 10px;
        font-weight: bold; font-size: 16px;
    }
    div.stButton > button:hover {
        background-color: #003366; color: white;
    }
    .card {
        background-color: white; padding: 20px;
        border-radius: 10px; border-top: 5px solid #003366;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1); margin-bottom: 20px;
    }
    #MainMenu, footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# --- FUNCIONES DE ACCESO ---
def login(usuario, password):
    if not DB_ONLINE:
        st.error("Error de conexión a base de datos.")
        return

    try:
        # Buscamos en la tabla 'usuarios' de Supabase
        response = supabase.table("usuarios").select("*").eq("usuario", usuario).eq("password", password).execute()
        
        if len(response.data) > 0:
            user_data = response.data[0]
            st.session_state.user = user_data
            st.session_state.rol = user_data['rol']
            st.success(f"Bienvenido {user_data['nombre']}")
            time.sleep(1)
            st.rerun()
        else:
            st.error("Usuario o contraseña incorrectos")
    except Exception as e:
        st.error(f"Error de sistema: {e}")

def logout():
    st.session_state.user = None
    st.session_state.rol = None
    st.rerun()

# --- INICIALIZACIÓN DE ESTADO ---
if 'user' not in st.session_state: st.session_state.user = None

# --- VISTAS ---

# 1. LOGIN
if not st.session_state.user:
    st.markdown("<h1 style='text-align:center;'>Excelencia Consultora</h1>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        with st.container():
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown("### Iniciar Sesión")
            usr = st.text_input("Usuario")
            pwd = st.text_input("Contraseña", type="password")
            
            if st.button("INGRESAR"):
                login(usr, pwd)
                
            st.caption("Si es la primera vez, el administrador debe crear tu usuario en la Base de Datos.")
            st.markdown('</div>', unsafe_allow_html=True)

# 2. SISTEMA (DENTRO)
else:
    rol = st.session_state.rol
    usuario = st.session_state.user
    
    # Barra Superior
    c1, c2 = st.columns([3,1])
    c1.subheader(f"Hola, {usuario['nombre']}")
    if c2.button("Cerrar Sesión"): logout()
    
    st.markdown("---")

    # --- VISTA SUPER ADMIN (EXCELENCIA) ---
    if rol == 'admin':
        st.info("🔧 Panel de Administrador (Excelencia)")
        col_1, col_2 = st.columns(2)
        with col_1:
            st.markdown('<div class="card"><h4>Empresas</h4><p>Gestionar Clientes</p></div>', unsafe_allow_html=True)
            if st.button("Ver Empresas"): st.toast("Cargando lista...")
        with col_2:
            st.markdown('<div class="card"><h4>Funcionarios</h4><p>Gestionar Personal</p></div>', unsafe_allow_html=True)
            if st.button("Ver Todos los Funcionarios"): st.toast("Cargando personal...")

    # --- VISTA EMPRESA ---
    elif rol == 'empresa':
        st.info(f"🏢 Panel Corporativo: {usuario.get('empresa_nombre', 'Cliente')}")
        st.warning("⚠️ Tienes 2 contratos próximos a vencer.")
        
        st.subheader("Tus Funcionarios")
        # Aquí cargaríamos desde Supabase
        st.text_input("🔍 Buscar funcionario...")
        st.markdown('<div class="card">Juan Pérez - Analista</div>', unsafe_allow_html=True)

    # --- VISTA FUNCIONARIO ---
    elif rol == 'funcionario':
        st.info("👤 Portal del Colaborador")
        
        c1, c2 = st.columns(2)
        with c1: 
            if st.button("👤 Perfil"): st.toast("Datos personales")
        with c2: 
            if st.button("💼 Laboral"): st.toast("Info contrato")
            
        c3, c4 = st.columns(2)
        with c3: 
            if st.button("💰 Pagos"): st.toast("Ver liquidaciones")
        with c4: 
            if st.button("🏥 IPS"): st.toast("Estado de seguro")
