"""
Módulo de Definición de Patrones Léxicos 
Este archivo contiene las Expresiones Regulares utilizadas para clasificar los tokens.
"""

# 1. ER_PALABRA_BASICA:
# Regla: ^ (inicio) + [rango de letras a-z y caracteres especiales] + (uno o más) + $ (fin)
# Acepta: "hola", "canción", "año"
# No acepta: "hola123", "Hola" (porque se valida tras normalizar a minúsculas)
ER_PALABRA_BASICA = r"^[a-zñáéíóúü]+$"

# 2. ER_PUNTUACION:
# Regla: ^ + [lista de caracteres permitidos] + $
# Acepta: . , ; : ¿ ? ¡ !
ER_PUNTUACION = r"^[.,;:¿?¡!]$"

# 3. ER_DIGITO:
# Regla: ^ + \d (cualquier digito 0-9) + (uno o más) + $
# Acepta: "1", "100", "2025"
ER_DIGITO = r"^\d+$"