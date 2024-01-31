DROP USER IF EXISTS 'recepcion'@'localhost';
DROP USER IF EXISTS 'disenador'@'localhost';
DROP USER IF EXISTS 'comercial'@'localhost';
DROP USER IF EXISTS 'cliente'@'localhost';
DROP USER IF EXISTS 'jefe_produccion'@'localhost';
DROP USER IF EXISTS 'operario'@'localhost';

CREATE USER 'recepcion'@'localhost' IDENTIFIED BY '11111';
CREATE USER 'disenador'@'localhost' IDENTIFIED BY '11111';
CREATE USER 'comercial'@'localhost' IDENTIFIED BY '11111';
CREATE USER 'cliente'@'localhost' IDENTIFIED BY '11111';
CREATE USER 'jefe_produccion'@'localhost' IDENTIFIED BY '11111';
CREATE USER 'operario'@'localhost' IDENTIFIED BY '11111';


			-- RECEPCION -- 
GRANT SELECT ON vw_venta TO 'recepcion'@'localhost';
GRANT SELECT ON vw_produccion TO 'recepcion'@'localhost';
GRANT SELECT ON vw_comercial TO 'recepcion'@'localhost';
GRANT SELECT ON vw_producto TO 'recepcion'@'localhost';
GRANT SELECT ON vw_jefe_produccion TO 'recepcion'@'localhost';
GRANT SELECT ON vw_material TO 'recepcion'@'localhost';
GRANT SELECT ON vw_revision TO 'recepcion'@'localhost';
GRANT SELECT ON vw_infogeneral_administrativa TO 'recepcion'@'localhost';

GRANT INSERT, DELETE, UPDATE, DELETE ON vw_operario TO 'recepcion'@'localhost';
GRANT INSERT, DELETE, UPDATE, DELETE ON vw_recepcion TO 'recepcion'@'localhost';
GRANT INSERT, DELETE, UPDATE, DELETE ON vw_empleado TO 'recepcion'@'localhost';
GRANT INSERT, DELETE, UPDATE, DELETE ON vw_administrativa TO 'recepcion'@'localhost';
GRANT INSERT, DELETE, UPDATE, DELETE ON vw_cliente TO 'recepcion'@'localhost';
GRANT INSERT, DELETE, UPDATE, DELETE ON vw_atencion TO 'recepcion'@'localhost';


GRANT EXECUTE ON PROCEDURE sp_clienteMes TO 'recepcion'@'localhost';
GRANT EXECUTE ON PROCEDURE sp_proyectarVistaOperario TO 'recepcion'@'localhost';
GRANT EXECUTE ON PROCEDURE sp_MostrarUltimosOperarios TO 'recepcion'@'localhost';
GRANT EXECUTE ON PROCEDURE sp_verOrdenRecepcionistasMasAtendidos TO 'recepcion'@'localhost';
GRANT EXECUTE ON PROCEDURE sp_verComprasPorCliente TO 'recepcion'@'localhost';





			-- DISENADOR --
GRANT SELECT ON vw_produccion TO 'disenador'@'localhost';
GRANT SELECT ON vw_material TO 'disenador'@'localhost';
GRANT SELECT ON vw_inventario_fabricacion TO 'disenador'@'localhost';
GRANT SELECT ON vw_cliente TO 'disenador'@'localhost';
GRANT SELECT ON vw_inventario TO 'disenador'@'localhost';
GRANT SELECT ON vw_revision TO 'disenador'@'localhost';
GRANT SELECT ON vw_infogeneral_produccion TO 'disenador'@'localhost';

GRANT INSERT, SELECT, UPDATE, DELETE ON vw_disenador TO 'disenador'@'localhost';
GRANT INSERT, SELECT, UPDATE, DELETE ON vw_producto TO 'disenador'@'localhost';
GRANT INSERT, SELECT, UPDATE, DELETE ON vw_infogeneral_produccion TO 'disenador'@'localhost';

GRANT EXECUTE ON PROCEDURE sp_agregarDisenador TO 'disenador'@'localhost';
GRANT EXECUTE ON PROCEDURE sp_obtenerDetallesDisenador TO 'disenador'@'localhost';
GRANT EXECUTE ON PROCEDURE sp_actualizarInfoDisenador TO 'disenador'@'localhost';
GRANT EXECUTE ON PROCEDURE sp_mostrarDisenador TO 'disenador'@'localhost';
GRANT EXECUTE ON PROCEDURE sp_obtenerCedulasNoPresentes TO 'disenador'@'localhost';






			-- COMERCIAL --
GRANT SELECT ON vw_produccion TO 'comercial'@'localhost';
GRANT SELECT ON vw_disenador TO 'comercial'@'localhost';
GRANT SELECT ON vw_producto TO 'comercial'@'localhost';
GRANT SELECT ON vw_jefe_produccion TO 'comercial'@'localhost';
GRANT SELECT ON vw_material TO 'comercial'@'localhost';
GRANT SELECT ON vw_inventario_fabricacion TO 'comercial'@'localhost';
GRANT SELECT ON vw_administrativa TO 'comercial'@'localhost';
GRANT SELECT ON vw_inventario TO 'comercial'@'localhost';
GRANT SELECT ON vw_atencion TO 'comercial'@'localhost';
GRANT SELECT ON vw_revision TO 'comercial'@'localhost';
GRANT SELECT ON vw_infogeneral_administrativa TO 'comercial'@'localhost';

GRANT INSERT, SELECT, UPDATE, DELETE ON vw_venta TO 'comercial'@'localhost';
GRANT INSERT, SELECT, UPDATE, DELETE ON vw_comercial TO 'comercial'@'localhost';

GRANT SELECT, UPDATE ON vw_recepcion TO 'comercial'@'localhost';
GRANT SELECT, UPDATE ON vw_cliente TO 'comercial'@'localhost';


			-- CLIENTE --
GRANT SELECT ON vw_produccion TO 'cliente'@'localhost';
GRANT SELECT ON vw_disenador TO 'cliente'@'localhost';
GRANT SELECT ON vw_producto TO 'cliente'@'localhost';
GRANT SELECT ON vw_jefe_produccion TO 'cliente'@'localhost';
GRANT SELECT ON vw_material TO 'cliente'@'localhost';
GRANT SELECT ON vw_inventario_fabricacion TO 'cliente'@'localhost';
GRANT SELECT ON vw_administrativa TO 'cliente'@'localhost';
GRANT SELECT ON vw_inventario TO 'cliente'@'localhost';
GRANT SELECT ON vw_atencion TO 'cliente'@'localhost';
GRANT SELECT ON vw_revision TO 'cliente'@'localhost';


GRANT INSERT, SELECT, UPDATE, DELETE ON vw_venta TO 'cliente'@'localhost';
GRANT INSERT, SELECT, UPDATE, DELETE ON vw_comercial TO 'cliente'@'localhost';


GRANT SELECT, UPDATE ON vw_venta TO 'cliente'@'localhost';
GRANT SELECT, UPDATE ON vw_produccion TO 'cliente'@'localhost';
GRANT SELECT, UPDATE ON vw_producto TO 'cliente'@'localhost';
GRANT SELECT, UPDATE ON vw_jefe_produccion TO 'cliente'@'localhost';


GRANT EXECUTE ON PROCEDURE sp_mostrarVentasPorCliente TO 'cliente'@'localhost';
GRANT EXECUTE ON PROCEDURE sp_mostrarVistaProductoPorCliente TO 'cliente'@'localhost';
GRANT EXECUTE ON PROCEDURE sp_comerciales TO 'cliente'@'localhost';
GRANT EXECUTE ON PROCEDURE sp_recepcionistas TO 'cliente'@'localhost';









			-- JEFE_PRODUCCION ---------------------------------------------------------------
            
GRANT INSERT, SELECT, UPDATE, DELETE ON vw_produccion TO 'jefe_produccion'@'localhost';
GRANT INSERT, SELECT, UPDATE, DELETE ON vw_jefe_produccion TO 'jefe_produccion'@'localhost';
GRANT INSERT, SELECT, UPDATE, DELETE ON vw_maquina TO 'jefe_produccion'@'localhost';
GRANT INSERT, SELECT, UPDATE, DELETE ON vw_material TO 'jefe_produccion'@'localhost';
GRANT INSERT, SELECT, UPDATE, DELETE ON vw_inventario_fabricacion TO 'jefe_produccion'@'localhost';
GRANT INSERT, SELECT, UPDATE, DELETE ON vw_revision TO 'jefe_produccion'@'localhost';
GRANT INSERT, SELECT, UPDATE, DELETE ON vw_manejo TO 'jefe_produccion'@'localhost';
GRANT INSERT, SELECT, UPDATE, DELETE ON vw_infogeneral_produccion TO 'jefe_produccion'@'localhost';

GRANT SELECT ON vw_disenador TO 'jefe_produccion'@'localhost';
GRANT SELECT ON vw_empleado TO 'jefe_produccion'@'localhost';
GRANT SELECT ON vw_inventario TO 'jefe_produccion'@'localhost';
GRANT SELECT ON vw_almacenamiento TO 'jefe_produccion'@'localhost';

GRANT SELECT, UPDATE ON vw_producto TO 'jefe_produccion'@'localhost';

GRANT SELECT, DELETE ON vw_operario TO 'jefe_produccion'@'localhost';


GRANT EXECUTE ON PROCEDURE sp_eliminarMaquina TO 'jefe_produccion'@'localhost';
GRANT EXECUTE ON PROCEDURE sp_actualizarMaterial TO 'jefe_produccion'@'localhost';
GRANT EXECUTE ON PROCEDURE sp_actualizarMaterial_producto TO 'jefe_produccion'@'localhost';
GRANT EXECUTE ON PROCEDURE sp_agregarEmpleado TO 'jefe_produccion'@'localhost';








			-- OPERARIO -------------------------------------------
GRANT SELECT ON vw_produccion TO 'operario'@'localhost';
GRANT SELECT ON vw_producto TO 'operario'@'localhost';
GRANT SELECT ON vw_maquina TO 'operario'@'localhost';
GRANT SELECT ON vw_inventario TO 'operario'@'localhost';
GRANT SELECT ON vw_inventario_fabricacion TO 'operario'@'localhost';
GRANT SELECT ON vw_revision TO 'operario'@'localhost';
GRANT SELECT ON vw_infogeneral_produccion TO 'operario'@'localhost';

GRANT SELECT, UPDATE, DELETE ON vw_material TO 'operario'@'localhost';

GRANT SELECT, INSERT ON vw_manejo TO 'operario'@'localhost';

GRANT INSERT, SELECT, UPDATE, DELETE ON vw_inventario TO 'operario'@'localhost';
GRANT INSERT, SELECT, UPDATE, DELETE ON vw_almacenamiento TO 'operario'@'localhost';


GRANT EXECUTE ON PROCEDURE sp_mostrarVistaRevision TO 'operario'@'localhost';
GRANT EXECUTE ON PROCEDURE sp_mostrarVistaMaquina TO 'operario'@'localhost';
GRANT EXECUTE ON PROCEDURE sp_mostrarVistaInventarioFabricacion TO 'operario'@'localhost';
GRANT EXECUTE ON PROCEDURE sp_eliminarInventario TO 'operario'@'localhost';
GRANT EXECUTE ON PROCEDURE sp_cantidadMaterial TO 'operario'@'localhost';







