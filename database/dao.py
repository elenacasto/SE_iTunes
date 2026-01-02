from database.DB_connect import DBConnect
from model.album import Album


class DAO:
    @staticmethod
    def getDurataAlbum(min_duration):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT sum(t.milliseconds)/60000 AS durata, a.id, a.title, a.artist_id
                    FROM track t, album a 
                    WHERE t.album_id = a.id 
                    GROUP BY a.id, a.title, a.artist_id
                    HAVING durata > %s """

        cursor.execute(query, (min_duration,))

        for row in cursor:
            album = Album(id = row['id'], title = row['title'], artist_id = row['artist_id'], durata = row["durata"])
            result.append(album)

        cursor.close()
        conn.close()

        return result


    @staticmethod
    def getCoppieAlbum():
        conn = DBConnect.get_connection()
        result = []


        cursor = conn.cursor(dictionary=True)
        query =  """ SELECT DISTINCT
                           x.album_id AS a1,
                           y.album_id AS a2
                     FROM (
                        SELECT DISTINCT pt.playlist_id, t.album_id
                        FROM playlist_track pt
                        JOIN track t ON pt.track_id = t.id
                     ) x
                     JOIN (
                        SELECT DISTINCT pt.playlist_id, t.album_id
                        FROM playlist_track pt
                        JOIN track t ON pt.track_id = t.id
                     ) y
                     ON x.playlist_id = y.playlist_id
                     AND x.album_id < y.album_id """
        #query più complessa per rendere semplice il model

        cursor.execute(query)
        for row in cursor:
            result.append((row['a1'],row['a2']))


        cursor.close()
        conn.close()

        return result
