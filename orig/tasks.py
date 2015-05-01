from celery import Celery

app = Celery('tasks', broker='amqp://guest@some-rabbit//')

@app.task
def add(x, y):
    return x + y

