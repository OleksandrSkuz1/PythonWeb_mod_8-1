import json

# Завантаження цитат з JSON файлу
with open('quotes.json', 'r', encoding='utf-8') as file:
    quotes = json.load(file)

# Функція для пошуку цитат за тегом
def search_by_tag(tag):
    results = [quote for quote in quotes if tag in quote['tags']]
    return results

# Функція для пошуку цитат за ім'ям автора
def search_by_author(author):
    results = [quote for quote in quotes if author.lower() in quote['author'].lower()]
    return results

# Функція для пошуку цитат за набором тегів
def search_by_tags(tags):
    tags_list = tags.split(',')
    results = [quote for quote in quotes if any(tag in quote['tags'] for tag in tags_list)]
    return results

# Головний цикл програми
while True:
    command = input("Введіть команду (наприклад, 'tag:life', 'name:Albert Einstein', 'tags:life,live' або 'exit'): ")

    # Пошук за тегом
    if command.startswith('tag:'):
        tag = command.split(':')[1]
        results = search_by_tag(tag)
        for quote in results:
            print(quote['quote'])

    # Пошук за ім'ям автора
    elif command.startswith('name:'):
        author = command.split(':')[1]
        results = search_by_author(author)
        for quote in results:
            print(quote['quote'])

    # Пошук за набором тегів
    elif command.startswith('tags:'):
        tags = command.split(':')[1]
        results = search_by_tags(tags)
        for quote in results:
            print(quote['quote'])

    # Вихід з програми
    elif command == 'exit':
        break

    # Невідома команда
    else:
        print("Невідома команда. Будь ласка, спробуйте ще раз.")
