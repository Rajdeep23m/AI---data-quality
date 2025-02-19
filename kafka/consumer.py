from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'test-topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    value_deserializer=lambda v: json.loads(v.decode('utf-8')) if v else None
)

print("Listening for messages...")

for message in consumer:
    if message.value:
        print(f"Received message: {message.value}")
    else:
        print("Received an empty message.")
