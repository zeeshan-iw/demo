{
    'name': 'Book Store',
    'version': '1.0',
    'summary': 'Manage books in a simple bookstore',
    'author': 'Zeeshan',
    'category': 'Library',
    'depends': ['base'],
    'data': [
        'views/book_views.xml',
        'security/ir.model.access.csv',
    ],
    'test': [
        'tests/test_book_model.py',
    ],
    'installable': True,
    'application': True,
    'external_dependencies': {
        'python': ['requests'],
    },
}
