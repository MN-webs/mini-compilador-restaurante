import re
import time

def compilar_pedido(texto):
    inicio = time.time()
    if not texto.strip():
        tiempo_ms = (time.time() - inicio) * 1000
        return {
            "mensaje": "Analizador léxico-sintáctico — Restaurante Lima Metropolitana\nIngrese instrucciones válidas.",
            "correctas": 0, "err_sintacticos": 0, "err_lexicos": 1,
            "tiempo": f"{tiempo_ms:.3f} ms",
            "tokens": [], "sentencias": []
        }
    
    tokens = []
    sentencias = []
    err_sintacticos = 0
    err_lexicos = 0
    correctas = 0
    
    # Dividir por líneas o instrucciones terminadas en punto y coma o saltos
    lineas = texto.strip().split('\n')
    consola_log = []
    
    for i, linea in enumerate(lineas, 1):
        linea = linea.strip()
        if not linea:
            continue
        
        sentencias.append({"id": i, "texto": linea})
        
        # Patrón esperado: Cantidad y Código de plato (Ej: 2 LMO)
        patron = r'^(\d+)\s+([A-Za-z]+)$'
        match = re.match(patron, linea)
        
        if match:
            cantidad, codigo = match.groups()
            codigo_upper = codigo.upper()
            
            # Validar si el código existe en nuestro diccionario de referencia
            codigos_validos = ["LMO", "AJO", "CEV", "SCP", "CAU"]
            if codigo_upper in codigos_validos:
                correctas += 1
                tokens.append({"tipo": "CANTIDAD", "valor": cantidad})
                tokens.append({"tipo": "CODIGO_PLATO", "valor": codigo_upper})
                consola_log.append(f"[OK] Línea {i}: Comando válido -> {cantidad}x {codigo_upper}")
            else:
                err_lexicos += 1
                consola_log.append(f"[ERROR LÉXICO] Línea {i}: El código '{codigo_upper}' no está registrado en el diccionario.")
        else:
            err_sintacticos += 1
            consola_log.append(f"[ERROR SINTÁCTICO] Línea {i}: Formato incorrecto. Use: [Cantidad] [Código] (Ej: 2 LMO)")

    tiempo_ms = (time.time() - inicio) * 1000
    resultado_str = "\n".join(consola_log)
    
    return {
        "mensaje": resultado_str,
        "correctas": correctas,
        "err_sintacticos": err_sintacticos,
        "err_lexicos": err_lexicos,
        "tiempo": f"{tiempo_ms:.3f} ms",
        "tokens": tokens,
        "sentencias": sentencias
    }