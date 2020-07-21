# -*- coding: utf-8 -*-
"""Final task DEV-PY200"""
import json
import random

from model import *

# method 1 serialization
dataBookJSON = json.dumps({'books': [
    {'name': 'Атлант расправил плечи',
     'author': 'Айн Рэнд',
     'year': '1994'},
    {'name': 'Руслан и Людмила',
     'author': 'Александр Пушкин',
     'year': '1989'},
    {'name': 'Преступление и наказание',
     'author': 'Федор Достоевский ',
     'year': '2000'},
    {'name': 'Когда Ницше плакал',
     'author': ' Ирвин Ялом',
     'year': '2010'}]})

jsonLoad = json.loads(dataBookJSON)
data = jsonLoad['books']

# method 2 from file
# path = '/Users/npletnyova/PycharmProjects/final200/files/catalog.json'
# with open(path, "r") as f:
#     jsonLoad = json.load(f)
#     data = jsonLoad['books']

def createTables():
    """create tables"""
    db.connect()
    Catalog.create_table()
    Book.create_table()
    Catalog.create(name='Мой каталог', id=1)


def fillInTheTables():
    """Fill in the tables with random data"""
    for element in data:
        name = element['name']
        author = element['author']
        year = element['year']
        Book.create(name=name, author=author, year=year, catalog_id=1, id=output_book_id)


createTables()
fillInTheTables()
