DELETE FROM inventario_fabricacion;
DELETE FROM manejo;
DELETE FROM almacenamiento;
DELETE FROM maquina;
DELETE FROM material;
DELETE FROM revision;
DELETE FROM venta;
DELETE FROM producto;
DELETE FROM inventario;
DELETE FROM disenador;
DELETE FROM operario;
DELETE FROM jefe_produccion;
DELETE FROM comercial;
DELETE FROM atencion;
DELETE FROM cliente;
DELETE FROM recepcion;
DELETE FROM produccion;
DELETE FROM administrativa;
DELETE FROM empleado;


INSERT INTO empleado VALUES
(1, 'Juan Perez', 30, 'Masculino', '555-1234', '08:00:00', 2500, '2020-01-15'),
(2, 'Ana García', 28, 'Femenino', '555-5678', '08:00:00', 2800, '2019-02-10'),
(3, 'Carlos López', 25, 'Masculino', '555-9876', '08:00:00', 2200, '2022-03-05'),
(4, 'Maria Rodríguez', 32, 'Femenino', '555-4321', '08:00:00', 2700, '2023-04-20'),
(5, 'Luis Hernandez', 29, 'Masculino', '555-8765', '08:00:00', 2900, '2022-05-14'),
(6, 'Sofia Ramirez', 27, 'Femenino', '555-3456', '08:00:00', 2100, '2020-06-30'),
(7, 'Jorge Torres', 31, 'Masculino', '555-6543', '08:00:00', 2600, '2021-07-25'),
(8, 'Laura González', 26, 'Femenino', '555-2345', '08:00:00', 3100, '2021-08-10'),
(9, 'Pedro Sánchez', 33, 'Masculino', '555-5432', '08:00:00', 2300, '2020-09-05'),
(10, 'Ana Martínez', 30, 'Femenino', '555-7654', '08:00:00', 2700, '2018-10-20'),
(11, 'Raul Gómez', 29, 'Masculino', '555-8765', '08:00:00', 2800, '2019-11-14'),
(12, 'Carmen Jiménez', 28, 'Femenino', '555-2345', '08:00:00', 2400, '2015-12-30'),
(13, 'Diego Ortega', 27, 'Masculino', '555-5432', '08:00:00', 2700, '2013-01-25'),
(14, 'Elena Castro', 32, 'Femenino', '555-7654', '08:00:00', 2900, '2011-02-10'),
(15, 'Fernando Ruiz', 31, 'Masculino', '555-6543', '08:00:00', 2200, '2016-03-05'),
(16, 'Isabel Silva', 26, 'Femenino', '555-9876', '08:00:00', 3300, '2020-04-20'),
(17, 'Gabriel Mendoza', 29, 'Masculino', '555-4321', '08:00:00', 2700, '2021-05-14'),
(18, 'Marta Vargas', 28, 'Femenino', '555-1234', '08:00:00', 3000, '2021-06-30'),
(19, 'Alejandro Paredes', 34, 'Masculino', '555-8765', '08:00:00', 2500, '2021-07-25'),
(20, 'Lucia Rojas', 27, 'Femenino', '555-3456', '08:00:00', 2600, '2020-08-10');


INSERT INTO administrativa VALUES
(1, 101),
(2, 202),
(6, 303),
(7, 404),
(8, 505),
(12, 606),
(13, 707),
(14, 808),
(18, 909),
(19, 102),
(20, 203);


INSERT INTO produccion VALUES 
(3, 'maquinaria pesada'),
(4, 'creacion'),
(5, 'maquinaria pesada'),
(9, 'creacion'),
(10, 'creacion'),
(11, 'creacion'),
(15, 'maquinaria pesada'),
(16, 'creacion'),
(17, 'maquinaria pesada');


INSERT INTO recepcion VALUES
(1, 'Excelente'),  
(2, 'Buena'),
(6, 'Regular'),
(7, 'Mala'),
(8, 'Insuficiente');


INSERT INTO cliente VALUES
(21, 'Martín Sánchez', '555-7890', 'ABC Corp', 'martin.sanchez@email.com'),
(22, 'Lorena Torres', '555-2345', 'XYZ Solutions', 'lorena.torres@email.com'),
(23, 'Andrés Rodríguez', '555-6789', 'LMN Technologies', 'andres.rodriguez@email.com'),
(24, 'Paula Pérez', '555-4567', 'PQR Innovations', 'paula.perez@email.com'),
(25, 'Hugo Ramírez', '555-8901', 'Tech Connect', 'hugo.ramirez@email.com'),
(26, 'Carolina Gómez', '555-1234', 'Global Services', 'carolina.gomez@email.com'),
(27, 'Felipe Martínez', '555-5678', 'ACME Solutions', 'felipe.martinez@email.com'),
(28, 'Natalia Silva', '555-9876', 'Swift Innovations', 'natalia.silva@email.com'),
(29, 'Gonzalo Jiménez', '555-6543', 'Innovate Co.', 'gonzalo.jimenez@email.com'),
(30, 'Valentina López', '555-8765', 'Web Technologies', 'valentina.lopez@email.com'),
(31, 'Diego Ortega', '555-5432', 'Tech Solutions Inc.', 'diego.ortega@email.com'),
(32, 'Camila Castro', '555-7654', 'BlueSky Systems', 'camila.castro@email.com'),
(33, 'Tomás Vargas', '555-3210', 'NexTech Corporation', 'tomas.vargas@email.com'),
(34, 'Isabella Mendoza', '555-2345', 'Creative Designs', 'isabella.mendoza@email.com'),
(35, 'Santiago Rojas', '555-9876', 'Bright Ideas Inc.', 'santiago.rojas@email.com'),
(36, 'Amelia Sánchez', '555-7890', 'Infinite Solutions', 'amelia.sanchez@email.com'),
(37, 'Javier García', '555-4567', 'NextGen Technologies', 'javier.garcia@email.com'),
(38, 'Laura Pérez', '555-6543', 'XYZ Innovations', 'laura.perez@email.com'),
(39, 'Felipe Ramírez', '555-8765', 'Spectrum Solutions', 'felipe.ramirez@email.com'),
(40, 'Victoria López', '555-1234', 'Alpha Innovations', 'victoria.lopez@email.com');


INSERT INTO atencion VALUES
(1, 21, 'telefonica'), 
(1, 22, 'presencial'), 
(1, 23, 'correo'), 
(1, 24, 'presencial'),  
(2, 25, 'telefonica'),
(2, 26, 'presencial'),
(2, 27, 'telefonica'),
(2, 28, 'presencial'),
(6, 29, 'presencial'),
(6, 30, 'telefonica'),
(6, 31, 'presencial'),
(6, 32, 'correo'),
(7, 33, 'telefonica'),
(7, 34, 'presencial'),
(7, 35, 'correo'),
(7, 36, 'telefonica'),
(8, 37, 'presencial'),
(8, 38, 'telefonica'),
(8, 39, 'correo'),
(8, 40, 'presencial');



INSERT INTO comercial VALUES
(12, 4.5, 4),
(13, 3.2, 6),
(14, 7.2, 2),
(18, 1.9, 4),
(19, 4.3, 2),
(20, 5.1, 2);


INSERT INTO jefe_produccion VALUES
(3, '2023-10-31'),
(11, '2023-11-15');


INSERT INTO operario VALUES
(5, 11, 'almacenista'),
(15, 3, 'maquinaria'),
(16, 11, 'almacenista'),
(17, 3, 'maquinaria');


INSERT INTO disenador VALUES
(4, 'figma'),
(9, 'blender'),
(10, 'blender');


INSERT INTO inventario VALUES
(101, 50, 'papel', 10, '2023-01-15'),
(102, 75, 'adhesivo', 15, '2022-12-10'),
(103, 30, 'insumo', 20, '2022-11-05'),
(104, 45, 'quimico', 25, '2022-10-20'),
(105, 60, 'corrugados', 30, '2022-09-14'),
(106, 85, 'papel', 12, '2022-08-30'),
(107, 10, 'adhesivo', 18, '2022-07-25'),
(108, 70, 'insumo', 22, '2022-06-10'),
(109, 40, 'quimico', 28, '2022-05-05'),
(110, 55, 'corrugados', 35, '2022-04-20'),
(111, 90, 'papel', 11, '2022-03-14'),
(112, 15, 'adhesivo', 17, '2022-02-28'),
(113, 65, 'insumo', 24, '2022-01-25'),
(114, 35, 'quimico', 26, '2021-12-30'),
(115, 80, 'corrugados', 32, '2021-11-25'),
(116, 95, 'papel', 14, '2021-10-10'),
(117, 5, 'adhesivo', 16, '2021-09-05'),
(118, 50, 'insumo', 21, '2021-08-20'),
(119, 70, 'quimico', 27, '2021-07-14'),
(120, 60, 'corrugados', 33, '2021-06-30'),
(121, 80, 'maquina', 13, '2021-05-15'),
(122, 20, 'maquina', 19, '2021-04-10'),
(123, 45, 'maquina', 23, '2021-03-05'),
(124, 55, 'maquina', 29, '2021-02-20'),
(125, 75, 'maquina', 37, '2021-01-14'),
(126, 60, 'maquina', 12, '2020-12-30'),
(127, 40, 'maquina', 20, '2020-11-25'),
(128, 70, 'maquina', 26, '2020-10-10'),
(129, 50, 'maquina', 31, '2020-09-05'),
(130, 85, 'maquina', 40, '2020-08-20');


INSERT INTO producto VALUES
(101, 4, 'bloc de notas'),
(102, 9, 'cinta escolar'),
(103, 10, 'papel'),
(104, 4, 'diluyentes y limpiadores'),
(105, 4, 'carton corrugado'),
(106, 9, 'carton corrugado'),
(107, 9, 'papel a3'),
(108, 10, 'Plastisoles'),
(109, 10, 'kit colorantes'),
(110, 10, 'caja mediana');



INSERT INTO venta VALUES
(21, 12, 101, '2022-01-20', 'T', 0.2),
(22, 13, 102, '2020-02-11', 'F', 0.3),
(23, 14, 103, '2021-03-12', 'T', 0.4),
(24, 18, 104, '2022-01-14', 'F', 0.2),
(25, 19, 105, '2022-06-15', 'T', 0.5),
(26, 20, 106, '2023-12-18', 'F', 0.6),
(26, 12, 101, '2023-11-20', 'T', 0.2),
(27, 13, 107, '2022-02-19', 'T', 0.4),
(28, 14, 108, '2023-12-10', 'T', 0.3),
(29, 18, 109, '2022-04-11', 'F', 0.2),
(30, 19, 110, '2023-03-12', 'T', 0.1),
(31, 20, 101, '2022-02-14', 'T', 0.2),
(32, 12, 102, '2021-03-16', 'F', 0.1),
(33, 13, 103, '2022-04-14', 'T', 0.2),
(34, 14, 104, '2022-05-20', 'T', 0.2),
(35, 18, 105, '2023-12-23', 'F', 0.1),
(36, 19, 106, '2023-11-29', 'T', 0.1),
(37, 20, 107, '2023-12-22', 'T', 0.3),
(38, 12, 108, '2020-07-10', 'T', 0.1),
(39, 12, 109, '2023-03-19', 'F', 0.2),
(40, 12, 110, '2022-04-12', 'F', 0.1),
(40, 13, 109, '2023-04-15', 'T', 0.1);



INSERT INTO revision VALUES
(101, 3, 'T'),
(102, 3, 'T'),
(103, 11, 'F'),
(104, 11, 'T'),
(105, 3, 'T'),
(106, 11, 'T'),
(107, 3, 'T'),
(108, 11, 'T'),
(109, 11, 'T'),
(110, 11, 'F');


INSERT INTO material VALUES
(111, 'Papel', 'alta'),
(112, 'Adhesivo', 'media'),
(113, 'Insumo', 'baja'),
(114, 'Químico', 'alta'),
(115, 'Corrugados', 'media'),
(116, 'Papel', 'baja'),
(117, 'Adhesivo', 'alta'),
(118, 'Insumo', 'media'),
(119, 'Químico', 'baja'),
(120, 'Corrugados', 'alta');


INSERT INTO maquina  VALUES
(121, 'APS Novastar', '2021-05-15', '2022-05-15'),
(122, 'AUREL Automation Division', '2021-04-10', '2022-04-10'),
(123, 'AUREL Automation Division', '2021-03-05', '2022-03-05'),
(124, 'APS Novastar', '2021-02-20', '2022-02-20'),
(125, 'ASM Assembly Systems', '2021-01-14', '2022-01-14'),
(126, 'ASM Assembly Systems', '2020-12-30', '2021-12-30'),
(127, 'ASYS GROUP', '2020-11-25', '2021-11-25'),
(128, 'Beijing Torch SMT Co., Ltd.', '2020-10-10', '2021-10-10'),
(129, 'Cougartron2I', '2020-09-05', '2021-09-05'),
(130, 'ASM Assembly Systems', '2020-08-20', '2021-08-20');


INSERT INTO almacenamiento VALUES
(111, 16),
(112, 5),
(113, 5),
(114, 5),
(115, 5),
(116, 5),
(117, 5),
(118, 5),
(119, 16),
(120, 16);


INSERT INTO manejo VALUES 
(121, 15),
(122, 17),
(123, 15),
(124, 17),
(125, 17),
(126, 17),
(127, 15),
(128, 15),
(129, 17),
(130, 15);


INSERT INTO inventario_fabricacion VALUES
(111, 101, 10),
(112, 102, 15),
(113, 103, 20),
(114, 104, 25),
(115, 105, 30),
(116, 106, 12),
(117, 107, 18),
(119, 108, 22),
(120, 109, 28);







