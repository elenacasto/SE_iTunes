from database.DB_connect import DBConnect

class DAO:
    @staticmethod
    def getSommaAlbum():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select sum(t.milliseconds) as somma, a.id
                    from track t , album a 
                    where t.album_id = a.id 
                    group by a.id """

        cursor.execute(query)

        for row in cursor:
            result.append((row['somma'],row['id']))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getCoppieAlbum():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """ select a1.id as a1, a2.id as a2
                    from track t1, track t2, album a1, album a2
                    where a1.id < a2.id and 
                          t1.album_id = a1.id and t2.album_id = a2.id 
                          and a1.artist_id = a2.artist_id """
        cursor.execute(query)
        for row in cursor:
            result.append((row['a1'],row['a2']))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAlbum():
        conn = DBConnect.get_connection()

        result = []
        cursor = conn.cursor(dictionary=True)
        query = """ select *
                    from album """
        cursor.execute(query)
        for row in cursor:
            result.append(row)

        cursor.close()
        conn.close()
        return result