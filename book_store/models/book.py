from odoo import models, fields

class Book(models.Model):
    _name = 'book_store.book'
    _description = 'Book'

    title = fields.Char(string='Title', required=True)
    author = fields.Char(string='Author')
    price = fields.Float(string='Price')
    published_date = fields.Date(string='Published Date')
