import pika
from models import Contact

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='email_queue')

def send_email(contact):
    print(f"Sending contact email: {contact.fullname} ({contact.email})")
    return True

def callback(ch, method, properties, body):
    contact_id = body.decode()
    contact = Contact.objects(id=contact_id).first()

    if contact and not contact.message_sent:
        if send_email(contact):
            contact.message_sent = True
            contact.save()
            print(f"Message delivered and status updated for contact ID: {contact.id}")

channel.basic_consume(
    queue='email_queue',
    on_message_callback=callback,
    auto_ack=True
)

print('Waiting for message. To exit press CTRL+C')
channel.start_consuming()
