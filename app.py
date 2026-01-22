import streamlit as st
import pandas as pd
from datetime import datetime, date

# --- 1. CONFIGURAÇÃO DE PÁGINA E TEMA ---
st.set_page_config(
    page_title="RHH Gestión Integral",
    layout="centered",
    page_icon="📱",
    initial_sidebar_state="expanded"
)

# --- 2. ESTILO CSS PERSONALIZADO (Para imitar o app mobile) ---
st.markdown("""
<style>
    .stApp {
        background-color: #F0F2F5; /* Cor de fundo clara */
        color: #333;
    }
    .stSidebar {
        background-color: #003366; /* Cor de fundo da barra lateral (azul escuro) */
        color: white;
    }
    .stSidebar .stSelectbox, .stSidebar .stRadio, .stSidebar h1 {
        color: white !important;
    }
    .main-header {
        text-align: center;
        color: #003366;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .card-container {
        background-color: white;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    .app-button {
        background-color: #007BFF; /* Azul principal */
        color: white;
        border: none;
        border-radius: 10px;
        padding: 15px;
        text-align: center;
        font-weight: bold;
        cursor: pointer;
        width: 100%;
        margin-bottom: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }
    .app-button.red {
        background-color: #DC3545; /* Botão vermelho para alertas */
    }
    .app-button.green {
        background-color: #28A745; /* Botão verde para ações positivas */
    }
    .profile-pic {
        border-radius: 50%;
        width: 120px;
        height: 120px;
        display: block;
        margin-left: auto;
        margin-right: auto;
        margin-bottom: 15px;
    }
    .alert-box {
        background-color: #FFF3CD;
        border: 1px solid #FEEBA5;
        color: #856404;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 10px;
        display: flex;
        align-items: center;
    }
    .alert-box.error {
        background-color: #F8D7DA;
        border: 1px solid #F5C6CB;
        color: #721C24;
    }
    .calendar-day {
        background-color: #E9ECEF;
        border-radius: 50%;
        width: 30px;
        height: 30px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 14px;
        margin: 2px;
    }
    .calendar-day.selected {
        background-color: #28A745;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. ESTADO DA SESSÃO ---
if 'current_page' not in st.session_state:
    st.session_state['current_page'] = "Menu Principal"

# --- 4. NAVEGAÇÃO ---
with st.sidebar:
    st.markdown("<h1 style='text-align: center;'>RHH Gestión Integral</h1>", unsafe_allow_html=True)
    st.markdown("---")
    page = st.radio("Navegação", [
        "Menu Principal",
        "1. Datos del Colaborador",
        "2. Info Laboral",
        "3. Asistencia & Horarios",
        "4. Remuneraciones",
        "5. Vacaciones & Licencias",
        "6. Seguridad Social",
        "7. Evaluación & Disciplina",
        "8. Desvinculación"
    ], index=0 if st.session_state['current_page'] == "Menu Principal" else 1)

    if page != st.session_state['current_page']:
        st.session_state['current_page'] = page
        st.experimental_rerun()

# --- 5. PÁGINAS DA APLICAÇÃO ---

# --- PÁGINA INICIAL (MENU PRINCIPAL) ---
if st.session_state['current_page'] == "Menu Principal":
    st.markdown("<div class='main-header'><h1>Bem-vindo ao RHH App</h1></div>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""<div class='card-container app-button' style='background-color: #FFC107; color: #333;'><span style='font-size: 2em;'>👤</span><br>Perfil</div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""<div class='card-container app-button' style='background-color: #17A2B8;'><span style='font-size: 2em;'>👔</span><br>Laboral</div>""", unsafe_allow_html=True)
    with col3:
        st.markdown("""<div class='card-container app-button' style='background-color: #28A745;'><span style='font-size: 2em;'>✅</span><br>Asistencia</div>""", unsafe_allow_html=True)
    
    col4, col5, col6 = st.columns(3)
    with col4:
        st.markdown("""<div class='card-container app-button' style='background-color: #DC3545;'><span style='font-size: 2em;'>💼</span><br>Pago</div>""", unsafe_allow_html=True)
    with col5:
        st.markdown("""<div class='card-container app-button' style='background-color: #007BFF;'><span style='font-size: 2em;'>📅</span><br>Vacaciones</div>""", unsafe_allow_html=True)
    with col6:
        st.markdown("""<div class='card-container app-button' style='background-color: #6C757D;'><span style='font-size: 2em;'>🏥</span><br>IPS</div>""", unsafe_allow_html=True)

# --- MÓDULO 1: DATOS DEL COLABORADOR ---
elif st.session_state['current_page'] == "1. Datos del Colaborador":
    st.markdown("<div class='main-header'><h2>1. Datos del Colaborador</h2></div>", unsafe_allow_html=True)
    with st.container():
        st.markdown("<div class='card-container'>", unsafe_allow_html=True)
        st.markdown("""<img src="https://www.w3schools.com/howto/img_avatar.png" class="profile-pic" alt="Juan Pérez">""", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center; color: #003366;'>Juan Pérez</h3>", unsafe_allow_html=True)
        st.markdown("---")
        
        st.text_input("Cédula:", "12345678")
        st.text_input("Correo:", "juanperez@email.com")
        st.text_input("Teléfono:", "0981 123 456")
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<button class='app-button'>Editar Datos > </button>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# --- MÓDULO 2: INFO LABORAL ---
elif st.session_state['current_page'] == "2. Info Laboral":
    st.markdown("<div class='main-header'><h2>2. Info Laboral</h2></div>", unsafe_allow_html=True)
    with st.container():
        st.markdown("<div class='card-container'>", unsafe_allow_html=True)
        st.selectbox("Cargo:", ["Analista"], index=0)
        st.selectbox("Departamento:", ["Finanzas"], index=0)
        st.selectbox("Contrato:", ["Indefinido"], index=0)
        st.date_input("Fecha de Ingreso:", value=pd.to_datetime("2020-05-10"))
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<button class='app-button'>Ver Beneficios > </button>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# --- MÓDULO 3: ASISTENCIA & HORARIOS ---
elif st.session_state['current_page'] == "3. Asistencia & Horarios":
    st.markdown("<div class='main-header'><h2>3. Asistencia & Horarios</h2></div>", unsafe_allow_html=True)
    with st.container():
        st.markdown("<div class='card-container'>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.time_input("Entrada:", value=pd.to_datetime("08:02").time())
        with col2:
            st.time_input("Salida:", value=pd.to_datetime("17:15").time())
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""<div class='alert-box' style='background-color: #28A745; color: white; text-align: center;'>Horas Extras: 2:00 Hs</div>""", unsafe_allow_html=True)
        st.markdown("""<div class='alert-box' style='text-align: center;'>⚠️ Alerta: 1 Tardanza</div>""", unsafe_allow_html=True)
        st.markdown("""<div class='alert-box error' style='text-align: center;'>🚨 Falta Injustificada</div>""", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# --- MÓDULO 4: REMUNERACIONES ---
elif st.session_state['current_page'] == "4. Remuneraciones":
    st.markdown("<div class='main-header'><h2>4. Remuneraciones</h2></div>", unsafe_allow_html=True)
    with st.container():
        st.markdown("<div class='card-container'>", unsafe_allow_html=True)
        st.markdown("<h3>Salario: Gs. 3.500.000</h3>", unsafe_allow_html=True)
        st.markdown("<h4>Horas Extras: Gs. 500.000</h4>", unsafe_allow_html=True)
        st.markdown("---")
        st.markdown("<button class='app-button' style='background-color: #F8F9FA; color: #333; text-align: left;'>Descuentos IPS y Otros > </button>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<button class='app-button'>Recibo de Pago 📄</button>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# --- MÓDULO 5: VACACIONES & LICENCIAS ---
elif st.session_state['current_page'] == "5. Vacaciones & Licencias":
    st.markdown("<div class='main-header'><h2>5. Vacaciones & Licencias</h2></div>", unsafe_allow_html=True)
    with st.container():
        st.markdown("<div class='card-container'>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center;'>Mis Vacaciones</h3>", unsafe_allow_html=True)
        # Calendário simplificado visualmente
        st.markdown("""
        <div style='display: flex; justify-content: center; flex-wrap: wrap; gap: 5px;'>
            <div class='calendar-day'>1</div><div class='calendar-day'>2</div><div class='calendar-day'>3</div><div class='calendar-day'>4</div>
            <div class='calendar-day selected'>5</div><div class='calendar-day selected'>6</div><div class='calendar-day'>7</div><div class='calendar-day'>8</div>
            <div class='calendar-day'>9</div><div class='calendar-day'>10</div><div class='calendar-day'>11</div><div class='calendar-day'>12</div>
            <div class='calendar-day'>13</div><div class='calendar-day'>14</div><div class='calendar-day'>15</div><div class='calendar-day'>16</div>
            <div class='calendar-day'>17</div><div class='calendar-day'>18</div><div class='calendar-day'>19</div><div class='calendar-day'>20</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<button class='app-button green'>Solicitar Licencia > </button>", unsafe_allow_html=True)
        st.markdown("<button class='app-button' style='background-color: #F8F9FA; color: #333;'>Historial > </button>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# --- MÓDULO 6: SEGURIDAD SOCIAL ---
elif st.session_state['current_page'] == "6. Seguridad Social":
    st.markdown("<div class='main-header'><h2>6. Seguridad Social</h2></div>", unsafe_allow_html=True)
    with st.container():
        st.markdown("<div class='card-container'>", unsafe_allow_html=True)
        st.markdown("""<div class='alert-box' style='background-color: #D4EDDA; border-color: #C3E6CB; color: #155724;'>✅ Afiliado a IPS</div>""", unsafe_allow_html=True)
        st.markdown("""<div class='alert-box' style='background-color: #D4EDDA; border-color: #C3E6CB; color: #155724;'>✅ Aportes al día</div>""", unsafe_allow_html=True)
        st.markdown("""<div class='alert-box error'>🚨 Reposo Médico</div>""", unsafe_allow_html=True)
        st.markdown("""<div class='alert-box error'>🚨 Reporte de Accidente</div>""", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# --- MÓDULO 7: EVALUACIÓN & DISCIPLINA ---
elif st.session_state['current_page'] == "7. Evaluación & Disciplina":
    st.markdown("<div class='main-header'><h2>7. Evaluación & Disciplina</h2></div>", unsafe_allow_html=True)
    with st.container():
        st.markdown("<div class='card-container'>", unsafe_allow_html=True)
        st.date_input("Fecha de Salida:")
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<button class='app-button' style='text-align: left;'>📋 Liquidación Final > </button>", unsafe_allow_html=True)
        st.markdown("<button class='app-button' style='text-align: left;'>🏥 Baja en IPS > </button>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# --- MÓDULO 8: DESVINCULACIÓN ---
elif st.session_state['current_page'] == "8. Desvinculación":
    st.markdown("<div class='main-header'><h2>8. Desvinculación</h2></div>", unsafe_allow_html=True)
    with st.container():
        st.markdown("<div class='card-container'>", unsafe_allow_html=True)
        st.text_input("Fecha de Salida:", "30/11/2022")
        st.text_input("Liquidación Final", "")
        st.text_input("Baja en IPS", "")
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<button class='app-button'>Generar Constancia > </button>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
