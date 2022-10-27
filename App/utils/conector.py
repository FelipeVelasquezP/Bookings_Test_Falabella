import pymysql


DBINFO = {
    'host' : "localhost",
    'user' : "root",
    'password': "1234",
    'database': "Bookings"
}
TYPE_CURSOR =  {
  "Cursor": None,
  "SSCursor": pymysql.cursors.SSCursor,
  "DictCursor": pymysql.cursors.DictCursor,
  "SSDictCursor": pymysql.cursors.SSDictCursor
}


class Conector:

    def __init__(self, host=None, user=None, password=None, database=None):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        self.connection = pymysql.connect(
            host=self.host, user=self.user, password=self.password, database=self.database)

    def execute_query(self, query, data=()):
        c = self.get_cursor()
        c.execute(query, data)
        return c.fetchall()

    def commit_change(self):
        self.connection.commit()

    def get_cursor(self):
        return self.connection.cursor()

    def close(self):
        self.connection.close()