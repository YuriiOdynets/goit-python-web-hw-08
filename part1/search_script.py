def search_quotes():
    while True:
        query = input("Введіть запит (name: ім'я автора, tag: тег, tags: тег1,тег2, exit): ")
        if query.startswith("name:"):
            author_name = query.split(":", 1)[1].strip()
            author = Author.objects(fullname=author_name).first()
            if author:
                quotes = Quote.objects(author=author)
                for q in quotes:
                    print(q.quote)
            else:
                print(f"Автор {author_name} не знайдений.")
        
        elif query.startswith("tag:"):
            tag = query.split(":", 1)[1].strip()
            quotes = Quote.objects(tags=tag)
            for q in quotes:
                print(q.quote)
        
        elif query.startswith("tags:"):
            tags = query.split(":", 1)[1].split(",")
            quotes = Quote.objects(tags__in=tags)
            for q in quotes:
                print(q.quote)
        
        elif query == "exit":
            break
        
        else:
            print("Неправильний формат запиту.")

if __name__ == "__main__":
    import connect
    from models import Author, Quote
    search_quotes()