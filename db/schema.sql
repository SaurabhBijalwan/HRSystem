CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    phone VARCHAR(20),
    hire_date DATE
);

CREATE TABLE employee_history (
    id SERIAL PRIMARY KEY,
    employee_id INT REFERENCES employees(id),
    job_title VARCHAR(100),
    start_date DATE,
    end_date DATE,
    project_name VARCHAR(100),
    lob_name VARCHAR(100)
);

CREATE TABLE employee_education_certification (
    id SERIAL PRIMARY KEY,
    employee_id INT REFERENCES employees(id),
    degree VARCHAR(100),
    institution VARCHAR(100),
    certification VARCHAR(100),
    completion_date DATE
);
