import streamlit as st
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application

st.set_page_config(page_title="DerivaLab", page_icon="⚡", layout="wide")

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .stApp {
        background-color: #f8fafc;
        color: #1e293b;
    }
    
    .card-box {
        background: white;
        padding: 22px;
        border-radius: 16px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.04);
        border: 1px solid #e2e8f0;
        margin-bottom: 16px;
    }
    
    .hero-banner {
        background: linear-gradient(135deg, #4f46e5 0%, #6366f1 100%);
        color: white;
        padding: 28px;
        border-radius: 18px;
        margin-bottom: 24px;
        box-shadow: 0 8px 24px rgba(79, 70, 229, 0.25);
    }
    
    .stButton>button {
        background-color: #4f46e5;
        color: white;
        border-radius: 10px;
        width: 100%;
        border: none;
        height: 42px;
        font-weight: 600;
        box-shadow: 0 4px 12px rgba(79, 70, 229, 0.2);
    }
    .stButton>button:hover {
        background-color: #4338ca;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

if 'curso_seleccionado' not in st.session_state:
    st.session_state.curso_seleccionado = None

transformations = standard_transformations + (implicit_multiplication_application,)

# Encabezado principal
st.markdown("""
    <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 20px;">
        <div style="display: flex; align-items: center; gap: 12px;">
            <div style="background: #4f46e5; color: white; width: 44px; height: 44px; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 18px; font-weight: bold;">d/dx</div>
            <h2 style="margin:0; color: #0f172a; font-size: 24px;">DerivaLab</h2>
        </div>
        <span style="color: #64748b; font-size: 14px; font-weight: 500;">Cálculo Universitario Paso a Paso</span>
    </div>
""", unsafe_allow_html=True)

tab_inicio, tab_cursos, tab_calc, tab_quiz = st.tabs(["🏠 Inicio", "📚 Temario y Cursos", "🧮 Calculadora Avanzada", "🧠 Quiz de Evaluación"])

# ==================== 1. INICIO ====================
with tab_inicio:
    col1, col2 = st.columns([1.5, 1], gap="large")
    with col1:
        st.markdown("""
            <div class="hero-banner">
                <h2 style="margin:0; color: white; font-size: 24px;">¡Hola, Estudiante!</h2>
                <p style="margin:8px 0 16px 0; font-size: 14px; opacity: 0.9;">Hoy seguimos dominando el cálculo universitario.</p>
                <div style="background: rgba(255,255,255,0.15); padding: 14px; border-radius: 12px; display: inline-block;">
                    <span style="font-size: 12px;">Racha de estudio</span><br>
                    <strong style="font-size: 18px;">🔥 7 días consecutivos - ¡Sigue así!</strong>
                </div>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
            <div class="card-box">
                <h4 style="margin-top:0; color:#1e293b;">⚡ Acceso Directo</h4>
                <p style="color:#64748b; font-size:13px;">Navega por las pestañas superiores para revisar el temario teórico, usar la calculadora o practicar en el quiz.</p>
            </div>
        """, unsafe_allow_html=True)

# ==================== 2. CURSOS (SIN LÍNEAS AZULES, LIMPIO Y CLICKEABLE) ====================
with tab_cursos:
    if st.session_state.curso_seleccionado is None:
        st.markdown("### 📚 Temario de Cálculo")
        st.caption("Selecciona cualquier módulo para desplegar sus lecciones teóricas y ejemplos resueltos.")
        
        cursos_data = [
            ("1. Regla de la Potencia y Polinomios", "f(x) = xⁿ · Derivadas y reglas básicas", 1),
            ("2. Derivadas Trigonométricas", "sin, cos, sec, csc, cot · Fórmulas e identidades", 2),
            ("3. Trigonométricas Inversas", "arcsin, arccos, arctan · Demostraciones", 3),
            ("4. Integrales Inmediatas y Exponenciales", "∫ xⁿ dx, e^x, ln(x) · Métodos directos", 4)
        ]
        
        for titulo, desc, cid in cursos_data:
            col_info, col_btn = st.columns([3, 1], gap="medium")
            with col_info:
                st.markdown(f"""
                    <div class="card-box" style="margin-bottom: 0px; padding: 16px;">
                        <strong style="font-size: 15px; color: #1e293b;">{titulo}</strong>
                        <p style="margin: 4px 0 0 0; font-size: 13px; color: #64748b;">{desc}</p>
                    </div>
                """, unsafe_allow_html=True)
            with col_btn:
                st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
                if st.button(f"📖 Ver Lección", key=f"btn_curso_{cid}"):
                    st.session_state.curso_seleccionado = cid
                    st.rerun()
            st.markdown("<div style='height: 8px;'></div>", unsafe_allow_html=True)
    else:
        if st.button("← Volver a la lista de cursos"):
            st.session_state.curso_seleccionado = None
            st.rerun()
            
        cid = st.session_state.curso_seleccionado
        
        if cid == 1:
            st.markdown("### 📖 Módulo 1: Regla de la Potencia y Polinomios")
            st.markdown("""
                <div class="card-box">
                    <h4>Fundamento Teórico</h4>
                    <p style="color:#475569; font-size:14px;">La regla de la potencia es la base para derivar funciones polinómicas:</p>
                """, unsafe_allow_html=True)
            st.latex(r"\frac{d}{dx}(x^n) = n \cdot x^{n-1}")
            st.markdown("""
                    <hr style="margin: 15px 0; border: none; border-top: 1px solid #e2e8f0;">
                    <h4>Ejemplo Práctico</h4>
                """, unsafe_allow_html=True)
            st.latex(r"f(x) = 3x^4 - 5x^2 + 7 \implies f'(x) = 12x^3 - 10x")
            st.markdown("</div>", unsafe_allow_html=True)

        elif cid == 2:
            st.markdown("### 📖 Módulo 2: Derivadas Trigonométricas")
            st.markdown("""
                <div class="card-box">
                    <h4>Fórmulas Esenciales</h4>
                """, unsafe_allow_html=True)
            st.latex(r"\frac{d}{dx}(\sin(x)) = \cos(x), \quad \frac{d}{dx}(\cos(x)) = -\sin(x)")
            st.latex(r"\frac{d}{dx}(\sec(x)) = \sec(x)\tan(x), \quad \frac{d}{dx}(\csc(x)) = -\csc(x)\cot(x)")
            st.markdown("</div>", unsafe_allow_html=True)

        elif cid == 3:
            st.markdown("### 📖 Módulo 3: Trigonométricas Inversas")
            st.markdown("""
                <div class="card-box">
                    <h4>Derivadas de Funciones Inversas</h4>
                """, unsafe_allow_html=True)
            st.latex(r"\frac{d}{dx}(\arcsin(x)) = \frac{1}{\sqrt{1 - x^2}}, \quad \frac{d}{dx}(\arctan(x)) = \frac{1}{1 + x^2}")
            st.markdown("</div>", unsafe_allow_html=True)

        elif cid == 4:
            st.markdown("### 📖 Módulo 4: Integrales Inmediatas y Exponenciales")
            st.markdown("""
                <div class="card-box">
                    <h4>Antiderivadas Fundamentales</h4>
                """, unsafe_allow_html=True)
            st.latex(r"\int x^n \, dx = \frac{x^{n+1}}{n+1} + C \quad (n \neq -1)")
            st.latex(r"\int e^x \, dx = e^x + C, \quad \int \frac{1}{x} \, dx = \ln|x| + C")
            st.markdown("</div>", unsafe_allow_html=True)

# ==================== 3. CALCULADORA ====================
with tab_calc:
    st.markdown("""
        <div class="card-box">
            <h3 style="margin-top:0; color:#1e293b;">🧮 Calculadora Paso a Paso</h3>
            <p style="color:#64748b; font-size:13px;">Motor SymPy con soporte para funciones algebraicas, trigonométricas, inversas y exponenciales.</p>
        </div>
    """, unsafe_allow_html=True)
    
    col_c1, col_c2 = st.columns([1, 2], gap="large")
    with col_c1:
        tipo_op = st.radio("Operación a realizar:", ["Derivada d/dx", "Integral ∫ dx"], horizontal=False)
        funcion_input = st.text_input("Ingresa f(x):", value="sec(x)**2 + arcsin(x)")
        st.caption("💡 *Ejemplos: `sec(x)`, `csc(x)`, `arcsin(x)`, `e^x`, `ln(x)`*")
        resolver_btn = st.button("Resolver Expresión")

    with col_c2:
        if resolver_btn:
            if funcion_input.strip():
                try:
                    x = sp.Symbol('x')
                    clean_input = funcion_input.replace('^', '**').replace('e', 'E')
                    local_dict = {
                        'x': x, 'E': sp.E, 'exp': sp.exp, 'ln': sp.log, 'log': sp.log,
                        'sin': sp.sin, 'cos': sp.cos, 'tan': sp.tan,
                        'sec': sp.sec, 'csc': sp.csc, 'cot': sp.cot,
                        'asin': sp.asin, 'acos': sp.acos, 'atan': sp.atan,
                        'arcsin': sp.asin, 'arccos': sp.acos, 'arctan': sp.atan, 'sqrt': sp.sqrt
                    }
                    expr = parse_expr(clean_input, local_dict=local_dict, transformations=transformations, evaluate=False)
                    
                    st.markdown('<div class="card-box" style="background: #f1f5f9;">', unsafe_allow_html=True)
                    st.markdown("<strong>DESGLOSE PASO A PASO</strong>", unsafe_allow_html=True)
                    
                    if "Derivada" in tipo_op:
                        res = sp.diff(expr, x)
                        st.latex(f"\\frac{{d}}{{dx}}\\left({sp.latex(expr)}\\right) = {sp.latex(res)}")
                    else:
                        res = sp.integrate(expr, x)
                        st.latex(f"\\int \\left({sp.latex(expr)}\\right) dx = {sp.latex(res)} + C")
                        
                    st.markdown("<p style='font-size:12px; color:#475569; margin-top:10px;'>Paso 1 · Aplicación de identidades y reglas algebraicas inmediatas.</p>", unsafe_allow_html=True)
                    st.markdown("</div>", unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"Error de sintaxis en la expresión: {e}")
            else:
                st.warning("Por favor ingresa una función válida.")

# ==================== 4. QUIZ ====================
with tab_quiz:
    st.markdown("""
        <div class="card-box">
            <h3 style="margin-top:0; color:#1e293b;">🧠 Quiz de Evaluación</h3>
            <p style="color:#64748b; font-size:13px;">Pon a prueba tus conocimientos seleccionando la respuesta correcta.</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("**Pregunta 1:** ¿Cuál es la derivada de $f(x) = \\ln(x)$?")
    opcion_quiz = st.radio("Elige tu respuesta:", ["A) x", "B) 1/x", "C) e^x", "D) -1/x²"], key="quiz_opcion_multiple")
    
    if st.button("Comprobar Respuesta del Quiz"):
        if opcion_quiz.startswith("B)"):
            st.success("¡Excelente! Respuesta correcta 🎉 (La derivada de ln(x) es 1/x)")
        else:
            st.error("Incorrecto. Inténtalo de nuevo o repasa el módulo de teoría.")