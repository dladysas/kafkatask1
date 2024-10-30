from confluent_kafka import Producer

producer_config = {
    'bootstrap.servers': 'localhost:9092'
}
producer = Producer(producer_config)

def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

for i in range(5):
    producer.produce('topic_name', key=f'key-{i}', value=f'message-{i}', callback=delivery_report)
    producer.flush()
