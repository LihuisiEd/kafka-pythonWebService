from flask import Flask, render_template
from kafka import KafkaConsumer
from threading import Thread

app = Flask(__name__)
messages = []

def consume_messages():
    consumer = KafkaConsumer('test',
                             bootstrap_servers='localhost:9092',
                             auto_offset_reset='earliest',
                             enable_auto_commit=True,
                             group_id='my-group')
    
    for message in consumer:
        messages.append(message.value.decode('utf-8'))

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

if __name__ == '__main__':
    consumer_thread = Thread(target=consume_messages)
    consumer_thread.start()
    app.run()
