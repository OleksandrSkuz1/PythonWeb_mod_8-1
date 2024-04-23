from models import connection, Author, Quote

# Підключення до MongoDB
connection()

def search_quotes(query):
    if query.startswith("name:"):
        author_name = query.split(":")[1].strip()
        author = Author.objects(fullname__icontains=author_name).first()
        if author:
            quotes = Quote.objects(author=author)
            return quotes
        else:
            return []

    elif query.startswith("tags:"):
        tags = [t.strip() for t in query.split(":")[1].split(",")]
        quotes = Quote.objects(tags__in=tags)
        return quotes

    elif query.startswith("tag:"):
        tag = query.split(":")[1].strip()
        quotes = Quote.objects(tags__icontains=tag)
        return quotes

    else:
        print("Invalid command. Please enter 'name', 'tag', 'tags', or 'exit'.")
        return []


if __name__ == "__main__":
    while True:
        user_input = input("Enter the command: ")
        if user_input.lower() == "exit":
            break

        quotes_result = search_quotes(user_input)
        if quotes_result:
            print(f"Number of quotes found: {len(quotes_result)}")
            for quote in quotes_result:
                author_name = quote.author.fullname
                quote_text = quote.quote
                tags = quote.tags
                print(f"Author: {author_name}, Quote: {quote_text}")
                print("Tags:")
                for tag in tags:
                    print(tag)
        else:
            print("No quotes found.")

