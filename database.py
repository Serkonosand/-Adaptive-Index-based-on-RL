import psycopg2
from psycopg2 import sql
import time
FILEPATH = '.\\testdata\\city.txt'

class Database:

    # tables = {}

    def __init__(self):
        self.dbname = "rltestdb"
        self.username = "postgres"
        self.pswd = "ssh0511"
        self.hst = "127.0.0.1"
        self.port = "5432"
        self.idxname = "idx_1"
        self.tablename = "city"

    def modif_index(self, table, type, column):
        cmd0 = sql.SQL("DROP INDEX {idx_name}").format(idx_name=sql.Identifier(self.idxname))
        if type == 'hash':
            cmd1 = sql.SQL("CREATE INDEX {idx_name} ON {table_name} USING HASH ({column_name})").format(
                idx_name=sql.Identifier(self.idxname),
                table_name=sql.Identifier(table),
                column_name=sql.Identifier(column))
        else:
            cmd1 = sql.SQL("CREATE INDEX {idx_name} ON {table_name} ({column_name})").format(
                idx_name=sql.Identifier(self.idxname),
                table_name=sql.Identifier(table),
                column_name=sql.Identifier(column))
        try:
            conn = psycopg2.connect(database=self.dbname, user=self.username, password=self.pswd, host=self.hst,
                                    port=self.port)
            cursor = conn.cursor()
            print("connect correct!\n")
            cursor.execute(cmd0)
            cursor.execute(cmd1)
            conn.commit()
            cursor.close()
            conn.close()
            print('Dropped index on (%s) %s' % (table, column) + '\n')
            print('Created index on (%s) %s' % (table, column))
        except psycopg2.Error as ex:
            print("Didn't drop index on %s, error %s" % (column, ex) + '\n')
            print("Didn't create index on %s, error %s" % (column, ex))

    def create_table(self):
        cmd = sql.SQL("CREATE TABLE {table_name}(id serial PRIMARY KEY, city_name varchar, population int, "
                      "country_name varchar, state_name varchar)").format(
            table_name=sql.Identifier(self.tablename)
        )
        with open(FILEPATH, 'r') as f:
            q = f.read()
        print(q)
        try:
            conn = psycopg2.connect(database=self.dbname, user=self.username, password=self.pswd, host=self.hst,
                                    port=self.port)
            cur = conn.cursor()
            print("connect correct!\n")
            cur.execute(sql.SQL("DROP TABLE IF EXISTS {table_name}").format(table_name=sql.Identifier(self.tablename)))
            cur.execute(cmd)
            print("create table correct!\n")
            # insert one item
            cur.execute(q)
            print("create query correct!\n")
            conn.commit()
            cur.close()
            conn.close()
        except psycopg2.Error as ex:
            print("sth error!\n")
        return self.tablename

    def create_index_table(self, table, type, column):
        if type == 'hash':
            cmd1 = sql.SQL("CREATE INDEX {idx_name} ON {table_name} USING HASH ({column_name})").format(
                idx_name=sql.Identifier(self.idxname),
                table_name=sql.Identifier(table),
                column_name=sql.Identifier(column))
        else:
            cmd1 = sql.SQL("CREATE INDEX {idx_name} ON {table_name} ({column_name})").format(
                idx_name=sql.Identifier(self.idxname),
                table_name=sql.Identifier(table),
                column_name=sql.Identifier(column))
        try:
            conn = psycopg2.connect(database=self.dbname, user=self.username, password=self.pswd, host=self.hst,
                                    port=self.port)
            cursor = conn.cursor()
            print("connect correct!\n")
            cursor.execute(cmd1)
            conn.commit()
            cursor.close()
            conn.close()
            print('Created index on (%s) %s' % (table, column))
        except psycopg2.Error as ex:
            print('sth error: ' + ex.pgcode)

    def query_execute(self, query):
        try:
            conn = psycopg2.connect(database=self.dbname, user=self.username, password=self.pswd, host=self.hst,
                                    port=self.port)
            cursor = conn.cursor()
            print("connect correct!\n")
            # time start
            start_time = time.perf_counter()
            cursor.execute(query)
            rows = cursor.fetchall()  # all rows in table
            executeTime = time.perf_counter() - start_time
            # time end
            conn.commit()
            cursor.close()
            conn.close()
            print("get query correct!\n")
            """
            for i in rows:
                print(i)
            print('\n')
            """
            return executeTime
        except psycopg2.Error as ex:
            print('sth error \n' + ex.pgcode)


if __name__ == '__main__':
    db = Database()
    db.modif_index('city', 'b+tree', 'population')
#    Q = "SELECT * FROM city"
    # start_time = time.process_time()
    # executeTime = db.query_execute(Q)
    # executeTime = time.process_time() - start_time
#    print(db.query_execute(Q))
