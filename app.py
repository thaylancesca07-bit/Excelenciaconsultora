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
        height: 100px;
        border-radius: 15px;
        border: none;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        font-weight: bold;
        font-size: 16px;
        transition: transform 0.2s;
    }
    div.stButton > button:hover {
        transform: scale(1.02);
    }

    /* Colores específicos para botones (Hack visual usando orden) */
    /* Esto es genérico, Streamlit no permite colorear botones individuales fácilmente sin librerías extra */
    
    /* Contenedores de tarjetas de información */
    .info-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        margin-bottom: 15px;
        border-left: 5px solid #003366;
    }

    /* Alertas */
    .alert-success { background-color: #D4EDDA; color: #155724; padding: 10px; border-radius: 10px; text-align: center; margin-bottom: 10px; }
    .alert-warning { background-color: #FFF3CD; color: #856404; padding: 10px; border-radius: 10px; text-align: center; margin-bottom: 10px; }
    .alert-danger { background-color: #F8D7DA; color: #721C24; padding: 10px; border-radius: 10px; text-align: center; margin-bottom: 10px; }

</style>
""", unsafe_allow_html=True)

# --- 3. GESTIÓN DE ESTADO (SESSION STATE) ---
# Aquí guardamos los datos para que no se borren al cambiar de pantalla
if 'page' not in st.session_state:
    st.session_state.page = 'home'

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

# --- 4. FUNCIONES DE NAVEGACIÓN ---
def navegar_a(pagina):
    st.session_state.page = pagina

def volver_inicio():
    if st.button("⬅️ Volver al Menú", use_container_width=True):
        st.session_state.page = 'home'
        st.rerun()

# --- 5. PANTALLAS DE LA APP ---

# === PANTALLA PRINCIPAL (MENÚ) ===
if st.session_state.page == 'home':
    st.image("https://cdn-icons-png.flaticon.com/512/9323/9323499.png", width=80) # Logo genérico
    st.title("RRHH Gestión Integral")
    st.markdown("---")

    # Fila 1
    c1, c2 = st.columns(2)
    with c1:
        if st.button("👤\nDatos Personales"): navegar_a('datos')
    with c2:
        if st.button("💼\nInfo Laboral"): navegar_a('laboral')
    
    # Fila 2
    c3, c4 = st.columns(2)
    with c3:
        if st.button("⏰\nAsistencia"): navegar_a('asistencia')
    with c4:
        if st.button("💰\nRemuneraciones"): navegar_a('pagos')

    # Fila 3
    c5, c6 = st.columns(2)
    with c5:
        if st.button("🏖️\nVacaciones"): navegar_a('vacaciones')
    with c6:
        if st.button("🏥\nIPS / Social"): navegar_a('ips')

    # Fila 4
    c7, c8 = st.columns(2)
    with c7:
        if st.button("📋\nEvaluación"): navegar_a('evaluacion')
    with c8:
        if st.button("🚪\nDesvinculación"): navegar_a('salida')


# === 1. DATOS DEL COLABORADOR ===
elif st.session_state.page == 'datos':
    st.title("1. Datos del Colaborador")
    
    with st.container():
        st.markdown('<div class="info-card">', unsafe_allow_html=True)
        # Foto de perfil simulada
        c_img, c_info = st.columns([1, 2])
        with c_img:
            st.image("https://www.w3schools.com/howto/img_avatar.png", width=100)
        with c_info:
            st.subheader(st.session_state.datos_colaborador["nombre"])
            st.caption(st.session_state.datos_colaborador["cargo"])

        # Formulario
        nuevo_nombre = st.text_input("Nombre Completo", st.session_state.datos_colaborador["nombre"])
        nueva_cedula = st.text_input("Cédula de Identidad", st.session_state.datos_colaborador["cedula"])
        nuevo_correo = st.text_input("Correo Electrónico", st.session_state.datos_colaborador["correo"])
        nuevo_tel = st.text_input("Teléfono", st.session_state.datos_colaborador["telefono"])
        
        if st.button("💾 Guardar Cambios", type="primary"):
            st.session_state.datos_colaborador.update({
                "nombre": nuevo_nombre, "cedula": nueva_cedula, 
                "correo": nuevo_correo, "telefono": nuevo_tel
            })
            st.success("¡Datos actualizados!")
        
        st.markdown('</div>', unsafe_allow_html=True)
    volver_inicio()


# === 2. INFORMACIÓN LABORAL ===
elif st.session_state.page == 'laboral':
    st.title("2. Información Laboral")
    
    with st.container():
        st.markdown('<div class="info-card">', unsafe_allow_html=True)
        
        cargo = st.selectbox("Cargo", ["Analista", "Gerente", "Operario", "Vendedor"], index=0)
        area = st.selectbox("Área / Departamento", ["Finanzas", "RRHH", "Operaciones", "Comercial"], index=0)
        contrato = st.selectbox("Tipo de Contrato", ["Indefinido", "Jornalero", "Prestación de Servicios"])
        
        st.date_input("Fecha de Ingreso", value=st.session_state.datos_colaborador["ingreso"])
        
        st.markdown("---")
        with st.expander("🎁 Ver Beneficios Activos"):
            st.write("✅ Seguro Médico Privado")
            st.write("✅ Vales de Almuerzo")
            st.write("✅ Plus por Asistencia Perfecta")
            
        st.markdown('</div>', unsafe_allow_html=True)
    volver_inicio()


# === 3. ASISTENCIA Y HORARIOS ===
elif st.session_state.page == 'asistencia':
    st.title("3. Asistencia")
    
    with st.container():
        st.markdown('<div class="info-card">', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            entrada = st.time_input("Hora Entrada", value=time(8, 0))
        with col2:
            salida = st.time_input("Hora Salida", value=time(17, 30))
            
        # Cálculo simple de horas (simulado)
        if st.button("Registrar Marca"):
            st.success(f"Marca registrada: {entrada} - {salida}")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Alertas Visuales
        st.markdown('<div class="alert-success">Horas Extras Acumuladas: 2:00 Hs</div>', unsafe_allow_html=True)
        st.markdown('<div class="alert-warning">⚠️ Alerta: 1 Llegada tardía esta semana</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    volver_inicio()


# === 4. REMUNERACIONES ===
elif st.session_state.page == 'pagos':
    st.title("4. Remuneraciones")
    
    salario = st.session_state.datos_colaborador["salario"]
    ips_obrero = salario * 0.09
    neto = salario - ips_obrero
    
    with st.container():
        st.markdown('<div class="info-card">', unsafe_allow_html=True)
        
        st.metric("Salario Base", f"Gs. {salario:,.0f}".replace(",", "."))
        
        col1, col2 = st.columns(2)
        col1.metric("Descuento IPS (9%)", f"- {ips_obrero:,.0f}".replace(",", "."))
        col2.metric("Horas Extras", "Gs. 0")
        
        st.markdown("---")
        st.subheader(f"Neto a Cobrar: Gs. {neto:,.0f}".replace(",", "."))
        
        if st.button("📩 Enviar Recibo de Salario"):
            st.toast("Recibo enviado al correo del colaborador")
            
        st.markdown('</div>', unsafe_allow_html=True)
    volver_inicio()


# === 5. VACACIONES ===
elif st.session_state.page == 'vacaciones':
    st.title("5. Vacaciones")
    
    with st.container():
        st.markdown('<div class="info-card">', unsafe_allow_html=True)
        
        st.write("### 📅 Calendario de Solicitud")
        fechas = st.date_input("Seleccione rango de vacaciones", [])
        
        if len(fechas) == 2:
            dias = (fechas[1] - fechas[0]).days + 1
            st.info(f"Días seleccionados: {dias}")
            st.button("Enviar Solicitud", type="primary")
        
        st.markdown("---")
        st.write("*Saldo Disponible:* 12 Días")
        
        st.markdown('</div>', unsafe_allow_html=True)
    volver_inicio()


# === 6. SEGURIDAD SOCIAL (IPS) ===
elif st.session_state.page == 'ips':
    st.title("6. Seguridad Social - IPS")
    
    with st.container():
        st.markdown('<div class="info-card">', unsafe_allow_html=True)
        
        st.markdown('<div class="alert-success">✅ Afiliado a IPS Activo</div>', unsafe_allow_html=True)
        st.markdown('<div class="alert-success">✅ Aportes al día</div>', unsafe_allow_html=True)
        
        st.markdown("---")
        st.subheader("Reportar Novedad")
        tipo_novedad = st.selectbox("Tipo", ["Reposo Médico", "Accidente Laboral", "Maternidad"])
        archivo = st.file_uploader("Subir Certificado / Foto")
        
        if st.button("Enviar a RRHH"):
            st.warning("Novedad reportada. Pendiente de verificación.")
            
        st.markdown('</div>', unsafe_allow_html=True)
    volver_inicio()


# === 7. EVALUACIÓN Y DISCIPLINA ===
elif st.session_state.page == 'evaluacion':
    st.title("7. Evaluación y Disciplina")
    
    with st.container():
        st.markdown('<div class="info-card">', unsafe_allow_html=True)
        
        st.write("### Desempeño Mensual")
        prod = st.slider("Productividad", 0, 100, 80)
        asis = st.slider("Asistencia", 0, 100, 95)
        
        st.progress((prod + asis) / 200)
        st.caption(f"Promedio General: {(prod + asis) / 2}%")
        
        st.markdown("---")
        st.write("### Historial Disciplinario")
        st.info("Sin sanciones registradas en los últimos 6 meses.")
        
        st.markdown('</div>', unsafe_allow_html=True)
    volver_inicio()


# === 8. DESVINCULACIÓN ===
elif st.session_state.page == 'salida':
    st.title("8. Desvinculación")
    
    with st.container():
        st.markdown('<div class="info-card">', unsafe_allow_html=True)
        
        st.date_input("Fecha de Salida")
        motivo = st.selectbox("Motivo de Salida", ["Renuncia Voluntaria", "Despido Justificado", "Despido Injustificado", "Término de Contrato"])
        
        check1 = st.checkbox("Checklist: Devolución de Uniforme")
        check2 = st.checkbox("Checklist: Baja en IPS procesada")
        
        if st.button("Generar Liquidación Final"):
            st.success("Liquidación calculada. Lista para descargar.")
            
        st.button("📄 Descargar Constancia Laboral")
        
        st.markdown('</div>', unsafe_allow_html=True)
    volver_inicio()
