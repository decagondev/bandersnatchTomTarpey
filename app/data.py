from os import getenv

from certifi import where
from dotenv import load_dotenv
from MonsterLab import Monster
from pandas import DataFrame
from pymongo import MongoClient


class Database:
    """ Class to create and manage a Database that stores Monsters with their attributes.

    This class stores and manages Monster data in a MongoDB database. The class provides methods to
    seed the database with Monsters, reset the database, count the instances of monsters and extract
    data in different formats.

    Attributes:
        collection: A collection in a MongoDB database where you want the data stored.

    Methods:
        - __init__(self, collection: str): Initializes the Database class, with the collection name gives as a string.
        - seed(self, amount: int): Seeds the collection with specified amount of Monster instances
        - count(self) -> int: Counts and returns the number of monsters in the collection
        - dataframe(self) -> DataFrame: Returns data in the collection as a pandas DataFrame
        - html_table(self) -> str: Returns html table of the data for display

    Example:
        db = Database('Monsters')
        db.seed(1000)
        print(db.count())  # Output : 1000
        db.reset()
        print(db.count())  # Output : 0

    """
    def seed(self, amount):
        pass

    def reset(self):
        pass

    def count(self) -> int:
        pass

    def dataframe(self) -> DataFrame:
        pass

    def html_table(self) -> str:
        pass
