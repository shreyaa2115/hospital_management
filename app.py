from flask import Flask, render_template, request, jsonify
import mysql.connector
import os
from datetime import datetime  # Import datetime module

app = Flask("hospital-management", template_folder="templates", static_folder="static")

# Test route to verify app is running
@app.route('/test')
def test():
    return "The application is running!"

def get_db_connection():
    """Establish a connection to the MySQL database."""
    return mysql.connector.connect(
        host="127.0.0.1",  
        user="root",      
        password="sowmi",  
        database="HospitalManagement"  
    )

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/doctors')
def doctors():
    return render_template('doctors.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            # Extract form data
            id_number = request.form['id_number']
            name = request.form['name']
            age = request.form['age']
            gender = request.form['gender']
            department = request.form['department']
            login_timing = request.form['login_timing']

            # Store data in the database
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO login_records (IDNumber, Name, Age, Gender, Department, LoginTime)
                VALUES (%s, %s, %s, %s, %s, %s)
            ''', (id_number, name, age, gender, department, login_timing))
            conn.commit()
            conn.close()

            return "Login data stored successfully!"
        except Exception as e:
            return f"An error occurred: {e}"
    return render_template('login.html')

@app.route('/register', methods=['GET'])
def register():
    return render_template('login.html')

@app.route('/login/doctors', methods=['GET', 'POST'])
def login_doctors():
    if request.method == 'POST':
        try:
            # Debugging: Log form data
            print("Form Data:", request.form)

            # Validate form data
            required_fields = ['id_number', 'name', 'age', 'gender', 'department', 'login_timing']
            form_data = dict(request.form)  # Create a mutable copy of request.form
            for field in required_fields:
                if field not in form_data or not form_data[field]:
                    if field == 'login_timing':
                        # Provide a valid default datetime value for login_timing if missing
                        form_data['login_timing'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    else:
                        return f"Missing or invalid field: {field}", 400

            # Extract form data
            id_number = form_data['id_number']
            name = form_data['name']
            age = form_data['age']
            gender = form_data['gender']
            department = form_data['department']
            login_timing = form_data['login_timing']

            # Check for duplicate IDNumber
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('SELECT COUNT(*) FROM Doctors WHERE IDNumber = %s', (id_number,))
            if cursor.fetchone()[0] > 0:
                conn.close()
                return f"Error: IDNumber {id_number} already exists in the Doctors table.", 400

            # Store data in the Doctors table
            cursor.execute('''
                INSERT INTO Doctors (IDNumber, Name, Age, Gender, Department, LoginTime)
                VALUES (%s, %s, %s, %s, %s, %s)
            ''', (id_number, name, age, gender, department, login_timing))
            conn.commit()
            conn.close()

            return render_template('login_success.html', user_type="Doctor", details=form_data)
        except Exception as e:
            return f"An error occurred: {e}", 500
    return render_template('login_form.html', user_type="Doctor")

@app.route('/login/nurses', methods=['GET', 'POST'])
def login_nurses():
    if request.method == 'POST':
        try:
            # Debugging: Log form data
            print("Form Data:", request.form)

            # Validate form data
            required_fields = ['name', 'id_number', 'age', 'gender', 'department', 'login_timing']
            form_data = dict(request.form)  # Create a mutable copy of request.form
            for field in required_fields:
                if field not in form_data or not form_data[field]:
                    if field == 'login_timing':
                        # Provide a valid default datetime value for login_timing if missing
                        form_data['login_timing'] = datetime.now().strftime('%H:%M:%S')
                    else:
                        return f"Missing or invalid field: {field}", 400

            # Extract form data
            name = form_data['name']
            id_number = form_data['id_number']
            age = form_data['age']
            gender = form_data['gender']
            department = form_data['department']
            login_timing = form_data['login_timing']

            # Check for duplicate IDNumber
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('SELECT COUNT(*) FROM Nurses WHERE IDNumber = %s', (id_number,))
            if cursor.fetchone()[0] > 0:
                conn.close()
                return f"Error: IDNumber {id_number} already exists in the Nurses table.", 400

            # Store data in the Nurses table
            cursor.execute('''
                INSERT INTO Nurses (Name, IDNumber, Age, Gender, Department, LoginTime)
                VALUES (%s, %s, %s, %s, %s, %s)
            ''', (name, id_number, age, gender, department, login_timing))
            conn.commit()
            conn.close()

            return render_template('login_success.html', user_type="Nurse", details=form_data)
        except Exception as e:
            return f"An error occurred: {e}", 500
    return render_template('login_form.html', user_type="Nurse")

@app.route('/login/employees', methods=['GET', 'POST'])
def login_employees():
    if request.method == 'POST':
        try:
            # Debugging: Log form data
            print("Form Data:", request.form)

            # Validate form data
            required_fields = ['name', 'id_number', 'age', 'gender', 'department', 'login_timing']
            form_data = dict(request.form)  # Create a mutable copy of request.form
            for field in required_fields:
                if field not in form_data or not form_data[field]:
                    if field == 'login_timing':
                        # Provide a valid default datetime value for login_timing if missing
                        form_data['login_timing'] = datetime.now().strftime('%H:%M:%S')
                    else:
                        return f"Missing or invalid field: {field}", 400

            # Extract form data
            name = form_data['name']
            id_number = form_data['id_number']
            age = form_data['age']
            gender = form_data['gender']
            department = form_data['department']
            login_timing = form_data['login_timing']

            # Check for duplicate IDNumber
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('SELECT COUNT(*) FROM Employees WHERE IDNumber = %s', (id_number,))
            if cursor.fetchone()[0] > 0:
                conn.close()
                return f"Error: IDNumber {id_number} already exists in the Employees table.", 400

            # Store data in the Employees table
            cursor.execute('''
                INSERT INTO Employees (Name, IDNumber, Age, Gender, Department, LoginTime)
                VALUES (%s, %s, %s, %s, %s, %s)
            ''', (name, id_number, age, gender, department, login_timing))
            conn.commit()
            conn.close()

            return render_template('login_success.html', user_type="Employee", details=form_data)
        except Exception as e:
            return f"An error occurred: {e}", 500
    return render_template('login_form.html', user_type="Employee")

if __name__ == '__main__':
    app.run(debug=True, port=8080)