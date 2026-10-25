import streamlit as st
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application

st.set_page_config(page_title="DerivaLab", page_icon="⚡", layout="centered")

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .stApp {
        background-color: #f1f5f9 !important;
        color: #0f172a !important;
    }
    
    .block-container {
        padding: 10px !important;
        max-width: 100% !important;
    }
    
    p, span, label, div, li {
        font-size: 16px !important;
    }
    
    h2 { font-size: 20px !important; }
    h3 { font-size: 18px !important; }
    
    .card-box {
        background: white;
        padding: 14px;
        border-radius: 12px;
        border: 1px solid #cbd5e1;
        margin-bottom: 10px;
        width: 100%;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    }
    
    .hero-banner {
        background: linear-gradient(135deg, #4f46e5 0%, #6366f1 100%);
        color: white;
        padding: 16px;
        border-radius: 12px;
        margin-bottom: 10px;
    }
    
    .stButton>button {
        background-color: #4f46e5 !important;
        color: white !important;
        border-radius: 10px !important;
        width: 100% !important;
        height: 45px !important;
        font-size: 16px !important;
        font-weight: bold !important;
        border: none !important;
    }
    </style>
""", unsafe_allow_html=True)

if 'curso_seleccionado' not in st.session_state:
    st.session_state.curso_seleccionado = None

transformations = standard_transformations + (implicit_multiplication_application,)

st.markdown("""
    <div class="card-box" style="display: flex; align-items: center; gap: 10px; background: #4f46e5; color: white; margin-bottom: 10px;">
        <div style="background: white; color: #4f46e5; width: 38px; height: 38px; border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 16px; font-weight: bold;">d/dx</div>
        <div>
            <h2 style="margin:0; color: white; font-size: 18px;">DerivaLab</h2>
            <span style="font-size: 13px; opacity: 0.9;">Cálculo Universitario</span>
        </div>
    </div>
""", unsafe_allow_html=True)

tab_inicio, tab_cursos, tab_calc, tab_quiz = st.tabs(["🏠 Inicio", "📚 Cursos", "🧮 Calc", "🧠 Quiz"])

with tab_inicio:
    st.markdown("""
        <div class="hero-banner">
            <h3 style="margin:0; color: white; font-size: 18px;">¡Hola, Estudiante!</h3>
            <p style="margin:6px 0 0 0; font-size: 14px;">Listo para dominar el cálculo paso a paso.</p>
        </div>
        <div class="card-box">
            <h3 style="margin-top:0; color:#1e293b;">⚡ Acceso Rápido</h3>
            <p style="color:#475569; margin-bottom:0; font-size: 14px;">Usa las pestañas superiores para navegar por los contenidos.</p>
        </div>
    """, unsafe_allow_html=True)

with tab_cursos:
    if st.session_state.curso_seleccionado is None:
        st.markdown("### 📚 Temario")
        cursos = [
            ("1. Regla de la Potencia", "Polinomios y derivadas básicas", 1),
            ("2. Trigonométricas", "sin, cos, sec, csc, cot", 2),
            ("3. Trig. Inversas", "arcsin, arccos, arctan", 3),
            ("4. Integrales Inmediatas", "∫ xⁿ dx, e^x, ln(x)", 4)
        ]
        for tit, desc, cid in cursos:
            st.markdown(f"""
                <div class="card-box" style="margin-bottom: 8px;">
                    <strong style="font-size: 16px; color: #1e293b;">{tit}</strong>
                    <p style="margin: 2px 0 0 0; font-size: 13px; color: #64748b;">{desc}</p>
                </div>
            """, unsafe_allow_html=True)
            if st.button(f"Abrir Módulo {cid}", key=f"b_{cid}"):
                st.session_state.curso_seleccionado = cid
                st.rerun()
    else:
        if st.button("← Volver al Temario"):
            st.session_state.curso_seleccionado = None
            st.rerun()
        cid = st.session_state.curso_seleccionado
        if cid == 1:
            st.markdown("### Módulo 1: Potencia")
            st.markdown('<div class="card-box"><p>Fórmula principal:</p>', unsafe_allow_html=True)
            st.latex(r"\frac{d}{dx}(x^n) = n \cdot x^{n-1}")
            st.markdown("<p>Ejemplo: $f(x) = 3x^4 \implies f'(x) = 12x^3$</p></div>", unsafe_allow_html=True)
        elif cid == 2:
            st.markdown("### Módulo 2: Trigonométricas")
            st.markdown('<div class="card-box"><p>Derivadas:</p>', unsafe_allow_html=True)
            st.latex(r"\frac{d}{dx}(\sec(x)) = \sec(x)\tan(x)")
            st.markdown("</div>", unsafe_allow_html=True)
        elif cid == 3:
            st.markdown("### Módulo 3: Trig. Inversas")
            st.markdown('<div class="card-box"><p>Inversas:</p>', unsafe_allow_html=True)
            st.latex(r"\frac{d}{dx}(\arcsin(x)) = \frac{1}{\sqrt{1 - x^2}}")
            st.markdown("</div>", unsafe_allow_html=True)
        elif cid == 4:
            st.markdown("### Módulo 4: Integrales")
            st.markdown('<div class="card-box"><p>Antiderivadas:</p>', unsafe_allow_html=True)
            st.latex(r"\int x^n \, dx = \frac{x^{n+1}}{n+1} + C")
            st.markdown("</div>", unsafe_allow_html=True)

with tab_calc:
    st.markdown('<div class="card-box"><h3 style="margin-top:0;">🧮 Calculadora</h3>', unsafe_allow_html=True)
    tipo_op = st.radio("Operación:", ["Derivada d/dx", "Integral ∫ dx"], horizontal=True)
    funcion_input = st.text_input("Función f(x):", value="sec(x)**2 + arcsin(x)")
    
    if st.button("Calcular Ahora"):
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
                st.markdown('<div class="card-box" style="background: #f1f5f9; margin-top: 8px;">', unsafe_allow_html=True)
                if "Derivada" in tipo_op:
                    res = sp.diff(expr, x)
                    st.latex(f"\\frac{{d}}{{dx}}({sp.latex(expr)}) = {sp.latex(res)}")
                else:
                    res = sp.integrate(expr, x)
                    st.latex(f"\\int ({sp.latex(expr)}) dx = {sp.latex(res)} + C")
                st.markdown("</div>", unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Error: {e}")
    st.markdown('</div>', unsafe_allow_html=True)

with tab_quiz:
    st.markdown('<div class="card-box"><h3 style="margin-top:0;">🧠 Quiz Rápido</h3><p>¿Cuál es la derivada de $f(x) = \\ln(x)$?</p></div>', unsafe_allow_html=True)
    opcion_quiz = st.radio("Elige una opción:", ["A) x", "B) 1/x", "C) e^x", "D) -1/x²"], key="q_mobile")
    if st.button("Verificar Respuesta"):
        if opcion_quiz.startswith("B)"):
            st.success("¡Correcto! 🎉")
        else:
            st.error("Incorrecto. Inténtalo de nuevo.")
