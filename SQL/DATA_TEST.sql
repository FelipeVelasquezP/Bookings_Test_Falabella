#Datos de preba para Hoteles 
insert into Hotel values(null,'Santa Clara','Colombia',43.43,895.3542,'des1',true);
insert into Hotel values(null,'Blue Suits','EEUU',413.43,89.352,'des2',true);
insert into Hotel values(null,'Villa Hotel','Peru',143.433,819.352,'des3',false);
insert into Hotel values(null,'Tequendama','Colombia',443.43,489.32,'des4',true);
#select*from Hotel;

#Datos de prueba para Habitaciones 
insert into Habitacion values(null,2);
insert into Habitacion values(null,2);
insert into Habitacion values(null,1);
insert into Habitacion values(null,2);
insert into Habitacion values(null,1);
insert into Habitacion values(null,1);
insert into Habitacion values(null,3);
insert into Habitacion values(null,3);
insert into Habitacion values(null,3);
insert into Habitacion values(null,4);
insert into Habitacion values(null,4);
insert into Habitacion values(null,2);
#select*from Habitacion;

#Datos de prueba para Usuarios 
insert into Usuario values ('1002549404','Luis Felipe','Velasquez','cll 76','ingvelasquezfelipe@mail.com');
insert into Usuario values ('236752','Jahana','Puentes','vdl','joahanpuentes@mail.com');
insert into Usuario values ('87945','Juan','Perez','bog','juanperez@mail.com');
insert into Usuario values ('334523','Camilo','Blanco','bq','camilobl@mail.com');
insert into Usuario values ('8474','Karent','Saenz','bog','kasaen@mail.com');
insert into Usuario values ('9698453','Lina','Arciniegas','miam','linanrci@mail.com');
insert into Usuario values ('834943875','Andres','Lopez','car','alopez@mail.com');
insert into Usuario values ('837983','Lorena','Alvarez','fus','loalvare@mail.com');
#select*from Usuario;

#Datos de prueba para reservas
insert into Reserva values(null,'2022-11-11','2022-11-15',utc_date(),'reservado','1002549404',3) ;
insert into Reserva values(null,'2022-11-13','2022-11-14',utc_date(),'reservado','1002549404',4) ;
insert into Reserva values(null,'2022-11-19','2022-11-24',utc_date(),'reservado','1002549404',5) ;
insert into Reserva values(null,'2022-11-28','2022-11-30',utc_date(),'reservado','1002549404',5) ;

select*from Reserva;


-- -----------------------------------------------------
-- Registrar una reserva dado usurio, hotel y checkin y checkout
-- -----------------------------------------------------
#Buscar las habitacione a las que nuncan se le han hecho reserva
SELECT  idHabitacion FROM habitacion
 WHERE Hotel_idHotel=1 and  idHabitacion NOT IN (SELECT Habitacion_idHabitacion FROM Reserva);

SELECT distinct idHabitacion FROM Reserva,Habitacion
WHERE Hotel_idHotel=2 and Habitacion_idHabitacion=idHabitacion;


-- -----------------------------------------------------
-- cancelar la reserva
-- -----------------------------------------------------
#actualizar el estado de la habitación 
update Reserva set estadoReserva="cancelado",checkin='1677-09-21',checkout='1677-09-21' where idReserva=2;

-- -----------------------------------------------------
-- consultar reservas activas en un rango de fechas
-- -----------------------------------------------------
#traer info de reserva, nombre de hotel y mail de usuario
select idReserva,checkin,checkout,fechaReserva,idHabitacion,nombreHotel,emailUsuario from Reserva,Usuario,Habitacion,Hotel
where idHabitacion=Habitacion_idHabitacion and idHotel=Hotel_idHotel and idUsuario=Usuario_idUsuario 
and estadoReserva='reservado' and checkin between '2022-6-10' and '2022-7-13'
and checkout between '2022-6-10' and '2022-7-13' and idHotel=2;