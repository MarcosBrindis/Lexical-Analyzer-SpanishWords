# INSTRUCCIONES DE EJECUCIÓN

## Requisitos
- Python 3.x instalado
- Tkinter (normalmente viene incluido con Python)

## Cómo ejecutar el programa

### Opción 1: Desde la terminal
```bash
python main.py
```

### Opción 2: Desde VS Code
1. Abre el archivo `main.py`
2. Presiona F5 o haz clic en "Run" -> "Run Without Debugging"

## Uso de la aplicación

### 1. Inicio
Al ejecutar el programa, se cargará automáticamente el diccionario desde `data/las-mil-palabras-mas-frecuentes`.

### 2. Ingresar texto para analizar
Tienes dos opciones:
- **Opción A:** Escribir directamente en la caja de texto de la pestaña "Escribir Texto"
- **Opción B:** Usar el botón "Cargar TXT" para importar un archivo (por ejemplo, `texto_entrada.txt`)

### 3. Analizar
Haz clic en el botón "▶ ANALIZAR" para procesar el texto.

### 4. Ver resultados
Los tokens clasificados aparecerán en la tabla de la derecha:
- **Verde:** Palabras válidas del diccionario
- **Rojo:** Errores ortográficos
- **Negro:** Puntuación y dígitos

### 5. Exportar resultados
Haz clic en "Exportar Resultados (.txt)" para guardar el análisis en `data/output/tokens_salida.txt`.

## Estructura del proyecto
```
AnalizadorLéxicoPalabrasVálidasEspañol/
│
├── main.py                         # ← EJECUTA ESTE ARCHIVO
├── README.md                       # Documentación del proyecto
├── INSTRUCCIONES.md               # Este archivo
│
├── data/
│   ├── input/
│   │   ├── diccionario_espanol.csv    # Diccionario de palabras válidas
│   │   ├── las-mil-palabras-mas-frecuentes.csv  # Archivo original
│   │   └── texto_entrada.txt          # Texto de prueba
│   │
│   └── output/
│       └── tokens_salida.txt      # Se genera al exportar resultados
│
└── src/
    ├── logica/
    │   ├── reglas.py              # Expresiones regulares (Regex)
    │   └── analizador.py          # Lógica del analizador léxico
    │
    └── ui/
        ├── app.py                 # Interfaz gráfica (diseño)
        └── controlador.py         # Controlador (conecta UI con lógica)
```

## Tipos de Tokens detectados

| Tipo                    | Descripción                                    | Ejemplo        |
|-------------------------|------------------------------------------------|----------------|
| PALABRA_VALIDA_ESPANOL  | Palabra que existe en el diccionario          | "computadora"  |
| ERROR_ORTOGRAFICO       | Palabra mal escrita o no reconocida           | "kasa"         |
| PUNTUACION             | Signos de puntuación                           | "." "¿" "!"    |
| DIGITO                 | Números                                        | "123" "2025"   |

## Expresiones Regulares utilizadas

### 1. ER_PALABRA_BASICA
```regex
^[a-zñáéíóúü]+$
```
- Acepta: letras minúsculas del español (incluyendo ñ y tildes)
- Ejemplos válidos: "hola", "canción", "año"

### 2. ER_PUNTUACION
```regex
^[.,;:¿?¡!]$
```
- Acepta: signos de puntuación comunes
- Ejemplos válidos: "." "," "¿" "!"

### 3. ER_DIGITO
```regex
^\d+$
```
- Acepta: uno o más dígitos numéricos
- Ejemplos válidos: "1", "123", "2025"

## Flujo del Analizador (Autómata Finito)

Para cada palabra (lexema) del texto:

1. **Paso A:** ¿Está en el diccionario? → `PALABRA_VALIDA_ESPANOL`
2. **Paso B:** ¿Coincide con ER_PUNTUACION? → `PUNTUACION`
3. **Paso C:** ¿Coincide con ER_DIGITO? → `DIGITO`
4. **Paso D:** Si no coincide con nada → `ERROR_ORTOGRAFICO`

## Solución de problemas

### Error: "No se encuentra el diccionario"
- Verifica que existe el archivo `data/input/diccionario_espanol.csv`

### Error: "ModuleNotFoundError: No module named 'src'"
- Asegúrate de ejecutar `main.py` desde la carpeta raíz del proyecto

### La interfaz no se muestra
- Verifica que Tkinter esté instalado:
  ```bash
  python -m tkinter
  ```

## Notas técnicas

### ¿Por qué usar HashSet?
El diccionario se almacena en un **HashSet (conjunto)** en Python.
- **Búsqueda en lista:** O(n) - lenta para miles de palabras
- **Búsqueda en HashSet:** O(1) - tiempo constante, instantánea

Esto garantiza que validar cada palabra sea extremadamente rápido, incluso con un diccionario de 1000+ palabras.

### Simulación de Autómata Finito
El programa simula un **Autómata Finito Determinista (AFD)** porque:
- Para cada entrada (lexema), sigue una secuencia determinista de validaciones
- Los "estados" son las reglas: Diccionario → Puntuación → Dígito → Error
- La transición entre estados depende de las entradas y las reglas definidas

---

**¡Listo para usar!** Si tienes dudas, revisa el archivo `README.md` o consulta los comentarios en el código.
