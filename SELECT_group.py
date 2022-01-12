import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://radik:260185@localhost:5432/ecom')
connection = engine.connect()

# количество исполнителей в каждом жанре
count_artist = connection.execute("""
SELECT name_genre, COUNT(id) artist_q FROM genres g
JOIN artistsgenres ag ON g.id = ag.id_genre
GROUP BY g.name_genre;
""").fetchall()

#print(count_artist)

# количество треков, вошедших в альбомы 2018-2020 годов
tracks_in_albums = connection.execute("""
SELECT name_album, COUNT(id_album) track_q FROM albums a
JOIN tracks t ON a.id = t.id_album
WHERE year_album BETWEEN 2018 AND 2020
GROUP BY name_album;
""").fetchall()

# print(tracks_in_albums)

# средняя продолжительность треков по каждому альбому
avg_tracks_in_album = connection.execute("""
SELECT name_album, AVG(time_track) time_avg FROM tracks t
JOIN albums a ON a.id = t.id_album
GROUP BY name_album
ORDER BY time_avg;
""").fetchall()

# print(avg_tracks_in_album)

# все исполнители, которые не выпустили альбомы в 2020 году
artists_all = connection.execute("""
SELECT name_artist FROM artists
WHERE name_artist NOT IN (
    SELECT name_artist FROM artists a
    JOIN artistsalbums aa ON a.id = aa.id_artist
    JOIN albums al ON aa.id_album = al.id
    WHERE year_album = 2020)
GROUP BY name_artist;
""").fetchall()

# print(artists_all)

# названия сборников, в которых присутствует конкретный исполнитель - Би-2
collection_one_artist = connection.execute("""
SELECT name_collection FROM collection c
JOIN collectionstracks ct ON c.id = ct.id_collection
JOIN tracks t ON ct.id_tracks = t.id
JOIN albums al ON t.id_album = al.id
JOIN artistsalbums aa ON aa.id_album = al.id
JOIN artists a ON a.id = aa.id_artist
WHERE name_artist = 'Би-2'
GROUP BY name_collection;
""").fetchall()

# print(collection_one_artist)

# название альбомов, в которых присутствуют исполнители более 1 жанра
album_genre = connection.execute("""
SELECT name_album, COUNT(id_genre) FROM albums al
JOIN artistsalbums aa ON al.id = aa.id_album
JOIN artists a ON a.id = aa.id_artist
JOIN artistsgenres ag ON ag.id_artist = a.id
GROUP BY name_album
HAVING COUNT(id_genre) > 1;
""").fetchall()

# print(album_genre)

# наименование треков, которые не входят в сборники;
track_name = connection.execute("""
SELECT name_track FROM tracks
WHERE name_track NOT IN (
    SELECT name_track FROM tracks t
    JOIN collectionstracks ct ON t.id = ct.id_tracks);
""").fetchall()

# print(track_name)

# исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть несколько);
artist_min_time_track = connection.execute("""
SELECT name_artist FROM artists a
JOIN artistsalbums aa ON a.id = aa.id_artist
JOIN albums al ON aa.id_album = al.id
JOIN tracks t ON t.id_album = al.id
WHERE time_track = (
    SELECT MIN (time_track) FROM tracks);
""").fetchall()

# print(artist_min_time_track)

# название альбомов, содержащих наименьшее количество треков.
album_min_tracks = connection.execute("""
SELECT name_album FROM albums a
JOIN tracks t ON a.id = t.id_album
GROUP BY name_album
HAVING COUNT(t.id) = (
    SELECT MIN (track_q) FROM (
        SELECT name_album, COUNT(t.id) track_q FROM tracks t
        JOIN albums a ON a.id = t.id_album
        GROUP BY name_album) q);
""").fetchall()

# print(album_min_tracks)