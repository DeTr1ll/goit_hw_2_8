import json
from mongoengine import connect
from models import Author, Quote 

connect(db="HumiderCluster", host="mongodb+srv://Humider:4U7m5q80uf0UaSZo@humidercluster.5in6y.mongodb.net/?retryWrites=true&w=majority&appName=HumiderCluster")

def load_authors(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for item in data:
            author = Author(
                fullname=item['fullname'],
                born_date=item.get('born_date'),
                born_location=item.get('born_location'),
                description=item.get('description')
            )
            author.save()

def load_quotes(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for item in data:
            author = Author.objects(fullname=item['author']).first()
            if author:
                quote = Quote(
                    tags=item.get('tags', []),
                    author=author,
                    quote=item['quote']
                )
                quote.save()

load_authors('authors.json')
load_quotes('qoutes.json')