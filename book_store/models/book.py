from odoo import models, fields, api
import requests
import json
from datetime import datetime, date
import logging

_logger = logging.getLogger(__name__)


class Book(models.Model):
    _name = 'book_store.book'
    _description = 'Book'

    title = fields.Char(string='Title', required=True)
    author = fields.Char(string='Author')
    price = fields.Float(string='Price')
    published_date = fields.Date(string='Published Date')

    def fetch_book_from_api(self):
        try:
            api_url = "https://randomuser.me/api/"

            response = requests.get(api_url, timeout=10)
            response.raise_for_status()

            data = response.json()

            if data and 'results' in data and len(data['results']) > 0:
                user_data = data['results'][0]
                name = user_data['name']

                first_name = name.get('first', 'Unknown').title()
                last_name = name.get('last', 'Person').title()

                import random
                title_formats = [
                    f"The Adventures of {first_name} {last_name}",
                    f"{first_name}'s Journey",
                    f"The Life of {first_name}",
                    f"{last_name} Chronicles",
                    f"Memories of {first_name} {last_name}",
                    f"The Story of {first_name}",
                    f"{first_name} and the Mystery",
                    f"Tales from {last_name}",
                ]

                title = random.choice(title_formats)

                hardcoded_authors = [
                    'John Smith', 'Jane Doe', 'Michael Johnson', 'Sarah Wilson',
                    'David Brown', 'Lisa Davis', 'Tom Miller', 'Amy Garcia',
                    'Robert Taylor', 'Emily Anderson', 'James Wilson', 'Maria Rodriguez'
                ]

                author = random.choice(hardcoded_authors)
                price = round(random.uniform(15.0, 45.0), 2)
                published_date = date.today()

                new_book = self.create({
                    'title': title,
                    'author': author,
                    'price': price,
                    'published_date': published_date,
                })

                return {
                    'type': 'ir.actions.client',
                    'tag': 'display_notification',
                    'params': {
                        'title': 'Success!',
                        'message': f'Book "{title}" by {author} has been added successfully!',
                        'type': 'success',
                        'sticky': False,
                    }
                }
            else:
                return {
                    'type': 'ir.actions.client',
                    'tag': 'display_notification',
                    'params': {
                        'title': 'Error!',
                        'message': 'No data received from API',
                        'type': 'danger',
                        'sticky': False,
                    }
                }

        except Exception as e:
            _logger.error(f"Error fetching random name: {str(e)}")
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': 'API Error!',
                    'message': f'Failed to fetch data from API: {str(e)}',
                    'type': 'danger',
                    'sticky': False,
                }
            }
