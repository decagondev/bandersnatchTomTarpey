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
    load_dotenv()
    database = MongoClient(getenv("DB_URL"), tlsCAFile=where())["Database"]

    def __init__(self, collection: str):
        """Initializes the Database class with the specified collection.

        Args:
            collection (str): The name of the collection to work with, passed as string.
        """
        self.collection = self.database[collection]

    def seed(self, amount):
        """Seeds the collection with a specified number of random Monster records.

        Args:
            amount (int): The number of Monster records to generate and insert.

        Returns:
            Formatted string to report if seed was successful.
        """
        pass

    def reset(self):
        """Resets the collection by removing all records.

        Returns:
            Formatted string providing boolean about reset success.
        """      
        pass

    def count(self) -> int:
        """Counts the number of records in the collection.

        Returns:
            int: Number of records in the collection.
        """
        pass

    def dataframe(self) -> DataFrame:
        """Retrieves data from the collection and returns it as a pandas DataFrame.

        Returns:
            DataFrame: A pandas DataFrame containing the collection data.
        """
        pass

    def html_table(self) -> str:
        """Generates an HTML table from the data for display in flask app.

        Returns:
            str: An HTML table as a string, or 'None' if the collection is empty.
        """
        pass
