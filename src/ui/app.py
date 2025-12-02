import tkinter as tk
from tkinter import ttk, scrolledtext

class InterfazAnalizador:
    def __init__(self, root, controlador):
        self.controlador = controlador
        self.root = root
        self.root.title("Analizador Léxico - UP Chiapas")
        self.root.geometry("1500x700")
        
        # Estilos
        style = ttk.Style()
        style.configure("TButton", font=("Arial", 10), padding=5)
        style.configure("TLabel", font=("Arial", 11))
        
        # --- Cabecera ---
        frame_head = tk.Frame(root, bg="#005792", height=80)
        frame_head.pack(fill=tk.X)
        lbl_titulo = tk.Label(frame_head, text="Práctica 2: Analizador Léxico Español", 
                              font=("Helvetica", 16, "bold"), bg="#005792", fg="white")
        lbl_titulo.pack(pady=20)

        # --- Contenedor Principal (PanedWindow) ---
        paned = ttk.PanedWindow(root, orient=tk.HORIZONTAL)
        paned.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # === PANEL IZQUIERDO (Entrada) ===
        frame_izq = ttk.LabelFrame(paned, text=" Entrada de Texto ")
        paned.add(frame_izq, weight=1)

        # Pestañas para modos de entrada
        notebook = ttk.Notebook(frame_izq)
        notebook.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Tab 1: Manual
        self.tab_manual = tk.Frame(notebook)
        notebook.add(self.tab_manual, text="Escribir Texto")
        
        self.txt_entrada = scrolledtext.ScrolledText(self.tab_manual, height=10, font=("Consolas", 11))
        self.txt_entrada.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Tab 2: Archivo (Solo informativo, la acción está en botones)
        self.tab_archivo = tk.Frame(notebook)
        notebook.add(self.tab_archivo, text="Cargar Archivo")
        
        lbl_info = tk.Label(self.tab_archivo, text="Utilice el botón 'Cargar TXT' para importar contenido.", pady=20)
        lbl_info.pack()
        self.lbl_archivo_cargado = tk.Label(self.tab_archivo, text="Ningún archivo cargado", fg="gray", font=("Arial", 9, "italic"))
        self.lbl_archivo_cargado.pack()

        # Botones de Acción (Entrada)
        frame_btn_izq = tk.Frame(frame_izq)
        frame_btn_izq.pack(fill=tk.X, padx=5, pady=5)
        
        btn_cargar = ttk.Button(frame_btn_izq, text="📂 Cargar TXT", command=self.controlador.cargar_archivo_txt)
        btn_cargar.pack(side=tk.LEFT, padx=5)
        
        btn_limpiar = ttk.Button(frame_btn_izq, text="🧹 Limpiar", command=lambda: self.txt_entrada.delete("1.0", tk.END))
        btn_limpiar.pack(side=tk.LEFT, padx=5)

        btn_analizar = ttk.Button(frame_btn_izq, text="▶ ANALIZAR", command=self.controlador.ejecutar_analisis)
        btn_analizar.pack(side=tk.RIGHT, padx=5)

        # === PANEL DERECHO (Salida) ===
        frame_der = ttk.LabelFrame(paned, text=" Tabla de Resultados (Tokens) ")
        paned.add(frame_der, weight=1)

        # Tabla (Treeview)
        cols = ("Tipo Token", "Lexema")
        self.tree = ttk.Treeview(frame_der, columns=cols, show="headings", height=20)
        self.tree.heading("Tipo Token", text="Tipo de Token")
        self.tree.heading("Lexema", text="Lexema (Palabra)")
        
        self.tree.column("Tipo Token", width=200)
        self.tree.column("Lexema", width=150)
        
        # Scrollbar para la tabla
        vsb = ttk.Scrollbar(frame_der, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)
        
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(5,0), pady=5)
        vsb.pack(side=tk.RIGHT, fill=tk.Y, pady=5)

        # Botones de Acción (Salida)
        frame_btn_der = tk.Frame(frame_der)
        frame_btn_der.pack(side=tk.BOTTOM, fill=tk.X, padx=5, pady=5)
        
        btn_exportar = ttk.Button(frame_btn_der, text="💾 Exportar Resultados (.txt)", command=self.controlador.exportar_resultados)
        btn_exportar.pack(fill=tk.X)

        # Barra de estado
        self.lbl_status = tk.Label(root, text="Listo.", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.lbl_status.pack(side=tk.BOTTOM, fill=tk.X)
    
    def actualizar_status(self, mensaje):
        self.lbl_status.config(text=mensaje)

    def mostrar_resultados(self, lista_tokens):
        # Limpiar tabla
        for i in self.tree.get_children():
            self.tree.delete(i)
        
        # Llenar tabla y colorear errores
        for token, lexema in lista_tokens:
            tag = "normal"
            if token == "ERROR_ORTOGRAFICO":
                tag = "error"
            elif token == "PALABRA_VALIDA_ESPANOL":
                tag = "valid"
            
            self.tree.insert("", tk.END, values=(token, lexema), tags=(tag,))
        
        self.tree.tag_configure("error", foreground="red")
        self.tree.tag_configure("valid", foreground="green")

    def obtener_texto(self):
        return self.txt_entrada.get("1.0", tk.END).strip()

    def set_texto(self, texto):
        self.txt_entrada.delete("1.0", tk.END)
        self.txt_entrada.insert(tk.END, texto)