from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

topic_name = "test-topic"
message = {"data": "Hello from AI-data-quality project!"}

producer.send(topic_name, value=message)
producer.flush()
print(f"Message sent to {topic_name}")
