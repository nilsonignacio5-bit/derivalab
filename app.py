import streamlit as st
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application

st.set_page_config(page_title="DerivaLab", page_icon="⚡", layout="centered")

# CSS agresivo para eliminar espacios en blanco y forzar diseño móvil real a pantalla completa
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Eliminar los espacios y márgenes gigantes por defecto de Streamlit en móviles */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 2rem !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        max-width: 100% !important;
    }
    
    .stApp {
        background-color: #f8fafc;
        color: #1e293b;
    }
    
    /* Tarjetas de contenido adaptadas al ancho completo */
    .card-box {
        background: white;
        padding: 16px;
        border-radius: 14px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
        border: 1px solid #e2e8f0;
        margin-bottom: 14px;
        width: 100%;
    }
    
    .hero-banner {
        background: linear-gradient(135deg, #4f46e5 0%, #6366f1 100%);
        color: white;
        padding: 20px;
        border-radius: 14px;
        margin-bottom: 14px;
        box-shadow: 0 6px 20px rgba(79, 70, 229, 0.25);
    }
    
    /* Botones limpios y grandes para toque en celular */
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
    
    /* Pestañas limpias */
    .stTabs [data-baseweb="tab-list"] {
        gap: 4px;
        background-color: #e2e8f0;
        padding: 4px;
        border-radius: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 38px;
        border-radius: 8px;
        font-weight: 600;
        font-size: 13px;
    }
    </style>
""", unsafe_allow_html=True)

if 'curso_seleccionado' not in st.session_state:
    st.session_state.curso_seleccionado = None

transformations = standard_transformations + (implicit_multiplication_application,)

# Cabecera principal compacta
st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 12px;">
        <div style="background: #4f46e5; color: white; width: 38px; height: 38px; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 15px; font-weight: bold;">d/dx</div>
        <div>
            <h2 style="margin:0; color: #0f172a; font-size: 18px;">DerivaLab</h2>
            <span style="color: #64748b; font-size: 11px;">Cálculo Universitario</span>
        </div>
    </div>
""", unsafe_allow_html=True)

tab_inicio, tab_cursos, tab_calc, tab_quiz = st.tabs(["🏠 Inicio", "📚 Cursos", "🧮 Calc", "🧠 Quiz"])

with tab_inicio:
    st.markdown("""
        <div class="hero-banner">
            <h3 style="margin:0; color: white; font-size: 16px;">¡Hola, Estudiante!</h3>
            <p style="margin:4px 0 10px 0; font-size: 12px; opacity: 0.9;">Hoy seguimos dominando el cálculo.</p>
            <div style="background: rgba(255,255,255,0.15); padding: 8px 12px; border-radius: 8px; display: inline-block;">
                <span style="font-size: 10px;">Racha actual</span><br>
                <strong style="font-size: 13px;">🔥 7 días consecutivos</strong>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="card-box">
            <h4 style="margin-top:0; color:#1e293b; font-size: 14px;">⚡ Acceso Directo</h4>
            <p style="color:#64748b; font-size:12px; margin-bottom:0;">Usa las pestañas superiores para ver el temario, usar la calculadora o practicar.</p>
        </div>
    """, unsafe_allow_html=True)

with tab_cursos:
    if st.session_state.curso_seleccionado is None:
        st.markdown("### Temario de Cálculo")
        cursos_data = [
            ("1. Regla de la Potencia", "f(x) = xⁿ · Derivadas básicas", 1),
            ("2. Trigonométricas", "sin, cos, sec, csc, cot", 2),
            ("3. Trig. Inversas", "arcsin, arccos, arctan", 3),
            ("4. Integrales Inmediatas", "∫ xⁿ dx, e^x, ln(x)", 4)
        ]
        for titulo, desc, cid in cursos_data:
            st.markdown(f"""
                <div class="card-box" style="padding: 12px; margin-bottom: 8px;">
                    <strong style="font-size: 13px; color: #1e293b;">{titulo}</strong>
                    <p style="margin: 2px 0 6px 0; font-size: 11px; color: #64748b;">{desc}</p>
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
            st.markdown('<div class="card-box"><p style="font-size:12px; color:#475569;">Fórmula base:</p>', unsafe_allow_html=True)
            st.latex(r"\frac{d}{dx}(x^n) = n \cdot x^{n-1}")
            st.markdown("<p style='font-size:12px; color:#475569;'>Ejemplo: $f(x) = 3x^4 \implies f'(x) = 12x^3$</p></div>", unsafe_allow_html=True)
        elif cid == 2:
            st.markdown("### Módulo 2: Trigonométricas")
            st.markdown('<div class="card-box"><p style="font-size:12px; color:#475569;">Derivadas circulares:</p>', unsafe_allow_html=True)
            st.latex(r"\frac{d}{dx}(\sec(x)) = \sec(x)\tan(x)")
            st.markdown("</div>", unsafe_allow_html=True)
        elif cid == 3:
            st.markdown("### Módulo 3: Trig. Inversas")
            st.markdown('<div class="card-box"><p style="font-size:12px; color:#475569;">Funciones inversas:</p>', unsafe_allow_html=True)
            st.latex(r"\frac{d}{dx}(\arcsin(x)) = \frac{1}{\sqrt{1 - x^2}}")
            st.markdown("</div>", unsafe_allow_html=True)
        elif cid == 4:
            st.markdown("### Módulo 4: Integrales")
            st.markdown('<div class="card-box"><p style="font-size:12px; color:#475569;">Antiderivadas:</p>', unsafe_allow_html=True)
            st.latex(r"\int x^n \, dx = \frac{x^{n+1}}{n+1} + C")
            st.markdown("</div>", unsafe_allow_html=True)

with tab_calc:
    st.markdown('<div class="card-box"><h3 style="margin-top:0; font-size:15px;">🧮 Calculadora</h3></div>', unsafe_allow_html=True)
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
    st.markdown('<div class="card-box"><h3 style="margin-top:0; font-size:15px;">🧠 Quiz</h3><p style="font-size:12px;">Derivada de $f(x) = \\ln(x)$?</p></div>', unsafe_allow_html=True)
    opcion_quiz = st.radio("Elige:", ["A) x", "B) 1/x", "C) e^x", "D) -1/x²"], key="q_m")
    if st.button("Comprobar"):
        if opcion_quiz.startswith("B)"):
            st.success("¡Correcto! 🎉")
        else:
            st.error("Incorrecto.")
