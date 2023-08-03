from flask import Blueprint
from ..services.employee_service import EmployeeService

employee_ms = Blueprint('employee', __name__)

@employee_ms.route('/employees', methods=['POST'])
def create_employee():
    return EmployeeService.create_employee()

@employee_ms.route('/employees/<int:id>', methods=['GET'])
def get_employee(id):
    return EmployeeService.get_employee(id)

@employee_ms.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    return EmployeeService.update_employee(id)

@employee_ms.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    return EmployeeService.delete_employee(id)
