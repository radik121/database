SELECT name_album, year_album FROM albums
WHERE year_album = 2018;

SELECT name_track, time_track FROM tracks
WHERE time_track = (SELECT MAX(time_track) FROM tracks);

SELECT name_track FROM tracks
WHERE time_track >= (3.3 * 60000);

SELECT name_collection FROM collection
WHERE year_collection BETWEEN 2018 AND 2020;

SELECT name_artist FROM artists
WHERE name_artist NOT LIKE '% %';

SELECT name_track FROM tracks
WHERE name_track iLIKE '%мой%' OR name_track iLIKE '%my%';
