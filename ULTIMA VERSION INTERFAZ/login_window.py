from tkinter import * 
import tkinter as tk
from tkinter import messagebox    
from welcome_window import *
from conexion import DAO


class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1200x800')
        self.root.title('Servioffset')
        self.root.iconbitmap("logo.ico")
        self.root.resizable(False, False)

        # Crear frame izquierdo para la imagen
        left_frame = tk.Frame(self.root, width=600, height=800, bg='white')
        left_frame.pack_propagate(0)
        left_frame.pack(side='left')

        # Cargar y mostrar la imagen
        img = tk.PhotoImage(file="presentacion.png")
        img_label = tk.Label(left_frame, image=img, bg='white')
        img_label.image = img  # Guardar una referencia a la imagen

        # Obtener las dimensiones de la imagen
        img_width = img.width()
        img_height = img.height()

        # Calcular la posición para centrar la imagen
        x = (600 - img_width) / 2
        y = (800 - img_height) / 2

        img_label.place(x=x, y=y)

        # Crear frame derecho para el formulario de inicio de sesión
        right_frame = tk.Frame(self.root, width=600, height=800, bg='#306EE5')
        right_frame.pack_propagate(0)
        right_frame.pack(side='right')

        # Crear un frame blanco más grande dentro del frame derecho
        login_frame = tk.Frame(right_frame, width=400, height=500, bg='white')
        login_frame.pack_propagate(0)  # Desactivar la propagación de geometría
        login_frame.place(relx=0.5, rely=0.5, anchor='center')

        # Crear el formulario de inicio de sesión dentro del frame blanco
        login_label = tk.Label(login_frame, text='LOGIN', bg='white', fg='black', font=('Helvetica', 24))
        login_label.pack(pady=40)  # Aumentar el espacio alrededor del label

        # Crear variables de control para los campos de entrada
        user_var = tk.StringVar()
        user_var.set('Usuario')
        password_var = tk.StringVar()
        password_var.set('Contraseña')

        # Crear los campos de entrada
        user_entry = tk.Entry(login_frame, textvariable=user_var, font=('Helvetica', 16), fg='dark grey', bg='#EFEFEF')
        user_entry.pack(ipady=5, pady=40)  # Aumentar el espacio alrededor del campo de entrada

        password_entry = tk.Entry(login_frame, textvariable=password_var, show='*', font=('Helvetica', 16), fg='dark grey', bg='#EFEFEF')
        password_entry.pack(ipady=5, pady=40)

        # Función para borrar el texto de los campos de entrada cuando se hace clic en ellos
        def clear_entry(event, entry, default_text):
            if entry.get() == default_text:
                entry.delete(0, 'end')

        # Vincular la función a los campos de entrada
        user_entry.bind('<FocusIn>', lambda event: clear_entry(event, user_entry, 'Usuario'))
        password_entry.bind('<FocusIn>', lambda event: clear_entry(event, password_entry, 'Contraseña'))

        login_button = tk.Button(login_frame, text='Ingresar', bg='#306EE5', fg='white', command=lambda:self.open_new_window(user_entry.get(), password_entry.get()))
        login_button.place(x=50, y=375)
        login_button.config(height=2, width=15)  # Aumentar el tamaño del botón

        # Boton SALIR
        exit_button = tk.Button(login_frame, text='Salir', bg='red', fg='white', command=self.root.destroy)
        exit_button.place(x=250, y=375)
        exit_button.config(height=2, width=15)  # Aumentar el tamaño del botón



    


    def open_new_window(self, user, password):    
        if user=="recepcion" and password=="11111":
            self.root.destroy()  # Cerrar la ventana de inicio de sesión
            self.new_window = tk.Tk()  # Crear una nueva instancia de Tk()
            self.app = WelcomeWindowRecepcion(self.new_window)
        elif user == "disenador" and password=="11111":
            self.root.destroy()  # Cerrar la ventana de inicio de sesión
            self.new_window = tk.Tk()  # Crear una nueva instancia de Tk()
            self.app = WelcomeWindowDisenador(self.new_window)
        elif user == "comercial" and password=="11111":
            self.root.destroy()  # Cerrar la ventana de inicio de sesión
            self.new_window = tk.Tk()  # Crear una nueva instancia de Tk()
            self.app = WelcomeWindowComercial(self.new_window)
        elif user == "cliente" and password=="11111":
            self.root.destroy()  # Cerrar la ventana de inicio de sesión
            self.new_window = tk.Tk()  # Crear una nueva instancia de Tk()
            self.app = WelcomeWindowCliente(self.new_window)
        elif user == "jefeproduccion" and password=="11111":
            self.root.destroy()  # Cerrar la ventana de inicio de sesión
            self.new_window = tk.Tk()  # Crear una nueva instancia de Tk()
            self.app = WelcomeWindowJefeProduccion(self.new_window)
        elif user == "operario" and password=="11111":
            self.root.destroy()  # Cerrar la ventana de inicio de sesión
            self.new_window = tk.Tk()  # Crear una nueva instancia de Tk()
            self.app = WelcomeWindowOperario(self.new_window)
        else:
            messagebox.showwarning("CUIDADO", "USUARIO INVALIDO")


        self.new_window.mainloop()  # Iniciar el bucle principal de la nueva ventana