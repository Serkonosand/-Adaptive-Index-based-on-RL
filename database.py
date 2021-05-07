import psycopg2
from psycopg2 import sql
import time


class Database:

    # tables = {}

    def __init__(self):
        self.dbname = "rltestdb"
        self.username = "postgres"
        self.pswd = "ssh0511"
        self.hst = "127.0.0.1"
        self.port = "5432"
        self.idxname = "idx_0"
        self.tablename = "test0"

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
        try:
            conn = psycopg2.connect(database=self.dbname, user=self.username, password=self.pswd, host=self.hst,
                                    port=self.port)
            cur = conn.cursor()
            print("connect correct!\n")
            cmd = sql.SQL("CREATE TABLE {table_name}(id serial PRIMARY KEY, num integer,data varchar)").format(
                table_name=sql.Identifier(self.tablename)
            )
            cur.execute(cmd)
            print("create table correct!\n")
            # insert one item
            cur.execute("INSERT INTO test0(num, data)VALUES(%s, %s)", (1, 'aaa'))
            cur.execute("INSERT INTO test0(num, data)VALUES(%s, %s)", (2, 'bbb'))
            cur.execute("INSERT INTO test0(num, data)VALUES(%s, %s)", (3, 'ccc'))
            cur.execute("INSERT INTO test0(num, data)VALUES(%s, %s)", (4, 'ddd'))
            cur.execute("INSERT INTO test0(num, data)VALUES(%s, %s)", (5, 'eee'))
            cur.execute("INSERT INTO test0(num, data)VALUES(%s, %s)", (6, 'fff'))
            cur.execute("INSERT INTO test0(num, data)VALUES(%s, %s)", (7, 'ggg'))
            print("create query correct!\n")
            cur.execute("SELECT * FROM test0;")
            print("get query correct!\n")
            rows = cur.fetchall()  # all rows in table
            print(rows)
            for i in rows:
                print(i)
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
            print('sth error')

    def query_excute(self, query):
        try:
            conn = psycopg2.connect(database=self.dbname, user=self.username, password=self.pswd, host=self.hst,
                                    port=self.port)
            cursor = conn.cursor()
            print("connect correct!\n")
            # time start
            start_time = time.perf_counter()
            cursor.execute(query)
            excuteTime = time.perf_counter() - start_time
            print(excuteTime)
            # time end
            rows = cursor.fetchall()  # all rows in table
            conn.commit()
            cursor.close()
            conn.close()
            print("get query correct!\n")
            for i in rows:
                print(i)
            print('\n')
            return excuteTime
        except psycopg2.Error as ex:
            print('sth error \n')


if __name__ == '__main__':
    db = Database()
    #    db.create_table()
    #    db.create_index_table('test0', 'b+tree', 'data')
    #    db.modif_index('test0', 'b+tree', 'data')
    # Q = "SELECT * FROM test0 WHERE data = 'bbb' "
    # start_time = time.process_time()
    # excuteTime = db.query_excute(Q)
    # excuteTime = time.process_time() - start_time
    # print(excuteTime)
