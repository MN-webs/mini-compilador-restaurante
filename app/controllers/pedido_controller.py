from app.services.compiler_service import CompilerService
from app.models.pedido_model import PedidoModel

class PedidoController:
    @staticmethod
    def procesar(texto_orden):
        resultado = CompilerService.analizar_orden(texto_orden)
        
        if resultado["estado"] == "Éxito":
            pedido = PedidoModel(resultado["detalles"], "Validado")
            pedido.guardar_en_base_datos()
            
        return resultado