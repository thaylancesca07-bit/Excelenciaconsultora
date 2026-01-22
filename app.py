import streamlit as st
import pandas as pd
from datetime import datetime, time

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="RRHH Gestión Integral 🇵🇾",
    layout="centered",
    page_icon="📱",
    initial_sidebar_state="collapsed" # Ocultamos sidebar para parecer más una App móvil
)

# --- 2. ESTILO CSS (Personalizado para parecer App Móvil) ---
st.markdown("""
<style>
    /* Fondo general */
    .stApp {
        background-color: #F0F2F5;
    }
    
    /* Encabezados */
    h1, h2, h3 {
        color: #003366;
        text-align: center;
        font-family: 'Arial', sans-serif;
    }

    /* Estilo de los Botones del Menú Principal (Simulando Tarjetas) */
    div.stButton > button {
        width: 100%;
        height: 100p…
[11:00 AM, 22/01/2026] Thaylan Cesca: import streamlit as st
import pandas as pd
from datetime import datetime, time
import base64

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="RRHH Gestión Integral 🇵🇾",
    layout="centered", # 'centered' es mejor para simular App móvil. Usa 'wide' para llenar toda la pantalla de PC.
    page_icon="📱",
    initial_sidebar_state="auto" # 'auto' colapsa en móvil y expande en PC
)

# --- 2. ESTILO CSS RESPONSIVO (LA MAGIA ESTÁ AQUÍ 🪄) ---
st.markdown("""
<style>
    /* Fondo general */
    .stApp {
        background-color: #F0F2F5;
    }
    
    /* Títulos */
    h1, h2, h3 {
        color: #003366;
        font-family: 'Helvetica', sans-serif;
        font-weight: 700;
        text-align: center;
    }

    /* ESTILO BASE DE BOTONES (PC y MÓVIL) */
    div.stButton > button {
        background-color: #FFFFFF;
        color: #003366;
        font-weight: 800;
        border: 2px solid #E0E0E0;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: all 0.2s ease;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        line-height: 1.4;
        width: 100%;
    }

    div.stButton > button:hover {
        transform: translateY(-3px);
        background-color: #F8F9FA;
        color: #0056b3;
        border-color: #003366;
    }

    /* --- MEDIA QUERY: REGLAS SOLO PARA CELULARES (Pantallas < 768px) --- */
    @media (max-width: 768px) {
        div.stButton > button {
            height: 100px !important;  /* Botones ALTOS en celular para tocar fácil */
            font-size: 18px !important; /* Letra GRANDE en celular */
        }
        /* Ocultar elementos decorativos en móvil si molestan */
        .desktop-only { display: none; }
    }

    /* --- MEDIA QUERY: REGLAS SOLO PARA PC (Pantallas > 768px) --- */
    @media (min-width: 769px) {
        div.stButton > button {
            height: 80px !important;   /* Botones más compactos en PC */
            font-size: 16px !important; /* Letra normal */
        }
        /* Clase para ocultar cosas en PC que son solo de móvil */
        .mobile-only { display: none; }
    }

    /* Estilo de Tarjetas de Info */
    .info-card {
        background-color: white;
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        margin-bottom: 20px;
        border-top: 5px solid #003366;
    }

    /* Ocultar menú default de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
</style>
""", unsafe_allow_html=True)

# --- 3. GESTIÓN DE ESTADO ---
if 'page' not in st.session_state: st.session_state.page = 'home'
if 'datos_colaborador' not in st.session_state:
    st.session_state.datos_colaborador = {
        "nombre": "Juan Pérez", "cedula": "1.234.567",
        "correo": "juan.perez@email.com", "telefono": "0981 123 456",
        "cargo": "Analista", "area": "Finanzas",
        "salario": 3500000, "ingreso": datetime.today()
    }

# --- 4. NAVEGACIÓN ---
def navegar_a(pagina):
    st.session_state.page = pagina
    st.rerun()

def volver_inicio():
    st.markdown("---")
    c1, c2, c3 = st.columns([1,2,1])
    with c2:
        if st.button("🏠 Menú Principal"):
            st.session_state.page = 'home'
            st.rerun()

# --- 5. PANTALLAS ---

# === PANTALLA PRINCIPAL (MENÚ) ===
if st.session_state.page == 'home':
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Encabezado Diferente según dispositivo (Usando clases CSS)
    st.markdown(f"""
    <div style='text-align: left;'>
        <h2>👋 Hola, {st.session_state.datos_colaborador['nombre'].split()[0]}</h2>
        <p class='mobile-only' style='color:gray;'>Versión Móvil 📱</p>
        <p class='desktop-only' style='color:gray;'>Versión Escritorio 💻 - Panel de Control</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")

    # --- DISEÑO RESPONSIVO (GRID) ---
    # En PC queremos 4 botones por fila. En Celular Streamlit fuerza 1 por fila automáticamente.
    
    # Fila 1
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("👤\nDatos"): navegar_a('datos')
    with col2:
        if st.button("💼\nLaboral"): navegar_a('laboral')
    with col3:
        if st.button("⏰\nAsistencia"): navegar_a('asistencia')
    with col4:
        if st.button("💰\nPagos"): navegar_a('pagos')

    # Fila 2
    col5, col6, col7, col8 = st.columns(4)
    with col5:
        if st.button("🏖️\nVacas"): navegar_a('vacaciones')
    with col6:
        if st.button("🏥\nIPS"): navegar_a('ips')
    with col7:
        if st.button("📈\nEval"): navegar_a('evaluacion')
    with col8:
        if st.button("🚪\nSalida"): navegar_a('salida')

# === 1. DATOS DEL COLABORADOR ===
elif st.session_state.page == 'datos':
    st.title("👤 Datos Personales")
    with st.container():
        st.markdown('<div class="info-card">', unsafe_allow_html=True)
        c_img, c_txt = st.columns([1, 3])
        with c_img: st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=80)
        with c_txt:
            st.subheader(st.session_state.datos_colaborador["nombre"])
            st.write(f"*C.I.:* {st.session_state.datos_colaborador['cedula']}")
        
        st.markdown("---")
        nuevo_nombre = st.text_input("Nombre Completo", st.session_state.datos_colaborador["nombre"])
        nuevo_correo = st.text_input("Correo", st.session_state.datos_colaborador["correo"])
        nuevo_tel = st.text_input("Teléfono", st.session_state.datos_colaborador["telefono"])
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("💾 Guardar"):
            st.session_state.datos_colaborador.update({"nombre": nuevo_nombre, "correo": nuevo_correo, "telefono": nuevo_tel})
            st.success("Guardado")
        st.markdown('</div>', unsafe_allow_html=True)
    volver_inicio()

# === 2. INFORMACIÓN LABORAL ===
elif st.session_state.page == 'laboral':
    st.title("💼 Información Laboral")
    with st.container():
        st.markdown('<div class="info-card">', unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        c1.write(f"*Cargo:* {st.session_state.datos_colaborador['cargo']}")
        c2.write(f"*Área:* {st.session_state.datos_colaborador['area']}")
        st.markdown("---")
        cargo = st.selectbox("Cargo", ["Analista", "Gerente", "Operario"], index=0)
        area = st.selectbox("Área", ["Finanzas", "RRHH", "Operaciones"], index=0)
        st.date_input("Ingreso", value=st.session_state.datos_colaborador["ingreso"])
        st.markdown('</div>', unsafe_allow_html=True)
    volver_inicio()

# === 3. ASISTENCIA ===
elif st.session_state.page == 'asistencia':
    st.title("⏰ Asistencia")
    with st.container():
        st.markdown('<div class="info-card">', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1: entrada = st.time_input("Entrada", value=time(8, 0))
        with col2: salida = st.time_input("Salida", value=time(17, 30))
        if st.button("✅ Marcar"): st.success(f"Registrado: {entrada} - {salida}")
        st.markdown("<br>", unsafe_allow_html=True)
        st.info("Horas Extras Hoy: 02:00 Hs")
        st.markdown('</div>', unsafe_allow_html=True)
    volver_inicio()

# === 4. PAGOS ===
elif st.session_state.page == 'pagos':
    st.title("💰 Remuneraciones")
    salario = st.session_state.datos_colaborador["salario"]
    ips = salario * 0.09
    neto = salario - ips
    with st.container():
        st.markdown('<div class="info-card">', unsafe_allow_html=True)
        st.metric("Base", f"Gs. {salario:,.0f}".replace(",", "."))
        st.metric("IPS (9%)", f"- {ips:,.0f}".replace(",", "."))
        st.markdown("---")
        st.markdown(f"<h3 style='color:green; text-align:center;'>Neto: Gs. {neto:,.0f}</h3>".replace(",", "."), unsafe_allow_html=True)
        if st.button("📩 Enviar Recibo"): st.toast("Enviado")
        st.markdown('</div>', unsafe_allow_html=True)
    volver_inicio()

# === 5. VACACIONES ===
elif st.session_state.page == 'vacaciones':
    st.title("🏖️ Vacaciones")
    with st.container():
        st.markdown('<div class="info-card">', unsafe_allow_html=True)
        fechas = st.date_input("Rango", [])
        if st.button("Solicitar"): st.success("Enviado a aprobación")
        st.markdown("---")
        c1, c2 = st.columns(2)
        c1.metric("Saldo", "12 Días")
        c2.metric("Usados", "0 Días")
        st.markdown('</div>', unsafe_allow_html=True)
    volver_inicio()

# === 6. IPS ===
elif st.session_state.page == 'ips':
    st.title("🏥 IPS / Social")
    with st.container():
        st.markdown('<div class="info-card">', unsafe_allow_html=True)
        st.success("✅ IPS: ACTIVO")
        st.markdown("---")
        tipo = st.selectbox("Reposo por:", ["Enfermedad", "Accidente", "Maternidad"])
        archivo = st.file_uploader("Foto Certificado")
        if st.button("Subir"): st.warning("Enviado a RRHH")
        st.markdown('</div>', unsafe_allow_html=True)
    volver_inicio()

# === 7. EVALUACIÓN ===
elif st.session_state.page == 'evaluacion':
    st.title("📈 Desempeño")
    with st.container():
        st.markdown('<div class="info-card">', unsafe_allow_html=True)
        prod = st.slider("Productividad", 0, 100, 85)
        st.progress(prod / 100)
        st.markdown(f"<h3 style='text-align:center;'>{prod}/100</h3>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    volver_inicio()

# === 8. SALIDA ===
elif st.session_state.page == 'salida':
    st.title("🚪 Desvinculación")
    with st.container():
        st.markdown('<div class="info-card">', unsafe_allow_html=True)
        st.date_input("Fecha Salida")
        st.selectbox("Motivo", ["Renuncia", "Despido"])
        st.checkbox("Devolución Uniforme")
        if st.button("Generar Liquidación"): st.success("Calculado")
        st.markdown('</div>', unsafe_allow_html=True)
    volver_inicio()

