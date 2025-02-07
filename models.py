from app import db

class Employee(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    hire_date = db.Column(db.Date)

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'phone': self.phone,
            'hire_date': self.hire_date
        }

class EmployeeHistory(db.Model):
    __tablename__ = 'employee_history'
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'))
    job_title = db.Column(db.String(100))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    project_name = db.Column(db.String(100))
    lob_name = db.Column(db.String(100))

    def to_dict(self):
        return {
            'id': self.id,
            'employee_id': self.employee_id,
            'job_title': self.job_title,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'project_name': self.project_name,
            'lob_name': self.lob_name
        }

class EmployeeEducationCertification(db.Model):
    __tablename__ = 'employee_education_certification'
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'))
    degree = db.Column(db.String(100))
    institution = db.Column(db.String(100))
    certification = db.Column(db.String(100))
    completion_date = db.Column(db.Date)

    def to_dict(self):
        return {
            'id': self.id,
            'employee_id': self.employee_id,
            'degree': self.degree,
            'institution': self.institution,
            'certification': self.certification,
            'completion_date': self.completion_date
        }
