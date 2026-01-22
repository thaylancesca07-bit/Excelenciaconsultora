import streamlit as st
import pandas as pd
from datetime import datetime, time
import base64

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="RRHH Gestión Integral 🇵🇾",
    layout="centered",
    page_icon="📱",
    initial_sidebar_state="collapsed"
)

# --- 2. ESTILO CSS MEJORADO (Estilo Tarjeta App Móvil) ---
st.markdown("""
<style>
    /* Fondo general de la App */
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

    /* ESTILO DE LOS BOTONES (LAS TARJETAS DEL MENÚ) */
    div.stButton > button {
        width: 100%;
        height: 110px;              /* Altura fija para que parezcan tarjetas */
        background-color: #FFFFFF;  /* Fondo Blanco para máxima legibilidad */
        color: #003366;             /* Texto Azul Oscuro */
        font-size: 18px;            /* Texto grande */
        font-weight: 800;           /* Texto en negrita */
        border: 2px solid #E0E0E0;  /* Borde suave */
        border-radius: 15px;        /* Bordes redondeados */
        box-shadow: 0 4px 6px rgba(0,0,0,0.1); /* Sombra suave */
        transition: all 0.2s ease;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        line-height: 1.4;
    }

    /* Efecto al pasar el mouse (Hover) */
    div.stButton > button:hover {
        transform: translateY(-3px); /* Se levanta un poco */
        box-shadow: 0 6px 12px rgba(0,0,0,0.15);
        border-color: #003366;
        background-color: #F8F9FA;
        color: #0056b3;
    }

    /* Estilo de los Contenedores de Información (Info Cards) */
    .info-card {
        background-color: white;
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        margin-bottom: 20px;
        border-top: 5px solid #003366; /* Detalle de color arriba */
    }

    /* Alertas personalizadas */
    .alert-box {
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 10px;
        font-weight: bold;
        text-align: center;
    }
    .success { background-color: #D4EDDA; color: #155724; border: 1px solid #C3E6CB; }
    .warning { background-color: #FFF3CD; color: #856404; border: 1px solid #FFEEBA; }
    .danger  { background-color: #F8D7DA; color: #721C24; border: 1px solid #F5C6CB; }

    /* Forzar ocultar el menú de hamburguesa de Streamlit para que parezca más App */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
</style>
""", unsafe_allow_html=True)

# --- 3. GESTIÓN DE ESTADO (SESSION STATE) ---
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Datos de ejemplo persistentes
if 'datos_colaborador' not in st.session_state:
    st.session_state.datos_colaborador = {
        "nombre": "Juan Pérez",
        "cedula": "1.234.567",
        "correo": "juan.perez@email.com",
        "telefono": "0981 123 456",
        "cargo": "Analista",
        "area": "Finanzas",
        "salario": 3500000,
        "ingreso": datetime.today()
    }

# --- 4. NAVEGACIÓN ---
def navegar_a(pagina):
    st.session_state.page = pagina
    st.rerun()

def volver_inicio():
    st.markdown("---")
    # Botón de volver con estilo distinto (más pequeño)
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("🏠 Volver al Menú Principal"):
            st.session_state.page = 'home'
            st.rerun()

# --- 5. PANTALLAS DE LA APP ---

# === PANTALLA PRINCIPAL (MENÚ) ===
if st.session_state.page == 'home':
    # Encabezado
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='text-align: left;'>👋 Hola, {st.session_state.datos_colaborador['nombre'].split()[0]}</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: left; color: gray;'>Gestión de Recursos Humanos</p>", unsafe_allow_html=True)
    st.markdown("---")

    # GRID DE BOTONES (2 Columnas)
    # Usamos Emojis grandes para dar color y contexto visual
    
    c1, c2 = st.columns(2)
    with c1:
        if st.button("👤\nDatos Personales"): navegar_a('datos')
    with c2:
        if st.button("💼\nInfo Laboral"): navegar_a('laboral')
    
    c3, c4 = st.columns(2)
    with c3:
        if st.button("⏰\nAsistencia"): navegar_a('asistencia')
    with c4:
        if st.button("💰\nPagos"): navegar_a('pagos')

    c5, c6 = st.columns(2)
    with c5:
        if st.button("🏖️\nVacaciones"): navegar_a('vacaciones')
    with c6:
        if st.button("🏥\nIPS / Social"): navegar_a('ips')

    c7, c8 = st.columns(2)
    with c7:
        if st.button("📈\nEvaluación"): navegar_a('evaluacion')
    with c8:
        if st.button("🚪\nSalida"): navegar_a('salida')


# === 1. DATOS DEL COLABORADOR ===
elif st.session_state.page == 'datos':
    st.title("👤 Datos Personales")
    
    with st.container():
        st.markdown('<div class="info-card">', unsafe_allow_html=True)
        
        # Perfil Visual
        c_img, c_txt = st.columns([1, 2])
        with c_img:
            # Avatar genérico
            st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=90)
        with c_txt:
            st.subheader(st.session_state.datos_colaborador["nombre"])
            st.write(f"**C.I.:** {st.session_state.datos_colaborador['cedula']}")
        
        st.markdown("---")
        
        # Formulario
        nuevo_nombre = st.text_input("Nombre Completo", st.session_state.datos_colaborador["nombre"])
        nuevo_correo = st.text_input("Correo Electrónico", st.session_state.datos_colaborador["correo"])
        nuevo_tel = st.text_input("Teléfono / Celular", st.session_state.datos_colaborador["telefono"])
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("💾 Guardar Cambios"):
            st.session_state.datos_colaborador.update({
                "nombre": nuevo_nombre, "correo": nuevo_correo, "telefono": nuevo_tel
            })
            st.success("¡Datos actualizados correctamente!")
        
        st.markdown('</div>', unsafe_allow_html=True)
    volver_inicio()


# === 2. INFORMACIÓN LABORAL ===
elif st.session_state.page == 'laboral':
    st.title("💼 Información Laboral")
    
    with st.container():
        st.markdown('<div class="info-card">', unsafe_allow_html=True)
        
        st.write(f"**Cargo Actual:** {st.session_state.datos_colaborador['cargo']}")
        st.write(f"**Área:** {st.session_state.datos_colaborador['area']}")
        
        st.markdown("---")
        cargo = st.selectbox("Cambiar Cargo", ["Analista", "Gerente", "Operario", "Vendedor"], index=0)
        area = st.selectbox("Cambiar Área", ["Finanzas", "RRHH", "Operaciones", "Comercial"], index=0)
        contrato = st.selectbox("Tipo de Contrato", ["Indefinido", "Jornalero", "Prestación de Servicios"])
        st.date_input("Fecha de Ingreso", value=st.session_state.datos_colaborador["ingreso"])
        
        st.markdown("---")
        with st.expander("🎁 Ver Beneficios Corporativos"):
            st.info("• Seguro Médico Privado (Santa Clara)\n• Vales de Almuerzo\n• Plus por Asistencia")
            
        st.markdown('</div>', unsafe_allow_html=True)
    volver_inicio()


# === 3. ASISTENCIA ===
elif st.session_state.page == 'asistencia':
    st.title("⏰ Control de Asistencia")
    
    with st.container():
        st.markdown('<div class="info-card">', unsafe_allow_html=True)
        
        fecha_hoy = datetime.now().strftime("%d/%m/%Y")
        st.write(f"**Fecha:** {fecha_hoy}")
        
        col1, col2 = st.columns(2)
        with col1:
            entrada = st.time_input("Entrada", value=time(8, 0))
        with col2:
            salida = st.time_input("Salida", value=time(17, 30))
            
        if st.button("✅ Registrar Marca"):
            st.balloons()
            st.success(f"Marca guardada: {entrada} a {salida}")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Alertas HTML
        st.markdown('<div class="alert-box success">Horas Extras Hoy: 02:00 Hs</div>', unsafe_allow_html=True)
        st.markdown('<div class="alert-box warning">⚠️ Llegada tardía registrada ayer</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    volver_inicio()


# === 4. REMUNERACIONES ===
elif st.session_state.page == 'pagos':
    st.title("💰 Remuneraciones")
    
    salario = st.session_state.datos_colaborador["salario"]
    ips_obrero = salario * 0.09
    neto = salario - ips_obrero
    
    with st.container():
        st.markdown('<div class="info-card">', unsafe_allow_html=True)
        
        st.metric("Salario Base", f"Gs. {salario:,.0f}".replace(",", "."))
        
        c1, c2 = st.columns(2)
        c1.metric("Desc. IPS (9%)", f"- {ips_obrero:,.0f}".replace(",", "."))
        c2.metric("Bonificaciones", "Gs. 0")
        
        st.markdown("---")
        st.markdown(f"<h3 style='color:green;'>Neto a Cobrar: Gs. {neto:,.0f}</h3>".replace(",", "."), unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("📩 Enviar Recibo por Correo"):
            st.toast("Recibo enviado exitosamente.")
            
        st.markdown('</div>', unsafe_allow_html=True)
    volver_inicio()


# === 5. VACACIONES ===
elif st.session_state.page == 'vacaciones':
    st.title("🏖️ Gestión de Vacaciones")
    
    with st.container():
        st.markdown('<div class="info-card">', unsafe_allow_html=True)
        
        st.write("### 📅 Solicitar Días")
        fechas = st.date_input("Seleccione fecha inicio y fin", [])
        
        if len(fechas) == 2:
            dias = (fechas[1] - fechas[0]).days + 1
            st.info(f"Días solicitados: **{dias}**")
            if st.button("Enviar Solicitud"):
                st.success("Solicitud enviada a aprobación.")
        
        st.markdown("---")
        
        c1, c2 = st.columns(2)
        c1.metric("Días Causados", "12")
        c2.metric("Días Tomados", "0")
        
        st.markdown('</div>', unsafe_allow_html=True)
    volver_inicio()


# === 6. IPS ===
elif st.session_state.page == 'ips':
    st.title("🏥 IPS y Seguridad Social")
    
    with st.container():
        st.markdown('<div class="info-card">', unsafe_allow_html=True)
        
        st.markdown('<div class="alert-box success">✅ Afiliación IPS: ACTIVO</div>', unsafe_allow_html=True)
        st.markdown('<div class="alert-box success">✅ Último Aporte: PAGADO</div>', unsafe_allow_html=True)
        
        st.markdown("---")
        st.subheader("Reportar Reposo")
        
        tipo = st.selectbox("Motivo", ["Enfermedad Común", "Accidente Laboral", "Maternidad"])
        archivo = st.file_uploader("Adjuntar Certificado Médico")
        
        if st.button("Subir Reposo"):
            st.warning("Certificado subido. RRHH lo verificará pronto.")
            
        st.markdown('</div>', unsafe_allow_html=True)
    volver_inicio()


# === 7. EVALUACIÓN ===
elif st.session_state.page == 'evaluacion':
    st.title("📈 Evaluación de Desempeño")
    
    with st.container():
        st.markdown('<div class="info-card">', unsafe_allow_html=True)
        
        st.subheader("Evaluación Mensual")
        prod = st.slider("Productividad", 0, 100, 85)
        asis = st.slider("Puntualidad", 0, 100, 90)
        equipo = st.slider("Trabajo en Equipo", 0, 100, 100)
        
        promedio = (prod + asis + equipo) / 3
        st.markdown(f"### Calificación: {promedio:.1f}/100")
        st.progress(promedio / 100)
        
        if promedio > 80:
            st.success("🌟 ¡Excelente Desempeño!")
        
        st.markdown('</div>', unsafe_allow_html=True)
    volver_inicio()


# === 8. DESVINCULACIÓN ===
elif st.session_state.page == 'salida':
    st.title("🚪 Desvinculación")
    
    with st.container():
        st.markdown('<div class="info-card">', unsafe_allow_html=True)
        
        st.date_input("Fecha de Salida Prevista")
        st.selectbox("Motivo", ["Renuncia", "Mutuo Acuerdo", "Despido", "Fin de Contrato"])
        
        st.write("Checklist de Salida:")
        st.checkbox("Devolución de Uniforme")
        st.checkbox("Devolución de Notebook/Celular")
        st.checkbox("Baja IPS Procesada")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        with c1:
            st.button("Calcular Liquidación")
        with c2:
            st.button("Descargar Constancia")
        
        st.markdown('</div>', unsafe_allow_html=True)
    volver_inicio()
