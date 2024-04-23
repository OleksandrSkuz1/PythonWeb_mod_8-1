import json
from datetime import datetime
from models import connection, Author, Quote

# Підключення до MongoDB
connection()

with open("authors.json", "r", encoding="utf-8") as file:
    authors_data = json.load(file)

for author_data in authors_data:
    born_date = datetime.strptime(author_data["born_date"], "%B %d, %Y")
    existing_author = Author.objects(fullname=author_data["fullname"]).first()
    if existing_author:
        print(f'Author "{author_data["fullname"]}" already exists.')
        continue

    author = Author(
        fullname=author_data["fullname"],
        born_date=born_date,
        born_location=author_data["born_location"],
        description=author_data["description"],
    )
    author.save()


with open("quotes.json", "r", encoding="utf-8") as file:
    quotes_data = json.load(file)

for quote_data in quotes_data:
    author = Author.objects(fullname=quote_data["author"]).first()
    quote = Quote(tags=quote_data["tags"], author=author, quote=quote_data["quote"])
    quote.save()

