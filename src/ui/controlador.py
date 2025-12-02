import os
import tkinter as tk
from tkinter import filedialog, messagebox
from src.logica.analizador import AnalizadorLexico
from src.ui.app import InterfazAnalizador

class ControladorApp:
    def __init__(self, root):
        self.analizador = AnalizadorLexico()
        self.vista = InterfazAnalizador(root, self)
        
        # Inicialización de rutas
        self.BASE_DIR = os.getcwd() # Asume ejecución desde main.py
        self.RUTA_INPUT = os.path.join(self.BASE_DIR, 'data', 'input')
        self.RUTA_OUTPUT = os.path.join(self.BASE_DIR, 'data', 'output')
        
        # Carga automática del diccionario al iniciar
        self.iniciar_diccionario()
        
        # Variable para guardar los últimos resultados
        self.ultimos_resultados = []

    def iniciar_diccionario(self):
        ruta_dic = os.path.join(self.RUTA_INPUT, 'las-mil-palabras-mas-frecuentes.csv')
        
        # Verificación básica
        if not os.path.exists(ruta_dic):
            messagebox.showerror("Error Crítico", f"No se encuentra el diccionario en:\n{ruta_dic}")
            return

        exito, mensaje = self.analizador.cargar_diccionario_csv(ruta_dic)
        self.vista.actualizar_status(mensaje)
        if not exito:
            messagebox.showwarning("Advertencia", mensaje)

    def cargar_archivo_txt(self):
        """Abre diálogo para seleccionar archivo de entrada"""
        archivo = filedialog.askopenfilename(
            initialdir=self.RUTA_INPUT,
            title="Seleccionar texto de entrada",
            filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*"))
        )
        
        if archivo:
            try:
                with open(archivo, 'r', encoding='utf-8') as f:
                    contenido = f.read()
                    self.vista.set_texto(contenido)
                    nombre = os.path.basename(archivo)
                    self.vista.lbl_archivo_cargado.config(text=f"Cargado: {nombre}", fg="blue")
                    self.vista.actualizar_status(f"Archivo cargado: {nombre}")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo leer el archivo:\n{e}")

    def ejecutar_analisis(self):
        texto = self.vista.obtener_texto()
        if not texto:
            messagebox.showinfo("Información", "El campo de texto está vacío.")
            return
        
        # Llamada a la capa lógica
        self.ultimos_resultados = self.analizador.analizar_texto(texto)
        
        # Actualizar UI
        self.vista.mostrar_resultados(self.ultimos_resultados)
        
        # Reporte rápido en status
        num_errores = sum(1 for t, l in self.ultimos_resultados if t == "ERROR_ORTOGRAFICO")
        self.vista.actualizar_status(f"Análisis completado. Errores detectados: {num_errores}")

    def exportar_resultados(self):
        if not self.ultimos_resultados:
            messagebox.showinfo("Información", "Primero debe realizar un análisis.")
            return
            
        ruta_defecto = os.path.join(self.RUTA_OUTPUT, 'tokens_salida.txt')
        
        archivo_guardar = filedialog.asksaveasfilename(
            initialdir=self.RUTA_OUTPUT,
            initialfile="tokens_salida.txt",
            defaultextension=".txt",
            filetypes=(("Archivos de texto", "*.txt"),)
        )
        
        if archivo_guardar:
            try:
                with open(archivo_guardar, 'w', encoding='utf-8') as f:
                    # Encabezado alineado
                    f.write(f"{'TOKEN':<30} {'LEXEMA'}\n")
                    f.write("-" * 50 + "\n")
                    for tipo, lexema in self.ultimos_resultados:
                        f.write(f"{tipo:<30} {lexema}\n")
                
                self.vista.actualizar_status(f"Resultados guardados en: {os.path.basename(archivo_guardar)}")
                messagebox.showinfo("Éxito", "Archivo exportado correctamente.")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar el archivo:\n{e}")