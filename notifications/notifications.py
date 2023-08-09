from kafka import KafkaConsumer
import json

kafka_broker = 'kafka1:9092'
topic_name = 'employee-events'  

consumer = KafkaConsumer(
    topic_name,
    bootstrap_servers=kafka_broker,
    api_version=(2,0,2),
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

def handle_employee_event(event_data):
    print(f"Received Employee Event: {event_data}", flush=True)

def run_consumer():
    try:
        for message in consumer:
            event_data = message.value
            handle_employee_event(event_data)
    except Exception as e:
        print(f"Consumer failed: {e}", flush=True)
    finally:
        consumer.close()
        print("Consumer closed", flush=True)

if __name__ == "__main__":
    print("Notications server is running")
    run_consumer()
