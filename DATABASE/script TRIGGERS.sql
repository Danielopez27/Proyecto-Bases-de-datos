-- USE servioffset;
DROP TRIGGER IF EXISTS tg_insertar_disenador;
DROP TRIGGER IF EXISTS tg_eliminar_maquina_manejo;
DROP TRIGGER IF EXISTS tg_eliminar_inventario;
DROP TRIGGER IF EXISTS tg_eliminar_material;
DROP TRIGGER IF EXISTS tg_insertar_produccion;
DROP TRIGGER IF EXISTS tg_eliminar_empleado;
DROP TRIGGER IF EXISTS tg_eliminar_produccion;






DELIMITER $$
CREATE TRIGGER tg_insertar_disenador BEFORE INSERT ON disenador FOR EACH ROW
BEGIN

    INSERT INTO produccion VALUES(NEW.dis_prd_emp_cedula, "creacion");

END;
$$
DELIMITER ;




DELIMITER $$
CREATE TRIGGER tg_eliminar_maquina_manejo BEFORE DELETE ON maquina FOR EACH ROW
BEGIN

    DELETE FROM manejo WHERE man_maq_inv_id=OLD.maq_inv_id;

END;
$$
DELIMITER ;




DELIMITER $$
CREATE TRIGGER tg_eliminar_inventario BEFORE DELETE ON inventario FOR EACH ROW
BEGIN

    DELETE FROM material WHERE mat_inv_id=OLD.inv_id;
    DELETE FROM maquina WHERE maq_inv_id=OLD.inv_id;

END;
$$
DELIMITER ;


DELIMITER $$
CREATE TRIGGER tg_eliminar_material BEFORE DELETE ON material FOR EACH ROW
BEGIN

	DELETE FROM inventario_fabricacion WHERE invfa_mat_inv_id = OLD.mat_inv_id;
    DELETE FROM almacenamiento WHERE alm_mat_inv_id = OLD.mat_inv_id;

END;
$$
DELIMITER ;


DELIMITER $$
CREATE TRIGGER tg_eliminar_empleado BEFORE DELETE ON empleado FOR EACH ROW
BEGIN

	DELETE FROM produccion WHERE prd_emp_cedula = OLD.emp_cedula;

END;
$$
DELIMITER ;


DELIMITER $$
CREATE TRIGGER tg_eliminar_produccion BEFORE DELETE ON produccion FOR EACH ROW
BEGIN

	DELETE FROM disenador WHERE dis_prd_emp_cedula = OLD.prd_emp_cedula;

END;
$$
DELIMITER ;



