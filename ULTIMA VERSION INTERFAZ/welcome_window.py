from aifc import Error
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.tix import Tree
from conexion import DAO
from tkinter.ttk import Treeview
from xml.etree.ElementTree import TreeBuilder
from tkinter import messagebox

class WelcomeWindow:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1200x800')
        self.root.title('Bienvenido')
        self.root.iconbitmap("logo.ico")
        self.root.resizable(False, False)

        # Crear frame azul
        blue_frame = tk.Frame(self.root, width=1200, height=800, bg='#306EE5')
        blue_frame.pack(fill='both', expand=True)

        # Crear frame blanco encima del frame azul
        white_frame = tk.Frame(blue_frame, width=1150, height=750, bg='white')
        white_frame.pack_propagate(0)
        white_frame.place(relx=0.5, rely=0.5, anchor='center')

        # Crear título 'Bienvenido'
        welcome_label = tk.Label(white_frame, text='Bienvenido', bg='#306EE5', fg='white', font=('Helvetica', 24))
        welcome_label.pack(pady=40, ipadx=250, ipady=10)

        # Crear un frame para 'Seleccione una opción' y los botones
        option_button_frame = tk.Frame(white_frame, bg='white')
        option_button_frame.pack(side='left', padx=40)  # Añadir espacio a la izquierda

        # Crear recuadro 'Seleccione una opción' dentro del frame de opción y botones
        option_label = tk.Label(option_button_frame, text='Seleccione una opción', bg='#FFA825', fg='black', font=('Helvetica', 16))
        option_label.pack(pady=10, ipadx=85, ipady=10)

        # Crear los botones de forma independiente dentro del frame de opción y botones
        button1 = tk.Button(option_button_frame, text='Botón 1', bg='#5ABAFF', fg='white', font=('Helvetica', 16))
        button1.pack(pady=10, ipadx=80, ipady=8)  # Aumentar el tamaño interno del botón

        button2 = tk.Button(option_button_frame, text='Botón 2', bg='#5ABAFF', fg='white', font=('Helvetica', 16))
        button2.pack(pady=10, ipadx=80, ipady=8)

        button3 = tk.Button(option_button_frame, text='Botón 3', bg='#5ABAFF', fg='white', font=('Helvetica', 16))
        button3.pack(pady=10, ipadx=80, ipady=8)

        button4 = tk.Button(option_button_frame, text='Botón 4', bg='#5ABAFF', fg='white', font=('Helvetica', 16))
        button4.pack(pady=10, ipadx=80, ipady=8)

        button5 = tk.Button(option_button_frame, text='Botón 5', bg='#5ABAFF', fg='white', font=('Helvetica', 16))
        button5.pack(pady=10, ipadx=80, ipady=8)

        # Crear frame gris a la derecha
        gray_frame = tk.Frame(white_frame, width=680, height=600, bg='#EFEFEF')
        gray_frame.pack_propagate(0)
        gray_frame.place(relx=0.699, rely=0.585, anchor='center')



# ---------------------------------------------- RECEPCION ----------------------------------------------





class WelcomeWindowRecepcion:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1200x800')
        self.root.title('Bienvenido Recepcionista')
        self.root.iconbitmap("logo.ico")
        self.root.resizable(False, False)

        self.dao = DAO("recepcion", "11111")
        self.mostrador= StringVar()

        # Crear frame azul
        blue_frame = tk.Frame(self.root, width=1200, height=800, bg='#306EE5')
        blue_frame.pack(fill='both', expand=True)

        # Crear frame blanco encima del frame azul
        white_frame = tk.Frame(blue_frame, width=1150, height=750, bg='white')
        white_frame.pack_propagate(0)
        white_frame.place(relx=0.5, rely=0.5, anchor='center')

        # Crear título 'Bienvenido'
        welcome_label = tk.Label(white_frame, text='Recepcionista', bg='#306EE5', fg='white', font=('Helvetica', 24))
        welcome_label.pack(pady=40, ipadx=250, ipady=10)

        # Crear un frame para 'Seleccione una opción' y los botones
        option_button_frame = tk.Frame(white_frame, bg='white')
        option_button_frame.pack(side='left', padx=40)  # Añadir espacio a la izquierda

        # Crear recuadro 'Seleccione una opción' dentro del frame de opción y botones
        option_label = tk.Label(option_button_frame, text='Seleccione una opción', bg='#FFA825', fg='black', font=('Helvetica', 16))
        option_label.pack(pady=10, ipadx=85, ipady=10)


        # Crear frame gris a la derecha
        gray_frame = tk.Frame(white_frame, width=680, height=600, bg='#EFEFEF')
        gray_frame.pack_propagate(0)
        gray_frame.place(relx=0.699, rely=0.585, anchor='center')


        # Crear un Treeview vacío con Scrollbars dentro del frame gris
        self.tree = ttk.Treeview(gray_frame)

        # Creamos el scrollbar
        vsb = ttk.Scrollbar(gray_frame, orient="vertical")
        vsb.pack(side ="right", fill ="y")
        self.tree.config(height = 23, yscrollcommand=vsb.set)
        vsb.config(command=self.tree.yview)
        self.tree.pack(expand=True, fill='both')  # Hacer que el Treeview se expanda para llenar el frame gris


        # Crear los botones de forma independiente dentro del frame de opción y botones
        cliente_con_mas_ventas_button = tk.Button(option_button_frame, text='Cliente con mas ventas', bg='#5ABAFF', fg='white', font=('Helvetica', 16), width=18, command=lambda:self.cliente_mas_ventas(gray_frame))
        cliente_con_mas_ventas_button.pack(pady=10, ipadx=80, ipady=8)  # Aumentar el tamaño interno del botón

        informacion_de_operario_button = tk.Button(option_button_frame, text='Información de operario', bg='#5ABAFF', fg='white', font=('Helvetica', 16), width=18, command=lambda:self.informacion_operario(gray_frame))
        informacion_de_operario_button.pack(pady=10, ipadx=80, ipady=8)

        ultimos_operarios_ingresados_botton = tk.Button(option_button_frame, text='Ultimos operarios ingresados', bg='#5ABAFF', fg='white', font=('Helvetica', 16), width=18, command=lambda:self.ultimos_operarios_ingresados(gray_frame))
        ultimos_operarios_ingresados_botton.pack(pady=10, ipadx=80, ipady=8)

        cantidad_de_atenciones_botton = tk.Button(option_button_frame, text='Cantidad de atenciones', bg='#5ABAFF', fg='white', font=('Helvetica', 16), width=18, command=lambda:self.cantidad_atenciones(gray_frame))
        cantidad_de_atenciones_botton.pack(pady=10, ipadx=80, ipady=8)

        compra_por_cliente_button = tk.Button(option_button_frame, text='Compra por cliente', bg='#5ABAFF', fg='white', font=('Helvetica', 16), width=18, command=lambda:self.construir_entry(gray_frame))
        compra_por_cliente_button.pack(pady=10, ipadx=80, ipady=8)

        # Agregar botón rojo en la parte superior derecha para volver a la pantalla de inicio de sesión
        back_button = tk.Button(white_frame, text='Salir', bg='red', fg='white', font=('Helvetica', 16), command=lambda:[self.back_to_login(),self.dao.cerrar_conexion()])
        back_button.pack(pady=10, padx=10, anchor='ne')  # Añadir espacio alrededor del botón y anclarlo al noreste (parte superior derecha)
        back_button.place(x=1050, y=75)



    def back_to_login(self):

        # Importar LoginWindow localmente para evitar la importación circular
        from login_window import LoginWindow

        # Destruir el frame actual
        for widget in self.root.winfo_children():
            widget.destroy()

        # Crear una nueva instancia de LoginWindow
        LoginWindow(self.root)





    def cliente_mas_ventas(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

        # Crear un Treeview con Scrollbars
        tree = ttk.Treeview(frame)

        # Definir las características del treeview
        tree.column("#0", width=120, anchor="center")  # Añadir anchor="center" para centrar los datos
        tree.heading("#0", text="Cliente", anchor="center")

        # Creamos el scrollbar
        vsb = ttk.Scrollbar(frame, orient="vertical")
        vsb.pack(side ="right", fill ="y")
        tree.config(height = 23, yscrollcommand=vsb.set)
        vsb.config(command=tree.yview)
        tree.pack(expand=True, fill='both')  # Hacer que el Treeview se expanda para llenar el frame

        self.dao.clientes_mas_ventas(tree)  # Pasamos el objeto tree como argumento



    def informacion_operario(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

        # Crear un Treeview con Scrollbars
        tree = ttk.Treeview(frame, columns=("col1", "col2"))

        # Definir las características del treeview
        tree.column("#0", width=120, anchor= CENTER)
        tree.column("col1", width=120, anchor=CENTER)
        tree.column("col2", width=120, anchor=CENTER)
        #tree.column("col3", width=120, anchor="center")

        tree.heading("#0", text="Cedula Empleado", anchor="center")
        tree.heading("col1", text="Cedula Jefe de Producción", anchor="center")
        tree.heading("col2", text="Cargo", anchor="center")

        # Creamos el scrollbar
        vsb = ttk.Scrollbar(frame, orient="vertical")
        vsb.pack(side ="right", fill ="y")
        tree.config(height = 23, yscrollcommand=vsb.set)
        vsb.config(command=tree.yview)
        tree.pack(expand=True, fill='both')  # Hacer que el Treeview se expanda para llenar el frame

        self.dao.informacion_operario(tree)  # Pasamos el objeto tree como argumento


    def ultimos_operarios_ingresados(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

        # Crear un Treeview con Scrollbars
        tree = ttk.Treeview(frame, columns=("Nombre", "Cedula", "Telefono", "Sueldo", "Fecha de Ingreso"))

        # Definir las características del treeview
        tree.column("#0", width=0, stretch="no")  # Ocultar la columna "#0"
        tree.column("Nombre", width=120)
        tree.column("Cedula", width=120)
        tree.column("Telefono", width=120)
        tree.column("Sueldo", width=120)
        tree.column("Fecha de Ingreso", width=120)

        tree.heading("Nombre", text="Nombre", anchor="center")
        tree.heading("Cedula", text="Cedula", anchor="center")
        tree.heading("Telefono", text="Telefono", anchor="center")
        tree.heading("Sueldo", text="Sueldo", anchor="center")
        tree.heading("Fecha de Ingreso", text="Fecha de Ingreso", anchor="center")

        # Creamos el scrollbar
        vsb = ttk.Scrollbar(frame, orient="vertical")
        vsb.pack(side ="right", fill ="y")
        tree.config(height = 23, yscrollcommand=vsb.set)
        vsb.config(command=tree.yview)
        tree.pack(expand=True, fill='both')  # Hacer que el Treeview se expanda para llenar el frame

        self.dao.ultimos_operarios_ingresados(tree)  # Pasamos el objeto tree como argumento


    def cantidad_atenciones(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

        # Crear un Treeview con Scrollbars
        tree = ttk.Treeview(frame, columns=("Cedula", "Total de Atenciones al cliente"))

        # Definir las características del treeview
        tree.column("#0", width=0, stretch="no")  # Ocultar la columna "#0"
        tree.column("Cedula", width=120, anchor=CENTER)
        tree.column("Total de Atenciones al cliente", width=120, anchor=CENTER)

        tree.heading("Cedula", text="Cedula", anchor="center")
        tree.heading("Total de Atenciones al cliente", text="Total de Atenciones al cliente", anchor="center")

        # Creamos el scrollbar
        vsb = ttk.Scrollbar(frame, orient="vertical")
        vsb.pack(side ="right", fill ="y")
        tree.config(height = 23, yscrollcommand=vsb.set)
        vsb.config(command=tree.yview)
        tree.pack(expand=True, fill='both')  # Hacer que el Treeview se expanda para llenar el frame

        self.dao.cantidad_de_atenciones(tree)  # Pasamos el objeto tree como argumento



    def construir_entry(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

        # Crear un Label en el frame principal
        label = Label(frame, text="Ingresa Cedula del Cliente")
        label.pack()

        # Crear un Entry en el frame principal
        entry = Entry(frame)
        entry.pack()

        # Crear un botón en el frame principal
        button = Button(frame, text="Ingresar", command=lambda:self.introducir_cedula(frame, entry, label, button))
        button.pack()
   


    def introducir_cedula(self, frame, entry, label, button):
        cedula = entry.get()

        # Verificar que la entrada sea solo numérica
        if not cedula.isdigit():
            messagebox.showerror("Error", "Por favor, ingrese solo números.")
            return

        detalles = self.dao.compra_por_cliente(cedula)  # Pasamos la cédula como argumento

        if detalles:
            label.pack_forget()  # Ocultar el Label
            entry.pack_forget()  # Ocultar el Entry
            button.pack_forget()  # Ocultar el botón

            # Crear un Treeview con Scrollbars
            tree = ttk.Treeview(frame, columns=("Cedula Cliente", "Cedula Comercial", "Orden de Produccion", "Fecha de Venta", "Aprobacion", "Porcentaje de descuento"))

            # Definir las características del treeview
            tree.column("#0", width=0, stretch="no")  # Ocultar la columna "#0"
            tree.column("Cedula Cliente", width=80)
            tree.column("Cedula Comercial", width=100)
            tree.column("Orden de Produccion", width=120)
            tree.column("Fecha de Venta", width=90)
            tree.column("Aprobacion", width=68)
            tree.column("Porcentaje de descuento", width=130)

            tree.heading("Cedula Cliente", text="Cedula Cliente", anchor="center")
            tree.heading("Cedula Comercial", text="Cedula Comercial", anchor="center")
            tree.heading("Orden de Produccion", text="Orden de Produccion", anchor="center")
            tree.heading("Fecha de Venta", text="Fecha de Venta", anchor="center")
            tree.heading("Aprobacion", text="Aprobacion", anchor="center")
            tree.heading("Porcentaje de descuento", text="Porcentaje de descuento", anchor="center")

            # Creamos los scrollbars
            vsb = ttk.Scrollbar(frame, orient="vertical")
            vsb.pack(side ="right", fill ="y")
            hsb = ttk.Scrollbar(frame, orient="horizontal")
            hsb.pack(side ="bottom", fill ="x")
            tree.config(height = 23, yscrollcommand=vsb.set, xscrollcommand=hsb.set)
            vsb.config(command=tree.yview)
            hsb.config(command=tree.xview)
            tree.pack(expand=True, fill='both')  # Hacer que el Treeview se expanda para llenar el frame

            # Llenar el treeview con los datos
            for detalle in detalles:
                if len(detalle) >= 6:
                    tree.insert('', 'end', values=(detalle[0], detalle[1], detalle[2], detalle[3], detalle[4], detalle[5]))

            # Actualizar el Treeview
            tree.update_idletasks()
        else:
            messagebox.showinfo("Información", "La cédula ingresada no tiene registros.")
            self.construir_entry(frame)  # Reconstruir el Entry, el Label y el botón    


    
    

   
    

# ---------------------------------------------- DISEÑADOR ----------------------------------------------   

    
    

    


class WelcomeWindowDisenador:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1200x800')
        self.root.title('Bienvenido Diseñador')
        self.root.iconbitmap("logo.ico")
        self.root.resizable(False, False)

        self.dao = DAO("disenador", "11111")
        self.mostrador= StringVar()


        # Crear frame azul
        blue_frame = tk.Frame(self.root, width=1200, height=800, bg='#306EE5')
        blue_frame.pack(fill='both', expand=True)

        # Crear frame blanco encima del frame azul
        white_frame = tk.Frame(blue_frame, width=1150, height=750, bg='white')
        white_frame.pack_propagate(0)
        white_frame.place(relx=0.5, rely=0.5, anchor='center')

        # Crear título 'Bienvenido'
        welcome_label = tk.Label(white_frame, text='Diseñador', bg='#306EE5', fg='white', font=('Helvetica', 24))
        welcome_label.pack(pady=40, ipadx=250, ipady=10)

        # Crear un frame para 'Seleccione una opción' y los botones
        option_button_frame = tk.Frame(white_frame, bg='white')
        option_button_frame.pack(side='left', padx=40)  # Añadir espacio a la izquierda

        # Crear recuadro 'Seleccione una opción' dentro del frame de opción y botones
        option_label = tk.Label(option_button_frame, text='Seleccione una opción', bg='#FFA825', fg='black', font=('Helvetica', 16))
        option_label.pack(pady=10, ipadx=85, ipady=10)

        # Crear los botones de forma independiente dentro del frame de opción y botones
        agregar_disenador_botton = tk.Button(option_button_frame, text='Agregar diseñador', bg='#5ABAFF', fg='white', font=('Helvetica', 16), width=18, command=lambda:self.agregar_disenador(gray_frame))
        agregar_disenador_botton.pack(pady=10, ipadx=80, ipady=8)  # Aumentar el tamaño interno del botón

        ver_informacion_disenador_botton = tk.Button(option_button_frame, text='Ver información del diseñador', bg='#5ABAFF', fg='white', font=('Helvetica', 16), width=18, command=lambda:self.informacion_disenador(gray_frame))
        ver_informacion_disenador_botton.pack(pady=10, ipadx=80, ipady=8)

        actualizar_detalles_disenador_button = tk.Button(option_button_frame, text='Actualizar detalles de diseñador', bg='#5ABAFF', fg='white', font=('Helvetica', 16), width=18, command=lambda:self.actualizar_disenador(gray_frame))
        actualizar_detalles_disenador_button.pack(pady=10, ipadx=80, ipady=8)


        # Crear frame gris a la derecha
        gray_frame = tk.Frame(white_frame, width=680, height=600, bg='#EFEFEF')
        gray_frame.pack_propagate(0)
        gray_frame.place(relx=0.699, rely=0.585, anchor='center')

        # Agregar botón rojo en la parte superior derecha para volver a la pantalla de inicio de sesión
        back_button = tk.Button(white_frame, text='Salir', bg='red', fg='white', font=('Helvetica', 16), command=lambda:[self.back_to_login(), self.dao.cerrar_conexion()])
        back_button.pack(pady=10, padx=10, anchor='ne')  # Añadir espacio alrededor del botón y anclarlo al noreste (parte superior derecha)
        back_button.place(x=1050, y=75)

    def back_to_login(self):

        # Importar LoginWindow localmente para evitar la importación circular
        from login_window import LoginWindow

        # Destruir el frame actual
        for widget in self.root.winfo_children():
            widget.destroy()

        # Crear una nueva instancia de LoginWindow
        LoginWindow(self.root)








    def agregar_disenador(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()
        input_frame = tk.Frame(frame)
        cedulas = self.dao.obtener_cedulas_no_presentes()
        # Verificar si hay cédulas disponibles
        if not cedulas:
            messagebox.showerror("Error", "No se ha encontrado cedulas para ingresar.")
            return
        self.cedula_var = StringVar()
        self.cedula_var.set(cedulas[0])  # Valor por defecto
        label_cedula = Label(input_frame, text="Seleccione la cedula del diseñador")
        label_cedula.pack(side="left")
        dropdown_cedula = OptionMenu(input_frame, self.cedula_var, *cedulas)
        dropdown_cedula.pack(side="left")
        label_software = Label(input_frame, text="Ingrese el software")
        label_software.pack(side="left")
        entry_software = Entry(input_frame)
        entry_software.pack(side="left")
        button = Button(input_frame, text="Ingresar", command=lambda:self.introducir_datos_agregar(frame, entry_software))
        button.pack(side="left")
        input_frame.pack()



    def introducir_datos_agregar(self, frame, entry_software):
        cedula = self.cedula_var.get()
        software = entry_software.get()
        # Verificar que se haya ingresado el software
        if not software:
            messagebox.showerror("Error", "Ingresa el software utilizado.")
            return
        self.dao.agregar_disenador(cedula, software)
        self.mostrar_disenador(frame)





    def informacion_disenador(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

        # Crear un Label en el frame principal
        label = Label(frame, text="Ingrese la cedula del diseñador")
        label.pack()

        # Crear un Entry en el frame principal
        entry = Entry(frame)
        entry.pack()

        # Crear un botón en el frame principal
        button = Button(frame, text="Ingresar", command=lambda:self.introducir_cedula(frame, entry, label, button))
        button.pack()
    

    def introducir_cedula(self, frame, entry, label, button):
        cedula = entry.get()

        # Verificar que la entrada sea solo numérica
        if not cedula.isdigit():
            messagebox.showerror("Error", "El valor debe ser numerico.")
            return

        detalles = self.dao.informacion_disenador(cedula)  # Pasamos la cédula como argumento

        if detalles:
            label.pack_forget()  # Ocultar el Label
            entry.pack_forget()  # Ocultar el Entry
            button.pack_forget()  # Ocultar el botón

            # Crear un Treeview con Scrollbars
            tree = ttk.Treeview(frame, columns=("Cedula", "Nombre", "Software", "Edad", "Genero", "Telefono", "Horario", "Sueldo", "Fecha de ingreso"))

            # Definir las características del treeview
            tree.column("#0", width=0, stretch="no")  # Ocultar la columna "#0"
            tree.column("Cedula", width=80)
            tree.column("Nombre", width=100)
            tree.column("Software", width=120)
            tree.column("Edad", width=90)
            tree.column("Genero", width=68)
            tree.column("Telefono", width=130)
            tree.column("Horario", width=80)
            tree.column("Sueldo", width=100)
            tree.column("Fecha de ingreso", width=120)

            tree.heading("Cedula", text="Cedula", anchor="center")
            tree.heading("Nombre", text="Nombre", anchor="center")
            tree.heading("Software", text="Software", anchor="center")
            tree.heading("Edad", text="Edad", anchor="center")
            tree.heading("Genero", text="Genero", anchor="center")
            tree.heading("Telefono", text="Telefono", anchor="center")
            tree.heading("Horario", text="Horario", anchor="center")
            tree.heading("Sueldo", text="Sueldo", anchor="center")
            tree.heading("Fecha de ingreso", text="Fecha de ingreso", anchor="center")

            # Creamos los scrollbars
            vsb = ttk.Scrollbar(frame, orient="vertical")
            vsb.pack(side ="right", fill ="y")
            hsb = ttk.Scrollbar(frame, orient="horizontal")
            hsb.pack(side ="bottom", fill ="x")
            tree.config(height = 23, yscrollcommand=vsb.set, xscrollcommand=hsb.set)
            vsb.config(command=tree.yview)
            hsb.config(command=tree.xview)
            tree.pack(expand=True, fill='both')  # Hacer que el Treeview se expanda para llenar el frame

            # Llenar el treeview con los datos
            for detalle in detalles:
                if len(detalle) >= 9:
                    tree.insert('', 'end', values=(detalle[0], detalle[1], detalle[2], detalle[3], detalle[4], detalle[5], detalle[6], detalle[7], detalle[8]))

            # Actualizar el Treeview
            tree.update_idletasks()
        else:
            messagebox.showinfo("Información", "Esta cédula no cuenta con registros.")
            self.informacion_disenador(frame)  # Reconstruir el Entry, el Label y el botón

    def actualizar_disenador(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

        # Crear un Label y un Entry para la cédula
        label_cedula = Label(frame, text="Ingrese la cedula del diseñador")
        label_cedula.pack()
        entry_cedula = Entry(frame)
        entry_cedula.pack()

        # Crear un Label y un Entry para el software
        label_software = Label(frame, text="Ingrese el software")
        label_software.pack()
        entry_software = Entry(frame)
        entry_software.pack()

        # Crear un botón para enviar los datos
        button = Button(frame, text="Ingresar", command=lambda:self.introducir_datos(frame, entry_cedula, entry_software, label_cedula, label_software, button))
        button.pack()




    def introducir_datos(self, frame, entry_cedula, entry_software, label_cedula, label_software, button):
        cedula = entry_cedula.get()
        software = entry_software.get()

        # Verificar que la entrada de la cédula sea solo numérica
        if not cedula.isdigit():
            messagebox.showerror("Error", "El valor de la cédula debe ser numerico.")
            return

        # Verificar que se hayan ingresado ambos campos
        if not cedula or not software:
            messagebox.showerror("Error", "Falta agregar la cédula del diseñador o el software.")
            return

        # Verificar si la cédula existe en la base de datos
        detalles = self.dao.mostrar_disenador()
        cedulas = [str(detalle[0]) for detalle in detalles]
        if cedula not in cedulas:
            messagebox.showinfo("Información", "Cedula incorrecta.")
            self.actualizar_disenador(frame)
            return

        # Actualizar la información del diseñador en la base de datos
        self.dao.actualizar_info_disenador(cedula, software)

        # Reconstruir el Entry, el Label y el botón
        self.mostrar_disenador(frame)



    def mostrar_disenador(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

        # Crear un Treeview con Scrollbars
        tree = ttk.Treeview(frame, columns=("Cedula Diseñador", "Software"))

        # Definir las características del treeview
        tree.column("#0", width=0, stretch="no")  # Ocultar la columna "#0"
        tree.column("Cedula Diseñador", width=80)
        tree.column("Software", width=100)

        tree.heading("Cedula Diseñador", text="Cedula Diseñador", anchor="center")
        tree.heading("Software", text="Software", anchor="center")

        # Creamos los scrollbars
        vsb = ttk.Scrollbar(frame, orient="vertical")
        vsb.pack(side ="right", fill ="y")
        hsb = ttk.Scrollbar(frame, orient="horizontal")
        hsb.pack(side ="bottom", fill ="x")
        tree.config(height = 23, yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        vsb.config(command=tree.yview)
        hsb.config(command=tree.xview)
        tree.pack(expand=True, fill='both')  # Hacer que el Treeview se expanda para llenar el frame

        # Llenar el treeview con los datos
        detalles = self.dao.mostrar_disenador()
        for detalle in detalles:
            if len(detalle) >= 2:
                tree.insert('', 'end', values=(detalle[0], detalle[1]))

        # Actualizar el Treeview
        tree.update_idletasks()








# ---------------------------------------------- COMERCIAL ----------------------------------------------   






        


class WelcomeWindowComercial:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1200x800')
        self.root.title('Bienvenido Comercial')
        self.root.iconbitmap("logo.ico")
        self.root.resizable(False, False)

        # Crear frame azul
        blue_frame = tk.Frame(self.root, width=1200, height=800, bg='#306EE5')
        blue_frame.pack(fill='both', expand=True)

        # Crear frame blanco encima del frame azul
        white_frame = tk.Frame(blue_frame, width=1150, height=750, bg='white')
        white_frame.pack_propagate(0)
        white_frame.place(relx=0.5, rely=0.5, anchor='center')

        # Crear título 'Bienvenido'
        welcome_label = tk.Label(white_frame, text='Comercial', bg='#306EE5', fg='white', font=('Helvetica', 24))
        welcome_label.pack(pady=40, ipadx=250, ipady=10)

        # Crear un frame para 'Seleccione una opción' y los botones
        option_button_frame = tk.Frame(white_frame, bg='white')
        option_button_frame.pack(side='left', padx=40)  # Añadir espacio a la izquierda

        # Crear recuadro 'Seleccione una opción' dentro del frame de opción y botones
        option_label = tk.Label(option_button_frame, text='Seleccione una opción', bg='#FFA825', fg='black', font=('Helvetica', 16))
        option_label.pack(pady=10, ipadx=85, ipady=10)

        # Crear frame gris a la derecha
        gray_frame = tk.Frame(white_frame, width=680, height=600, bg='#EFEFEF')
        gray_frame.pack_propagate(0)
        gray_frame.place(relx=0.699, rely=0.585, anchor='center')

        # Crear los botones de forma independiente dentro del frame de opción y botones
        producto_menos_vendido_mes_button = tk.Button(option_button_frame, text='Producto menos vendido del mes', bg='#5ABAFF', fg='white', font=('Helvetica', 16), width=18)
        producto_menos_vendido_mes_button.pack(pady=10, ipadx=80, ipady=8)  # Aumentar el tamaño interno del botón

        historial_ventas_button = tk.Button(option_button_frame, text='Historial de ventas', bg='#5ABAFF', fg='white', font=('Helvetica', 16), width=18)
        historial_ventas_button.pack(pady=10, ipadx=80, ipady=8)

        cliente_mas_atendido_button = tk.Button(option_button_frame, text='Cliente más atendido', bg='#5ABAFF', fg='white', font=('Helvetica', 16), width=18)
        cliente_mas_atendido_button.pack(pady=10, ipadx=80, ipady=8)

        producto_mas_vendido_button = tk.Button(option_button_frame, text='Producto más vendido', bg='#5ABAFF', fg='white', font=('Helvetica', 16), width=18)
        producto_mas_vendido_button.pack(pady=10, ipadx=80, ipady=8)

        # Agregar botón rojo en la parte superior derecha para volver a la pantalla de inicio de sesión
        back_button = tk.Button(white_frame, text='Salir', bg='red', fg='white', font=('Helvetica', 16), command=lambda:[self.back_to_login(), self.dao.cerrar_conexion()])
        back_button.pack(pady=10, padx=10, anchor='ne')  # Añadir espacio alrededor del botón y anclarlo al noreste (parte superior derecha)
        back_button.place(x=1050, y=75)

    def back_to_login(self):

        # Importar LoginWindow localmente para evitar la importación circular
        from login_window import LoginWindow

        # Destruir el frame actual
        for widget in self.root.winfo_children():
            widget.destroy()

        # Crear una nueva instancia de LoginWindow
        LoginWindow(self.root)









# ---------------------------------------------- CLIENTE ----------------------------------------------   











class WelcomeWindowCliente:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1200x800')
        self.root.title('Bienvenido Cliente')
        self.root.iconbitmap("logo.ico")
        self.root.resizable(False, False)
        self.dao = DAO("cliente", "11111")

        # Crear frame azul
        blue_frame = tk.Frame(self.root, width=1200, height=800, bg='#306EE5')
        blue_frame.pack(fill='both', expand=True)

        # Crear frame blanco encima del frame azul
        white_frame = tk.Frame(blue_frame, width=1150, height=750, bg='white')
        white_frame.pack_propagate(0)
        white_frame.place(relx=0.5, rely=0.5, anchor='center')

        # Crear título 'Bienvenido'
        welcome_label = tk.Label(white_frame, text='Cliente', bg='#306EE5', fg='white', font=('Helvetica', 24))
        welcome_label.pack(pady=40, ipadx=250, ipady=10)

        # Crear un frame para 'Seleccione una opción' y los botones
        option_button_frame = tk.Frame(white_frame, bg='white')
        option_button_frame.pack(side='left', padx=40)  # Añadir espacio a la izquierda

        # Crear recuadro 'Seleccione una opción' dentro del frame de opción y botones
        option_label = tk.Label(option_button_frame, text='Seleccione una opción', bg='#FFA825', fg='black', font=('Helvetica', 16))
        option_label.pack(pady=10, ipadx=85, ipady=10)

        # Crear los botones de forma independiente dentro del frame de opción y botones
        compras_realizadas_botton = tk.Button(option_button_frame, text='Compras realizadas', bg='#5ABAFF', fg='white', font=('Helvetica', 16), width=18, command=lambda:self.compras_realizadas(gray_frame))
        compras_realizadas_botton.pack(pady=10, ipadx=80, ipady=8)  # Aumentar el tamaño interno del botón

        productos_botton = tk.Button(option_button_frame, text='Productos', bg='#5ABAFF', fg='white', font=('Helvetica', 16), width=18, command=lambda:self.mostrar_productos_cliente(gray_frame))
        productos_botton.pack(pady=10, ipadx=80, ipady=8)

        tus_comerciales_button = tk.Button(option_button_frame, text='Tus comerciales', bg='#5ABAFF', fg='white', font=('Helvetica', 16), width=18, command=lambda:self.mostrar_tus_comerciales(gray_frame))
        tus_comerciales_button.pack(pady=10, ipadx=80, ipady=8)

        tus_recepcionistas_button = tk.Button(option_button_frame, text='Tus recepcionistas', bg='#5ABAFF', fg='white', font=('Helvetica', 16), width=18, command=lambda:self.mostrar_tus_recepcionistas(gray_frame))
        tus_recepcionistas_button.pack(pady=10, ipadx=80, ipady=8)


        # Crear frame gris a la derecha
        gray_frame = tk.Frame(white_frame, width=680, height=600, bg='#EFEFEF')
        gray_frame.pack_propagate(0)
        gray_frame.place(relx=0.699, rely=0.585, anchor='center')


        # Crear un Treeview vacío con Scrollbars dentro del frame gris
        self.tree = ttk.Treeview(gray_frame)

        # Creamos el scrollbar
        vsb = ttk.Scrollbar(gray_frame, orient="vertical")
        vsb.pack(side ="right", fill ="y")
        self.tree.config(height = 23, yscrollcommand=vsb.set)
        vsb.config(command=self.tree.yview)
        self.tree.pack(expand=True, fill='both')  # Hacer que el Treeview se expanda para llenar el frame gris


        # Agregar botón rojo en la parte superior derecha para volver a la pantalla de inicio de sesión
        back_button = tk.Button(white_frame, text='Salir', bg='red', fg='white', font=('Helvetica', 16), command=lambda:[self.back_to_login(), self.dao.cerrar_conexion()])
        back_button.pack(pady=10, padx=10, anchor='ne')  # Añadir espacio alrededor del botón y anclarlo al noreste (parte superior derecha)
        back_button.place(x=1050, y=75)




    def back_to_login(self):

        # Importar LoginWindow localmente para evitar la importación circular
        from login_window import LoginWindow

        # Destruir el frame actual
        for widget in self.root.winfo_children():
            widget.destroy()

        # Crear una nueva instancia de LoginWindow
        LoginWindow(self.root)



    def compras_realizadas(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

        # Crear un Treeview con Scrollbars
        tree = ttk.Treeview(frame, columns=("Cedula Cliente", "Cedula Comercial", "Orden de Produccion", "Fecha de Venta", "Aprobacion", "Porcentaje de descuento"))

        # Definir las características del treeview
        tree.column("#0", width=0, stretch="no")  # Ocultar la columna "#0"
        tree.column("Cedula Cliente", width=80, anchor=CENTER)
        tree.column("Cedula Comercial", width=100, anchor=CENTER)
        tree.column("Orden de Produccion", width=120, anchor=CENTER)
        tree.column("Fecha de Venta", width=90, anchor=CENTER)
        tree.column("Aprobacion", width=68, anchor=CENTER)
        tree.column("Porcentaje de descuento", width=130, anchor=CENTER)

        tree.heading("Cedula Cliente", text="Cedula Cliente", anchor="center")
        tree.heading("Cedula Comercial", text="Cedula Comercial", anchor="center")
        tree.heading("Orden de Produccion", text="Orden de Produccion", anchor="center")
        tree.heading("Fecha de Venta", text="Fecha de Venta", anchor="center")
        tree.heading("Aprobacion", text="Aprobacion", anchor="center")
        tree.heading("Porcentaje de descuento", text="Porcentaje de descuento", anchor="center")

        # Creamos los scrollbars
        vsb = ttk.Scrollbar(frame, orient="vertical")
        vsb.pack(side ="right", fill ="y")
        hsb = ttk.Scrollbar(frame, orient="horizontal")
        hsb.pack(side ="bottom", fill ="x")
        tree.config(height = 23, yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        vsb.config(command=tree.yview)
        hsb.config(command=tree.xview)
        tree.pack(expand=True, fill='both')  # Hacer que el Treeview se expanda para llenar el frame

        self.dao.compras_del_cliente(tree, "40")  # Pasamos el objeto tree y la cédula como argumentos
    
    

    def mostrar_productos_cliente(self, frame):
        
        for widget in frame.winfo_children():
            widget.destroy()

        # Crear un Treeview con Scrollbars
        tree = ttk.Treeview(frame, columns=("ID Producto", "Cedula del diseñador", "Nombre del producto"))

        # Definir las características del treeview
        tree.column("#0", width=0, stretch="no")  # Ocultar la columna "#0"
        tree.column("ID Producto", width=80, anchor=CENTER)
        tree.column("Cedula del diseñador", width=100, anchor=CENTER)
        tree.column("Nombre del producto", width=120, anchor=CENTER)

        tree.heading("ID Producto", text="ID Producto", anchor="center")
        tree.heading("Cedula del diseñador", text="Cedula del diseñador", anchor="center")
        tree.heading("Nombre del producto", text="Nombre del producto", anchor="center")


        # Creamos los scrollbars
        vsb = ttk.Scrollbar(frame, orient="vertical")
        vsb.pack(side ="right", fill ="y")
        hsb = ttk.Scrollbar(frame, orient="horizontal")
        hsb.pack(side ="bottom", fill ="x")
        tree.config(height = 23, yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        vsb.config(command=tree.yview)
        hsb.config(command=tree.xview)
        tree.pack(expand=True, fill='both')  # Hacer que el Treeview se expanda para llenar el frame

        self.dao.mostrar_productos_cliente(tree, "40")

    
    def mostrar_tus_comerciales(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

        # Crear un Treeview con Scrollbars
        tree = ttk.Treeview(frame)

        # Definir las características del treeview
        tree.column("#0", width=120, anchor=CENTER)  # Añadir anchor="center" para centrar los datos
        tree.heading("#0", text="Tus Comerciales", anchor=CENTER)

        # Creamos el scrollbar
        vsb = ttk.Scrollbar(frame, orient="vertical")
        vsb.pack(side ="right", fill ="y")
        tree.config(height = 23, yscrollcommand=vsb.set)
        vsb.config(command=tree.yview)
        tree.pack(expand=True, fill='both')  # Hacer que el Treeview se expanda para llenar el frame

        self.dao.mostrar_tus_comerciales(tree, "40")  # Pasamos el objeto tree como argumento

    

    def mostrar_tus_recepcionistas(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

        # Crear un Treeview con Scrollbars
        tree = ttk.Treeview(frame)

        # Definir las características del treeview
        tree.column("#0", width=120, anchor="center")  # Añadir anchor="center" para centrar los datos
        tree.heading("#0", text="Tus Recepcionistas", anchor="center")

        # Creamos el scrollbar
        vsb = ttk.Scrollbar(frame, orient="vertical")
        vsb.pack(side ="right", fill ="y")
        tree.config(height = 23, yscrollcommand=vsb.set)
        vsb.config(command=tree.yview)
        tree.pack(expand=True, fill='both')  # Hacer que el Treeview se expanda para llenar el frame

        self.dao.mostrar_tus_recepcionistas(tree, "40")  # Pasamos el objeto tree como argumento
    













# ---------------------------------------------- JEFE PRODUCCION ----------------------------------------------   














class WelcomeWindowJefeProduccion:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1200x800')
        self.root.title('Bienvenido Jefe de Producción')
        self.root.iconbitmap("logo.ico")
        self.root.resizable(False, False)
        self.dao=DAO("jefe_produccion", "11111")

        # Crear frame azul
        blue_frame = tk.Frame(self.root, width=1200, height=800, bg='#306EE5')
        blue_frame.pack(fill='both', expand=True)

        # Crear frame blanco encima del frame azul
        white_frame = tk.Frame(blue_frame, width=1150, height=750, bg='white')
        white_frame.pack_propagate(0)
        white_frame.place(relx=0.5, rely=0.5, anchor='center')

        # Crear título 'Bienvenido'
        welcome_label = tk.Label(white_frame, text='Jefe de Producción', bg='#306EE5', fg='white', font=('Helvetica', 24))
        welcome_label.pack(pady=40, ipadx=250, ipady=10)

        # Crear un frame para 'Seleccione una opción' y los botones
        option_button_frame = tk.Frame(white_frame, bg='white')
        option_button_frame.pack(side='left', padx=40)  # Añadir espacio a la izquierda

        # Crear recuadro 'Seleccione una opción' dentro del frame de opción y botones
        option_label = tk.Label(option_button_frame, text='Seleccione una opción', bg='#FFA825', fg='black', font=('Helvetica', 16))
        option_label.pack(pady=10, ipadx=85, ipady=10)

        # Crear los botones de forma independiente dentro del frame de opción y botones
        actualizar_material_comprado_button = tk.Button(option_button_frame, text='Actualizar material comprado', bg='#5ABAFF', fg='white', font=('Helvetica', 16), width=18, command=lambda:self.actualizar_material(gray_frame))
        actualizar_material_comprado_button.pack(pady=10, ipadx=80, ipady=8)  # Aumentar el tamaño interno del botón

        agregar_empleado_button = tk.Button(option_button_frame, text='Agregar empleado', bg='#5ABAFF', fg='white', font=('Helvetica', 16), width=18, command=lambda:self.datos_empleado(gray_frame))
        agregar_empleado_button.pack(pady=10, ipadx=80, ipady=8)

        cantidad_material_producto_botton = tk.Button(option_button_frame, text='Actualizar cantidad de material del producto', bg='#5ABAFF', fg='white', font=('Helvetica', 16), width=18, command=lambda:self.cantidad_material_producto(gray_frame))
        cantidad_material_producto_botton.pack(pady=10, ipadx=80, ipady=8)

        eliminar_una_maquina_botton = tk.Button(option_button_frame, text='Eliminar una maquina', bg='#5ABAFF', fg='white', font=('Helvetica', 16), width=18, command=lambda:self.borrar_maquina(gray_frame))
        eliminar_una_maquina_botton.pack(pady=10, ipadx=80, ipady=8)

        # Crear frame gris a la derecha
        gray_frame = tk.Frame(white_frame, width=680, height=600, bg='#EFEFEF')
        gray_frame.pack_propagate(0)
        gray_frame.place(relx=0.699, rely=0.585, anchor='center')

        # Agregar botón rojo en la parte superior derecha para volver a la pantalla de inicio de sesión
        back_button = tk.Button(white_frame, text='Salir', bg='red', fg='white', font=('Helvetica', 16), command=lambda:[self.back_to_login(), self.dao.cerrar_conexion()])
        back_button.pack(pady=10, padx=10, anchor='ne')  # Añadir espacio alrededor del botón y anclarlo al noreste (parte superior derecha)
        back_button.place(x=1050, y=75)


    def back_to_login(self):

        # Importar LoginWindow localmente para evitar la importación circular
        from login_window import LoginWindow

        # Destruir el frame actual
        for widget in self.root.winfo_children():
            widget.destroy()

        # Crear una nueva instancia de LoginWindow
        LoginWindow(self.root)


    
    def actualizar_material(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

        # Crear un Label y un Entry para la cédula
        label_material = Label(frame, text="Ingrese el id del material")
        label_material.pack()
        entry_material = Entry(frame)
        entry_material.pack()

        # Crear un Label y un Entry para el software
        label_cantidad = Label(frame, text="Ingrese la nueva cantidad")
        label_cantidad.pack()
        entry_cantidad = Entry(frame)
        entry_cantidad.pack()

        # Crear un botón para enviar los datos
        button = Button(frame, text="Ingresar", command=lambda:self.introducir_datos_material(frame, entry_material, entry_cantidad))
        button.pack()





            ###  BOTON 1  ###





    def introducir_datos_material(self, frame, entry_material, entry_cantidad):
        material = entry_material.get()
        cantidad = entry_cantidad.get()

        # Verificar que la entrada de la cédula sea solo numérica
        if not material.isdigit():
            messagebox.showerror("Error", "El valor del ID debe ser numérico.")
            return

        # Verificar que se hayan ingresado ambos campos
        if not material or not cantidad:
            messagebox.showerror("Error", "Faltan datos que agregar.")
            return

        # Verificar si la cédula existe en la base de datos
        detalles = self.dao.mostrar_materiales_id()
        materiales = [str(detalle[0]) for detalle in detalles]
        if material not in materiales:
            messagebox.showinfo("Información", "ID incorrecto.")
            self.actualizar_material(frame)
            return



        for widget in frame.winfo_children():
            widget.destroy()

        # Crear un Treeview con Scrollbars
        tree = ttk.Treeview(frame, columns=("ID", "Material", "Calidad", "Cantidad", "Clasificacion", "Precio", "Vida_util"))

        # Definir las características del treeview
        tree.column("#0", width=0, stretch="no")  # Ocultar la columna "#0"
        tree.column("ID", width=80, anchor=CENTER)
        tree.column("Material", width=100, anchor=CENTER)
        tree.column("Calidad", width=100, anchor= CENTER)
        tree.column("Cantidad", width=100, anchor= CENTER)
        tree.column("Clasificacion", width=100, anchor= CENTER)
        tree.column("Precio", width=100, anchor= CENTER)
        tree.column("Vida_util", width=100, anchor= CENTER)


        tree.heading("ID", text="ID", anchor=CENTER)
        tree.heading("Material", text="Material", anchor=CENTER)
        tree.heading("Calidad", text="Calidad", anchor=CENTER) 
        tree.heading("Cantidad", text="Cantidad", anchor=CENTER)
        tree.heading("Clasificacion", text="Clasificación", anchor=CENTER)
        tree.heading("Precio", text="Precio", anchor=CENTER)
        tree.heading("Vida_util", text="Vida útil", anchor=CENTER)


        # Creamos los scrollbars
        vsb = ttk.Scrollbar(frame, orient="vertical")
        vsb.pack(side ="right", fill ="y")
        hsb = ttk.Scrollbar(frame, orient="horizontal")
        hsb.pack(side ="bottom", fill ="x")
        tree.config(height = 23, yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        vsb.config(command=tree.yview)
        hsb.config(command=tree.xview)
        tree.pack(expand=True, fill='both')  # Hacer que el Treeview se expanda para llenar el frame

        # Actualizar cantidad material en la base de datos
        self.dao.actualizar_material(tree, material, cantidad)









            ###  BOTON 2  ###







    def datos_empleado(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

        # Crear un Label y un Entry para la cédula
        label_cedula = Label(frame, text="Ingrese la cédula:")
        label_cedula.grid(row=0, column=0)
        entry_cedula = Entry(frame)
        entry_cedula.grid(row=0, column=1)

        label_nombre = Label(frame, text="Ingrese el nombre:")
        label_nombre.grid(row=1, column=0)
        entry_nombre = Entry(frame)
        entry_nombre.grid(row=1, column=1)

        label_edad = Label(frame, text="Ingrese la edad:")
        label_edad.grid(row=2, column=0)
        entry_edad = Entry(frame)
        entry_edad.grid(row=2, column=1)

        label_genero = Label(frame, text="Ingrese el genero:")
        label_genero.grid(row=3, column=0)
        entry_genero = Entry(frame)
        entry_genero.grid(row=3, column=1)

        label_telefono = Label(frame, text="Ingrese el teléfono:")
        label_telefono.grid(row=4, column=0)
        entry_telefono = Entry(frame)
        entry_telefono.grid(row=4, column=1)

        label_horario = Label(frame, text="Ingrese el horario (HH:MM:SS):")
        label_horario.grid(row=5, column=0)
        entry_horario = Entry(frame)
        entry_horario.grid(row=5, column=1)

        label_sueldo = Label(frame, text="Ingrese el sueldo:")
        label_sueldo.grid(row=6, column=0)
        entry_sueldo = Entry(frame)
        entry_sueldo.grid(row=6, column=1)

        label_fecha_ingreso = Label(frame, text="Ingrese la fecha de ingreso (YYYY-MM-DD):")
        label_fecha_ingreso.grid(row=7, column=0)
        entry_fecha_ingreso = Entry(frame)
        entry_fecha_ingreso.grid(row=7, column=1)


        # Crear un botón para enviar los datos
        button = Button(frame, text="Ingresar", command=lambda:self.introducir_datos_empleado(frame,
                                                                                               entry_cedula,
                                                                                               entry_nombre, 
                                                                                               entry_edad, 
                                                                                               entry_genero, 
                                                                                               entry_telefono, 
                                                                                               entry_horario, 
                                                                                               entry_sueldo,
                                                                                               entry_fecha_ingreso))
        button.grid(row=8, columnspan=2)



    def introducir_datos_empleado(self, frame, 
                                  entry_cedula, 
                                  entry_nombre,
                                  entry_edad,
                                  entry_genero,
                                  entry_telefono,
                                  entry_horario,
                                  entry_sueldo,
                                  entry_fecha_ingreso):
        
        cedula = entry_cedula.get()
        nombre = entry_nombre.get()
        edad = entry_edad.get()
        genero = entry_genero.get()
        telefono = entry_telefono.get()
        horario = entry_horario.get()
        sueldo = entry_sueldo.get()
        fecha = entry_fecha_ingreso.get()

        # Verificar que la entrada de los datos son solo numérica
        if not cedula.isdigit() or not edad.isdigit() or not sueldo.isdigit():
            messagebox.showerror("Error", "Cèdula, edad y sueldo deben ser numericos.")
            return

        # Verificar que se hayan ingresado ambos campos
        if not cedula or not nombre or not edad or not genero or not telefono or not horario or not sueldo or not fecha:
            messagebox.showerror("Error", "Falta agregar datos.")
            return

        # Verificar si la cédula existe en la base de datos
        detalles = self.dao.mostrar_empleados()
        empleados = [str(detalle[0]) for detalle in detalles] 
        if cedula in empleados:
            messagebox.showinfo("Información", "Empleado y existente.")
            self.datos_empleado(frame) ## Se devuelve a la funcion inicial del boton
            return


        for widget in frame.winfo_children():
            widget.destroy()

        # Crear un Treeview con Scrollbars
        tree = ttk.Treeview(frame, columns=("Cedula", "Nombre", "Edad", "Genero", "Telefono", "Horario", "Sueldo", "Fecha"))

        # Definir las características del treeview
        tree.column("#0", width=0, stretch="no")  # Ocultar la columna "#0"
        tree.column("Cedula", width=80, anchor=CENTER)
        tree.column("Nombre", width=100, anchor=CENTER)
        tree.column("Edad", width=100, anchor= CENTER)
        tree.column("Genero", width=100, anchor= CENTER)
        tree.column("Telefono", width=100, anchor= CENTER)
        tree.column("Horario", width=100, anchor= CENTER)
        tree.column("Sueldo", width=100, anchor= CENTER)
        tree.column("Fecha", width=100, anchor= CENTER)


        tree.heading("Cedula", text="Cédula", anchor=CENTER)
        tree.heading("Nombre", text="Nombre", anchor=CENTER)
        tree.heading("Edad", text="Edad", anchor=CENTER) 
        tree.heading("Genero", text="Genero", anchor=CENTER)
        tree.heading("Telefono", text="Teléfono", anchor=CENTER)
        tree.heading("Horario", text="Horario", anchor=CENTER)
        tree.heading("Sueldo", text="Sueldo", anchor=CENTER)
        tree.heading("Fecha", text="Fecha de Ingreso", anchor=CENTER)


        # Creamos los scrollbars
        vsb = ttk.Scrollbar(frame, orient="vertical")
        vsb.pack(side ="right", fill ="y")
        hsb = ttk.Scrollbar(frame, orient="horizontal")
        hsb.pack(side ="bottom", fill ="x")
        tree.config(height = 23, yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        vsb.config(command=tree.yview)
        hsb.config(command=tree.xview)
        tree.pack(expand=True, fill='both')  # Hacer que el Treeview se expanda para llenar el frame

        # Llenar el treeview con los datos
        self.dao.agregar_empleado(tree, cedula, nombre, edad, genero, telefono, horario, sueldo, fecha)









            ###  BOTON 3  ###





    def cantidad_material_producto(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

        # Crear un Label y un Entry para la cédula
        label_producto = Label(frame, text="Ingrese el id del producto")
        label_producto.pack()
        entry_producto = Entry(frame)
        entry_producto.pack()

        label_cantidad = Label(frame, text="Ingrese la nueva cantidad del producto")
        label_cantidad.pack()
        entry_cantidad = Entry(frame)
        entry_cantidad.pack()


        # Crear un botón para enviar los datos
        button = Button(frame, text="Ingresar", command=lambda:self.introducir_datos_productos(frame, entry_producto, entry_cantidad))
        button.pack()



    def introducir_datos_productos(self, frame, entry_producto, entry_cantidad):
        producto = entry_producto.get()
        cantidad = entry_cantidad.get()

        # Verificar que la entrada de la cédula sea solo numérica
        if not producto.isdigit() or not cantidad.isdigit():
            messagebox.showerror("Error", "El dato debe ser numerico.")
            return

        # Verificar que se hayan ingresado ambos campos
        if not producto or not cantidad:
            messagebox.showerror("Error", "Falta agregar datos.")
            return

        # Verificar si la cédula existe en la base de datos
        detalles = self.dao.mostrar_productos()
        productos = [str(detalle[0]) for detalle in detalles] 
        if producto not in productos:
            messagebox.showinfo("Información", "Id incorrecto.")
            self.cantidad_material_producto(frame) ## Se devuelve a la funcion inicial del boton
            return


        for widget in frame.winfo_children():
            widget.destroy()

        # Crear un Treeview con Scrollbars
        tree = ttk.Treeview(frame, columns=("Id_producto", "Nombre", "Material", "Cantidad"))

        # Definir las características del treeview
        tree.column("#0", width=0, stretch="no")  # Ocultar la columna "#0"
        tree.column("Id_producto", width=80, anchor=CENTER)
        tree.column("Nombre", width=100, anchor=CENTER)
        tree.column("Material", width=100, anchor= CENTER)
        tree.column("Cantidad", width=100, anchor= CENTER)


        tree.heading("Id_producto", text="Id producto", anchor=CENTER)
        tree.heading("Nombre", text="Nombre", anchor=CENTER)
        tree.heading("Material", text="Material", anchor=CENTER) 
        tree.heading("Cantidad", text="Último Cantidad", anchor=CENTER)


        # Creamos los scrollbars
        vsb = ttk.Scrollbar(frame, orient="vertical")
        vsb.pack(side ="right", fill ="y")
        hsb = ttk.Scrollbar(frame, orient="horizontal")
        hsb.pack(side ="bottom", fill ="x")
        tree.config(height = 23, yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        vsb.config(command=tree.yview)
        hsb.config(command=tree.xview)
        tree.pack(expand=True, fill='both')  # Hacer que el Treeview se expanda para llenar el frame

        # Llenar el treeview con los datos
        self.dao.actualizar_cantidad_producto(tree, producto, cantidad)






            ###  BOTON 4 ###





    def borrar_maquina(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

        # Crear un Label y un Entry para la cédula
        label_maquina = Label(frame, text="Ingrese el id de la maquina")
        label_maquina.pack()
        entry_maquina = Entry(frame)
        entry_maquina.pack()


        # Crear un botón para enviar los datos
        button = Button(frame, text="Ingresar", command=lambda:self.introducir_datos_maquina(frame, entry_maquina))
        button.pack()



    def introducir_datos_maquina(self, frame, entry_maquina):
        maquina = entry_maquina.get()

        # Verificar que la entrada de la cédula sea solo numérica
        if not maquina.isdigit():
            messagebox.showerror("Error", "El id  debe ser numerico.")
            return

        # Verificar que se hayan ingresado ambos campos
        if not maquina:
            messagebox.showerror("Error", "Falta agregar el id de la maquina.")
            return

        # Verificar si la cédula existe en la base de datos
        detalles = self.dao.mostrar_maquinas()
        maquinas = [str(detalle[0]) for detalle in detalles]
        if maquina not in maquinas:
            messagebox.showinfo("Información", "Id incorrecto.")
            self.borrar_maquina(frame) ## Se devuelve a la funcion inicial del boton
            return


        for widget in frame.winfo_children():
            widget.destroy()

        # Crear un Treeview con Scrollbars
        tree = ttk.Treeview(frame, columns=("Id", "Marca", "Fecha_adquisición", "Último_mantenimiento"))

        # Definir las características del treeview
        tree.column("#0", width=0, stretch="no")  # Ocultar la columna "#0"
        tree.column("Id", width=80, anchor=CENTER)
        tree.column("Fecha_adquisición", width=100, anchor=CENTER)
        tree.column("Último_mantenimiento", width=100, anchor= CENTER)


        tree.heading("Id", text="Id", anchor=CENTER)
        tree.heading("Marca", text="Marca", anchor=CENTER)
        tree.heading("Fecha_adquisición", text="Fecha adquisición", anchor=CENTER) 
        tree.heading("Último_mantenimiento", text="Último mantenimiento", anchor=CENTER)


        # Creamos los scrollbars
        vsb = ttk.Scrollbar(frame, orient="vertical")
        vsb.pack(side ="right", fill ="y")
        hsb = ttk.Scrollbar(frame, orient="horizontal")
        hsb.pack(side ="bottom", fill ="x")
        tree.config(height = 23, yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        vsb.config(command=tree.yview)
        hsb.config(command=tree.xview)
        tree.pack(expand=True, fill='both')  # Hacer que el Treeview se expanda para llenar el frame

        # Llenar el treeview con los datos
        self.dao.borrar_maquina(tree, maquina)



            


        



        
        








# ---------------------------------------------- OPERARIO --------------------------------------------------------------   




















class WelcomeWindowOperario:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1200x800')
        self.root.title('Bienvenido Operario')
        self.root.iconbitmap("logo.ico")
        self.root.resizable(False, False)
        self.dao=DAO("operario", "11111")


        # Crear frame azul
        blue_frame = tk.Frame(self.root, width=1200, height=800, bg='#306EE5')
        blue_frame.pack(fill='both', expand=True)

        # Crear frame blanco encima del frame azul
        white_frame = tk.Frame(blue_frame, width=1150, height=750, bg='white')
        white_frame.pack_propagate(0)
        white_frame.place(relx=0.5, rely=0.5, anchor='center')

        # Crear título 'Bienvenido'
        welcome_label = tk.Label(white_frame, text='Operario', bg='#306EE5', fg='white', font=('Helvetica', 24))
        welcome_label.pack(pady=40, ipadx=250, ipady=10)

        # Crear un frame para 'Seleccione una opción' y los botones
        option_button_frame = tk.Frame(white_frame, bg='white')
        option_button_frame.pack(side='left', padx=40)  # Añadir espacio a la izquierda

        # Crear recuadro 'Seleccione una opción' dentro del frame de opción y botones
        option_label = tk.Label(option_button_frame, text='Seleccione una opción', bg='#FFA825', fg='black', font=('Helvetica', 16))
        option_label.pack(pady=10, ipadx=85, ipady=10)

        # Crear los botones de forma independiente dentro del frame de opción y botones
        cantidad_de_material_button = tk.Button(option_button_frame, text='Cantidad de material', bg='#5ABAFF', fg='white', font=('Helvetica', 16), width=18, command=lambda :self.ingrese_cantidad(gray_frame))
        cantidad_de_material_button.pack(pady=10, ipadx=80, ipady=8)  # Aumentar el tamaño interno del botón

        eliminar_inventario_button = tk.Button(option_button_frame, text='Eliminar elemento del inventario', bg='#5ABAFF', fg='white', font=('Helvetica', 16), width=18, command=lambda: self.construir_entry(gray_frame))
        eliminar_inventario_button.pack(pady=10, ipadx=80, ipady=8)

        material_fabricacion_button = tk.Button(option_button_frame, text='Material fabricación', bg='#5ABAFF', fg='white', font=('Helvetica', 16), width=18, command=lambda: self.mostrar_vista_inventario_fabricacion(gray_frame))
        material_fabricacion_button.pack(pady=10, ipadx=80, ipady=8)

        informacion_maquina_button = tk.Button(option_button_frame, text='Información de maquina', bg='#5ABAFF', fg='white', font=('Helvetica', 16), width=18, command=lambda: self.mostrar_vista_maquina(gray_frame))
        informacion_maquina_button.pack(pady=10, ipadx=80, ipady=8)

        revision_button = tk.Button(option_button_frame, text='Revisión', bg='#5ABAFF', fg='white', font=('Helvetica', 16), width=18, command=lambda: self.mostrar_vista_revision(gray_frame))
        revision_button.pack(pady=10, ipadx=80, ipady=8)

        # Crear frame gris a la derecha
        gray_frame = tk.Frame(white_frame, width=680, height=600, bg='#EFEFEF')
        gray_frame.pack_propagate(0)
        gray_frame.place(relx=0.699, rely=0.585, anchor='center')

        # Agregar botón rojo en la parte superior derecha para volver a la pantalla de inicio de sesión
        back_button = tk.Button(white_frame, text='Salir', bg='red', fg='white', font=('Helvetica', 16), command=lambda:[self.back_to_login(), self.dao.cerrar_conexion()])
        back_button.pack(pady=10, padx=10, anchor='ne')  # Añadir espacio alrededor del botón y anclarlo al noreste (parte superior derecha)
        back_button.place(x=1050, y=75)

    def back_to_login(self):

        # Importar LoginWindow localmente para evitar la importación circular
        from login_window import LoginWindow

        # Destruir el frame actual
        for widget in self.root.winfo_children():
            widget.destroy()

        # Crear una nueva instancia de LoginWindow
        LoginWindow(self.root)






            ###  BOTON 1  ###







    def ingrese_cantidad(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()


        Label(frame, text="Nombre del material", font=('Helvetica', 16)).pack()
        entry_material = Entry(frame)
        entry_material.pack(padx=50, pady=50)


        Label(frame, text="Calidad", font=('Helvetica', 16)).pack()
        entry_calidad = Entry(frame)
        entry_calidad.pack(padx=50, pady=50)


        botton = Button(frame, text="Buscar", command=lambda:self.cantidad_material(frame, entry_material, entry_calidad))
        botton.pack()



    def cantidad_material(self, frame, entry_material, entry_calidad ):
        material = entry_material.get()
        calidad = entry_calidad.get()

        # Verificar que la entrada de la cédula sea solo numérica
        if material.isdigit():
            messagebox.showerror("Error", "El material no debe ser numerico.")
            return

        # Verificar que se hayan ingresado ambos campos
        if not material or not calidad:
            messagebox.showerror("Error", "Faltan datos por agregar.")
            return

        # Verificar si la cédula existe en la base de datos
        detalles = self.dao.mostrar_materiales()
        materiales = [str(detalle[0]) for detalle in detalles]
        calidades = [str(detalle[1]) for detalle in detalles]
        flag = 0

        for i in range(len(materiales)):
            if material.lower() == materiales[i].lower()  and  calidad.lower() == calidades[i].lower():
                flag=1

        if flag==0:
            messagebox.showinfo("Información", "Material no encontrado.")
            self.ingrese_cantidad(frame) ## Se devuelve a la funcion inicial del boton
            return


        for widget in frame.winfo_children():
            widget.destroy()

        # Crear un Treeview con Scrollbars
        tree = ttk.Treeview(frame, columns=("Cantidad"))

        # Definir las características del treeview
        tree.column("#0", width=0, stretch="no")  # Ocultar la columna "#0"
        tree.column("Cantidad", width=80, anchor=CENTER)
        '''
        tree.column("Material", width=100, anchor=CENTER)
        tree.column("Calidad", width=100, anchor= CENTER)
        tree.column("Cantidad", width=100, anchor= CENTER)
        tree.column("Clasificacion", width=100, anchor= CENTER)
        tree.column("Precio", width=100, anchor= CENTER)
        tree.column("Vida_util", width=100, anchor= CENTER)
        '''

        tree.heading("Cantidad", text="Cantidad", anchor=CENTER)
        '''
        tree.heading("Material", text="Material", anchor=CENTER)
        tree.heading("Calidad", text="Calidad", anchor=CENTER) 
        tree.heading("Cantidad", text="Cantidad", anchor=CENTER)
        tree.heading("Clasificacion", text="Vida util", anchor=CENTER)
        tree.heading("Precio", text="Precio", anchor=CENTER)
        tree.heading("Vida_util", text="Vida útil", anchor=CENTER)
        '''



        # Creamos los scrollbars
        vsb = ttk.Scrollbar(frame, orient="vertical")
        vsb.pack(side ="right", fill ="y")
        hsb = ttk.Scrollbar(frame, orient="horizontal")
        hsb.pack(side ="bottom", fill ="x")
        tree.config(height = 23, yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        vsb.config(command=tree.yview)
        hsb.config(command=tree.xview)
        tree.pack(expand=True, fill='both')  # Hacer que el Treeview se expanda para llenar el frame

        # Llenar el treeview con los datos
        self.dao.cantidad_de_material(tree, material, calidad)







            ###  BOTON 2  ###








    def construir_entry(self, frame):

        for widget in frame.winfo_children():
            widget.destroy()

        Label(frame, text="Ingresar id de elemento a eliminar", font=('Helvetica', 16)).pack()

        entry_elemento = Entry(frame)
        entry_elemento.pack(padx=50, pady=50)

        botton = Button(frame, text="Eliminar", command=lambda: self.eliminar_inventario(frame, entry_elemento))
        botton.pack()




    def eliminar_inventario(self, frame, entry_elemento):
        elemento = entry_elemento.get()

        # Verificar que la entrada de la cédula sea solo numérica
        if not elemento.isdigit():
            messagebox.showerror("Error", "El id debe ser numerico.")
            return

        # Verificar que se hayan ingresado ambos campos
        if not elemento:
            messagebox.showerror("Error", "Falta agregar el id del elemento.")
            return

        # Verificar si la cédula existe en la base de datos
        detalles = self.dao.mostrar_elementos_inventario()
        elementos = [str(detalle[0]) for detalle in detalles]
        if elemento not in elementos:
            messagebox.showinfo("Información", "Id no encontrado.")
            self.construir_entry(frame) ## Se devuelve a la funcion inicial del boton
            return


        for widget in frame.winfo_children():
            widget.destroy()

        # Crear un Treeview con Scrollbars
        tree = ttk.Treeview(frame, columns=("Id", "Cantidad", "clasificacion", "precio", "vida_util"))

        # Definir las características del treeview
        tree.column("#0", width=0, stretch="no")  # Ocultar la columna "#0"
        tree.column("Cantidad", width=80, anchor=CENTER)
        tree.column("clasificacion", width=100, anchor=CENTER)
        tree.column("precio", width=100, anchor= CENTER)
        tree.column("vida_util", width=100, anchor= CENTER)


        tree.heading("Id", text="Id", anchor=CENTER)
        tree.heading("Cantidad", text="Cantidad", anchor=CENTER)
        tree.heading("clasificacion", text="Clasificacion", anchor=CENTER) 
        tree.heading("precio", text="Precio", anchor=CENTER)
        tree.heading("vida_util", text="Vida util", anchor=CENTER)


        # Creamos los scrollbars
        vsb = ttk.Scrollbar(frame, orient="vertical")
        vsb.pack(side ="right", fill ="y")
        hsb = ttk.Scrollbar(frame, orient="horizontal")
        hsb.pack(side ="bottom", fill ="x")
        tree.config(height = 23, yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        vsb.config(command=tree.yview)
        hsb.config(command=tree.xview)
        tree.pack(expand=True, fill='both')  # Hacer que el Treeview se expanda para llenar el frame

        # Llenar el treeview con los datos
        self.dao.borrar_elemento(tree, elemento)





            ###  BOTON 3  ###





    def mostrar_vista_inventario_fabricacion(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()
            # Crear un Treeview 
        tree = ttk.Treeview(frame, columns=(1,2,3,4))
        # Definir las características del treeview
        tree.column('#0', width=0, stretch="no")  # Ocultar la columna "#0"
        tree.column(1, width=80)
        tree.column(2, width=100)
        tree.column(3, width=120)
        tree.column(4, width=40)
        tree.heading(1, text="Id")
        tree.heading(2, text="Nombre")
        tree.heading(3, text="Material")
        tree.heading(4, text="Calidad")     
        tree.pack(expand=True, fill='both')  # Hacer que el Treeview se expanda para llenar el frame
        self.dao.material_fabricacion(tree)







            ###  BOTON 4  ###







    def mostrar_vista_maquina(self, frame):
        for widget in frame.winfo_children():
                widget.destroy()
            # Crear un Treeview 
        tree = ttk.Treeview(frame, columns=(1,2,3,4))
        # Definir las características del treeview
        tree.column('#0', width=0, stretch="no")  # Ocultar la columna "#0"
        tree.column(1, width=80)
        tree.column(2, width=100)
        tree.column(3, width=120)
        tree.column(4, width=40)
        tree.heading(1, text="Id")
        tree.heading(2, text="Marca")
        tree.heading(3, text="Fecha de adquisicion")
        tree.heading(4, text="Ultimo mantenimiento")     
        tree.pack(expand=True, fill='both')  # Hacer que el Treeview se expanda para llenar el frame
        self.dao.mostrar_vista_maquina(tree)
      






            ###  BOTON 3  ###








    def mostrar_vista_revision(self, frame):
            for widget in frame.winfo_children():
                widget.destroy()
            # Crear un Treeview 
            tree = ttk.Treeview(frame, columns=(1,2,3,4))
            # Definir las características del treeview
            tree.column('#0', width=0, stretch="no")  # Ocultar la columna "#0"
            tree.column(1, width=80, anchor=CENTER)
            tree.column(2, width=100, anchor=CENTER)
            tree.column(3, width=120, anchor=CENTER)
            tree.column(4, width=40, anchor=CENTER)
            tree.heading(1, text="Pedido", anchor="center")
            tree.heading(2, text="Revisor", anchor="center")
            tree.heading(3, text="Producto", anchor="center")
            tree.heading(4, text="Aprobacion", anchor="center")
            tree.pack(expand=True, fill='both')  # Hacer que el Treeview se expanda para llenar el frame
            self.dao.mostrar_vista_revision(tree)
      
      


    


    