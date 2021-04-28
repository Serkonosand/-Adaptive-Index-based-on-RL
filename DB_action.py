from database import Database


class Action:
    def __init__(self):
        # Database instance
        self.db = Database()

    def excute(self, table, type):
        self.db.modif_index(table, type)