from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify, abort
from flaskext.mysql import MySQL

app = Flask(__name__)

app.config["SECRET_KEY"] = "8d3c2c136be85cf7de1435eb"
app.config["MYSQL_DATABASE_HOST"] = "localhost"
app.config["MYSQL_DATABASE_USER"] = "root"
app.config["MYSQL_DATABASE_PASSWORD"] = "root"
app.config["MYSQL_DATABASE_DB"] = "dbmsproj"

mysql = MySQL(app)

@app.route('/fetchBB')
def fetchBB():
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM BloodBank")
    data = cursor.fetchall()
    return render_template('fetchBloodBank.html', data=data)


@app.route('/fetchDonor')
def fetchDonor():
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM Donor")
    data = cursor.fetchall()
    return render_template('fetchDonor.html', data=data)

@app.route('/fetchDonation')
def fetchDonation():
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM Donation")
    data = cursor.fetchall()
    return render_template('fetchDonation.html', data=data)

@app.route('/fetchPatient')
def fetchPatient():
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM Patient")
    data = cursor.fetchall()
    return render_template('fetchPatient.html', data=data)

@app.route('/fetchStaffMember')
def fetchStaffMember():
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM StaffMember")
    data = cursor.fetchall()
    return render_template('fetchStaffMember.html', data=data)

@app.route('/fetchResult')
def fetchResult():
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM BloodTestResult")
    data = cursor.fetchall()
    return render_template('fetchResult.html', data=data)


@app.route("/")
def home_page():
	return render_template("home.html")

@app.route("/entry")
def record_entry():
	return render_template("record_entry.html")

@app.route("/fetchEntry")
def fetchEntry():
	return render_template("fetchEntry.html")

@app.route("/BloodBank", methods=['GET', 'POST'])
def BloodBank():
    if request.method == 'POST':
        try:
            Name = request.form['Name']
            Location = request.form['Location']
            ContactInfo = request.form['ContactInfo']
            CurrentInventoryLevel = request.form['CurrentInventoryLevel']
            MaxCapacity = request.form['MaxCapacity']
            Address = request.form['Address']

            if not Name or not Location or not ContactInfo or not CurrentInventoryLevel or not MaxCapacity or not Address:
                flash('Please fill in all the fields', 'error')
                return render_template('BloodBank.html')

            # Assuming you have configured your MySQL connection elsewhere in your code
            cursor = mysql.get_db().cursor()
            cursor.execute('INSERT INTO BloodBank (Name, Location, ContactInfo, CurrentInventoryLevel, MaxCapacity, Address) VALUES (%(Name)s, %(Location)s, %(ContactInfo)s, %(CurrentInventoryLevel)s, %(MaxCapacity)s, %(Address)s);', {'Name': Name, 'Location': Location, 'ContactInfo': ContactInfo, 'CurrentInventoryLevel': CurrentInventoryLevel, 'MaxCapacity': MaxCapacity, 'Address': Address})
            mysql.get_db().commit()

            flash('Blood bank information added successfully', 'success')
            return render_template('BloodBank.html')

        except Exception as e:
            flash(f'An error occurred: {str(e)}', 'error')
            return render_template('BloodBank.html')

    return render_template('BloodBank.html')


		

@app.route("/Donor", methods=['GET', 'POST'])
def Donor():
    if request.method == 'POST':
        try:
            FirstName = request.form['FirstName']
            LastName = request.form['LastName']
            DateOfBirth = request.form['DateOfBirth']
            Gender = request.form.get('Gender')
            BloodType = request.form['BloodType']
            ContactInfo = request.form['ContactInfo']
            LastDonationDate = request.form['LastDonationDate']
            HealthStatus = request.form['HealthStatus']
            EligibilityStatus = request.form['EligibilityStatus']
            RegistrationDate = request.form['RegistrationDate']
            Address = request.form['Address']

            if not FirstName or not LastName or not DateOfBirth or not Gender or not BloodType or not ContactInfo or not LastDonationDate or not HealthStatus or not EligibilityStatus or not RegistrationDate or not Address:
                flash('Please fill in all the fields', 'error')
                return render_template('Donor.html')

            # Assuming you have configured your MySQL connection elsewhere in your code
            cursor = mysql.get_db().cursor()
            cursor.execute('INSERT INTO Donor (FirstName, LastName, DateOfBirth, Gender, BloodType, ContactInfo, LastDonationDate, HealthStatus, EligibilityStatus, RegistrationDate, Address) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);', (FirstName, LastName, DateOfBirth, Gender, BloodType, ContactInfo, LastDonationDate, HealthStatus, EligibilityStatus, RegistrationDate, Address))
            mysql.get_db().commit()

            flash('Donor information added successfully', 'success')
            return render_template('Donor.html')

        except Exception as e:
            flash(f'An error occurred: {str(e)}', 'error')
            return render_template('Donor.html')

    return render_template('Donor.html')

@app.route("/StaffMember", methods=['GET', 'POST'])
def StaffMember():
    if request.method == 'POST':
        try:
            FirstName = request.form['FirstName']
            LastName = request.form['LastName']
            Position = request.form['Position']
            ContactInfo = request.form['ContactInfo']

            if not FirstName or not LastName or not Position or not ContactInfo:
                flash('Please fill in all the fields', 'error')
                return render_template('StaffMember.html')

            # Assuming you have configured your MySQL connection elsewhere in your code
            cursor = mysql.get_db().cursor()
            cursor.execute('INSERT INTO StaffMember (FirstName, LastName, Position, ContactInfo) VALUES (%s, %s, %s, %s);', (FirstName, LastName, Position, ContactInfo))
            mysql.get_db().commit()

            flash('Staff member information added successfully', 'success')
            return render_template('StaffMember.html')

        except Exception as e:
            flash(f'An error occurred: {str(e)}', 'error')
            return render_template('StaffMember.html')

    return render_template('StaffMember.html')

@app.route("/Donation", methods=['GET', 'POST'])
def Donation():
    if request.method == 'POST':
        try:
            DonorID = request.form['DonorID']
            DonationDate = request.form['DonationDate']
            BloodType = request.form['BloodType']
            DonationCenter = request.form['DonationCenter']
            QuantityDonated = request.form['QuantityDonated']
            BloodTestResults = request.form['BloodTestResults']
            DonorHealthInfo = request.form['DonorHealthInfo']
            StaffMember = request.form['StaffMember']
            StorageConditions = request.form['StorageConditions']
            ExpiryDate = request.form['ExpiryDate']

            if not DonorID or not DonationDate or not BloodType or not DonationCenter or not QuantityDonated or not BloodTestResults or not DonorHealthInfo or not StaffMember or not StorageConditions or not ExpiryDate:
                flash('Please fill in all the fields', 'error')
                return render_template('Donation.html')

            # Assuming you have configured your MySQL connection elsewhere in your code
            cursor = mysql.get_db().cursor()
            cursor.execute('INSERT INTO Donation (DonorID, DonationDate, BloodType, DonationCenter, QuantityDonated, BloodTestResults, DonorHealthInfo, StaffMember, StorageConditions, ExpiryDate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);', (DonorID, DonationDate, BloodType, DonationCenter, QuantityDonated, BloodTestResults, DonorHealthInfo, StaffMember, StorageConditions, ExpiryDate))
            mysql.get_db().commit()

            flash('Donation information added successfully', 'success')
            return render_template('Donation.html')

        except Exception as e:
            flash(f'An error occurred: {str(e)}', 'error')
            return render_template('Donation.html')

    return render_template('Donation.html')

@app.route("/Patient", methods=['GET', 'POST'])
def Patient():
    if request.method == 'POST':
        try:
            FirstName = request.form['FirstName']
            LastName = request.form['LastName']
            DateOfBirth = request.form['DateOfBirth']
            Gender = request.form.get('Gender')
            BloodType = request.form['BloodType']
            MedicalCondition = request.form['MedicalCondition']
            ContactInfo = request.form['ContactInfo']
            DoctorInfo = request.form['DoctorInfo']
            Address = request.form['Address']
            TransfusionDate = request.form['TransfusionDate']
            TransfusionDetails = request.form['TransfusionDetails']

            if not FirstName or not LastName or not DateOfBirth or not Gender or not BloodType or not MedicalCondition or not ContactInfo or not DoctorInfo or not Address or not TransfusionDate or not TransfusionDetails:
                flash('Please fill in all the fields', 'error')
                return render_template('Patient.html')

            # Assuming you have configured your MySQL connection elsewhere in your code
            cursor = mysql.get_db().cursor()
            cursor.execute('INSERT INTO Patient (FirstName, LastName, DateOfBirth, Gender, BloodType, MedicalCondition, ContactInfo, DoctorInfo, Address, TransfusionDate, TransfusionDetails) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);', (FirstName, LastName, DateOfBirth, Gender, BloodType, MedicalCondition, ContactInfo, DoctorInfo, Address, TransfusionDate, TransfusionDetails))
            mysql.get_db().commit()

            flash('Patient information added successfully', 'success')
            return render_template('Patient.html')

        except Exception as e:
            flash(f'An error occurred: {str(e)}', 'error')
            return render_template('Patient.html')

    return render_template('Patient.html')

@app.route("/BloodTestResult", methods=['GET', 'POST'])
def BloodTestResult():
    if request.method == 'POST':
        try:
            DonationID = request.form['DonationID']
            TestDate = request.form['TestDate']
            TestType = request.form['TestType']
            TestResult = request.form['TestResult']

            if not DonationID or not TestDate or not TestType or not TestResult:
                flash('Please fill in all the fields', 'error')
                return render_template('BloodTestResult.html')

            # Assuming you have configured your MySQL connection elsewhere in your code
            cursor = mysql.get_db().cursor()
            cursor.execute('INSERT INTO BloodTestResult (DonationID, TestDate, TestType, TestResult) VALUES (%s, %s, %s, %s);', (DonationID, TestDate, TestType, TestResult))
            mysql.get_db().commit()

            flash('Blood test result added successfully', 'success')
            return render_template('BloodTestResult.html')

        except Exception as e:
            flash(f'An error occurred: {str(e)}', 'error')
            return render_template('BloodTestResult.html')

    return render_template('BloodTestResult.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)