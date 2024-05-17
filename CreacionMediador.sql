drop database if exists mediador;
create database mediador;

/* EmbalsesAst*/
drop table if exists mediador.embalsesAst;
CREATE TABLE mediador.embalsesAst (
    fecha VARCHAR(50),
    nombre VARCHAR(50),
    nombreEmbalse VARCHAR(100),
    provincia VARCHAR(50),
    agua_total REAL,
    agua_actual REAL,
    np_010 INT,
    n_nie INT,
    evap FLOAT,
    PRIMARY KEY (fecha, nombreEmbalse)
);

/* TemperaturaAst*/
drop table if exists mediador.temperaturaAst;
CREATE TABLE mediador.temperaturaAst (
    fecha VARCHAR(50),
    nombre VARCHAR(50),
    tmed REAL,
    tmed_max REAL,
    tmed_min REAL,
    PRIMARY KEY (fecha, nombre)
);

/* TemperaturaAst*/
drop table if exists mediador.precipitacionesAst;
CREATE TABLE mediador.precipitacionesAst (
    fecha VARCHAR(50),
    nombre VARCHAR(50),
    precip REAL,
    PRIMARY KEY (fecha, nombre)
);