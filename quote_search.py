from mongoengine import connect
from models import Author, Quote

def search_quotes():
    while True:
        command = input("Input command (name: [name]| tag: [tag] | tags: [tag1, tag2] | exit): ").strip()
        
        if command.startswith("name:"):
            author_name = command.split("name:")[1].strip()
            quotes = Quote.objects(author__fullname=author_name)
            for quote in quotes:
                print(f"{quote.author.fullname}: {quote.quote}")

        elif command.startswith("tag:"):
            tag = command.split("tag:")[1].strip()
            quotes = Quote.objects(tags=tag)
            for quote in quotes:
                print(f"{quote.author.fullname}: {quote.quote}")

        elif command.startswith("tags:"):
            tags = command.split("tags:")[1].strip().split(",")
            quotes = Quote.objects(tags__in=tags)
            for quote in quotes:
                print(f"{quote.author.fullname}: {quote.quote}")

        elif command == "exit":
            print("Bye bye.")
            break

        else:
            print("Unknown command. Try again.")

search_quotes()
