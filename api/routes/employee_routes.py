from flask import Blueprint
from ..services.employee_service import EmployeeService
from kafka import KafkaProducer
import json

employee_ms = Blueprint('employee', __name__)

producer = KafkaProducer(bootstrap_servers='localhost:9092')

@employee_ms.route('/employees', methods=['POST'])
def create_employee():
    employee_data = EmployeeService.create_employee()
    message = {'action': 'create', 'employee': employee_data[0].json}
    producer.send('employee-events', value=json.dumps(message).encode('utf-8'))
    return employee_data

@employee_ms.route('/employees/<int:id>', methods=['GET'])
def get_employee(id):
    employee_data = EmployeeService.get_employee(id)
    message = {'action': 'read', 'employee': employee_data.json}
    producer.send('employee-events', value=json.dumps(message).encode('utf-8'))
    return employee_data

@employee_ms.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    employee_data = EmployeeService.update_employee(id)
    message = {'action': 'update', 'employee': employee_data[0].json}
    producer.send('employee-events', value=json.dumps(message).encode('utf-8'))
    return employee_data

@employee_ms.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    return EmployeeService.delete_employee(id)
