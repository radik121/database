alter table genres drop column id_artist;

alter table tracks drop column track_duration;

alter table tracks add column track_duration int not null;

alter table artists add column id_genre integer references genres(id);