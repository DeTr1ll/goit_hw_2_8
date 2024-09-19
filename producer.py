import pika
from faker import Faker
from models import Contact

fake = Faker()

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='email_queue')

def generate_contacts(count):
    for _ in range(count):
        contact = Contact(
            fullname=fake.name(),
            email=fake.email(),
            phone=fake.phone_number(),
            address=fake.address()
        )
        contact.save()
        print(f"Contact created: {contact.fullname}, {contact.email}")

        channel.basic_publish(
            exchange='',
            routing_key='email_queue',
            body=str(contact.id)
        )
        print(f"Sent to queue contant ID: {contact.id}")

generate_contacts(10)

connection.close()
