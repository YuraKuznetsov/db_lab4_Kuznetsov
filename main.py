import psycopg2


class PostgresDB:
    def __init__(self, dbname, username, password, host='localhost', port=5432):
        self.dbname = dbname
        self.user = username
        self.password = password
        self.host = host
        self.port = port
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            self.cursor = self.connection.cursor()
        except Exception as e:
            print(f"Error connecting to the database: {e}")

    def execute_query(self, query, params=None):
        try:
            self.cursor.execute(query, params)
        except Exception as e:
            print(f"Error executing query: {e}")

    def fetch_all(self):
        return self.cursor.fetchall()

    def commit(self):
        self.connection.commit()

    def rollback(self):
        self.connection.rollback()

    def close_connection(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()


with open('solves_count.sql', 'r') as file:
    solves_count_sql = file.read()

with open('comments_count.sql', 'r') as file:
    comments_count_sql = file.read()

with open('user_solves.sql', 'r') as file:
    user_solves_sql = file.read()


database = PostgresDB(dbname='lab3', username='postgres', password='1000dollars')
database.connect()

database.execute_query(solves_count_sql)
print(database.fetch_all())

database.execute_query(comments_count_sql)
print(database.fetch_all())

database.execute_query(user_solves_sql)
print(database.fetch_all())

database.close_connection()
