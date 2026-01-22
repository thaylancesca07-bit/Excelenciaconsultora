import streamlit as st
from datetime import datetime, time

# --- 1. CONFIGURACIÓN ROBUSTA ---
st.set_page_config(
    page_title="RRHH Gestión 🇵🇾",
    layout="centered",
    page_icon="📱",
    initial_sidebar_state="collapsed"
)

# --- 2. ESTILO VISUAL (CSS LIMPIO) ---
# Eliminé los trucos complejos. Este estilo solo embellece los botones.
st.markdown("""
<style>
    /* Fondo limpio */
    .stApp { background-color: #F0F2F5; }
    
    /* Títulos en azul corporativo */
    h1, h2, h3 { color: #003366; text-align: center; }

    /* BOTONES ESTILO TARJETA (Grande y legible) */
    div.stButton > button {
        width: 100%;
        height: 90px;              /* Altura fija cómoda */
        background-color: white;   /* Fondo blanco */
        color: #003366;            /* Texto azul */
        font-size: 18px;           /* Letra grande */
        font-weight: bold;
        border: 1px solid #ddd;
        border-radius: 12px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        margin-bottom: 10px;
        transition: transform 0.1s;
    }
    div.stButton > button:hover {
        transform: scale(1.02);
        border-color: #003366;
        color: #0056b3;
    }

    /* Tarjetas de información (El marco blanco) */
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        border-top: 4px solid #003366;
    }
    
    /* Ocultar menú de desarrollo */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# --- 3. DATOS DE MEMORIA (SESSION STATE) ---
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Datos simulados que persisten mientras la app está abierta
if 'usuario' not in st.session_state:
    st.session_state.usuario = {
        "nombre": "Juan Pérez",
        "cargo": "Analista Senior",
        "area": "Finanzas",
        "salario": 3500000,
        "vacaciones_saldo": 12,
        "asistencia_hoy": {"entrada": None, "salida": None}
    }

# --- 4. FUNCIÓN DE NAVEGACIÓN SEGURA ---
def ir_a(pagina):
    st.session_state.page = pagina
    st.rerun()

def volver():
    st.markdown("---")
    # Columna central para el botón
    col1, col2, col3 = st.columns([1, 4, 1])
    with col2:
        if st.button("🏠 Volver al Menú Principal"):
            ir_a('home')

# --- 5. PANTALLAS ---

# === PANTALLA DE INICIO (MENÚ) ===
if st.session_state.page == 'home':
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"<h2>👋 Hola, {st.session_state.usuario['nombre'].split()[0]}</h2>", unsafe_allow_html=True)
    st.caption("Panel de Control RRHH")
    st.markdown("---")

    # GRID AUTOMÁTICO (4 columnas en PC, 1 en Celular automáticamente)
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("👤\nMi Perfil"): ir_a('perfil')
    with col2:
        if st.button("💼\nLaboral"): ir_a('laboral')
    with col3:
        if st.button("⏰\nAsistencia"): ir_a('asistencia')
    with col4:
        if st.button("💰\nPagos"): ir_a('pagos')

    col5, col6, col7, col8 = st.columns(4)
    
    with col5:
        if st.button("🏖️\nVacaciones"): ir_a('vacaciones')
    with col6:
        if st.button("🏥\nIPS"): ir_a('ips')
    with col7:
        if st.button("📋\nEvaluar"): ir_a('evaluacion')
    with col8:
        if st.button("🚪\nSalida"): ir_a('salida')

# === PANTALLA 1: PERFIL ===
elif st.session_state.page == 'perfil':
    st.title("👤 Mi Perfil")
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader(st.session_state.usuario['nombre'])
        st.write(f"*Cargo:* {st.session_state.usuario['cargo']}")
        st.markdown("---")
        
        # Formulario
        nuevo_nombre = st.text_input("Nombre Completo", st.session_state.usuario['nombre'])
        telefono = st.text_input("Celular", "0981 000 000")
        email = st.text_input("Correo", "juan@empresa.com")
        
        if st.button("💾 Guardar Datos"):
            st.session_state.usuario['nombre'] = nuevo_nombre
            st.success("Datos guardados correctamente")
        
        st.markdown('</div>', unsafe_allow_html=True)
    volver()

# === PANTALLA 2: LABORAL ===
elif st.session_state.page == 'laboral':
    st.title("💼 Info Laboral")
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        c1.metric("Área", st.session_state.usuario['area'])
        c2.metric("Antigüedad", "2 Años")
        
        st.markdown("---")
        st.info("📌 Tipo de Contrato: Indefinido")
        st.info("📌 Seguro Médico: Santa Clara (Activo)")
        
        st.markdown('</div>', unsafe_allow_html=True)
    volver()

# === PANTALLA 3: ASISTENCIA ===
elif st.session_state.page == 'asistencia':
    st.title("⏰ Asistencia")
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        
        st.write(f"Fecha: *{datetime.now().strftime('%d/%m/%Y')}*")
        
        c1, c2 = st.columns(2)
        with c1:
            hora_e = st.time_input("Entrada", value=time(8,0))
        with c2:
            hora_s = st.time_input("Salida", value=time(17,0))
            
        if st.button("✅ Marcar Asistencia", type="primary"):
            st.session_state.usuario['asistencia_hoy'] = {"entrada": hora_e, "salida": hora_s}
            st.success("Marca registrada con éxito")
            
        st.warning("⚠️ Alerta: Tienes 1 llegada tardía esta semana")
        st.markdown('</div>', unsafe_allow_html=True)
    volver()

# === PANTALLA 4: PAGOS ===
elif st.session_state.page == 'pagos':
    st.title("💰 Mis Pagos")
    
    # Cálculos
    salario = st.session_state.usuario['salario']
    ips = salario * 0.09
    neto = salario - ips
    
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        col1.metric("Salario Base", f"Gs. {salario:,.0f}")
        col2.metric("Descuento IPS", f"- {ips:,.0f}")
        
        st.divider()
        st.metric("💵 NETO A COBRAR", f"Gs. {neto:,.0f}")
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.button("📩 Descargar Recibo (PDF)")
        
        st.markdown('</div>', unsafe_allow_html=True)
    volver()

# === PANTALLA 5: VACACIONES ===
elif st.session_state.page == 'vacaciones':
    st.title("🏖️ Vacaciones")
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        
        saldo = st.session_state.usuario['vacaciones_saldo']
        st.metric("Días Disponibles", f"{saldo} Días")
        
        st.write("### Solicitar Días")
        fechas = st.date_input("Selecciona fecha inicio y fin", [])
        
        if st.button("Enviar Solicitud"):
            st.success("Solicitud enviada a tu jefe para aprobación.")
            
        st.markdown('</div>', unsafe_allow_html=True)
    volver()

# === PANTALLA 6: IPS ===
elif st.session_state.page == 'ips':
    st.title("🏥 IPS y Salud")
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        
        st.success("✅ Tu seguro IPS está ACTIVO")
        
        st.markdown("---")
        st.subheader("Subir Reposo Médico")
        archivo = st.file_uploader("Foto del certificado")
        
        if st.button("Enviar Reposo"):
            st.info("Documento enviado a RRHH.")
            
        st.markdown('</div>', unsafe_allow_html=True)
    volver()

# === PANTALLA 7: EVALUACIÓN ===
elif st.session_state.page == 'evaluacion':
    st.title("📋 Evaluación")
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        
        st.write("Autoevaluación Mensual")
        puntaje = st.slider("¿Cómo calificas tu desempeño?", 1, 10, 8)
        
        st.write(f"Tu calificación: *{puntaje}/10*")
        st.progress(puntaje / 10)
        
        st.text_area("Comentarios / Logros del mes")
        st.button("Enviar Evaluación")
        
        st.markdown('</div>', unsafe_allow_html=True)
    volver()

# === PANTALLA 8: SALIDA ===
elif st.session_state.page == 'salida':
    st.title("🚪 Desvinculación")
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        
        st.warning("Zona de Procesos de Salida")
        
        motivo = st.selectbox("Motivo", ["Renuncia", "Despido", "Jubilación"])
        fecha = st.date_input("Fecha de Salida")
        
        c1, c2 = st.columns(2)
        c1.button("Simular Liquidación")
        c2.button("Pedir Constancia")
        
        st.markdown('</div>', unsafe_allow_html=True)
    volver()
