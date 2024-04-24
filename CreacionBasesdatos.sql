# Practica SAII
# Creacion de bases de datos.

SET foreign_key_checks = 0;

drop database if exists f1;
create database f1;

drop table if exists f1.climatologiaAsturias;
CREATE TABLE f1.climatologiaAsturias (
    fecha DATE,
    indicativo VARCHAR(50),
    provincia VARCHAR(50),
    tm_mes FLOAT,
    tm_max FLOAT,
    tm_min FLOAT,
    p_mes INT,
    p_max INT,
    np_010 INT,
    n_nie INT,
    evap FLOAT
);



drop database if exists f2;
create database f2;

drop table if exists f2.temperaturaCyL;
CREATE TABLE f2.temperaturaCyL (
    fecha DATE,
    indicativo VARCHAR(10),
    nombre VARCHAR(100),
    provincia VARCHAR(50),
    tmin FLOAT,
    horatmin TIME,
    tmax FLOAT,
    horatmax TIME,
    tmed FLOAT,
    ubicacion VARCHAR(100),
    hora TIME,
    temperatura FLOAT
);


drop database if exists f3;
create database f3;
CREATE TABLE f3.ambitoEmbalse(
    provincia VARCHAR(20),
    nombre VARCHAR(20)
);


drop database if exists f4;
create database f4;

drop table if exists f4.temperaturaAsturias;
CREATE TABLE f4.temperaturaAsturias (
    fecha DATE,
    estacionClimatologica VARCHAR(20),
    tmed_max FLOAT,
    tmed_min FLOAT,
    precip FLOAT
);

