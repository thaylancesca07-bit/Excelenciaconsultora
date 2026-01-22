import streamlit as st
from datetime import datetime, date, timedelta
import time

# --- 1. CONFIGURACIÓN INICIAL ---
st.set_page_config(
    page_title="RRHH Excelencia",
    layout="centered",
    page_icon="👔",
    initial_sidebar_state="collapsed"
)

# --- 2. ESTILOS CSS (Diseño App Móvil Azul/Blanco) ---
st.markdown("""
<style>
    .stApp { background-color: #F0F2F5; }
    h1, h2, h3, h4 { color: #003366; font-family: 'Helvetica', sans-serif; }
    
    /* Botones Estilo Tarjeta */
    div.stButton > button {
        width: 100%;
        height: 90px;
        background-color: white;
        color: #003366;
        font-size: 16px;
        font-weight: 800;
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

    /* Botones Pequeños (Acciones secundarias) */
    .small-btn div.stButton > button {
        height: 40px;
        font-size: 14px;
        background-color: #003366;
        color: white;
    }

    /* Tarjetas de Contenido */
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        border-top: 4px solid #003366;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    
    /* Inputs deshabilitados (Solo lectura) */
    .stTextInput input:disabled {
        background-color: #f8f9fa;
        color: #333;
        border-color: #eee;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# --- 3. BASE DE DATOS SIMULADA (SESSION STATE) ---
if 'db_initialized' not in st.session_state:
    # Empresas
    st.session_state.empresas = [
        {"id": 1, "nombre": "Coca Cola Paresa", "rubro": "Bebidas"},
        {"id": 2, "nombre": "Farmacenter", "rubro": "Farmacia"}
    ]
    
    # Usuarios (Login)
    st.session_state.usuarios = {
        "admin": {"pass": "123", "rol": "excelencia", "nombre": "Admin Excelencia"},
        "coca":  {"pass": "123", "rol": "empresa", "empresa_id": 1, "nombre": "RRHH Coca Cola"},
        "farma": {"pass": "123", "rol": "empresa", "empresa_id": 2, "nombre": "RRHH Farmacenter"},
        "juan":  {"pass": "123", "rol": "funcionario", "empresa_id": 1, "funcionario_id": 101, "nombre": "Juan Pérez"},
        "ana":   {"pass": "123", "rol": "funcionario", "empresa_id": 1, "funcionario_id": 102, "nombre": "Ana Gómez"}
    }
    
    # Datos de Funcionarios
    st.session_state.funcionarios = [
        {
            "id": 101, "empresa_id": 1, "nombre": "Juan Pérez", "cedula": "1.234.567",
            "cargo": "Analista", "area": "Finanzas", "salario": 3500000, 
            "fecha_ingreso": date(2020, 5, 10), "contrato_vence": date(2026, 12, 31),
            "asistencia": {"entrada": "08:00", "salida": "17:00"},
            "vacaciones_saldo": 12, "ips_activo": True
        },
        {
            "id": 102, "empresa_id": 1, "nombre": "Ana Gómez", "cedula": "2.888.999",
            "cargo": "Vendedora", "area": "Comercial", "salario": 2800000,
            "fecha_ingreso": date(2022, 1, 15), "contrato_vence": date(2026, 3, 30), # Vence pronto
            "asistencia": {"entrada": "07:55", "salida": "18:00"},
            "vacaciones_saldo": 6, "ips_activo": True
        }
    ]
    st.session_state.db_initialized = True

# Estado de Navegación
if 'page' not in st.session_state: st.session_state.page = 'login'
if 'user_session' not in st.session_state: st.session_state.user_session = None
if 'selected_company' not in st.session_state: st.session_state.selected_company = None # Para Excelencia
if 'selected_employee' not in st.session_state: st.session_state.selected_employee = None # Para Ver Detalles

# --- 4. FUNCIONES AUXILIARES ---

def login(usuario, password):
    db_users = st.session_state.usuarios
    if usuario in db_users and db_users[usuario]["pass"] == password:
        st.session_state.user_session = {
            "user": usuario,
            "rol": db_users[usuario]["rol"],
            "nombre": db_users[usuario]["nombre"],
            "empresa_id": db_users[usuario].get("empresa_id"),
            "funcionario_id": db_users[usuario].get("funcionario_id")
        }
        st.session_state.page = 'dashboard'
        st.rerun()
    else:
        st.error("Credenciales incorrectas")

def logout():
    st.session_state.user_session = None
    st.session_state.page = 'login'
    st.session_state.selected_company = None
    st.session_state.selected_employee = None
    st.rerun()

def get_funcionarios_por_empresa(empresa_id):
    return [f for f in st.session_state.funcionarios if f['empresa_id'] == empresa_id]

def get_funcionario_by_id(func_id):
    for f in st.session_state.funcionarios:
        if f['id'] == func_id: return f
    return None

# Input inteligente: Si es editable usa text_input, si no, lo muestra deshabilitado
def smart_input(label, value, editable=True, type="text"):
    if not editable:
        st.text_input(label, value, disabled=True, key=f"read_{label}_{value}")
    else:
        if type == "date":
            return st.date_input(label, value)
        else:
            return st.text_input(label, value)

# --- 5. VISTAS DEL SISTEMA ---

# === A. LOGIN (PANTALLA INICIAL) ===
if st.session_state.page == 'login':
    st.markdown("<h1 style='text-align:center;'>Excelencia Consultora</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center;'>Gestión de Capital Humano</h3>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    rol_seleccionado = st.radio("Seleccione su perfil:", ["Consultora Excelencia", "Empresa Cliente", "Funcionario"], horizontal=True)
    
    with st.container():
        st.markdown('<div class="card" style="text-align:center;">', unsafe_allow_html=True)
        st.subheader(f"Ingreso: {rol_seleccionado}")
        user = st.text_input("Usuario")
        pw = st.text_input("Contraseña", type="password")
        
        if st.button("INGRESAR AL SISTEMA"):
            login(user, pw)
            
        st.markdown("---")
        # Ayuda visual para pruebas
        if rol_seleccionado == "Consultora Excelencia": st.caption("Prueba: admin / 123")
        elif rol_seleccionado == "Empresa Cliente": st.caption("Prueba: coca / 123")
        elif rol_seleccionado == "Funcionario": st.caption("Prueba: juan / 123")
        st.markdown('</div>', unsafe_allow_html=True)

# === B. DASHBOARD PRINCIPAL (LÓGICA POR ROL) ===
elif st.session_state.page == 'dashboard':
    rol = st.session_state.user_session["rol"]
    nombre_user = st.session_state.user_session["nombre"]
    
    # Header Común
    c1, c2 = st.columns([3, 1])
    with c1:
        st.subheader(f"Hola, {nombre_user}")
    with c2:
        if st.button("Salir", key="logout_top"): logout()
    st.markdown("---")

    # ---------------------------------------------------------
    # ROL 1: EXCELENCIA CONSULTORA (SUPER ADMIN)
    # ---------------------------------------------------------
    if rol == "excelencia":
        
        # Si no ha seleccionado empresa, mostrar lista
        if st.session_state.selected_company is None:
            c_titulo, c_btn = st.columns([2, 1])
            with c_titulo: st.title("🏢 Empresas Clientes")
            with c_btn: 
                # Botón para agregar empresa (arriba derecha)
                with st.expander("➕ Agregar Empresa"):
                    new_corp = st.text_input("Nombre Empresa")
                    if st.button("Guardar"):
                        new_id = len(st.session_state.empresas) + 1
                        st.session_state.empresas.append({"id": new_id, "nombre": new_corp, "rubro": "General"})
                        st.success("Empresa creada")
                        st.rerun()

            # Listado de Empresas
            for emp in st.session_state.empresas:
                with st.container():
                    st.markdown(f'<div class="card"><h3>{emp["nombre"]}</h3><p>Rubro: {emp["rubro"]}</p></div>', unsafe_allow_html=True)
                    if st.button(f"Gestionar {emp['nombre']}", key=f"btn_emp_{emp['id']}"):
                        st.session_state.selected_company = emp["id"]
                        st.rerun()
        
        else:
            # Empresa seleccionada -> Ver Funcionarios
            emp_id = st.session_state.selected_company
            emp_data = next((e for e in st.session_state.empresas if e["id"] == emp_id), None)
            
            if st.button("⬅️ Volver al listado de empresas"):
                st.session_state.selected_company = None
                st.session_state.selected_employee = None
                st.rerun()
                
            st.title(f"Gestionando: {emp_data['nombre']}")
            
            # Buscador y Agregar Funcionario
            col_s1, col_s2 = st.columns([3, 1])
            search = col_s1.text_input("🔍 Buscar funcionario...")
            with col_s2:
                if st.button("➕ Nuevo Funcionario"):
                    st.toast("Función de agregar funcionario")

            lista_funcs = get_funcionarios_por_empresa(emp_id)
            
            if not lista_funcs:
                st.info("No hay funcionarios registrados en esta empresa.")
            
            for f in lista_funcs:
                if search.lower() in f['nombre'].lower() or search in f['cedula']:
                    with st.container():
                        st.markdown(f'<div class="card"><h4>{f["nombre"]}</h4><p>C.I: {f["cedula"]} | Cargo: {f["cargo"]}</p></div>', unsafe_allow_html=True)
                        if st.button(f"Abrir Ficha de {f['nombre'].split()[0]}", key=f"adm_f_{f['id']}"):
                            st.session_state.selected_employee = f['id']
                            st.session_state.page = 'detalle_funcionario'
                            st.rerun()

    # ---------------------------------------------------------
    # ROL 2: EMPRESA CLIENTE (ADMIN LIMITADO)
    # ---------------------------------------------------------
    elif rol == "empresa":
        emp_id = st.session_state.user_session["empresa_id"]
        lista_funcs = get_funcionarios_por_empresa(emp_id)
        
        # --- SECCIÓN DE ALERTAS Y CALENDARIO ---
        with st.expander("📅 Calendario de Avisos y Vencimientos", expanded=True):
            hoy = date.today()
            alertas = []
            
            # Buscar vencimientos
            for f in lista_funcs:
                dias_vence = (f['contrato_vence'] - hoy).days
                if 0 < dias_vence < 90:
                    alertas.append(f"⚠️ Contrato de *{f['nombre']}* vence en {dias_vence} días ({f['contrato_vence']})")
            
            # Agregar aviso manual
            aviso_manual = st.text_input("Agregar nota al calendario (Ej: Pago de salario día 5)")
            if aviso_manual: st.info(f"📌 Nota: {aviso_manual}")
            
            if alertas:
                for a in alertas: st.markdown(f'<div style="background-color:#fff3cd; padding:10px; border-radius:5px; margin-bottom:5px;">{a}</div>', unsafe_allow_html=True)
            else:
                st.success("✅ No hay vencimientos de contrato próximos (90 días).")

        st.markdown("---")
        st.subheader("👥 Listado de Colaboradores")
        
        search = st.text_input("🔍 Buscar por nombre o cédula")
        
        for f in lista_funcs:
            if search.lower() in f['nombre'].lower() or search in f['cedula']:
                with st.container():
                    # Tarjeta simple
                    st.markdown(f"""
                    <div class="card" style="padding: 15px;">
                        <span style="font-weight:bold; font-size:18px;">{f['nombre']}</span><br>
                        <span style="color:gray;">{f['cargo']}</span>
                    </div>
                    """, unsafe_allow_html=True)
                    # Botón para ver detalle (SOLO LECTURA)
                    if st.button(f"👁️ Ver Datos de {f['nombre'].split()[0]}", key=f"emp_view_{f['id']}"):
                        st.session_state.selected_employee = f['id']
                        st.session_state.page = 'detalle_funcionario'
                        st.rerun()

    # ---------------------------------------------------------
    # ROL 3: FUNCIONARIO (SOLO SU PERFIL)
    # ---------------------------------------------------------
    elif rol == "funcionario":
        # Redirige directamente a la vista de detalle con SU ID
        st.session_state.selected_employee = st.session_state.user_session["funcionario_id"]
        st.session_state.page = 'detalle_funcionario'
        st.rerun()

# === C. DETALLE DE FUNCIONARIO (LOS 6 BOTONES) ===
elif st.session_state.page == 'detalle_funcionario':
    
    # Identificar quién está mirando
    rol_actual = st.session_state.user_session["rol"]
    es_excelencia = rol_actual == "excelencia" # Solo excelencia puede editar
    
    # Cargar datos del funcionario seleccionado
    f_id = st.session_state.selected_employee
    data = get_funcionario_by_id(f_id)
    
    if not data:
        st.error("Funcionario no encontrado")
        if st.button("Volver"): 
            st.session_state.page = 'dashboard'
            st.rerun()
    
    else:
        # Header de Navegación
        if rol_actual != "funcionario":
            if st.button("⬅️ Volver al Listado"):
                st.session_state.selected_employee = None
                st.session_state.page = 'dashboard'
                st.rerun()
        else:
             if st.button("🔒 Cerrar Sesión"): logout()

        st.markdown(f"<h2 style='text-align:center;'>{data['nombre']}</h2>", unsafe_allow_html=True)
        if es_excelencia: st.caption("Modo: EDICIÓN COMPLETA")
        else: st.caption("Modo: SOLO LECTURA")
        
        # --- LOS 6 BOTONES PRINCIPALES (TABS) ---
        tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
            "👤 Perfil", "💼 Laboral", "⏰ Asistencia", 
            "💰 Pagos", "🏖️ Vacaciones", "🏥 IPS"
        ])

        with tab1: # PERFIL
            with st.container():
                st.markdown('<div class="card">', unsafe_allow_html=True)
                smart_input("Nombre Completo", data['nombre'], es_excelencia)
                smart_input("Cédula", data['cedula'], es_excelencia)
                smart_input("Teléfono", "0981 111 222", es_excelencia)
                smart_input("Dirección", "Asunción, Centro", es_excelencia)
                if es_excelencia and st.button("💾 Guardar Perfil"): st.success("Datos actualizados")
                st.markdown('</div>', unsafe_allow_html=True)

        with tab2: # LABORAL
             with st.container():
                st.markdown('<div class="card">', unsafe_allow_html=True)
                smart_input("Cargo", data['cargo'], es_excelencia)
                smart_input("Área", data['area'], es_excelencia)
                smart_input("Fecha Ingreso", data['fecha_ingreso'], es_excelencia, type="date")
                smart_input("Vencimiento Contrato", data['contrato_vence'], es_excelencia, type="date")
                if es_excelencia and st.button("💾 Guardar Laboral"): st.success("Datos actualizados")
                st.markdown('</div>', unsafe_allow_html=True)

        with tab3: # ASISTENCIA
            with st.container():
                st.markdown('<div class="card">', unsafe_allow_html=True)
                c1, c2 = st.columns(2)
                with c1: smart_input("Entrada", data['asistencia']['entrada'], False) # Nadie edita historial aqui
                with c2: smart_input("Salida", data['asistencia']['salida'], False)
                st.info(f"Registro de hoy: {date.today()}")
                st.markdown('</div>', unsafe_allow_html=True)

        with tab4: # PAGOS
            with st.container():
                st.markdown('<div class="card">', unsafe_allow_html=True)
                salario = data['salario']
                smart_input("Salario Base", f"Gs. {salario:,.0f}", False)
                smart_input("IPS (9%)", f"- Gs. {salario*0.09:,.0f}", False)
                smart_input("Neto", f"Gs. {salario*0.91:,.0f}", False)
                st.download_button("Descargar Recibo", "Recibo Simulado", file_name="recibo.txt")
                st.markdown('</div>', unsafe_allow_html=True)

        with tab5: # VACACIONES
            with st.container():
                st.markdown('<div class="card">', unsafe_allow_html=True)
                st.metric("Saldo Disponible", f"{data['vacaciones_saldo']} Días")
                if es_excelencia:
                    st.number_input("Ajustar saldo", value=data['vacaciones_saldo'])
                else:
                    st.date_input("Solicitar Vacaciones")
                    if st.button("Enviar Solicitud"): st.success("Enviado a RRHH")
                st.markdown('</div>', unsafe_allow_html=True)

        with tab6: # IPS
             with st.container():
                st.markdown('<div class="card">', unsafe_allow_html=True)
                estado = "ACTIVO" if data['ips_activo'] else "INACTIVO"
                st.metric("Estado IPS", estado)
                if es_excelencia:
                    st.checkbox("IPS Activo", value=data['ips_activo'])
                else:
                    st.file_uploader("Subir Reposo")
                st.markdown('</div>', unsafe_allow_html=True)
