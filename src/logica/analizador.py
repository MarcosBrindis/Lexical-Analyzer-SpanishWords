import re
import csv
from src.logica.reglas import ER_PALABRA_BASICA, ER_PUNTUACION, ER_DIGITO

class AnalizadorLexico:
    def __init__(self):
        # Estructura de Datos (HashSet)
        self.diccionario_palabras_validas = set()

    def cargar_diccionario_csv(self, ruta_csv):
        """
        Lee el archivo CSV específico (Num, Frecuencia, Alfabetico)
        y carga las columnas 1 y 2 en el HashSet.
        """
        try:
            with open(ruta_csv, mode='r', encoding='utf-8') as archivo:
                lector = csv.reader(archivo)
                next(lector, None)  # Saltar encabezado (Número, Frecuencia, Alfabético)
                
                contador = 0
                for fila in lector:
                    if len(fila) >= 3:
                        # Columna 1: Frecuencia (ej. "de")
                        palabra_frec = fila[1].strip().lower()
                        if palabra_frec:
                            self.diccionario_palabras_validas.add(palabra_frec)
                        
                        # Columna 2: Alfabético (ej. "a")
                        palabra_alfa = fila[2].strip().lower()
                        if palabra_alfa:
                            self.diccionario_palabras_validas.add(palabra_alfa)
                        
                        contador += 1
            return True, f"Diccionario cargado con {len(self.diccionario_palabras_validas)} palabras únicas."
        except Exception as e:
            return False, f"Error al cargar diccionario: {str(e)}"

    def _tokenizar(self, texto):
        """
        Separa el texto en lexemas conservando puntuación.
        """
        texto = texto.lower() # Normalización
        # Regex de separación: Grupo 1 captura palabras, digitos o signos individuales
        patron = r"([a-zñáéíóúü]+|\d+|[.,;:¿?¡!]|\S+)"
        lexemas = re.findall(patron, texto)
        return lexemas

    def analizar_texto(self, texto_entrada):
        """
         Función principal (Simulación de Autómata Finito)
        """
        lexemas = self._tokenizar(texto_entrada)
        resultados = []

        for lexema in lexemas:
            tipo = "DESCONOCIDO"

            # Paso A: Diccionario (Búsqueda O(1))
            if lexema in self.diccionario_palabras_validas:
                tipo = "PALABRA_VALIDA_ESPANOL"
            
            # Paso B: Puntuación
            elif re.match(ER_PUNTUACION, lexema):
                tipo = "PUNTUACION"
            
            # Paso C: Dígito
            elif re.match(ER_DIGITO, lexema):
                tipo = "DIGITO"
            
            # Paso D: Error (Fallback)
            else:
                tipo = "ERROR_ORTOGRAFICO"
            
            resultados.append((tipo, lexema))
        
        return resultados