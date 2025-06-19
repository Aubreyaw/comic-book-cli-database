# - lib/category.py
from models.__init__ import CURSOR, CONN

class Category:
    
    def __init__(self, name):
        self.name = name

    @staticmethod
    def _validate_str(entry):
        if not isinstance(entry, str):
            raise TypeError("Entry must be a string")
        if len(entry) == 0:
            raise ValueError("Must not be left empty")

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._validate_str(name)
        self._name = name

    @classmethod
    def create_table(cls):
        sql = """
             CREATE TABLE IF NOT EXISTS categories (
             id INTEGER PRIMARY KEY,
             name TEXT
             )
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    def save(self):
        sql = """
             INSERT INTO categories (name)
             VALUES (?)
        """
        CURSOR.execute(sql, (self.name,))
        CONN.commit()
        self.id = CURSOR.lastrowid

    def delete(self):
        sql = """
             DELETE FROM categories
             WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

    @classmethod
    def create(cls, name):
        category = cls(name)
        category.save()
        return category

    @classmethod
    def instance_from_db(cls, row):
        id, name = row
        cls._validate_str(name)
        category = cls(name)
        category.id = id
        return category
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM categories
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM categories
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
             SELECT *
             FROM categories
             WHERE name = ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def get_collectibles(self):
        from models.collectible import Collectible
        sql = """
             SELECT *
             FROM collectibles
             WHERE category_id = ?
        """
        CURSOR.execute(sql, (self.id,))
        rows = CURSOR.fetchall()
        return [Collectible.instance_from_db(row) for row in rows]