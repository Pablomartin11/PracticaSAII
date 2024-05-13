# Practica SAII
# Creacion de bases de datos.

SET foreign_key_checks = 0;

drop database if exists f1;
create database f1;

drop table if exists f1.climatologiaAsturias;
CREATE TABLE f1.climatologiaAsturias (
    fecha VARCHAR(50),
    indicativo VARCHAR(50),
    nombre VARCHAR(50),
    provincia VARCHAR(50),
    tm_mes FLOAT,
    tm_max FLOAT,
    tm_min FLOAT,
    p_mes INT,
    p_max VARCHAR(50),
    np_010 INT,
    n_nie INT,
    evap FLOAT
);



drop database if exists f2;
create database f2;

drop table if exists f2.datosEmbalse;
CREATE TABLE f2.datosEmbalse (
    embalse_nombre VARCHAR(50),
    fecha DATE,
    agua_total INT,
    agua_actual INT
);


drop database if exists f3;
create database f3;
CREATE TABLE f3.ambitoEmbalse(
    provincia VARCHAR(50),
    nombreEmbalse VARCHAR(100)
);


drop database if exists f4;
create database f4;

drop table if exists f4.temperaturaAsturias;
CREATE TABLE f4.temperaturaAsturias (
    fecha DATE,
    estacionClimatologica VARCHAR(20),
    tmed FLOAT,
    tmed_max FLOAT,
    tmed_min FLOAT,
    precip FLOAT
);

