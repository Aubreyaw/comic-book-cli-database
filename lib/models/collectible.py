
from models.__init__ import CURSOR, CONN
from models.category import Category

class Collectible():

    def __init__(self, name, universe, est_value, category_id):
        self.name = name
        self.universe = universe
        self.est_value = est_value
        self.category_id = category_id

    @staticmethod
    def _validate_str(value):
        if not isinstance(value, str):
            raise TypeError("Value must be a string")
        if len(value) == 0:
            raise ValueError("Must not be left empty")    

    @staticmethod
    def _validate_int(value):
        if not isinstance(value, int):
            raise TypeError("Value must be an integer")
        if value < 0:
            raise ValueError("Must include a value")   
        
    @staticmethod
    def _validate_float(value):
        if not isinstance(value, float):
            raise TypeError("Value must be a decimal")
        if value < 0:
            raise ValueError("Value must be non-negative")
         
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._validate_str(name)
        self._name = name

    @property
    def universe(self):
        return self._universe

    @universe.setter
    def universe(self, universe):
        self._validate_str(universe)
        self._universe = universe

    @property
    def est_value(self):
        return self._est_value
    
    @est_value.setter
    def est_value(self, est_value):
        self._validate_float(est_value)
        self._est_value = est_value

    @property
    def category_id(self):
        return self._category_id
    
    @category_id.setter
    def category_id(self, category_id):
        self._validate_int(category_id)
        self._category_id = category_id
   
    @property
    def category(self):
        return Category.find_by_id(self.category_id)
    

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS collectibles (
            id INTEGER PRIMARY KEY,
            name TEXT,
            universe TEXT,
            est_value FLOAT,
            category_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES categories(id)
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS collectibles;
        """
        CURSOR.execute(sql)
        CONN.commit()     

    def save(self):
        sql = """
            INSERT INTO collectibles (name, universe, est_value, category_id)
            VALUES (?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.universe, self.est_value, self.category_id))
        CONN.commit()
        self.id = CURSOR.lastrowid

    def update(self):
        sql = """
            UPDATE collectibles
            SET name = ?, universe = ?, est_value = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.universe, self.est_value, self.id))
        CONN.commit()

    def delete(self): 
        sql = """
            DELETE FROM collectibles
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

    @classmethod
    def instance_from_db(cls, row):
        id, name, universe, est_value, category_id = row

        cls._validate_str(name)
        cls._validate_str(universe)
        cls._validate_float(est_value)
        cls._validate_int(category_id)
        
        collectible = cls(name, universe, est_value, category_id)
        collectible.id = id
        return collectible
 
    @classmethod
    def create(cls, name, universe, est_value, category_id):
        collectible = cls(
            name,
            universe,
            est_value,
            category_id
        )
        collectible.save()
        return collectible

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM collectibles
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
             SELECT *
             FROM collectibles
             WHERE name = ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM collectibles
        """
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    def display_details(self):
        return {
            "name": self.name,
            "universe": self.universe,
            "estimated value": f"${self.est_value}"
        }