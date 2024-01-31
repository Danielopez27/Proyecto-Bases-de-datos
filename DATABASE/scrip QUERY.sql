-- USE servioffset;
/*		
		-- Numero total clientes en el mes --
SELECT DISTINCT COUNT(ven_cli_cedula) FROM venta 
	WHERE DATE_ADD(NOW(), INTERVAL -1 MONTH) < ven_fecha_de_venta;

		-- Maquinas ordenadas por mantenimiento --
SELECT maq_inv_id, maq_fecha_ultimo_mantenimiento FROM maquina
	ORDER BY maq_fecha_ultimo_mantenimiento ASC; 

		-- Material mas caro del momento --
SELECT mat_inv_id, mat_nombre FROM inventario JOIN material ON(mat_inv_id=inv_id)
	WHERE inv_precio IN(SELECT MAX(inv_precio) FROM  
    material JOIN inventario ON(mat_inv_id=inv_id));

    		-- Sueldo del comercial --
SELECT com_porcentaje_comision * emp_sueldo/100 AS sueldo_total FROM 
	comercial JOIN administrativa ON(com_adm_emp_cedula=adm_emp_cedula)
	JOIN empleado ON(adm_emp_cedula=emp_cedula);

			-- Comprador del mes --
SELECT cli_cedula, cli_nombre FROM
	(SELECT cli_cedula, cli_nombre, COUNT(ven_fecha_de_venta) AS cantidad_compras FROM venta JOIN cliente ON(cli_cedula=ven_cli_cedula)
		WHERE DATE_ADD(NOW(), INTERVAL -1 MONTH) < ven_fecha_de_venta
		GROUP BY cli_cedula)t1
	WHERE cantidad_compras IN
		(SELECT MAX(cantidad_compras) FROM 
        (SELECT COUNT(ven_fecha_de_venta) AS cantidad_compras FROM venta JOIN cliente ON(cli_cedula=ven_cli_cedula)
		WHERE DATE_ADD(NOW(), INTERVAL -1 MONTH) < ven_fecha_de_venta
		GROUP BY cli_cedula)t2);

		-- Comercial con mas ventas --
SELECT emp_cedula, emp_nombre FROM empleado WHERE emp_cedula IN	
    (SELECT com_adm_emp_cedula FROM 
		(SELECT com_adm_emp_cedula, COUNT(ven_fecha_de_venta) AS cantidad_ventas FROM venta JOIN comercial ON(ven_com_adm_emp_cedula=com_adm_emp_cedula)
			GROUP BY com_adm_emp_cedula)T1
		WHERE cantidad_ventas IN
			(SELECT MAX(cantidad_ventas) FROM
				(SELECT com_adm_emp_cedula, COUNT(ven_fecha_de_venta) AS cantidad_ventas FROM venta JOIN comercial ON(ven_com_adm_emp_cedula=com_adm_emp_cedula)
					GROUP BY com_adm_emp_cedula)T2));


			-- Ventas aprovadas ultimo mes --
SELECT COUNT(ven_fecha_de_venta) AS cantidad_ventas FROM venta 
	WHERE ven_aprovacion='T' AND DATE_ADD(NOW(), INTERVAL -1 MONTH) < ven_fecha_de_venta;


		
			-- Ventas aprovadas y Negadas --
SELECT COUNT(ven_fecha_de_venta) AS ventas_aprovadas_y_negadas FROM venta 
	GROUP BY ven_aprovacion='T', ven_aprovacion='F';

			-- Sotfware más usado --
SELECT dis_sotfware FROM 
	(SELECT dis_sotfware, COUNT(dis_sotfware) AS veces_usado FROM disenador
		GROUP BY dis_sotfware) T1
	WHERE veces_usado IN
		(SELECT MAX(veces_usado) FROM
			(SELECT dis_sotfware, COUNT(dis_sotfware) AS veces_usado FROM disenador
				GROUP BY dis_sotfware) T2);

			-- Ordenar material por vida util --
SELECT mat_nombre, inv_vida_util FROM inventario JOIN material ON(inv_id = mat_inv_id)
	ORDER BY inv_vida_util ASC;


		-- Numero total clientes en el mes --
SELECT DISTINCT COUNT(ven_cli_cedula) FROM venta 
	WHERE DATE_ADD(NOW(), INTERVAL -1 MONTH) < ven_fecha_de_venta;


			-- Ordenar material por vida util --
SELECT mat_nombre, inv_vida_util FROM inventario JOIN material ON(inv_id = mat_inv_id)
	ORDER BY inv_vida_util ASC;
*/



/* 				CREACION DE INDICES
CREATE INDEX ind_fecha_venta ON venta(ven_fecha_de_venta);
CREATE UNIQUE INDEX ind_inv_id ON inventario(inv_id);
CREATE UNIQUE INDEX ind_orden_produccion ON producto(pro_inv_id_orden_produccion) ;
CREATE UNIQUE INDEX ind_cedula_empleado ON empleado(emp_cedula);
CREATE UNIQUE INDEX ind_cedula_cliente ON cliente(cli_cedula);
*/

    

