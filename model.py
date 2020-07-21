# -*- coding: utf-8 -*-
"""Final task DEV-PY200"""

from peewee import *

db = SqliteDatabase('library.db')


def createTables():
    """create tables"""
    db.connect()
    Catalog.create_table()
    Book.create_table()


class Catalog(Model):
    """Model~table"""
    id = IntegerField(primary_key=True)
    name = CharField()

    class Meta:
        database = db


class Book(Model):
    """Model~table.


    Attitude between models by catalog_id."""
    catalog_id = ForeignKeyField(Catalog, backref='books', lazy_load=True)
    id = IntegerField(unique=True)
    name = CharField()
    author = CharField()
    year = IntegerField()

    class Meta:
        database = db
