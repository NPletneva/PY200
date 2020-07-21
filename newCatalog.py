from model import Catalog, Book


class CatalogUtil():
    def create(self, name):
        Catalog.create(name=name, id=Catalog.select().count() + 1)

    def list(self):
        result = []
        for item in Catalog.select(Catalog.id, Catalog.name):
            result.append({'id': item.id, 'name': item.name})
        return result

    def current(self, id):
        result = []
        for item in Catalog.select(Catalog.id, Catalog.name).where(Catalog.id == id):
            result.append({'id': item.id, 'name': item.name})
        return result[0]


class BookUtil():
    def create(self, name, author, year, catalog_id):
        return Book.create(name=name, author=author, year=year, catalog_id=catalog_id, id=Book.select().count() + 1)
