# -*- coding: utf-8 -*-
"""Final task DEV-PY200"""
from model import *
import json
import csv
from newCatalog import BookUtil

file_json = '/Users/npletnyova/PycharmProjects/final200/files/addBook.json'
file_csv = r"/Users/npletnyova/PycharmProjects/final200/files/csvBook.csv"


class Actions:
    """Book actions by user"""

    def __init__(self, catalog_id):
        self.catalog_id = catalog_id

    def addBook(self, name, author, year):
        """Add the book to catalog"""
        if isinstance(name, str) and isinstance(author, str) and isinstance(year, int):
            return BookUtil().create(name=name, author=author, year=year, catalog_id=self.catalog_id)
        else:
            raise TypeError("Parameters: name,author - str; year - int")

    def addBookByJSON(self, some_json):
        """Add the book from JSON"""

        with open(some_json, "r") as file:
            bookDict = json.load(file)
        nameFromJSON = bookDict['name']
        authorFromJSON = bookDict['author']
        yearFromJSON = bookDict['year']
        if isinstance(nameFromJSON, str) and isinstance(authorFromJSON, str) and isinstance(yearFromJSON, int):
            return BookUtil().create(name=nameFromJSON, author=authorFromJSON, year=yearFromJSON,
                                     catalog_id=self.catalog_id)
        else:
            raise TypeError("Check json file! Parameters: name,author - str; year - int")

    def addBookByCVS(self, some_csv):
        """Add the book from CVS"""

        with open(some_csv, newline='') as f_obj:
            reader = csv.DictReader(f_obj, delimiter=';')
            for index in reader:
                return BookUtil().create(name=(index["name"]), author=(index["author"]), year=(index["year"]),
                                         catalog_id=self.catalog_id)

    def changeBookByName(self, source_name, target_name):
        """Change the book data: name"""

        if isinstance(target_name, str):
            new_name = (Book.update(name=target_name).where(
                ((Book.name == source_name) & (Book.catalog_id == self.catalog_id))).execute())
            return new_name
        else:
            raise TypeError("Parameter name - str")

    def changeBookByAuthor(self, source_author, target_author):

        """Change the book data: author"""
        if isinstance(target_author, str):
            new_author = (Book.update(author=target_author).where(
                ((Book.author == source_author) & (Book.catalog_id == self.catalog_id))).execute())
            return new_author
        else:
            raise TypeError("Parameter author - str")

    def changeBookByYear(self, source_year, target_year):

        """Change the book data: year"""
        if isinstance(target_year, int):
            new_year = (Book.update(year=target_year).where(
                ((Book.year == source_year) & (Book.catalog_id == self.catalog_id))).execute())
            return new_year
        else:
            raise TypeError("Parameter year - int")
