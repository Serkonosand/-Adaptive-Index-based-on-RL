import psycopg2
from psycopg2 import sql

class Database:
    
    tables = {}

    def __init__(self):
        self.dbname = "rltestdb"
        self.username = "postgre"
        self.pswd = "ssh0511"
        self.hst = "127.0.0.1"
        self.port = "5432"
        self.idxname = ""
        self.tablename = ""
    
    def __get_table_indexed_columns(self, table): 
        """
        try:
            conn = psycopg2.connet(database=self.dbname, user=self.username, password=self.pswd, host=self.hst, port=self.port)
            cursor = conn.cursor()
        """
        pass
                        

    def modif_index(self, table, type, column):
        cmd0 = sql.SQL("DROP INDEX {idx_name}").format(idx_name=sql.Identifier(self.idxname))
        if type = 'HASH':
            cmd1 = sql.SQL("CREATE INDEX {idx_name} ON {table_name} USING HASH ({column_name})").format(
                idx_name=sql.Identifier(self.idxname), 
                table_name = sql.Identifier(table), 
                column_name = sql.Identifier(column))
        else:
            cmd1 = sql.SQL("CREATE INDEX {idx_name} ON {table_name} ({column_name})").format(
                idx_name=sql.Identifier(self.idxname), 
                table_name = sql.Identifier(table), 
                column_name = sql.Identifier(column))
        try:
            conn = psycopg2.connet(database=self.dbname, user=self.username, password=self.pswd, host=self.hst, port=self.port)
            cursor = conn.cursor()
            cursor.execute(cmd0)
            cursor.execute(cmd1)
            conn.commit()
            cur.close()
            conn.close()
            print('Dropped index on (%s) %s' % (table, column) + '\n')
            print('Created index on (%s) %s' % (table, column))
        except psycopg2.Error as ex:
            print("Didn't drop index on %s, error %s" % (column, ex) + '\n')
            print("Didn't create index on %s, error %s" % (column, ex))
    
    def create_table(self):
        conn = psycopg2.connet(database=self.dbname, user=self.username, password=self.pswd, host=self.hst, port=self.port)
        cur = conn.cursor()
        cmd = sql.SQL("CREATE TABLE {table_name}(id serial PRIMARY KEY, num integer,data varchar)").format(
            table_name = sql.Identifier(self.tablename)
        )
        cur.execute(cmd)
        # insert one item
        cur.execute("INSERT INTO test(num, data)VALUES(%s, %s)", (1, 'aaa'))
        cur.execute("INSERT INTO test(num, data)VALUES(%s, %s)", (2, 'bbb'))
        cur.execute("INSERT INTO test(num, data)VALUES(%s, %s)", (3, 'ccc'))
        cur.execute("SELECT * FROM test;")
        rows = cur.fetchall()        # all rows in table
        print(rows)
        for i in rows:
            print(i)
        conn.commit()
        cur.close()
        conn.close()
        return self.tablename
    
    def create_index_table(self, table, type, column):
        if type = 'HASH':
            cmd1 = sql.SQL("CREATE INDEX {idx_name} ON {table_name} USING HASH ({column_name})").format(
                idx_name=sql.Identifier(self.idxname), 
                table_name = sql.Identifier(table), 
                column_name = sql.Identifier(column))
        else:
            cmd1 = sql.SQL("CREATE INDEX {idx_name} ON {table_name} ({column_name})").format(
                idx_name=sql.Identifier(self.idxname), 
                table_name = sql.Identifier(table), 
                column_name = sql.Identifier(column))
        conn = psycopg2.connet(database=self.dbname, user=self.username, password=self.pswd, host=self.hst, port=self.port)
        cursor = conn.cursor()
        cursor.execute(cmd1)
        conn.commit()
        cur.close()
        conn.close()
        print('Created index on (%s) %s' % (table, column))


 if __name__ == '__main__':
    pass       