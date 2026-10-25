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
        background-color: #f8fafc;
        color: #1e293b;
    }
    
    .card-box {
        background: white;
        padding: 20px;
        border-radius: 16px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.04);
        border: 1px solid #e2e8f0;
        margin-bottom: 16px;
    }
    
    .hero-banner {
        background: linear-gradient(135deg, #4f46e5 0%, #6366f1 100%);
        color: white;
        padding: 24px;
        border-radius: 16px;
        margin-bottom: 16px;
        box-shadow: 0 8px 24px rgba(79, 70, 229, 0.25);
    }
    
    .stButton>button {
        background-color: #4f46e5;
        color: white;
        border-radius: 10px;
        width: 100%;
        border: none;
        height: 44px;
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

# Cabecera optimizada para móvil
st.markdown("""
    <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 16px;">
        <div style="background: #4f46e5; color: white; width: 40px; height: 40px; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 16px; font-weight: bold;">d/dx</div>
        <div>
            <h2 style="margin:0; color: #0f172a; font-size: 20px;">DerivaLab</h2>
            <span style="color: #64748b; font-size: 12px;">Cálculo Universitario</span>
        </div>
    </div>
""", unsafe_allow_html=True)

tab_inicio, tab_cursos, tab_calc, tab_quiz = st.tabs(["🏠 Inicio", "📚 Cursos", "🧮 Calc", "🧠 Quiz"])

with tab_inicio:
    st.markdown("""
        <div class="hero-banner">
            <h3 style="margin:0; color: white; font-size: 18px;">¡Hola, Estudiante!</h3>
            <p style="margin:6px 0 12px 0; font-size: 13px; opacity: 0.9;">Hoy seguimos dominando el cálculo universitario.</p>
            <div style="background: rgba(255,255,255,0.15); padding: 10px; border-radius: 10px;">
                <span style="font-size: 11px;">Racha de estudio</span><br>
                <strong style="font-size: 15px;">🔥 7 días consecutivos - ¡Sigue así!</strong>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="card-box">
            <h4 style="margin-top:0; color:#1e293b; font-size: 15px;">⚡ Acceso Directo</h4>
            <p style="color:#64748b; font-size:12px; margin-bottom:0;">Usa las pestañas superiores para navegar entre los módulos, resolver derivadas en la calculadora o practicar en el quiz.</p>
        </div>
    """, unsafe_allow_html=True)

with tab_cursos:
    if st.session_state.curso_seleccionado is None:
        st.markdown("### 📚 Temario de Cálculo")
        cursos_data = [
            ("1. Regla de la Potencia y Polinomios", "f(x) = xⁿ · Derivadas básicas", 1),
            ("2. Derivadas Trigonométricas", "sin, cos, sec, csc, cot", 2),
            ("3. Trigonométricas Inversas", "arcsin, arccos, arctan", 3),
            ("4. Integrales Inmediatas", "∫ xⁿ dx, e^x, ln(x)", 4)
        ]
        for titulo, desc, cid in cursos_data:
            st.markdown(f"""
                <div class="card-box" style="padding: 14px; margin-bottom: 10px;">
                    <strong style="font-size: 14px; color: #1e293b;">{titulo}</strong>
                    <p style="margin: 2px 0 8px 0; font-size: 12px; color: #64748b;">{desc}</p>
                </div>
            """, unsafe_allow_html=True)
            if st.button(f"📖 Ver Módulo {cid}", key=f"btn_c_{cid}"):
                st.session_state.curso_seleccionado = cid
                st.rerun()
    else:
        if st.button("← Volver a Cursos"):
            st.session_state.curso_seleccionado = None
            st.rerun()
        cid = st.session_state.curso_seleccionado
        if cid == 1:
            st.markdown("### Módulo 1: Regla de la Potencia")
            st.markdown('<div class="card-box"><p style="font-size:13px; color:#475569;">Fórmula base para polinomios:</p>', unsafe_allow_html=True)
            st.latex(r"\frac{d}{dx}(x^n) = n \cdot x^{n-1}")
            st.markdown("<p style='font-size:13px; color:#475569;'>Ejemplo: $f(x) = 3x^4 \implies f'(x) = 12x^3$</p></div>", unsafe_allow_html=True)
        elif cid == 2:
            st.markdown("### Módulo 2: Trigonométricas")
            st.markdown('<div class="card-box"><p style="font-size:13px; color:#475569;">Derivadas circulares y recíprocas:</p>', unsafe_allow_html=True)
            st.latex(r"\frac{d}{dx}(\sec(x)) = \sec(x)\tan(x)")
            st.markdown("</div>", unsafe_allow_html=True)
        elif cid == 3:
            st.markdown("### Módulo 3: Trig. Inversas")
            st.markdown('<div class="card-box"><p style="font-size:13px; color:#475569;">Funciones inversas:</p>', unsafe_allow_html=True)
            st.latex(r"\frac{d}{dx}(\arcsin(x)) = \frac{1}{\sqrt{1 - x^2}}")
            st.markdown("</div>", unsafe_allow_html=True)
        elif cid == 4:
            st.markdown("### Módulo 4: Integrales")
            st.markdown('<div class="card-box"><p style="font-size:13px; color:#475569;">Antiderivadas:</p>', unsafe_allow_html=True)
            st.latex(r"\int x^n \, dx = \frac{x^{n+1}}{n+1} + C")
            st.markdown("</div>", unsafe_allow_html=True)

with tab_calc:
    st.markdown('<div class="card-box"><h3 style="margin-top:0; font-size:16px;">🧮 Calculadora</h3></div>', unsafe_allow_html=True)
    tipo_op = st.radio("Operación:", ["Derivada d/dx", "Integral ∫ dx"], horizontal=True)
    funcion_input = st.text_input("Ingresa f(x):", value="sec(x)**2 + arcsin(x)")
    
    if st.button("Resolver"):
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
                if "Derivada" in tipo_op:
                    res = sp.diff(expr, x)
                    st.latex(f"\\frac{{d}}{{dx}}({sp.latex(expr)}) = {sp.latex(res)}")
                else:
                    res = sp.integrate(expr, x)
                    st.latex(f"\\int ({sp.latex(expr)}) dx = {sp.latex(res)} + C")
                st.markdown("</div>", unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Error: {e}")

with tab_quiz:
    st.markdown('<div class="card-box"><h3 style="margin-top:0; font-size:16px;">🧠 Quiz</h3><p style="font-size:12px;">Derivada de $f(x) = \\ln(x)$?</p></div>', unsafe_allow_html=True)
    opcion_quiz = st.radio("Elige:", ["A) x", "B) 1/x", "C) e^x", "D) -1/x²"], key="q_m")
    if st.button("Comprobar"):
        if opcion_quiz.startswith("B)"):
            st.success("¡Correcto! 🎉")
        else:
            st.error("Incorrecto.")
