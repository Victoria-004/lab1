class Book:
    def __init__(self, title, price, numberOfPages, author, quantity, numberOfSales):
        self.title = title
        self.price = price
        self.numberOfPages = numberOfPages
        self.author = author
        self.quantity = quantity
        self.numberOfSales = numberOfSales

    def __str__(self):
        return f"Title: {self.title}, Price: {self.price}, Number of pages: {self.numberOfPages}, Author: {self.author}, Quantity: {self.quantity}, Number of Sales: {self.numberOfSales}"

class BookShop:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added book: {book.title}")

    def remove_book(self, book):
        for book in self.books:
            if book.title == title:
                self.book.remove(book)
                print(f"Removed book: {title}")
                return

    def top_books_by_price(self, top_n=5):
        sorted_books = sorted(self.books, key=lambda book: book.price, reverse=True)
        return sorted_books[:top_n]

    def top_books_by_sales(self, top_n=5):
        sorted_books = sorted(self.books, key=lambda book: book.numberOfSales, reverse=True)
        return sorted_books[:top_n]

    def get_books(self):
        print("Books in the shop:")
        for book in self.books:
            print(book)

def main():
        book1 = Book('Kobzar', 150, 296, 'Taras Shevchenko', 15, 8)
        book2 = Book('Little women', 190, 245, 'Louisa May', 23, 13)
        book3 = Book('Kristina', 360, 280, 'Stephen King', 18, 10)

        shop = BookShop()
        shop.add_book(book1)
        shop.add_book(book2)
        shop.add_book(book3)

        shop.get_books()

        print("\nTop books by price:")
        for book in shop.top_books_by_price():
            print(book)

        print("\nTop books by sales:")
        for book in shop.top_books_by_sales():
            print(book)

if __name__ == '__main__':
    main()





