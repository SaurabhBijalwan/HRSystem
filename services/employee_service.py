from models import Employee, EmployeeHistory, EmployeeEducationCertification
from app import db

def get_employee_by_id(employee_id):
    return Employee.query.get(employee_id)

def add_new_employee(employee_data):
    history_data = employee_data.pop('history', [])
    education_data = employee_data.pop('education', [])
    
    new_employee = Employee(**employee_data)
    db.session.add(new_employee)
    db.session.commit()

    for history in history_data:
        history_record = EmployeeHistory(employee_id=new_employee.id, **history)
        db.session.add(history_record)

    for education in education_data:
        education_record = EmployeeEducationCertification(employee_id=new_employee.id, **education)
        db.session.add(education_record)

    db.session.commit()
    return new_employee.to_dict()

def get_employee_history(employee_id):
    history = EmployeeHistory.query.filter_by(employee_id=employee_id).all()
    education = EmployeeEducationCertification.query.filter_by(employee_id=employee_id).all()
    return {
        'history': [h.to_dict() for h in history],
        'education': [e.to_dict() for e in education]
    }

def get_employees(filters, page, limit):
    query = Employee.query
    if filters.get('project_name'):
        query = query.join(EmployeeHistory).filter(EmployeeHistory.project_name == filters['project_name'])
    if filters.get('lob_name'):
        query = query.join(EmployeeHistory).filter(EmployeeHistory.lob_name == filters['lob_name'])
    return query.paginate(page=page, per_page=limit, error_out=True).items
