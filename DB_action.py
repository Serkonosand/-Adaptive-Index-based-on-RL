from database import Database


class Action:
    def __init__(self):
        # Database instance
        self.db = Database()

    def modif(self, table, type, column):
        self.db.modif_index(table, type, column)

    def create(self, table, type, column):
        self.db.create_index_table(table, type, column)