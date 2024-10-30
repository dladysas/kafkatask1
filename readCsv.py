import pandas as pd
from confluent_kafka import Producer
import json

# Load data
df = pd.read_csv("application_record.csv")

# Kafka producer configuration
producer_config = {
    'bootstrap.servers': 'localhost:9092'
}
producer = Producer(producer_config)

# Produce messages with IDs as keys
topic_name = 'credit_card_approvals'
for _, row in df.iterrows():
    # Convert each row to JSON format
    message = json.dumps(row.to_dict())  # Explicitly use json.dumps here
    key = str(row['ID'])  # Use 'ID' column as the message key

    # Produce message to Kafka topic
    producer.produce(topic_name, key=key, value=message)
    producer.flush()

print("Produced messages with duplicate IDs successfully.")
