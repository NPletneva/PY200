from cmd import Cmd

from actions import Actions
from model import createTables
from newCatalog import CatalogUtil
from search import Search


# createTables()


class AppPrompt(Cmd):

    def __init__(self, intro="Welcome!\n Type ? to list commands", prompt="> "):
        Cmd.__init__(self)

        self.intro = intro
        self.prompt = prompt
        self.doc_header = "App commands (type help <topic>):"

    def do_exit(self, inp):
        print("Bye")
        return True

    def help_exit(self):
        print("exit the app")

    def do_catalog(self, inp):
        CatalogPrompt().cmdloop()

    def help_catalog(self):
        print("catalog actions")

    do_EOF = do_exit
    help_EOF = help_exit


class CatalogPrompt(Cmd):
    catalog_util = CatalogUtil()

    def __init__(self, intro="\nWork with catalog CLI", prompt="Catalog > "):
        Cmd.__init__(self)

        self.intro = intro
        self.prompt = prompt
        self.doc_header = "Catalog commands (type help <topic>):"

    def do_exit(self, inp):
        print("Bye")
        return True

    def help_exit(self):
        print("exit the app")

    do_EOF = do_exit
    help_EOF = help_exit

    def do_add(self, inp):
        self.catalog_util.create(name=inp)

    def do_list(self, inp):
        for catalog in self.catalog_util.list():
            print(catalog)

    def do_select(self, inp):
        item = self.catalog_util.current(int(inp))
        BookPrompt(catalog=item).cmdloop()


class BookPrompt(Cmd):

    def __init__(self, catalog=None):
        Cmd.__init__(self)

        self.intro = f'\n [{catalog["name"]}] Work with book CLI'
        self.prompt = "Book > "
        self.doc_header = "Book commands (type help <topic>):"
        print(catalog['id'])
        self.actions = Actions(catalog['id'])
        self.search = Search(catalog['id'])

    def do_exit(self, inp):
        print("Bye")
        return True

    def help_exit(self):
        print("exit the app")

    do_EOF = do_exit
    help_EOF = help_exit

    def do_addBook(self, inp):
        [name, author, year] = inp.split(';')
        self.actions.addBook(name, author, int(year))

    def do_addBookByJSON(self, inp):
        self.actions.addBookByJSON(some_json=inp)

    def do_addBookByCVS(self, inp):
        self.actions.addBookByCVS(some_csv=inp)

    def do_changeBookByName(self, inp):
        [source_name, target_name] = inp.split(';')
        self.actions.changeBookByName(source_name, target_name)

    def do_changeBookByAuthor(self, inp):
        [source_author, target_author] = inp.split(';')
        self.actions.changeBookByAuthor(source_author, target_author)

    def do_changeBookByYear(self, inp):
        [source_year, target_year] = inp.split(';')
        self.actions.changeBookByYear(int(source_year), int(target_year))

    def do_searchByName(self, inp):
        self.search.searchByName(name=inp)

    def do_searchByAuthor(self, inp):
        self.search.searchByAuthor(author=inp)

    def do_searchByYear(self, inp):
        self.search.searchByYear(year=inp)


if __name__ == '__main__':
    AppPrompt().cmdloop()
