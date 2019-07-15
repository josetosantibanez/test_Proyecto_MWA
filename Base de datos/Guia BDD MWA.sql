#GUIA PARA CONFIGURAR LA BASE DE DATOS.

#-Crear la base de datos y su usuario con los respectivos privilegios	
	create database Medical_Weed_App_3;
	use Medical_Weed_App_3;

	CREATE USER admin_medical_weed_app_3 IDENTIFIED BY 'superadmin1289';
	GRANT ALL PRIVILEGES ON Medical_Weed_App_3.* TO admin_medical_weed_app_3;
	FLUSH PRIVILEGES;

#-Inserts basicos para que no caguetodo
	insert into clubes_club values(1,'111111111-1','Club de prueba','Avenida Probando','34565455','tester@probando.club',100,'2019-06-02 19:01:25.302164','2019-06-02 19:01:25.302164');
	insert into registration_tipo_cuenta values (1,'Paciente');
	insert into registration_tipo_cuenta values (2,'Club');
	insert into registration_tipo_cuenta values (3,'SuperAdministrador');

#-Selects basicos

	#-Selects de usuario
	select * from auth_user;

    #-Selects de miembros
	select *  from miembros_miembro;

	#-Selects de registrations
    select * from registration_profile;
	select * from registration_tipo_cuenta;

    #-Selects de clubes
	select * from clubes_club;

    #-Selects de productos
	select * from productos_producto;
	select * from productos_reserva;

    # Selects de eventos
    select * from eventos_evento;
    select * from eventos_asistentes;
	
	desc auth_user;
    desc miembros_miembro;
	desc registration_profile;
    desc clubes_club;


#Trabajar
update auth_user set first_name = "Club de prueba" where id = 8;
update registration_profile set tipo_cuenta_id = 2 where user_id = 8;
delete from productos_reserva where id > 1;
delete from auth_user where id = 3;
delete from productos_reserva where id = 35;
delete from registration_profile where id = 9;


#-Triggers:
	drop trigger user_de_miembro;

	DELIMITER //
	create trigger user_de_miembro before insert on miembros_miembro
	for each row
	BEGIN
	    declare var_user_id int;
			if exists (select * from auth_user where username = new.rut) then
				set var_user_id = (select id from auth_user where username = new.rut order by date_joined DESC LIMIT 1);
	            set new.user_id_id = var_user_id;
			else 
				insert into auth_user (username,password,first_name,last_name,email,is_superuser,is_staff,is_active,date_joined) values (new.rut, 'pbkdf2_sha256$120000$Kpyp2shQuEe9$5oV3qOMpFvruBdGeQp6+/O3RJdfo6KnUT2vNCknGdW8=',new.nombres,new.apellido_p,new.correo,0,0,1,now());
				set var_user_id = (select id from auth_user where username = new.rut order by date_joined DESC LIMIT 1);
	            set new.user_id_id = var_user_id;
                insert into registration_profile (tipo_cuenta_id,user_id) values (2,new.user_id_id);
	        end if;
		set new.nombres = CONCAT(UCASE(LEFT(new.nombres, 1)),LCASE(SUBSTRING(new.nombres, 2)));
	    set new.apellido_p = CONCAT(UCASE(LEFT(new.apellido_p, 1)),LCASE(SUBSTRING(new.apellido_p, 2)));
	    set new.apellido_m = CONCAT(UCASE(LEFT(new.apellido_m, 1)),LCASE(SUBSTRING(new.apellido_m, 2)));
		update clubes_club set cantidad_miembros = cantidad_miembros + 1 where id = new.club_id_id;
    END;
	DELIMITER;
    
    DELIMITER //
		create trigger cant_miembros_delete after delete on miembros_miembro
		for each row
        BEGIN
			declare m int;
            set m = old.id;
			update clubes_club set cantidad_miembros = cantidad_miembros - 1 where id = old.club_id_id;
            update productos_reserva set estado = 'C' where usuario_id = old.user_id_id;
            delete from eventos_asistentes where old.user_id_id = m;
		END;
    DELIMITER;
    
    drop trigger stock_productos;
    
    DELIMITER//
    create trigger stock_productos after insert on productos_reserva
    for each row 
    begin
		declare var_stock int;
        declare stock_final int;
        select stock from productos_producto where id = new.producto_id into var_stock;
        if var_stock > new.cantidad_reservar then
			set stock_final = var_stock - new.cantidad_reservar; 
			update productos_producto set stock = stock_final where id = new.producto_id;
        end if;
    end;
    DELIMITER;
    
    drop trigger user_de_club;
    DELIMITER//
		create trigger user_de_club before insert on clubes_club
        for each row 
        begin
			declare vari_user_id int;
			insert into auth_user (username,password,first_name,last_name,email,is_superuser,is_staff,is_active,date_joined) values (new.nombre_org, 'pbkdf2_sha256$120000$Kpyp2shQuEe9$5oV3qOMpFvruBdGeQp6+/O3RJdfo6KnUT2vNCknGdW8=',new.rut_org,"Club cannabico",new.correo_contacto,0,1,1,now());
			set vari_user_id = (select id from auth_user where username = new.nombre_org order by date_joined DESC LIMIT 1);
			set new.usuario_id = vari_user_id;
            insert into registration_profile (tipo_cuenta_id,user_id) values (2,new.usuario_id);
		end;
    DELIMITER;
    
    DELIMITER //
		create trigger cupos_eventos after insert on eventos_asistentes
        for each row
        begin
            update eventos_evento set cupos = cupos - 1 where id = new.evento_id;
		end;
    DELIMITER;
    
    DELIMITER //
		create trigger cupos_eventos_del after delete on eventos_asistentes
        for each row
        begin
			update eventos_evento set cupos = cupos + 1 where id = old.evento_id;
		end;
    DELIMITER;
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    