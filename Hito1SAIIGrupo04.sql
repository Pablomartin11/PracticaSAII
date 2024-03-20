# Hito 1  -  Practica SAII
# Creacion de bases de datos.

SET foreign_key_checks = 0;

#### DATABASE 3: climaCYL
# climaCYL(codigo, ubicacion, fecha, hora, precipitacion, temperatura, humedad_relativa, radiacion, velocidad_viento, direccion_viento)

drop database if exists ClimaCYL;
create database ClimaCYL;

drop table if exists ClimaCYL.Clima;
create table ClimaCYL.Clima(
    codigo varchar(5),
    ubicacion varchar(20),
    fecha date,
    hora int,
    precipitacion float,
    temperatura float,
    humedad_relativa float,
    radiacion float,
    velocidad_viento float,
    direccion_viento float,
    
    constraint Clima_pk primary key (codigo, hora)
);

insert into ClimaCYL.Clima values ('AV01',    'Nava de Arevalo',	str_to_date('2022-05-01', '%Y-%m-%d'),	200,	0.00,	7.25,	87.70,	0.00,	3.68,	227.90);
insert into ClimaCYL.Clima values ('BU03',	'Lerma',	str_to_date('2022-05-01','%Y-%m-%d'),	130,	0.00,	10.70,	79.50,	0.00,	0.00,	0.00);

