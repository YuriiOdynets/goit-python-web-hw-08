import json
import pika
import connect
from faker import Faker
from models import Contact

rabbitmq_host = 'localhost'
rabbitmq_port = 5672

connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host, port=rabbitmq_port))
channel = connection.channel()
channel.queue_declare(queue='email_queue')

# Генерація фейкових контактів
fake = Faker()
num_contacts = 10

for _ in range(num_contacts):
    contact = Contact(
        fullname=fake.name(),
        email=fake.email(),
        phone=fake.phone_number(),
        address=fake.address(),
        company=fake.company()
    )
    contact.save()

    # Поміщення повідомлення у чергу RabbitMQ
    message = {'contact_id': str(contact.id)}
    channel.basic_publish(exchange='', routing_key='email_queue', body=json.dumps(message))

print("Контакти створені та повідомлення надіслані у чергу.")
connection.close()