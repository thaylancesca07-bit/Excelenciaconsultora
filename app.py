import streamlit as st
import time
from datetime import datetime

# --- 1. CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="RRHH App",
    layout="centered",
    page_icon="👔",
    initial_sidebar_state="collapsed"
)

# --- 2. CSS FORZADO (PARA QUE SE LEA SÍ O SÍ) ---
st.markdown("""
<style>
    /* 1. Fondo General - Gris muy suave */
    .stApp {
        background-color: #E8EAF6 !important;
    }

    /* 2. Ocultar elementos molestos de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* 3. ENCABEZADO AZUL (Estilo App Nativa) */
    .css-10trblm {
        color: white !important;
    }
    
    /* Contenedor del Título */
    .app-header {
        background-color: #003366;
        padding: 20px;
        border-radius: 0 0 20px 20px;
        margin-top: -50px;
        margin-left: -50px;
        margin-right: -50px;
        margin-bottom: 20px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.2);
    }
    .app-header h2 {
        color: white !important;
        font-family: 'Arial', sans-serif;
        font-weight: bold;
        margin: 0;
    }
    .app-header p {
        color: #cfd8dc !important;
        margin: 0;
    }

    /* 4. BOTONES DEL MENÚ (Forzados para leerse bien) */
    div.stButton > button {
        width: 100%;
        height: 100px;
        background-color: #FFFFFF !important; /* Fondo BLANCO puro */
        color: #003366 !important;            /* Texto AZUL OSCURO fuerte */
        border: 2px solid #003366 !important; /* Borde AZUL */
        border-radius: 15px !important;
        font-size: 18px !important;
        font-weight: 900 !important;          /* Letra muy gruesa */
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: transform 0.1s;
    }
    div.stButton > button:hover {
        transform: scale(1.02);
        background-color: #003366 !important; /* Al pasar mouse: Fondo AZUL */
        color: #FFFFFF !important;            /* Texto BLANCO */
    }
    div.stButton > button:active {
        background-color: #002244 !important;
        color: white !important;
    }

    /* 5. TARJETAS DE CONTENIDO (Blanco sobre gris) */
    .content-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        border-top: 5px solid #003366;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        color: #333333 !important; /* Texto negro forzado */
    }
    
    /* Textos generales forzados a oscuro para leerse */
    p, label, span, div {
        color: #0d1b2a;
    }
    
    /* Inputs */
    .stTextInput input {
        background-color: white !important;
        color: black !important;
        border: 1px solid #ccc !important;
    }

</style>
""", unsafe_allow_html=True)

# --- 3. GESTIÓN DE SESIÓN (LOGIN Y DATOS) ---
if 'logueado' not in st.session_state:
    st.session_state.logueado = False

if 'pagina' not in st.session_state:
    st.session_state.pagina = 'login'

# Datos simulados del empleado
if 'usuario' not in st.session_state:
    st.session_state.usuario = {
        "nombre": "Juan Pérez",
        "cedula": "1.234.567",
        "cargo": "Analista",
        "img": "https://cdn-icons-png.flaticon.com/512/3135/3135715.png"
    }

# --- 4. FUNCIONES DE NAVEGACIÓN ---
def ir_a(destino):
    st.session_state.pagina = destino
    st.rerun()

def cerrar_sesion():
    st.session_state.logueado = False
    st.session_state.pagina = 'login'
    st.rerun()

# --- 5. PANTALLAS ---

# === PANTALLA DE LOGIN (LO PRIMERO QUE SE VE) ===
if not st.session_state.logueado:
    st.markdown("""
        <div class="app-header" style="background-color: transparent; box-shadow: none;">
            <h1 style="color:#003366!important; font-size: 40px;">RRHH</h1>
            <h3 style="color:#003366!important;">Gestión Integral</h3>
        </div>
    """, unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="content-card" style="text-align: center;">', unsafe_allow_html=True)
        st.markdown("#### Iniciar Sesión")
        usuario = st.text_input("Usuario (Cédula)")
        password = st.text_input("Contraseña", type="password")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        if st.button("INGRESAR"):
            if usuario and password: # Validación simple
                st.session_state.logueado = True
                st.session_state.pagina = 'home'
                st.rerun()
            else:
                st.error("Ingrese usuario y contraseña")
        st.markdown('</div>', unsafe_allow_html=True)

# === SI YA ESTÁ LOGUEADO ===
else:
    # ENCABEZADO AZUL FIJO (Estilo App)
    st.markdown(f"""
    <div class="app-header">
        <h2>Hola, {st.session_state.usuario['nombre'].split()[0]}</h2>
        <p>{st.session_state.usuario['cargo']} - ID: {st.session_state.usuario['cedula']}</p>
    </div>
    """, unsafe_allow_html=True)

    # === MENÚ PRINCIPAL (HOME) ===
    if st.session_state.pagina == 'home':
        
        # GRID DE BOTONES
        c1, c2 = st.columns(2)
        with c1:
            if st.button("👤\nPerfil"): ir_a('perfil')
        with c2:
            if st.button("💼\nLaboral"): ir_a('laboral')
        
        c3, c4 = st.columns(2)
        with c3:
            if st.button("⏰\nAsistencia"): ir_a('asistencia')
        with c4:
            if st.button("💰\nPagos"): ir_a('pagos')

        c5, c6 = st.columns(2)
        with c5:
            if st.button("🏖️\nVacaciones"): ir_a('vacaciones')
        with c6:
            if st.button("🏥\nIPS"): ir_a('ips')

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🔒 Cerrar Sesión", type="primary"): 
            cerrar_sesion()

    # === PANTALLA 1: PERFIL ===
    elif st.session_state.pagina == 'perfil':
        st.markdown(f"<h3 style='color:#003366;'>Datos del Colaborador</h3>", unsafe_allow_html=True)
        
        with st.container():
            st.markdown('<div class="content-card">', unsafe_allow_html=True)
            c_img, c_info = st.columns([1,2])
            with c_img:
                st.image(st.session_state.usuario['img'], width=80)
            with c_info:
                st.markdown(f"*{st.session_state.usuario['nombre']}*")
                st.caption("Estado: Activo")
            
            st.text_input("Cédula", st.session_state.usuario['cedula'], disabled=True)
            correo = st.text_input("Correo", "juan@gmail.com")
            tel = st.text_input("Teléfono", "0981 123 456")
            
            if st.button("Guardar Cambios"):
                st.success("Datos actualizados")
            st.markdown('</div>', unsafe_allow_html=True)
        
        if st.button("⬅️ Volver"): ir_a('home')

    # === PANTALLA 2: LABORAL ===
    elif st.session_state.pagina == 'laboral':
        st.markdown(f"<h3 style='color:#003366;'>Información Laboral</h3>", unsafe_allow_html=True)
        
        with st.container():
            st.markdown('<div class="content-card">', unsafe_allow_html=True)
            st.selectbox("Cargo", ["Analista", "Gerente"], index=0)
            st.selectbox("Departamento", ["Finanzas", "RRHH"], index=0)
            st.selectbox("Contrato", ["Indefinido", "Jornal"], index=0)
            st.date_input("Fecha Ingreso", value=datetime.today())
            st.markdown('</div>', unsafe_allow_html=True)
            
        if st.button("⬅️ Volver"): ir_a('home')

    # === PANTALLA 3: ASISTENCIA ===
    elif st.session_state.pagina == 'asistencia':
        st.markdown(f"<h3 style='color:#003366;'>Asistencia y Horarios</h3>", unsafe_allow_html=True)
        
        with st.container():
            st.markdown('<div class="content-card">', unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            with col1:
                st.text_input("Entrada", "08:00")
            with col2:
                st.text_input("Salida", "17:00")
            
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown('<div style="background-color:#d4edda; padding:10px; border-radius:5px; text-align:center; color:green; font-weight:bold;">Horas Extras: 2:00 Hs</div>', unsafe_allow_html=True)
            st.markdown('<div style="background-color:#fff3cd; padding:10px; border-radius:5px; text-align:center; color:#856404; font-weight:bold; margin-top:5px;">⚠️ Alerta: 1 Tardanza</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
        if st.button("⬅️ Volver"): ir_a('home')

    # === PANTALLA 4: PAGOS ===
    elif st.session_state.pagina == 'pagos':
        st.markdown(f"<h3 style='color:#003366;'>Remuneraciones</h3>", unsafe_allow_html=True)
        
        with st.container():
            st.markdown('<div class="content-card">', unsafe_allow_html=True)
            st.metric("Salario Base", "Gs. 3.500.000")
            st.metric("Horas Extras", "Gs. 500.000")
            st.markdown("---")
            if st.button("Ver Recibo de Pago"):
                st.info("Descargando PDF...")
            st.markdown('</div>', unsafe_allow_html=True)
            
        if st.button("⬅️ Volver"): ir_a('home')

    # === OTRAS PANTALLAS (Plantilla Genérica) ===
    else:
        st.markdown(f"<h3 style='color:#003366;'>{st.session_state.pagina.upper()}</h3>", unsafe_allow_html=True)
        st.info("Módulo en construcción")
        if st.button("⬅️ Volver"): ir_a('home')
