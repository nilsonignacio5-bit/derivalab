import flet as ft
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application

def main(page: ft.Page):
    page.title = "DerivaLab"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = "#0f172a"
    page.padding = 15
    page.scroll = ft.ScrollMode.AUTO

    transformations = standard_transformations + (implicit_multiplication_application,)

    # Componente de Resultado de la Calculadora
    calc_output = ft.Column()

    def calcular_expresion(e):
        calc_output.controls.clear()
        try:
            x = sp.Symbol('x')
            clean_input = func_input.value.replace('^', '**').replace('e', 'E')
            local_dict = {
                'x': x, 'E': sp.E, 'exp': sp.exp, 'ln': sp.log, 'log': sp.log,
                'sin': sp.sin, 'cos': sp.cos, 'tan': sp.tan,
                'sec': sp.sec, 'csc': sp.csc, 'cot': sp.cot,
                'asin': sp.asin, 'acos': sp.acos, 'atan': sp.atan,
                'arcsin': sp.asin, 'arccos': sp.acos, 'arctan': sp.atan, 'sqrt': sp.sqrt
            }
            expr = parse_expr(clean_input, local_dict=local_dict, transformations=transformations, evaluate=False)
            
            if op_radio.value == "Derivada":
                res = sp.diff(expr, x)
                resultado_texto = f"d/dx ({expr}) = {res}"
            else:
                res = sp.integrate(expr, x)
                resultado_texto = f"∫ ({expr}) dx = {res} + C"
                
            calc_output.controls.append(
                ft.Container(
                    content=ft.Text(resultado_texto, color="#38bdf8", size=16, weight=ft.FontWeight.BOLD),
                    bgcolor="#334155",
                    padding=15,
                    border_radius=10
                )
            )
        except Exception as ex:
            calc_output.controls.append(
                ft.Container(
                    content=ft.Text(f"Error de sintaxis: {ex}", color="#f87171", size=14),
                    bgcolor="#451a03",
                    padding=15,
                    border_radius=10
                )
            )
        page.update()

    # Vistas de las Pestañas
    banner_inicio = ft.Container(
        content=ft.Column([
            ft.Text("¡Hola, Estudiante!", size=20, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
            ft.Text("Listo para dominar el cálculo paso a paso.", size=14, color="#cbd5e1"),
            ft.Container(
                content=ft.Text("🔥 7 días de racha de estudio", size=12, color=ft.colors.WHITE, weight=ft.FontWeight.BOLD),
                bgcolor=ft.colors.with_opacity(0.2, ft.colors.WHITE),
                padding=8,
                border_radius=8,
                margin=ft.margin.only(top=10)
            )
        ]),
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
            colors=["#4f46e5", "#6366f1"],
        ),
        padding=20,
        border_radius=14,
        margin=ft.margin.only(bottom=15)
    )

    card_inicio = ft.Container(
        content=ft.Column([
            ft.Text("⚡ Acceso Rápido", size=16, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
            ft.Text("Usa la barra inferior para navegar entre el temario, la calculadora y los quizzes.", size=13, color="#94a3b8")
        ]),
        bgcolor="#1e293b",
        padding=16,
        border_radius=14,
        border=ft.border.all(1, "#334155")
    )

    tab_content = ft.Column([banner_inicio, card_inicio])

    # Contenido de Cursos
    cursos_view = ft.Column([
        ft.Text("📚 Temario de Cálculo", size=18, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
        ft.Container(
            content=ft.Column([
                ft.Text("1. Regla de la Potencia", size=15, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
                ft.Text("Polinomios y derivadas básicas: d/dx(x^n) = n*x^(n-1)", size=13, color="#94a3b8")
            ]),
            bgcolor="#1e293b", padding=14, border_radius=12, border=ft.border.all(1, "#334155")
        ),
        ft.Container(
            content=ft.Column([
                ft.Text("2. Derivadas Trigonométricas", size=15, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
                ft.Text("sin, cos, sec, csc, cot y sus identidades.", size=13, color="#94a3b8")
            ]),
            bgcolor="#1e293b", padding=14, border_radius=12, border=ft.border.all(1, "#334155")
        ),
        ft.Container(
            content=ft.Column([
                ft.Text("3. Trigonométricas Inversas", size=15, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
                ft.Text("arcsin, arccos, arctan y sus derivadas.", size=13, color="#94a3b8")
            ]),
            bgcolor="#1e293b", padding=14, border_radius=12, border=ft.border.all(1, "#334155")
        )
    ], spacing=10)

    # Contenido de Calculadora
    op_radio = ft.RadioGroup(
        content=ft.Row([
            ft.Radio(value="Derivada", label="Derivada d/dx", fill_color="#4f46e5"),
            ft.Radio(value="Integral", label="Integral ∫ dx", fill_color="#4f46e5")
        ], alignment=ft.MainAxisAlignment.CENTER),
        value="Derivada"
    )

    func_input = ft.TextField(
        label="Ingresa f(x)",
        value="sec(x)**2 + arcsin(x)",
        bgcolor="#0f172a",
        color=ft.colors.WHITE,
        border_color="#4f46e5",
        border_radius=10
    )

    calc_view = ft.Column([
        ft.Text("🧮 Calculadora Avanzada", size=18, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
        ft.Container(
            content=ft.Column([
                op_radio,
                func_input,
                ft.ElevatedButton("Calcular Expresión", on_click=calcular_expresion, bgcolor="#4f46e5", color=ft.colors.WHITE, width=300),
                calc_output
            ], spacing=12),
            bgcolor="#1e293b", padding=16, border_radius=14, border=ft.border.all(1, "#334155")
        )
    ], spacing=10)

    # Contenido de Quiz
    quiz_opciones = ft.RadioGroup(
        content=ft.Column([
            ft.Radio(value="A", label="A) x", fill_color="#4f46e5"),
            ft.Radio(value="B", label="B) 1/x", fill_color="#4f46e5"),
            ft.Radio(value="C", label="C) e^x", fill_color="#4f46e5"),
            ft.Radio(value="D", label="D) -1/x²", fill_color="#4f46e5")
        ]),
        value="A"
    )
    quiz_res = ft.Text("", size=14)

    def verificar_quiz(e):
        if quiz_opciones.value == "B":
            quiz_res.value = "¡Correcto! La derivada de ln(x) es 1/x 🎉"
            quiz_res.color = "#4ade80"
        else:
            quiz_res.value = "Incorrecto. Inténtalo de nuevo."
            quiz_res.color = "#f87171"
        page.update()

    quiz_view = ft.Column([
        ft.Text("🧠 Quiz de Evaluación", size=18, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
        ft.Container(
            content=ft.Column([
                ft.Text("¿Cuál es la derivada de f(x) = ln(x)?", size=15, color=ft.colors.WHITE, weight=ft.FontWeight.BOLD),
                quiz_opciones,
                ft.ElevatedButton("Comprobar Respuesta", on_click=verificar_quiz, bgcolor="#4f46e5", color=ft.colors.WHITE),
                quiz_res
            ], spacing=10),
            bgcolor="#1e293b", padding=16, border_radius=14, border=ft.border.all(1, "#334155")
        )
    ], spacing=10)

    # Área de visualización dinámica
    body_container = ft.Container(content=tab_content, expand=True)

    def change_tab(e):
        idx = e.control.selected_index
        if idx == 0:
            body_container.content = tab_content
        elif idx == 1:
            body_container.content = cursos_view
        elif idx == 2:
            body_container.content = calc_view
        elif idx == 3:
            body_container.content = quiz_view
        page.update()

    # Barra de navegación inferior estilo App móvil real
    page.navigation_bar = ft.NavigationBar(
        selected_index=0,
        on_change=change_tab,
        bgcolor="#1e293b",
        indicator_color="#4f46e5",
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.HOME_OUTLINED, selected_icon=ft.icons.HOME, label="Inicio"),
            ft.NavigationBarDestination(icon=ft.icons.BOOK_OUTLINED, selected_icon=ft.icons.BOOK, label="Cursos"),
            ft.NavigationBarDestination(icon=ft.icons.CALCULATE_OUTLINED, selected_icon=ft.icons.CALCULATE, label="Calc"),
            ft.NavigationBarDestination(icon=ft.icons.QUIZ_OUTLINED, selected_icon=ft.icons.QUIZ, label="Quiz"),
        ],
    )

    # Encabezado fijo de la App
    header = ft.Container(
        content=ft.Row([
            ft.Container(
                content=ft.Text("d/dx", color=ft.colors.WHITE, weight=ft.FontWeight.BOLD, size=16),
                bgcolor="#4f46e5", padding=10, border_radius=8
            ),
            ft.Column([
                ft.Text("DerivaLab", size=18, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
                ft.Text("Cálculo Universitario", size=12, color="#94a3b8")
            ], spacing=0)
        ], alignment=ft.MainAxisAlignment.START),
        bgcolor="#1e293b",
        padding=12,
        border_radius=12,
        margin=ft.margin.only(bottom=10)
    )

    page.add(header, body_container)

ft.app(target=main)
