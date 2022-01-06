CREATE TABLE IF NOT EXISTS Artists (
	id SERIAL PRIMARY KEY,
	name_artist VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS Albums (
	id SERIAL PRIMARY KEY,
	name_album VARCHAR(255) NOT NULL,
	year_album INT NOT NULL
);

CREATE TABLE IF NOT EXISTS Tracks (
	id SERIAL PRIMARY KEY,
	name_track VARCHAR(255) NOT NULL,
	time_track INT NOT NULL,
	id_album INT REFERENCES Albums(id)
);

CREATE TABLE IF NOT EXISTS Genres (
	id SERIAL PRIMARY KEY,
	name_genre VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS Collection (
	id SERIAL PRIMARY KEY,
	name_collection VARCHAR(255) NOT NULL UNIQUE,
	year_collection INT NOT NULL
);

CREATE TABLE IF NOT EXISTS ArtistsAlbums (
	id SERIAL PRIMARY KEY,
	id_artist INT REFERENCES Artists(id),
	id_album INT REFERENCES Albums(id)
);

CREATE TABLE IF NOT EXISTS ArtistsGenres (
	id_artist INT REFERENCES Artists(id),
	id_genre INT REFERENCES Genres(id),
	CONSTRAINT pk PRIMARY KEY (id_artist, id_genre)
);

CREATE TABLE IF NOT EXISTS CollectionsTracks (
	id_collection INT REFERENCES Collection(id),
	id_tracks INT REFERENCES Tracks(id),
	CONSTRAINT pk_CollectionsTracks PRIMARY KEY (id_collection, id_tracks)
);