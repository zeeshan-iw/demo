from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError


class TestBookModel(TransactionCase):

    def setUp(self):
        super().setUp()
        self.Book = self.env['book_store.book']

    def test_create_book(self):
        book = self.Book.create({
            'title': 'Test Book',
            'author': 'Test Author',
            'price': 10.0,
        })
        self.assertEqual(book.title, 'Test Book')
        self.assertEqual(book.author, 'Test Author')
        self.assertAlmostEqual(book.price, 10.0)

    def test_create_book_without_title(self):
        with self.assertRaises(Exception):
            self.Book.create({
                'author': 'Author Without Title',
                'price': 5.0,
            })

    def test_create_book_with_negative_price(self):
        # Assuming your model raises ValidationError on negative price
        with self.assertRaises(ValidationError):
            self.Book.create({
                'title': 'Negative Price Book',
                'author': 'Author',
                'price': -10.0,
            })

    def test_write_book(self):
        book = self.Book.create({
            'title': 'Old Title',
            'author': 'Old Author',
            'price': 20.0,
        })
        book.write({
            'title': 'New Title',
            'price': 25.0,
        })
        self.assertEqual(book.title, 'New Title')
        self.assertAlmostEqual(book.price, 25.0)

    def test_search_books(self):
        # Create multiple books
        self.Book.create({'title': 'Book One', 'author': 'Author A', 'price': 10})
        self.Book.create({'title': 'Book Two', 'author': 'Author B', 'price': 15})
        books = self.Book.search([('price', '>', 12)])
        self.assertTrue(all(book.price > 12 for book in books))
        self.assertEqual(len(books), 1)
