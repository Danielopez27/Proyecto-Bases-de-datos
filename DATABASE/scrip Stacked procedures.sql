
DROP PROCEDURE IF EXISTS sp_cantidadMaterial;

DELIMITER $$

CREATE PROCEDURE sp_cantidadMaterial(IN nombreMaterial VARCHAR(50), IN calidad VARCHAR(50))
BEGIN
	DECLARE cantidad INTEGER;
	
	SELECT inv_cantidad INTO cantidad FROM inventario JOIN material ON(inv_id=mat_inv_id)
		WHERE nombreMaterial=mat_nombre AND calidad = mat_calidad;
	
    SELECT cantidad;

END
$$

DELIMITER ;





DROP PROCEDURE IF EXISTS sp_clienteMes;
DELIMITER $$

CREATE PROCEDURE sp_clienteMes()
BEGIN
	DECLARE cliente VARCHAR(50);

	SELECT cli_nombre INTO cliente FROM
	(SELECT cli_cedula, cli_nombre, COUNT(ven_fecha_de_venta) AS cantidad_compras FROM venta JOIN cliente ON(cli_cedula=ven_cli_cedula)
		WHERE DATE_ADD(NOW(), INTERVAL -1 MONTH) < ven_fecha_de_venta
		GROUP BY cli_cedula)t1
	WHERE cantidad_compras IN
		(SELECT MAX(cantidad_compras) FROM 
        (SELECT COUNT(ven_fecha_de_venta) AS cantidad_compras FROM venta JOIN cliente ON(cli_cedula=ven_cli_cedula)
		WHERE DATE_ADD(NOW(), INTERVAL -1 MONTH) < ven_fecha_de_venta
		GROUP BY cli_cedula)t2);
        
        SELECT cliente;
END
$$

DELIMITER ;





DROP PROCEDURE IF EXISTS sp_mejorCliente;
DELIMITER $$

CREATE PROCEDURE sp_mejorcliente(IN idComercial INT)
BEGIN
	DECLARE cliente VARCHAR(50);

	SELECT cli_nombre INTO cliente FROM 
		(SELECT cli_cedula, cli_nombre, COUNT(ven_fecha_de_venta) AS cantidad_ventas FROM comercial JOIN venta ON(com_adm_emp_cedula = ven_com_adm_emp_cedula) JOIN cliente ON(cli_cedula = ven_cli_cedula)
            WHERE com_adm_emp_cedula = idComercial
            GROUP BY cli_cedula)t1
		WHERE cantidad_ventas IN
			(SELECT MAX(cantidad_ventas) AS mayor FROM 
				(SELECT COUNT(ven_fecha_de_venta) AS cantidad_ventas FROM comercial JOIN venta ON(com_adm_emp_cedula = ven_com_adm_emp_cedula) JOIN cliente ON(cli_cedula = ven_cli_cedula)
				WHERE com_adm_emp_cedula = idComercial
				GROUP BY cli_cedula)t2);
    
    SELECT cliente;
END
$$

DELIMITER ;



DROP PROCEDURE IF EXISTS sp_actualizarMaterial;
DELIMITER //

CREATE PROCEDURE sp_actualizarMaterial(
    IN p_mat_inv_id INTEGER,
    IN p_cantidad_comprada INTEGER
)
BEGIN
    -- Actualizar la cantidad de material comprada
    UPDATE inventario
    SET inv_cantidad = p_cantidad_comprada
    WHERE inv_id = p_mat_inv_id;
END //

DELIMITER ;



DROP PROCEDURE IF EXISTS sp_actualizarMaterial_producto;
DELIMITER $$

CREATE PROCEDURE sp_actualizarMaterial_producto(IN idProducto INT, IN nuevaCantidad INT)
BEGIN

	UPDATE inventario_fabricacion SET invfa_cantidad_material = nuevaCantidad 
		WHERE invfa_pro_inv_id_orden_produccion=idProducto;

END
$$

DELIMITER ;




DROP PROCEDURE IF EXISTS sp_productoMasVendido;
DELIMITER $$

CREATE PROCEDURE sp_productoMasVendido()
BEGIN
	
    SELECT pro_inv_id_orden_produccion, pro_nombre FROM 
		(SELECT pro_inv_id_orden_produccion, pro_nombre, COUNT(ven_fecha_de_venta) AS veces_vendido FROM producto JOIN venta ON(pro_inv_id_orden_produccion=ven_pro_inv_id_orden_produccion)
				GROUP BY pro_inv_id_orden_produccion)t1
		WHERE veces_vendido IN
			(SELECT MAX(veces_vendido) FROM 
				(SELECT COUNT(ven_fecha_de_venta) AS veces_vendido FROM producto JOIN venta ON(pro_inv_id_orden_produccion=ven_pro_inv_id_orden_produccion)
					GROUP BY pro_inv_id_orden_produccion)t2);
    
END
$$

DELIMITER ;




DROP PROCEDURE IF EXISTS sp_comerciales;
DELIMITER $$

CREATE PROCEDURE sp_comerciales(IN cedulaCliente INT)
BEGIN
	SELECT DISTINCT emp_nombre FROM empleado JOIN venta ON(emp_cedula=ven_com_adm_emp_cedula) JOIN cliente ON(cli_cedula=ven_cli_cedula)
		WHERE ven_cli_cedula=cedulaCliente;
END
$$

DELIMITER ;




DROP PROCEDURE IF EXISTS sp_recepcionistas;
DELIMITER $$

CREATE PROCEDURE sp_recepcionistas(IN cedulaCliente INT)
BEGIN
	SELECT DISTINCT emp_nombre FROM atencion JOIN empleado ON(ate_rec_adm_emp_cedula=emp_cedula) JOIN cliente ON(cli_cedula=ate_cli_cedula)
		WHERE ate_cli_cedula=cedulaCliente;
END
$$

DELIMITER ;



DROP PROCEDURE IF EXISTS sp_proyectarVistaOperario;
DELIMITER //

CREATE PROCEDURE sp_proyectarVistaOperario()
BEGIN
    SELECT *
    FROM vw_operario;
END //

DELIMITER ;


DROP PROCEDURE IF EXISTS sp_MostrarUltimosOperarios;

DELIMITER //
CREATE PROCEDURE sp_MostrarUltimosOperarios()
BEGIN
    SELECT  emp_nombre  AS Nombre,emp_cedula AS Cedula, emp_telefono AS Telefono,  emp_sueldo AS Sueldo, emp_fecha_ingreso AS Fecha_ingreso
    FROM empleado
    WHERE emp_cedula IN (
        SELECT ope_prd_emp_cedula
        FROM operario
    )ORDER BY emp_fecha_ingreso DESC LIMIT 5;
END //
DELIMITER ;


DROP PROCEDURE IF EXISTS sp_verOrdenRecepcionistasMasAtendidos;
DELIMITER //

CREATE PROCEDURE sp_verOrdenRecepcionistasMasAtendidos()
BEGIN
    -- Seleccionar los recepcionistas y contar el número de atenciones
    SELECT rec_adm_emp_cedula, COUNT(*) AS total_atenciones
    FROM vw_recepcion
    GROUP BY rec_adm_emp_cedula
    ORDER BY total_atenciones DESC;
END //

DELIMITER ;


DROP PROCEDURE IF EXISTS sp_verComprasPorCliente;
DELIMITER //

CREATE PROCEDURE sp_verComprasPorCliente(IN p_cli_cedula INTEGER)
BEGIN
    -- Seleccionar las compras del cliente proporcionado
    SELECT *
    FROM venta
    WHERE ven_cli_cedula = p_cli_cedula;
END //

DELIMITER ;


DROP PROCEDURE IF EXISTS sp_agregarDisenador;
DELIMITER //

CREATE PROCEDURE sp_agregarDisenador(
    IN p_cedula INTEGER,
    IN p_software CHAR(45)
)
BEGIN
    -- Insertar en la tabla de disenador
    INSERT INTO disenador (dis_prd_emp_cedula, dis_sotfware)
    VALUES (p_cedula, p_software);
END //

DELIMITER ;




DROP PROCEDURE IF EXISTS sp_obtenerDetallesDisenador;
DELIMITER //

CREATE PROCEDURE sp_obtenerDetallesDisenador(
    IN p_dis_prd_emp_cedula INT
)
BEGIN
    SELECT d.dis_prd_emp_cedula AS Cedula, 
           e.emp_nombre AS Nombre, d.dis_sotfware AS Software, e.emp_edad AS Edad, e.emp_genero AS Genero,
           e.emp_telefono AS Telefono, e.emp_horario AS Horario, 
           e.emp_sueldo AS Sueldo, e.emp_fecha_ingreso AS Fecha_ingreso
    FROM disenador d
    JOIN empleado e ON d.dis_prd_emp_cedula = e.emp_cedula
    WHERE d.dis_prd_emp_cedula = p_dis_prd_emp_cedula;
END //

DELIMITER ;



DROP PROCEDURE IF EXISTS sp_actualizarInfoDisenador;
DELIMITER &&

CREATE PROCEDURE sp_actualizarInfoDisenador(
    IN p_dis_prd_emp_cedula INTEGER,
    IN p_dis_sotfware CHAR(45)
)
BEGIN
    UPDATE disenador
    SET dis_sotfware = p_dis_sotfware
    WHERE dis_prd_emp_cedula = p_dis_prd_emp_cedula;
END &&

DELIMITER ;



DROP PROCEDURE IF EXISTS sp_mostrarVentasPorCliente;
DELIMITER //

CREATE PROCEDURE sp_mostrarVentasPorCliente(IN p_cli_cedula INTEGER)
BEGIN
    -- Seleccionar todos los registros de la vista vw_venta para un solo cliente
    SELECT *
    FROM vw_venta
    WHERE ven_cli_cedula = p_cli_cedula;
END //

DELIMITER ;




DROP PROCEDURE IF EXISTS sp_mostrarVistaProductoPorCliente;
DELIMITER //

CREATE PROCEDURE sp_mostrarVistaProductoPorCliente(IN p_cli_cedula INTEGER)
BEGIN
    -- Seleccionar los registros de la vista vw_producto filtrados por el cliente
    SELECT *
    FROM vw_producto
    WHERE pro_inv_id_orden_produccion IN (
        SELECT ven_pro_inv_id_orden_produccion
        FROM venta
        WHERE ven_cli_cedula = p_cli_cedula
    );
END //

DELIMITER ;



DROP PROCEDURE IF EXISTS sp_mostrarVistaMaquina;
DELIMITER //

CREATE PROCEDURE sp_mostrarVistaMaquina()
BEGIN
    -- Seleccionar todos los registros de la vista vw_maquina
    SELECT *
    FROM vw_maquina;
END //

DELIMITER ;




DROP PROCEDURE IF EXISTS sp_mostrarVistaInventarioFabricacion;

DELIMITER //
CREATE PROCEDURE sp_mostrarVistaInventarioFabricacion()
BEGIN
    -- Seleccionar todos los registros de la vista vw_inventario_fabricacion
    SELECT invfa_mat_inv_id, pro_nombre, mat_nombre, mat_calidad  FROM inventario_fabricacion 
    join material on invfa_mat_inv_id=mat_inv_id 
    join producto on pro_inv_id_orden_produccion=invfa_pro_inv_id_orden_produccion;
END //
DELIMITER ;


-- creación de procedimiento almacenado donde muestre una vista de la tabla revisa
DROP PROCEDURE IF EXISTS sp_mostrarVistaRevision;
DELIMITER //
CREATE PROCEDURE sp_mostrarVistaRevision()
BEGIN
    -- Seleccionar todos los registros de la vista vw_revision
	SELECT rev_pro_inv_id_orden_produccion AS Nro_pedido, emp_nombre AS revisor, pro_nombre AS producto, rev_aprovacion AS aprobacion
    FROM vw_revision join vw_empleado on rev_jef_prd_emp_cedula=  emp_cedula join producto on rev_pro_inv_id_orden_produccion=pro_inv_id_orden_produccion;
END //
DELIMITER ;




DROP PROCEDURE IF EXISTS sp_eliminarMaquina;
DELIMITER //
CREATE PROCEDURE sp_eliminarMaquina(
    IN p_maquina_id INT
)
BEGIN

    -- Eliminar el registro en la tabla maquina
    DELETE FROM maquina WHERE maq_inv_id = p_maquina_id;

END
//

DELIMITER ;



DROP PROCEDURE IF EXISTS sp_mostrarDisenador;
DELIMITER &&

CREATE PROCEDURE sp_mostrarDisenador()
BEGIN
    SELECT * FROM disenador;
END &&

DELIMITER ;





DROP PROCEDURE IF EXISTS sp_agregarEmpleado;
DELIMITER //

CREATE PROCEDURE sp_agregarEmpleado(
    IN p_emp_cedula INT,
    IN p_emp_nombre CHAR(45),
    IN p_emp_edad TINYINT,
    IN p_emp_genero CHAR(45),
    IN p_emp_telefono CHAR(45),
    IN p_emp_horario TIME,
    IN p_emp_sueldo INT,
    IN p_emp_fecha_ingreso DATE
)
BEGIN
    DECLARE emp_exist INT DEFAULT 0;

    SELECT COUNT(*) INTO emp_exist FROM empleado WHERE emp_cedula = p_emp_cedula;

    IF emp_exist = 0 THEN
        INSERT INTO empleado (emp_cedula, emp_nombre, emp_edad, emp_genero, emp_telefono, emp_horario, emp_sueldo, emp_fecha_ingreso)
        VALUES (p_emp_cedula, p_emp_nombre, p_emp_edad, p_emp_genero, p_emp_telefono, p_emp_horario, p_emp_sueldo, p_emp_fecha_ingreso);
    ELSE
        SELECT 'El empleado ya existe' As Agregar_empleado;
    END IF;
END //

DELIMITER ;




-- Creación de procedimiento almacenado para verificar la cedulas 
DROP PROCEDURE IF EXISTS sp_obtenerCedulasNoPresentes;
DELIMITER //

CREATE PROCEDURE sp_obtenerCedulasNoPresentes()
BEGIN
    SELECT emp_cedula
    FROM empleado
    WHERE emp_cedula NOT IN (SELECT adm_emp_cedula FROM administrativa)
    AND emp_cedula NOT IN (SELECT dis_prd_emp_cedula FROM disenador)
    AND emp_cedula NOT IN (SELECT prd_emp_cedula FROM produccion);
END //

DELIMITER ;



DROP PROCEDURE IF EXISTS sp_eliminarInventario;
--  Creación de procedimiento almacenado para eliminar un producto de inventario
DELIMITER //

CREATE PROCEDURE sp_eliminarInventario(IN p_inv_id INT)
BEGIN
    DELETE FROM inventario WHERE inv_id = p_inv_id;
END //

DELIMITER ;



DROP PROCEDURE IF EXISTS sp_obtenerProductosNoPresentes;
DELIMITER //

CREATE PROCEDURE sp_obtenerProductosNoPresentes()
BEGIN
    SELECT inv_id, inv_cantidad FROM inventario
    WHERE inv_id NOT IN (SELECT pro_inv_id_orden_produccion FROM producto);
END //

DELIMITER ;


