# many_to_many.py

class Book:
    def __init__(self, title):
        self.title = title
        self._authors = []      # private list of authors
        self._contracts = []    # list of Contract objects

    def authors(self):
        return self._authors

    def contracts(self):
        return self._contracts


class Author:
    def __init__(self, name):
        self.name = name
        self._books = []
        self._contracts = []

    def books(self):
        return self._books

    def contracts(self):
        return self._contracts

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum(contract.royalties for contract in self._contracts)


class Contract:
    all = []  # store all contracts

    def __init__(self, author, book, date, royalties):
        # Type validations
        if not isinstance(author, Author):
            raise Exception("author must be an Author object")
        if not isinstance(book, Book):
            raise Exception("book must be a Book object")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, int):
            raise Exception("royalties must be an integer")

        # Assign attributes
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        # Link author ↔ book
        if book not in author.books():
            author._books.append(book)
        if author not in book.authors():
            book._authors.append(author)

        # Add this contract to author's contracts
        author._contracts.append(self)
        # Add this contract to book's contracts
        book._contracts.append(self)

        # Add this contract to the global list
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]
