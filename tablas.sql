CREATE TABLE centro_acopio_hgcg(
    centro_acopio_hgcg_id int PRIMARY KEY,
    nombre_centro_acopio  varchar(200),
    tipo_ca varchar(40),
    necesidades varchar(200),
    horario varchar(40),
    tipo_detalles varchar(200),
    estatus varchar(40),
    verifica varchar(40),
    fecha_creacion varchar(40),
    ultima_actualizacion varchar(200),
    actualiza varchar(200),
    nota_actualiza varchar(200)
);
CREATE TABLE usuario_hgcg(
    usuario_id int PRIMARY KEY,
    telefono varchar(40),
    twitter varchar(40),
    facebook varchar(200),
    correo varchar(200),
    centro_acopio_hgcg_id int,
    CONSTRAINT fk_centro_acopio FOREIGN KEY (centro_acopio_hgcg_id) REFERENCES centro_acopio_hgcg (centro_acopio_hgcg_id)
);
CREATE TABLE ubicacion_hgcg(
    ubicacion_id int primary key,
    numero_exterior varchar(40),
    colonia  varchar(200),
    delegacion varchar(200),
    ciudad varchar(200),
    entidad varchar(200),
    zona varchar(200),
    direccion varchar(200),
    latitud varchar(200),
    altitud varchar(200),
    link_maps varchar(200),
    centro_acopio_hgcg_id int,
    CONSTRAINT fk_centro_acopio_fk FOREIGN KEY (centro_acopio_hgcg_id) REFERENCES centro_acopio_hgcg (centro_acopio_hgcg_id)            
);