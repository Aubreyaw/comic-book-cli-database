# - lib/character.py
from models.__init__ import CURSOR, CONN
from models.comic import Comic

class Character():

    all = []

    def __init__(self, name, secret_identity, universe):
        self._name = name
        self._secret_identity = secret_identity
        self._universe = universe

    @staticmethod
    def _validate_entry(entry):
        if not isinstance(entry, str):
            raise TypeError("Entry must be a string")
        if len(entry) == 0:
            raise ValueError("Must not be left empty")     

    def __repr__(self):   
        return f"{self.name}, {self.secret_identity}, {self.universe}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, updated_name):
        self._validate_entry(updated_name)
        self._name = updated_name

    @property
    def secret_identity(self):
        return self._secret_identity

    @secret_identity.setter
    def secret_identity(self, updated_secret_identity):
        self._validate_entry(updated_secret_identity)
        self._secret_identity = updated_secret_identity

    @property
    def universe(self):
        return self._universe

    @universe.setter
    def universe(self, updated_universe):
        self._validate_entry(updated_universe)
        self._universe = updated_universe

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS characters (
            id INTEGER PRIMARY KEY,
            name TEXT,
            secret_identity TEXT,
            universe TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS characters;
        """
        CURSOR.execute(sql)
        CONN.commit()     

    def save(self):
        sql = """
            INSERT INTO characters (name, secret_identity, universe)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.secret_identity, self.universe))
        CONN.commit()
    
        self.id = CURSOR.lastrowid
        Character.all.append(self)

    def delete(self):
        sql = """
            DELETE FROM characters
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        Character.all.remove(self)

    @classmethod
    def instance_from_db(cls, row):
        id, name, secret_identity, universe = row

        Character._validate_entry(name)
        Character._validate_entry(secret_identity)
        Character._validate_entry(universe)

        for character in cls.all:
            if character.id == id:
                return character
        
        character = cls(name, secret_identity, universe)
        character.id = id
        cls.all.append(character)
        return character

    @classmethod
    def create(cls, name, secret_identity, universe):
        character = cls(
            name,
            secret_identity,
            universe
        )
        character.save()
        return character

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM characters
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM characters
        """
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def get_comics_by_secret_identity(cls, secret_identity):
        sql = """
            SELECT comics.id, comics.title, comics.main_character, comics.issue_number, comics.universe, comics.price 
            FROM comics
            JOIN characters ON comics.main_character = characters.name
            WHERE characters.secret_identity = ?
        """
        CURSOR.execute(sql, (secret_identity,))
        rows = CURSOR.fetchall()
        return [Comic.instance_from_db(row) for row in rows]