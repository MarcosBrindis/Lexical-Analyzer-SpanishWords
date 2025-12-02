# Proyecto: Analizador Léxico para Palabras Válidas en Español

**Universidad Politécnica de Chiapas**  
**Materia:** Lenguajes y Autómatas  

## Proyecto Final - Práctica 2

###  Descripción del Proyecto
Este programa simula la primera fase de un compilador (**Análisis Léxico**).  
Lee un texto de entrada, separa las palabras (lexemas) y las clasifica según reglas predefinidas y un diccionario de palabras válidas.

---

###  Estructura de Datos
Se utiliza un **HashSet (Conjunto)** para almacenar el diccionario.

**Justificación:**  
La búsqueda en una lista tiene una complejidad de `O(n)`, mientras que en un **Hash Set** es de `O(1)` (tiempo constante).  
Para un diccionario de miles de palabras, esto garantiza que la validación sea instantánea.

---

###  Definición de Expresiones Regulares (Regex)
Estas son las reglas utilizadas en el archivo `src/logica/reglas.py`:

| Token              | Regex              | Descripción                                                                 |
|--------------------|-------------------|-----------------------------------------------------------------------------|
| **ER_PALABRA_BASICA** | `^[a-zñáéíóúü]+$` | Acepta cadenas que solo contienen letras minúsculas del alfabeto español (incluyendo ñ y tildes). Inicio `^` y fin `$` aseguran que sea la palabra completa. |
| **ER_PUNTUACION**     | `^[.,;:¿?¡!]$`    | Acepta exactamente uno de los caracteres de puntuación listados dentro de los corchetes `[]`. |
| **ER_DIGITO**         | `^\d+$`           | Acepta una secuencia de uno o más dígitos numéricos (0-9). |

---

###  Estructura del Proyecto
- **main.py** → Ejecutable principal.  
- **data/input/** → Contiene `diccionario_espanol.csv` y textos de prueba.  
- **src/ui/** → Interfaz gráfica (Tkinter).  
- **src/logica/** → Lógica del autómata y manejo de datos.  

---

###  Cómo ejecutar
```bash
python main.py
