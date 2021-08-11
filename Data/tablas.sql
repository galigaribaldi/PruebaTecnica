---Tabla correspondiente a Estado
CREATE TABLE estado(
    esatado_id serial primary key,
    nombre_enetidad character varying not null,
    clave_entidad integer not null
);
---Tabla correspondiente al municipio
CREATE TABLE municipio(
    municipio_id serial primary key,
    nombre_municipio character varying null,
    nombre_ciudad character varying null,
    clave_municipio integer not null,
    clave_ciudad integer null,
    esatado_id integer,
    CONSTRAINT esatado_id_fk FOREIGN KEY (esatado_id)
        REFERENCES estado (esatado_id)
);

---Tabla correspondiente a la colonia
CREATE TABLE colonia(
    colonia_id serial primary key,
    codigo_postal_asentamiento integer,
    nombre_colonia character varying null,
    tipo_asentamiento character varying null,
    codigo_postal_administracion integer,
    clave_tipo_asentamiento integer not null,
    asentamiento_id integer null,
    zona_asentamiento character varying null,
    esatado_id integer,
    municipio_id integer,
    CONSTRAINT esatado_id_fk FOREIGN KEY (esatado_id)
        REFERENCES estado (esatado_id),
    CONSTRAINT municipio_id_fk FOREIGN KEY (municipio_id)
        REFERENCES municipio (municipio_id)            
);
