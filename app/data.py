from os import getenv

from certifi import where
from dotenv import load_dotenv
from MonsterLab import Monster
from pandas import DataFrame
from pymongo import MongoClient


class Database:

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
