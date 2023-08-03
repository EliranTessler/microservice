import requests
from flask import request, jsonify
from ..models.employee_model import Employee, db

class EmployeeService:
    @staticmethod
    def create_employee():
        data = request.get_json()
        name = data.get('name')
        country = data.get('country')
        city = data.get('city')
        salary_usd = data.get('salary_usd')

        employee = Employee(name=name, country=country, city=city, salary_usd=salary_usd)
        db.session.add(employee)
        db.session.commit()

        return jsonify(employee.as_dict()), 201
    
    @staticmethod
    def get_employee(id):
        employee = Employee.query.get(id)
        if employee:
            return jsonify(employee.as_dict())
        else:
            return jsonify({'error': 'Employee not found.'}), 404
        
    @staticmethod
    def update_employee(id):
        employee = Employee.query.get(id)
        if not employee:
            return jsonify({'error': 'Employee not found.'}), 404
        
        data = request.get_json()
        employee.name = data.get('name', employee.name)
        employee.country = data.get('country', employee.country)
        employee.city = data.get('city', employee.city)
        employee.salary_usd = data.get('salary_usd', employee.salary_usd)

        db.session.commit()
        return jsonify(employee.as_dict()), 201
    
    @staticmethod
    def delete_employee(id):
        employee = Employee.query.get(id)
        if employee:
            db.session.delete(employee)
            db.session.commit()
            return jsonify({'message': 'Employee deleted successfully.'})
        else:
            return jsonify({'error': 'Employee not found.'}), 404

    @staticmethod
    def convert_currency(salary_usd):
        api_key = 'your_api_key'
        conversion_url = f'https://free.currencyconverterapi.com/api/v6/convert?q=USD_ILS&compact=ultra&apiKey={api_key}'
        
        response = requests.get(conversion_url)
        if response.status_code == 200:
            conversion_rate = response.json().get('USD_ILS')
            if conversion_rate:
                salary_ils = salary_usd * conversion_rate
                return salary_ils
        return None