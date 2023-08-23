import sqlite3
from email_sender import send_encouraging_email  # Import the function from email_sender.py


def insert_company(name):
    query = "INSERT INTO Companies (name) VALUES (?)"
    values = (name,)
    cursor.execute(query, values)
    connection.commit()
    print("Company inserted successfully.")

def insert_application(company_id, position, date_submitted):
   query = "INSERT INTO JobApplications (company_id, position, date_submitted) VALUES (?, ?, ?)"
   values = (company_id, position, date_submitted)
   cursor.execute(query, values)
   connection.commit()



# More functions and code

connection = sqlite3.connect('job_applications.db')
cursor = connection.cursor()

try:
    # Insert a new company 
    insert_company("VHB")

    # Retrieve the ID of the newly inserted company
    cursor.execute("SELECT last_insert_rowid()")
    company_id = cursor.fetchone()[0]

    # Insert a new job application
    insert_application(company_id, "Data Architect", "2023-08-22")

    # Send an encouraging email
    send_encouraging_email("Data Architect", 'recipient@example.com')

    # Retrieve and print job applications for a specific company
    applications = get_applications_by_company(1)
    for application in applications:
        print("Application ID:", application[0])
        print("Position:", application[2])
        print("Date Submitted:", application[3])
        print("---")

except sqlite3.Error as error:
    print("Error:", error)

finally: 
    connection.close()
