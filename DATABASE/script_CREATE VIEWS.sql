DROP VIEW IF EXISTS vw_venta;
DROP VIEW IF EXISTS vw_produccion;
DROP VIEW IF EXISTS vw_comercial;
DROP VIEW IF EXISTS vw_disenador;
DROP VIEW IF EXISTS vw_producto;
DROP VIEW IF EXISTS vw_jefe_produccion;
DROP VIEW IF EXISTS vw_operario;
DROP VIEW IF EXISTS vw_recepcion;
DROP VIEW IF EXISTS vw_maquina;
DROP VIEW IF EXISTS vw_material;
DROP VIEW IF EXISTS vw_inventario_fabricacion;
DROP VIEW IF EXISTS vw_empleado;
DROP VIEW IF EXISTS vw_administrativa;
DROP VIEW IF EXISTS vw_cliente;
DROP VIEW IF EXISTS vw_inventario;
DROP VIEW IF EXISTS vw_atencion;
DROP VIEW IF EXISTS vw_revision;
DROP VIEW IF EXISTS vw_manejo;
DROP VIEW IF EXISTS vw_almacenamiento;
DROP VIEW IF EXISTS vw_infogeneral_administrativa;
DROP VIEW IF EXISTS vw_infogeneral_produccion;




CREATE VIEW vw_venta AS SELECT * FROM venta;
CREATE VIEW vw_produccion AS SELECT * FROM produccion;
CREATE VIEW vw_comercial  AS SELECT * FROM comercial;
CREATE VIEW vw_disenador AS SELECT * FROM disenador;
CREATE VIEW vw_producto AS SELECT * FROM producto;
CREATE VIEW vw_jefe_produccion AS SELECT * FROM jefe_produccion;
CREATE VIEW vw_operario AS SELECT * FROM operario;
CREATE VIEW vw_recepcion AS SELECT * FROM recepcion ;
CREATE VIEW vw_maquina AS SELECT * FROM maquina;
CREATE VIEW vw_material AS SELECT inv_id, mat_nombre, mat_calidad, inv_cantidad, inv_clasificacion, inv_precio, inv_vida_util FROM material JOIN inventario ON(inv_id= mat_inv_id);
CREATE VIEW vw_inventario_fabricacion AS SELECT pro_inv_id_orden_produccion, pro_nombre, mat_nombre, invfa_cantidad_material FROM inventario_fabricacion JOIN producto ON(invfa_pro_inv_id_orden_produccion=pro_inv_id_orden_produccion) JOIN material ON(invfa_mat_inv_id=mat_inv_id);
CREATE VIEW vw_empleado AS SELECT * FROM empleado;
CREATE VIEW vw_administrativa AS SELECT * FROM administrativa;
CREATE VIEW vw_cliente AS SELECT * FROM cliente;
CREATE VIEW vw_inventario AS SELECT * FROM inventario;
CREATE VIEW vw_atencion AS SELECT * FROM atencion;
CREATE VIEW vw_revision AS SELECT * FROM revision;
CREATE VIEW vw_manejo AS SELECT * FROM manejo;
CREATE VIEW vw_almacenamiento AS SELECT * FROM almacenamiento;

CREATE VIEW vw_infogeneral_administrativa AS
	SELECT emp_cedula, emp_nombre, emp_edad, emp_genero, emp_telefono FROM empleado
		WHERE emp_cedula IN(SELECT adm_emp_cedula FROM administrativa);

CREATE VIEW vw_infogeneral_produccion AS
	SELECT emp_cedula, emp_nombre, emp_edad, emp_genero, emp_telefono FROM empleado
		WHERE emp_cedula IN(SELECT prd_emp_cedula FROM produccion);
