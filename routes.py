from flask import request, jsonify
from app import app, auth
from services import employee_service

@app.route('/employee/<int:id>', methods=['GET'])
@auth.login_required
def get_employee(id):
    employee = employee_service.get_employee_by_id(id)
    return jsonify(employee.to_dict())

@app.route('/employee', methods=['POST'])
@auth.login_required
def add_employee():
    employee_data = request.json
    new_employee = employee_service.add_new_employee(employee_data)
    return jsonify(new_employee)

@app.route('/employee/history/<int:id>', methods=['GET'])
@auth.login_required
def get_employee_history(id):
    history = employee_service.get_employee_history(id)
    return jsonify(history)

@app.route('/employees', methods=['GET'])
@auth.login_required
def get_employees():
    filters = {
        'project_name': request.args.get('project_name'),
        'lob_name': request.args.get('lob_name')
    }
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))
    employees = employee_service.get_employees(filters, page, limit)
    return jsonify([employee.to_dict() for employee in employees])
