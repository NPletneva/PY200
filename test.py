import peewee
from newCatalog import BookUtil


def showBook(name):
    """Show the book by name"""
    if isinstance(name, str):
        for i in BookUtil.select().where(BookUtil.name == name & BookUtil.catalog_id == 3).get():
            return i.catalog_id, i.id, i.name, i.author, i.year
    else:
        raise TypeError("Parameter name - str")




showBook()