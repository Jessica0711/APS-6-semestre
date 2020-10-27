import sqlite3


class ConnectionFactory():

    def getConnection(self):
        try:
            self.conn = sqlite3.connect('aps.db')
            return self.conn
        except Exception as inst:
            print(type(inst))
            print(inst.args)
            print(inst)

    def closeConnection(self):
        self.conn.close()
