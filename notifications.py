from kafka import KafkaConsumer
import json

kafka_broker = 'localhost:9092'
topic_name = 'employee-events'  

consumer = KafkaConsumer(
    topic_name,
    bootstrap_servers=kafka_broker,
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

def handle_employee_event(event_data):
    print(f"Received Employee Event: {event_data}")

def run_consumer():
    for message in consumer:
        event_data = message.value
        handle_employee_event(event_data)

if __name__ == "__main__":
    run_consumer()
