from database.DB_connect import DBConnect
from model.state import State


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getYears():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = ("""select distinct YEAR(datetime)
                    from sighting s 
                    order by YEAR(datetime) asc  """)

        cursor.execute(query, ())

        for row in cursor:
            result.append(row['YEAR(datetime)'])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def setShape(anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = ("""select distinct shape
                    from sighting s
                    where YEAR(datetime) = %s
                """)

        cursor.execute(query, (anno, ))

        for row in cursor:
            result.append(row['shape'])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllObjects():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = (""" select *
                     from state s """)

        cursor.execute(query, ())

        for row in cursor:
            result.append(State(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getPeso(stato1, stato2, anno, forma):
        conn = DBConnect.get_connection()

        result = 0
        cursor = conn.cursor(dictionary=True)
        query = ("""select count(*) as peso
                    from sighting s1, sighting s2
                    where s1.shape = %s and s2.shape = %s and year(s1.datetime)= %s and year(s2.datetime)=%s and s1.id<s2.id
                    and s1.state=%s and s2.state=%s
                    group by s1.state, s2.state
                """)

        cursor.execute(query, (forma, forma, anno, anno, stato1.id, stato2,))

        for row in cursor:
            result = int(row['peso'])

        cursor.close()
        conn.close()
        return result









