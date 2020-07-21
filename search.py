# -*- coding: utf-8 -*-
"""Final task DEV-PY200"""
from model import *


class Search:
    def __init__(self, catalog_id):
        self.catalog_id = catalog_id

    def searchByName(self, name):
        """Search by word in book name"""
        for index in Book.select().where((Book.catalog_id == self.catalog_id) & Book.name.contains(name)):
            print(index.id, index.name, index.author, index.year)

    def searchByAuthor(self, author):
        """Search by author in library"""
        for index in Book.select().where((Book.author == author) & (Book.catalog_id == self.catalog_id)):
            print(index.id, index.name, index.author, index.year)

    def searchByYear(self, year):
        """Search by year"""
        for index in Book.select().where((Book.year == year) & (Book.catalog_id == self.catalog_id)):
            print(index.id, index.name, index.author, index.year)
