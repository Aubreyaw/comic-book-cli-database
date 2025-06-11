from models.__init__ import CURSOR, CONN

class Distributor:

    all = []

    def __init__(self, name):
        self.name = name
        Distributor.all.append(self)

    def __repr__(self):
        return f"<Distributor {self.name}:>"