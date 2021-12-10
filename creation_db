create table if not exists artists (
	id serial primary key,
	name varchar(40) not null unique
);

create table if not exists albums (
	id serial primary key,
	album_title varchar(50) not null unique,
	release_year int not null,
	id_artist integer references artists(id)
);

create table if not exists tracks (
	id serial primary key,
	track_title varchar(50) unique not null,
	track_duration time not null,
	id_album integer references albums(id)
);

create table if not exists genres (
	id serial primary key,
	ganre_name varchar(50) unique not null,
	id_artist integer references artists(id)
);