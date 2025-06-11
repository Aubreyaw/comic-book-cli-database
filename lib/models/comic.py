# - lib/comic.py
from models.__init__ import CURSOR, CONN

class Comic:

    all = []

    @staticmethod
    def _validate_entry(entry):
        if not isinstance(entry, str):
            raise TypeError("Entry must be a string")
        if len(entry) == 0:
            raise ValueError("Must not be left empty")
        
    @staticmethod
    def _validate_price(price):
        if not isinstance(price, float):
            raise TypeError("Price must be a decimal number")
        if price < 0:
            raise ValueError("Must enter a price")
        
    @staticmethod
    def _validate_issue_number(issue_number):
        if not isinstance(issue_number, int):
            raise TypeError("Issue number must be an integer")
        if issue_number < 0:
            raise ValueError("Must include an issue number") 

    def __init__(self, title, main_character, issue_number, universe, price):
        self.title = title
        self.main_character = main_character
        self.issue_number = issue_number
        self.universe = universe
        self.price = price

    def __repr__(self):
        return f"{self.title}, {self.main_character}, {self.issue_number}, {self.universe}, price: {self.price:.2f}"
    
    @property
    def issue_number(self):
        return self._issue_number
    
    @issue_number.setter
    def issue_number(self, number):
        self._validate_issue_number(number)
        self._issue_number = number

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        self._validate_entry(title)
        self._title = title

    @property
    def main_character(self):
        return self._main_character
    
    @main_character.setter
    def main_character(self, value):
        self._validate_entry(value)
        self._main_character = value

    @property
    def universe(self):
        return self._universe
    
    @universe.setter
    def universe(self, value):
        self._validate_entry(value)
        self._universe = value

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, updated_price):
        self._validate_price(updated_price)
        self._price = updated_price
    
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS comics (
            id INTEGER PRIMARY KEY,
            title TEXT,
            main_character TEXT,
            issue_number INTEGER,
            universe TEXT,
            price REAL
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS comics;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO comics (title, main_character, issue_number, universe, price)
            VALUES (?, ?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.title, self.main_character, self.issue_number, self.universe, self.price))
        CONN.commit()

        self.id = CURSOR.lastrowid
        Comic.all.append(self)
        
    def delete(self):
        sql = """
            DELETE FROM comics
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        Comic.all.remove(self)

    @classmethod
    def instance_from_db(cls, row):
        id, title, main_character, issue_number, universe, price = row
        
        Comic._validate_entry(title)
        Comic._validate_entry(main_character)
        Comic._validate_issue_number(issue_number)
        Comic._validate_entry(universe)
        Comic._validate_price(price)
        
        for comic in cls.all:
            if comic.id == id:
                return comic
            
        comic = cls(title, main_character, issue_number, universe, price)
        comic.id = id
        cls.all.append(comic)
        return comic
            
    @classmethod
    def create(cls, title, main_character, issue_number, universe, price):
        comic = cls(
            title,
            main_character,
            issue_number,
            universe,
            price
        )
        comic.save()
        return comic

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM comics
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM comics
        """
        CURSOR.execute(sql)
        rows = CURSOR.fetchall() 
        return [cls.instance_from_db(row) for row in rows]
    
    def update_price(self):
        sql = """
            UPDATE comics
            SET price = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.price, self.id))
        CONN.commit()