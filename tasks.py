from celery import Celery
import pika
import time

# tasks.py is the reciever pulls msgs off queue
app = Celery('tasks', broker='amqp://guest@some-rabbit//')

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='some-rabbit'))
channel = connection.channel()

channel.queue_declare(queue='hello')

print ' [*] Waiting for messages. To exit press CTRL+C'

@app.task
def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)
    time.sleep( body.count('.') )
    print " [x] Done"

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

channel.start_consuming()
