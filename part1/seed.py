import json
import connect
from models import Author, Quote

with open ("authors.json") as f:
    authors_data = json.load(f)

with open ("quotes.json") as f:
    quotes_data = json.load(f)

authors_map = {}
for author_data in authors_data:
    author=Author(
        fullname=author_data["fullname"],
        born_date = author_data["born_date"],
        born_location = author_data["born_location"],
        description = author_data["description"]
    )
    author.save()
    authors_map[author.fullname] = author

for quote_data in quotes_data:
    author = authors_map[quote_data['author']]
    quote = Quote(
        tags=quote_data['tags'],
        author=author,
        quote=quote_data['quote']
    )
    quote.save()