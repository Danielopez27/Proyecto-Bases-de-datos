-- CREATE SCHEMA servioffset;
-- USE servioffset;


DROP TABLE IF EXISTS inventario_fabricacion;
DROP TABLE IF EXISTS manejo;
DROP TABLE IF EXISTS almacenamiento;
DROP TABLE IF EXISTS maquina;
DROP TABLE IF EXISTS material;
DROP TABLE IF EXISTS revision;
DROP TABLE IF EXISTS venta;
DROP TABLE IF EXISTS producto;
DROP TABLE IF EXISTS inventario;
DROP TABLE IF EXISTS disenador;
DROP TABLE IF EXISTS operario;
DROP TABLE IF EXISTS jefe_produccion;
DROP TABLE IF EXISTS comercial;
DROP TABLE IF EXISTS atencion;
DROP TABLE IF EXISTS cliente;
DROP TABLE IF EXISTS recepcion;
DROP TABLE IF EXISTS produccion;
DROP TABLE IF EXISTS administrativa;
DROP TABLE IF EXISTS empleado;



CREATE TABLE empleado(
	emp_cedula			integer		PRIMARY KEY,
	emp_nombre			char(45) 	NOT NULL,
	emp_edad			tinyint		NOT NULL,
    emp_genero			char(45) 	NOT NULL,
    emp_telefono		char(45)	NOT NULL,
    emp_horario			time		NOT NULL,
    emp_sueldo			integer 	NOT NULL,
    emp_fecha_ingreso	date		NOT NULL
);

CREATE TABLE administrativa(
	adm_emp_cedula		integer		PRIMARY KEY,
	adm_oficina			integer		NOT NULL,
    FOREIGN KEY(adm_emp_cedula) REFERENCES empleado(emp_cedula)
);

CREATE TABLE produccion(
	prd_emp_cedula		integer		PRIMARY KEY,
    prd_enfoque			ENUM('maquinaria pesada','creacion')	NOT NULL,
    FOREIGN KEY(prd_emp_cedula) REFERENCES empleado(emp_cedula)
);

CREATE TABLE recepcion(
	rec_adm_emp_cedula			integer 	PRIMARY KEY,
    rec_satisfaccion_cliente		ENUM('Excelente','Buena','Regular','Mala','Insuficiente')	DEFAULT 'Regular',
    FOREIGN KEY(rec_adm_emp_cedula) REFERENCES administrativa(adm_emp_cedula)
);

CREATE TABLE cliente(
	cli_cedula		integer 	PRIMARY KEY,
    cli_nombre		char(45)	NOT NULL,
    cli_telefono	char(45)	NOT NULL,
    cli_empresa		char(45) 	NOT NULL	DEFAULT 'ninguna',
    cli_email		char(45)	NULL
);

CREATE TABLE atencion(
	ate_rec_adm_emp_cedula		integer		NOT NULL,
    ate_cli_cedula				integer 	NOT NULL,
    ate_tipo_atencion			ENUM('telefonica', 'presencial','correo')	DEFAULT 'presencial',
    PRIMARY KEY(ate_rec_adm_emp_cedula, ate_cli_cedula),
    FOREIGN KEY(ate_rec_adm_emp_cedula) REFERENCES recepcion(rec_adm_emp_cedula),
    FOREIGN KEY(ate_cli_cedula) REFERENCES cliente(cli_cedula)
);

CREATE TABLE comercial(
	com_adm_emp_cedula			integer		PRIMARY KEY,
    com_porcentaje_comision		float		NOT NULL,
    com_cantidad_clientes		integer		NOT NULL,
    FOREIGN KEY(com_adm_emp_cedula) REFERENCES administrativa(adm_emp_cedula)
);

CREATE TABLE jefe_produccion(
	jef_prd_emp_cedula				integer		PRIMARY KEY,
    jef_fecha_cumplimiento			date		NOT NULL,
    FOREIGN KEY(jef_prd_emp_cedula) REFERENCES produccion(prd_emp_cedula)
);

CREATE TABLE operario(
	ope_prd_emp_cedula				integer 	PRIMARY KEY,
    ope_jef_prd_emp_cedula			integer		NOT NULL,
    ope_cargo						ENUM('almacenista','maquinaria') 	NOT NULL,
    FOREIGN KEY(ope_prd_emp_cedula) REFERENCES produccion(prd_emp_cedula),
    FOREIGN KEY(ope_jef_prd_emp_cedula) REFERENCES jefe_produccion(jef_prd_emp_cedula)
);

CREATE TABLE disenador(
	dis_prd_emp_cedula 				integer		PRIMARY KEY,
    dis_sotfware	 				char(45)	DEFAULT 'ninguno',
    FOREIGN KEY(dis_prd_emp_cedula) REFERENCES produccion(prd_emp_cedula)
);

CREATE TABLE inventario(
	inv_id					integer		PRIMARY KEY,
    inv_cantidad			integer		NOT NULL,
    inv_clasificacion		ENUM('papel','adhesivo','insumo','quimico','corrugados', 'maquina') 	NOT NULL,
    inv_precio				integer		NOT NULL,
    inv_vida_util			date		NOT NULL
);

CREATE TABLE producto(
	pro_inv_id_orden_produccion		integer 	PRIMARY KEY,
    pro_dis_prd_emp_cedula			integer		NOT NULL,
    pro_nombre						char(45)	NOT NULL,
    FOREIGN KEY(pro_inv_id_orden_produccion) REFERENCES inventario(inv_id),
    FOREIGN KEY(pro_dis_prd_emp_cedula) REFERENCES disenador(dis_prd_emp_cedula)
);

CREATE TABLE venta(
	ven_cli_cedula							integer		NOT NULL,
    ven_com_adm_emp_cedula				integer		NOT NULL,
    ven_pro_inv_id_orden_produccion		integer		NOT NULL,
    ven_fecha_de_venta					date		NOT NULL,
    ven_aprovacion						ENUM('T','F')	NOT NULL,
    ven_porcentaje_descuento			float 		DEFAULT 0,
    PRIMARY KEY(ven_cli_cedula, ven_com_adm_emp_cedula, ven_pro_inv_id_orden_produccion, ven_fecha_de_venta),
    FOREIGN KEY(ven_cli_cedula) REFERENCES cliente(cli_cedula),
    FOREIGN KEY(ven_com_adm_emp_cedula) REFERENCES comercial(com_adm_emp_cedula),
    FOREIGN KEY(ven_pro_inv_id_orden_produccion) REFERENCES producto(pro_inv_id_orden_produccion)
);

CREATE TABLE revision(
	rev_pro_inv_id_orden_produccion		integer 	NOT NULL,
    rev_jef_prd_emp_cedula				integer 	NOT NULL,
    rev_aprovacion						ENUM('T','F') 	NOT NULL,
    PRIMARY KEY(rev_pro_inv_id_orden_produccion, rev_jef_prd_emp_cedula),
    FOREIGN KEY(rev_pro_inv_id_orden_produccion) REFERENCES producto(pro_inv_id_orden_produccion),
    FOREIGN KEY(rev_jef_prd_emp_cedula) REFERENCES jefe_produccion(jef_prd_emp_cedula)
);

CREATE TABLE material(
	mat_inv_id		integer		PRIMARY KEY,
    mat_nombre		char(45)	NOT NULL,
    mat_calidad		ENUM('alta','media','baja') DEFAULT 'media',
    FOREIGN KEY(mat_inv_id) REFERENCES inventario(inv_id)
);

CREATE TABLE maquina(
	maq_inv_id								integer		PRIMARY KEY,
	maq_marca								char(45)	NOT NULL,
    maq_fecha_adquisicion					date		NOT NULL,
    maq_fecha_ultimo_mantenimiento			date		NOT NULL,
    FOREIGN KEY(maq_inv_id) REFERENCES inventario(inv_id)
);

CREATE TABLE almacenamiento(
	alm_mat_inv_id					integer		NOT NULL,
    alm_ope_prd_emp_cedula			integer		NOT NULL,
    PRIMARY KEY(alm_mat_inv_id, alm_ope_prd_emp_cedula),
    FOREIGN KEY(alm_mat_inv_id) REFERENCES material(mat_inv_id),
    FOREIGN KEY(alm_ope_prd_emp_cedula) REFERENCES operario(ope_prd_emp_cedula)
);

CREATE TABLE manejo(
	man_maq_inv_id					integer		NOT NULL,
    man_ope_prd_emp_cedula			integer		NOT NULL,
    PRIMARY KEY(man_maq_inv_id, man_ope_prd_emp_cedula),
    FOREIGN KEY(man_maq_inv_id) REFERENCES maquina(maq_inv_id),
    FOREIGN KEY(man_ope_prd_emp_cedula) REFERENCES operario(ope_prd_emp_cedula)
);

CREATE TABLE inventario_fabricacion(
	invfa_mat_inv_id 						integer		NOT NULL,
    invfa_pro_inv_id_orden_produccion		integer		NOT NULL,
    invfa_cantidad_material					integer		NOT NULL,
    PRIMARY KEY(invfa_mat_inv_id, invfa_pro_inv_id_orden_produccion),
    FOREIGN KEY(invfa_mat_inv_id ) REFERENCES material(mat_inv_id ),
    FOREIGN KEY(invfa_pro_inv_id_orden_produccion ) REFERENCES producto(pro_inv_id_orden_produccion )
);







