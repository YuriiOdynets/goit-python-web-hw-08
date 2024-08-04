import json
import pika
from models import Contact
import connect

rabbitmq_host = 'localhost'
rabbitmq_port = 5672

connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host, port=rabbitmq_port))
channel = connection.channel()
channel.queue_declare(queue='email_queue')

def send_email(contact):
    # Функція-заглушка для імітації відправлення email
    print(f"Sending email to {contact.email}")

def callback(ch, method, properties, body):
    message = json.loads(body)
    contact_id = message['contact_id']
    contact = Contact.objects(id=contact_id).first()
    if contact and not contact.message_sent:
        send_email(contact)
        contact.message_sent = True
        contact.save()
        print(f"Email sent to {contact.fullname} ({contact.email})")

channel.basic_consume(queue='email_queue', on_message_callback=callback, auto_ack=True)

print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()