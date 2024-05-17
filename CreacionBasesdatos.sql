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
    p_mes FLOAT,
    p_max VARCHAR(50),
    np_010 INT,
    n_nie INT,
    evap FLOAT,
    PRIMARY KEY (fecha, indicativo)
);



drop database if exists f2;
create database f2;

drop table if exists f2.datosEmbalse;
CREATE TABLE f2.datosEmbalse (
    embalse_nombre VARCHAR(100),
    fecha VARCHAR(50),
    agua_total REAL,
    agua_actual REAL,
    PRIMARY KEY (embalse_nombre, fecha)
);


drop database if exists f3;
create database f3;
CREATE TABLE f3.ambitoEmbalse(
    provincia VARCHAR(50),
    nombreEmbalse VARCHAR(100),
    PRIMARY KEY (nombreEmbalse, provincia)
);


drop database if exists f4;
create database f4;

drop table if exists f4.temperaturaAsturias;
CREATE TABLE f4.temperaturaAsturias (
    fecha VARCHAR(100),
    estacionClimatologica VARCHAR(100),
    tmed FLOAT,
    tmed_max FLOAT,
    tmed_min FLOAT,
    precip FLOAT,
    PRIMARY KEY (fecha, estacionClimatologica)
);

