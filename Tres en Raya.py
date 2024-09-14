import tkinter as tk
from tkinter import messagebox

class TresEnRaya:
    def __init__(self, root):
        """
        Inicializa la clase TresEnRaya. 
        Configura la ventana principal y los atributos del juego.
        """
        self.root = root
        self.root.title("Tres en Raya")
        self._jugador = "X"  # Inicia el juego con el jugador X
        self._tablero = [""] * 9  # Estado inicial del tablero
        self._botones = []  # Lista para almacenar botones del tablero
        self._punctuaciones = {'X': 0, 'O': 0}  # Contadores de puntos para cada jugador
        self.crear_interfaz()
    def crear_interfaz(self):
        """
        Crea la interfaz gráfica del juego.
        Incluye el título, botón de reinicio, y botones del tablero.
        """
        self.root.configure(bg="#A3C9C9")  # Cambia el fondo de la ventana principal
        titulo = tk.Label(self.root, text="Tres en Raya", font=("Helvetica", 30), bg="#A3C9C9", fg="#000000")  # Cambiado a negro
        titulo.pack(pady=10)

        # Etiqueta que muestra el turno actual
        self.indicador_turno = tk.Label(self.root, text=f"Turno: Jugador {self._jugador}", font=("Helvetica", 20), bg="#A3C9C9", fg="#FF5733")
        self.indicador_turno.pack(pady=10)
        # Etiquetas para mostrar las puntuaciones
        self.indicador_puntuacion = tk.Label(self.root, text=f"X: {self._punctuaciones['X']}  O: {self._punctuaciones['O']}", font=("Helvetica", 20), bg="#A3C9C9", fg="#000000")  # Cambiado a negro
        self.indicador_puntuacion.pack(pady=10)
        reiniciar_btn = tk.Button(self.root, text="Reiniciar Juego", font=("Helvetica", 16), command=self.reiniciar, bg="#FFB6C1", fg="#000000")  # Cambiado a negro
        reiniciar_btn.pack(pady=10)

        #Se crea un marco para los botones del tablero
        tablero_frame = tk.Frame(self.root, bg="#A3C9C9")
        tablero_frame.pack()

        for i in range(9):
            boton = tk.Button(
                tablero_frame, 
                text="", 
                font=("Helvetica", 24), 
                height=2, 
                width=5, 
                bg="#FFFFFF", 
                activebackground="#DDDDDD",
                command=lambda i=i: self.hacer_movimiento(i)
            )
            # Establecer el tamaño del botón usando grid en el marco
            boton.grid(row=i // 3, column=i % 3, padx=10, pady=10)
            self._botones.append(boton)