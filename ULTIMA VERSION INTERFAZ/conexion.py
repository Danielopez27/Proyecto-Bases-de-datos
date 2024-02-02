from tkinter import *
from tkinter.tix import Tree 
import mysql.connector
from mysql.connector import Error

class DAO():

    def __init__(self, myUser, myPassword):
        try:
            self.conexion = mysql.connector.connect(
                host = "localhost",
                port = 3306,
                user = myUser,
                password = myPassword,
                db = "servioffset"
                )

        except Error as ex:
            print("Error durante la conexión: ", ex)   
        
    



    def cerrar_conexion(self):
        self.conexion.close()








# ---------------------------------------------- RECEPCION ----------------------------------------------

        




    
    def clientes_mas_ventas(self, tree):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor() 
                cursor.callproc("sp_clienteMes")
                    
                for resultado in cursor.stored_results():
                    detalles = resultado.fetchall()

                # Llenar el treeview con los datos
                for detalle in detalles:
                    if len(detalle) >= 1:
                        tree.insert('', 'end', text=detalle[0])

                # Actualizar el Treeview
                tree.update_idletasks()

                return detalles

            except Error as ex:
                print("Error en la conexion: ", ex)
            

    
    def informacion_operario(self, tree):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                cursor.callproc("sp_proyectarVistaOperario")
                resultados = cursor.stored_results()

                for resultado in resultados:
                    detalles = resultado.fetchall()

                # Llenar el treeview con los datos
                for detalle in detalles:
                    if len(detalle) >= 3:
                        tree.insert('', 'end', text=detalle[0], values=(detalle[1], detalle[2]))


                # Actualizar el Treeview
                tree.update_idletasks()

                return detalles

            except Error as ex:
                print("Error en la conexion: ", ex)

    
    def ultimos_operarios_ingresados(self, tree):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                cursor.callproc("sp_MostrarUltimosOperarios")
                resultados = cursor.stored_results()

                for resultado in resultados:
                    detalles = resultado.fetchall()

                # Llenar el treeview con los datos
                for detalle in detalles:
                    if len(detalle) >= 5:
                        tree.insert('', 'end', values=(detalle[0], detalle[1], detalle[2], detalle[3], detalle[4]))

                # Actualizar el Treeview
                tree.update_idletasks()

                return detalles

            except Error as ex:
                print("Error en la conexion: ", ex)





    def cantidad_de_atenciones(self, tree):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                cursor.callproc("sp_verOrdenRecepcionistasMasAtendidos")
                resultados = cursor.stored_results()

                for resultado in resultados:
                    detalles = resultado.fetchall()

                # Llenar el treeview con los datos
                for detalle in detalles:
                    if len(detalle) >= 2:
                        tree.insert('', 'end', values=(detalle[0], detalle[1]))

                # Actualizar el Treeview
                tree.update_idletasks()

                return detalles

            except Error as ex:
                print("Error en la conexion: ", ex)






    
    def compra_por_cliente(self, cedula):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                cursor.callproc("sp_verComprasPorCliente", [str(cedula)])  # Asegúrate de que cedula esté en una lista
                resultados = cursor.stored_results()

                for resultado in resultados:
                    detalles = resultado.fetchall()

                return detalles

            except Error as ex:
                print("Error en la conexion: ", ex)











    # ---------------------------------------------- DISEÑADOR ----------------------------------------------
                











    def agregar_disenador(self, cedula, software):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor() 
                cursor.callproc("sp_agregarDisenador", [cedula, software])
                self.conexion.commit()
            except mysql.connector.Error as ex:
                print("Error en la conexion: ", ex)


    def obtener_cedulas_no_presentes(self):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor() 
                cursor.callproc("sp_obtenerCedulasNoPresentes")
                for resultado in cursor.stored_results():
                    cedulas = resultado.fetchall()
                return [cedula[0] for cedula in cedulas]
            except mysql.connector.Error as ex:
                print("Error en la conexion: ", ex)




    

    def informacion_disenador(self, cedula):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                cursor.callproc("sp_obtenerDetallesDisenador", [str(cedula)])  # Asegúrate de que cedula esté en una lista
                resultados = cursor.stored_results()

                for resultado in resultados:
                    detalles = resultado.fetchall()

                return detalles

            except Error as ex:
                print("Error en la conexion: ", ex)





    def actualizar_info_disenador(self, cedula, software):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                cursor.callproc("sp_actualizarInfoDisenador", [str(cedula), software])
                self.conexion.commit()

            except Error as ex:
                print("Error en la conexion: ", ex)

    
    def mostrar_disenador(self):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                cursor.callproc("sp_mostrarDisenador")
                resultados = cursor.stored_results()

                for resultado in resultados:
                    detalles = resultado.fetchall()

                return detalles

            except Error as ex:
                print("Error en la conexion: ", ex)










# ---------------------------------------------- CLIENTE ----------------------------------------------









    

    def compras_del_cliente(self, tree, cedula):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                cursor.callproc("sp_mostrarVentasPorCliente", [str(cedula)])  # Asegúrate de que cedula esté en una lista
                resultados = cursor.stored_results()

                for resultado in resultados:
                    detalles = resultado.fetchall()

                # Llenar el treeview con los datos
                for detalle in detalles:
                    if len(detalle) >= 6:
                        tree.insert('', 'end', values=(detalle[0], detalle[1], detalle[2], detalle[3], detalle[4], detalle[5]))

                # Actualizar el Treeview
                tree.update_idletasks()

                return detalles

            except Error as ex:
                print("Error en la conexion: ", ex)


    
    def mostrar_productos_cliente(self, tree, cedula):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                cursor.callproc("sp_mostrarVistaProductoPorCliente", [str(cedula)])  # Asegúrate de que cedula esté en una lista
                resultados = cursor.stored_results()

                for resultado in resultados:
                    detalles = resultado.fetchall()

                # Llenar el treeview con los datos
                for detalle in detalles:
                    if len(detalle) >= 3:
                        tree.insert('', 'end', values=(detalle[0], detalle[1], detalle[2]))

                # Actualizar el Treeview
                tree.update_idletasks()

                return detalles

            except Error as ex:
                print("Error en la conexion: ", ex)



    def mostrar_tus_comerciales(self, tree, cedula):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                cursor.callproc("sp_comerciales", [str(cedula)])  # Asegúrate de que cedula esté en una lista
                resultados = cursor.stored_results()

                for resultado in resultados:
                    detalles = resultado.fetchall()
                
                # Llenar el treeview con los datos
                for detalle in detalles:
                    if len(detalle) >= 1:
                        tree.insert('', 'end', text=detalle[0])

                # Actualizar el Treeview
                tree.update_idletasks()

                return detalles

            except Error as ex:
                print("Error en la conexion: ", ex)



    def mostrar_tus_recepcionistas(self, tree, cedula):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                cursor.callproc("sp_recepcionistas", [str(cedula)])  # Asegúrate de que cedula esté en una lista
                resultados = cursor.stored_results()

                for resultado in resultados:
                    detalles = resultado.fetchall()
                
                # Llenar el treeview con los datos
                for detalle in detalles:
                    if len(detalle) >= 1:
                        tree.insert('', 'end', text=detalle[0])

                # Actualizar el Treeview
                tree.update_idletasks()

                return detalles

            except Error as ex:
                print("Error en la conexion: ", ex)











# ---------------------------------------------- JEFE PRODUCCION  ----------------------------------------------










    def mostrar_maquinas(self):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                cursor.execute("SELECT * FROM vw_maquina")
                resultados=cursor.fetchall()

                return resultados

            except Error as ex:
                print("Error en la conexion: ", ex)


    def borrar_maquina(self, tree, maquina):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                cursor.callproc("sp_eliminarMaquina", [maquina])
                self.conexion.commit()

                cursor.execute("SELECT * FROM vw_maquina")
                detalles=cursor.fetchall()

                for detalle in detalles:
                    if len(detalle) >= 4:
                        tree.insert('', 'end', values=(detalle[0], detalle[1], detalle[2], detalle[3]))

                # Actualizar el Treeview
                tree.update_idletasks()

            except Error as ex:
                print("Error en la conexion: ", ex)




    def mostrar_productos(self):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                cursor.execute("SELECT * FROM vw_producto")
                resultados=cursor.fetchall()

                return resultados

            except Error as ex:
                print("Error en la conexion: ", ex)

    

    def actualizar_cantidad_producto(self, tree, producto, cantidad):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                cursor.callproc("sp_actualizarMaterial_producto", [producto, cantidad])
                self.conexion.commit()

                cursor.execute("SELECT * FROM vw_inventario_fabricacion")
                detalles=cursor.fetchall()

                for detalle in detalles:
                    if len(detalle) >= 4:
                        tree.insert('', 'end', values=(detalle[0], detalle[1], detalle[2], detalle[3]))

                # Actualizar el Treeview
                tree.update_idletasks()

            except Error as ex:
                print("Error en la conexion: ", ex)



        
    def mostrar_empleados(self):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                cursor.execute("SELECT * FROM vw_empleado")
                resultados=cursor.fetchall()

                return resultados

            except Error as ex:
                print("Error en la conexion: ", ex)

    

    def agregar_empleado(self, tree, cedula, nombre, edad, genero, telefono, horario, sueldo, fecha):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                cursor.callproc("sp_agregarEmpleado", [cedula, nombre, edad, genero, telefono, horario, sueldo, fecha])
                self.conexion.commit()

                cursor.execute("SELECT * FROM vw_empleado")
                detalles=cursor.fetchall()

                for detalle in detalles:
                    if len(detalle) >= 8:
                        tree.insert('', 'end', values=(detalle[0], detalle[1], detalle[2], detalle[3], detalle[4], detalle[5], detalle[6], detalle[7]))

                # Actualizar el Treeview
                tree.update_idletasks()

            except Error as ex:
                print("Error en la conexion: ", ex)



    


    def mostrar_materiales(self):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                cursor.execute("SELECT mat_nombre, mat_calidad FROM vw_material")
                resultados=cursor.fetchall()

                return resultados

            except Error as ex:
                print("Error en la conexion: ", ex)



    def actualizar_material(self, tree, material, cantidad):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                cursor.callproc("sp_actualizarMaterial", [material, cantidad])
                self.conexion.commit()

                cursor.execute("SELECT * FROM vw_material")
                detalles=cursor.fetchall()

                for detalle in detalles:
                    if len(detalle) >= 7:
                        tree.insert('', 'end', values=(detalle[0], detalle[1], detalle[2], detalle[3], detalle[4], detalle[5], detalle[6]))

                # Actualizar el Treeview
                tree.update_idletasks()

            except Error as ex:
                print("Error en la conexion: ", ex)


    

    def mostrar_materiales_id(self):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                cursor.execute("SELECT * FROM vw_material")
                resultados=cursor.fetchall()

                return resultados

            except Error as ex:
                print("Error en la conexion: ", ex)










# ---------------------------------------------- OPERARIO  ----------------------------------------------












    def ejecutar_procedimiento(self, nombre_procedimiento, parametros=None):
            global cursor
            detalles = None
            if self.conexion.is_connected():
                try:
                    cursor = self.conexion.cursor()
                    if parametros:
                        cursor.callproc(nombre_procedimiento, parametros)
                    else:
                        cursor.callproc(nombre_procedimiento)

                    resultados = cursor.stored_results()
                    for resultado in resultados:
                        detalles = resultado.fetchall()

                    # Realizar el commit después de ejecutar el procedimiento almacenado
                    self.conexion.commit()

                except Error as ex:
                    print("Error en la conexión: ", ex)
                

            return detalles

    def construir_tabla(self, frame, resultados):

        # Crear tabla de muestra de datos
        self.tabla = Frame(frame, width=600, height=600, bg='#FFFFFF')
        self.tabla.pack(expand=True, anchor=CENTER)

        lst = resultados
        total_rows = len(lst)
        total_columns = len(lst[0])

        for i in range(total_rows):
            for j in range(total_columns):
                label = Label(frame, fg='blue', borderwidth=1, relief="solid", font=('Arial', 16, 'bold'),
                              anchor="center")

                label.grid(row=i, column=j, ipadx=3, padx=0)
                label.config(text=lst[i][j])






    def mostrar_vista_revision(self, tree):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.callproc("sp_mostrarVistaRevision")
                resultados = cursor.stored_results()

                for resultado in resultados:
                    detalles = resultado.fetchall()

                # Llenar el treeview con los datos
                for detalle in detalles:
                    if len(detalle) >= 4:
                        tree.insert('', 'end', values=(detalle[0], detalle[1], detalle[2], detalle[3]))

                # Actualizar el Treeview
                tree.update_idletasks()

                return detalles

            except Error as ex:
                print("Error en la conexión: ", ex)



    def mostrar_vista_maquina(self, tree):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.callproc("sp_mostrarVistaMaquina")
                resultados = cursor.stored_results()

                for resultado in resultados:
                    detalles = resultado.fetchall()

                # Llenar el treeview con los datos
                for detalle in detalles:
                    if len(detalle) >= 4:
                        tree.insert('', 'end', values=(detalle[0], detalle[1], detalle[2], detalle[3]))

                # Actualizar el Treeview
                tree.update_idletasks()

                return detalles

            except Error as ex:
                print("Error en la conexión: ", ex)



    def material_fabricacion(self, tree):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.callproc("sp_mostrarVistaInventarioFabricacion")
                resultados = cursor.stored_results()

                for resultado in resultados:
                    detalles = resultado.fetchall()

                # Llenar el treeview con los datos
                for detalle in detalles:
                    if len(detalle) >= 4:
                        tree.insert('', 'end', values=(detalle[0], detalle[1], detalle[2], detalle[3]))

                # Actualizar el Treeview
                tree.update_idletasks()

                return detalles

            except Error as ex:
                print("Error en la conexión: ", ex)





            ###  BOTON 2  ###


    def mostrar_elementos_inventario(self):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                cursor.execute("select * FROM vw_inventario WHERE inv_id NOT IN (SELECT pro_inv_id_orden_produccion FROM vw_producto)")
                resultados=cursor.fetchall()

                return resultados
                

            except Error as ex:
                print("Error en la conexion: ", ex)




    def borrar_elemento(self, tree, elemento):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.callproc("sp_eliminarInventario", [elemento])
                self.conexion.commit()

                cursor.execute("SELECT * FROM vw_inventario")
                detalles=cursor.fetchall()

                # Llenar el treeview con los datos
                for detalle in detalles:
                    if len(detalle) >= 5:
                        tree.insert('', 'end', values=(detalle[0], detalle[1], detalle[2], detalle[3], detalle[4]))

                # Actualizar el Treeview
                tree.update_idletasks()

                return detalles

            except Error as ex:
                print("Error en la conexión: ", ex)




    def cantidad_de_material(self, tree, material, calidad):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.callproc("sp_cantidadMaterial", [material, calidad])

                resultados = cursor.stored_results()

                for resultado in resultados:
                    detalles = resultado.fetchall()

                # Llenar el treeview con los datos
                for detalle in detalles:
                    if len(detalle) >= 1:
                        tree.insert('', 'end', values=(detalle[0]))

                # Actualizar el Treeview
                tree.update_idletasks()

                return detalles

            except Error as ex:
                print("Error en la conexión: ", ex)

