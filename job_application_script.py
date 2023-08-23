import sqlite3

def insert_application(company_id, position, date_submitted):
   query = "INSERT INTO JobApplications (company_id, position, date_submitted) VALUES (?, ?, ?)"
   values = (company_id, position, date_submitted)
   cursor.execute(query, values)
   connection.commit()

def get_applications_by_company(company_id):
   query = "SELECT * FROM JobApplications WHERE company_id = ?"
   cursor.execute(query, (company_id,))
   applications = cursor.fetchall()
   return applications


# More functions and code

connection = sqlite3.connect('job_applications.db')
cursor = connection.cursor()

try:
    # Insert a new job application
    insert_application(1, 'Software Developer', '2023-08-15')

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
