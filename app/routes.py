from flask import Blueprint, render_template, request
from app.services.compiler_service import compilar_pedido

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET', 'POST'])
def index():
    res = None
    texto_ingresado = ""
    if request.method == 'POST':
        texto_ingresado = request.form.get('pedido', '')
        res = compilar_pedido(texto_ingresado)
    return render_template('index.html', res=res, texto_ingresado=texto_ingresado)

@main_bp.route('/diccionario')
def diccionario():
    platos_validos = [
        {"codigo": "LMO", "nombre": "Lomo Saltado", "descripcion": "Plato base de carne de res, cebolla, tomate y papas fritas."},
        {"codigo": "AJO", "nombre": "Ají de Gallina", "descripcion": "Crema espesa a base de ají amarillo, gallina deshilachada y leche."},
        {"codigo": "CEV", "nombre": "Cebiche", "descripcion": "Pescado fresco marinado en limones de Piura, cebolla roja y ají limo."},
        {"codigo": "SCP", "nombre": "Seco de Pollo", "descripcion": "Guiso de pollo con culantro, alberjas y zanahoria acompañado de yuca."},
        {"codigo": "CAU", "nombre": "Cau Cau", "descripcion": "Guiso tradicional a base de mondongo, papas amarillas y hierbabuena."}
    ]
    return render_template('diccionario.html', platos=platos_validos)