import mysql.connector


class Db:
    def __init__(self):
        self.cnx = mysql.connector.connect(hostname='carehand.mysql.database.azure.com',username='carehand',password='admin@123',ssl-mode=require,ssl='Digi.crt.pem',database='rcm')
        self.cur = self.cnx.cursor(dictionary=True)
# import psycopg2


# class Db:
#     def __init__(self):
#         self.cnx = psycopg2.connect(
#             host="dpg-chme5dv8hiejrmm9ta8g-a.oregon-postgres.render.com ",
#             user="carehand",
#             port="5432",
#             password="hCq169mNY550rVOhy8J90ZzDpe39tTt3",
#             database="carehand"
#         )
#         self.cur = self.cnx.cursor(cursor_factory=psycopg2.extras.DictCursor)

    def select(self, q):
        self.cur.execute(q)
        return self.cur.fetchall()

    def selectOne(self, q):
        self.cur.execute(q)
        return self.cur.fetchone()


    def insert(self, q):
        self.cur.execute(q)
        self.cnx.commit()
        return self.cur.lastrowid

    def update(self, q):
        self.cur.execute(q)
        self.cnx.commit()
        return self.cur.rowcount

    def delete(self, q):
        self.cur.execute(q)
        self.cnx.commit()
        return self.cur.rowcount

