"""
Este programa simula la primera fase del análisis léxico para español,
utilizando una base de datos de palabras válidas y reglas específicas
para identificar, clasificar y manejar errores en un texto de entrada.
"""

import tkinter as tk
from src.ui.controlador import ControladorApp

def main():
    """
    Función principal que inicia la aplicación.
    Crea la ventana principal de Tkinter y lanza el controlador.
    """
    # Crear ventana principal
    root = tk.Tk()
    
    # Inicializar el controlador (que a su vez inicializa la vista)
    app = ControladorApp(root)
    
    # Centrar la ventana en la pantalla
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')
    
    # Iniciar el loop de eventos de Tkinter
    root.mainloop()

if __name__ == "__main__":
    main()
