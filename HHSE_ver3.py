import streamlit as st
import sqlite3
from datetime import datetime
import pandas as pd

# Step 2: Initialize the SQLite database and schema
def initialize_db():
    conn = sqlite3.connect('HHSE.db')
    cursor = conn.cursor()


    # Create table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            Student_Name TEXT,
            Student_DOB DATE,
            Student_Address TEXT,
            School_District TEXT,
            Physician_Name TEXT,
            Physician_Phone_Number INTEGER,
            Type_Of_Authorizer TEXT,
            License_Num INTEGER,
            Physician_Address TEXT,
            Home_Hospital_Both TEXT,
            Consecutive_Recurring_Basis TEXT,
            Admittance_Date DATE,
            Regular_Reduced_Workload TEXT,
            Return_Date DATE
        )
    ''')

    # Parse Excel file and insert data into the database
    df = pd.read_excel('HHSE.xlsx')
    df.to_sql('students', conn, if_exists='append', index=False)

    conn.commit()
    conn.close()

# Step 3: Streamlit Application
def main():
    st.title('HHSE Data Viewer')
    conn = connect_to_db()

    # Insert new student
    st.write("Insert new student:")
    student_data = st.form(key='insert_student_form')
    student_name = student_data.text_input("Student Name")
    student_dob = student_data.date_input("Student DOB")
    student_address = student_data.text_input("Student Address")
    school_district = student_data.text_input("School District")
    physician_name = student_data.text_input("Physician Name")
    physician_phone_number = student_data.number_input("Physician Phone Number")
    type_of_authorizer = student_data.text_input("Type of Authorizer")
    license_num = student_data.number_input("License Number")
    physician_address = student_data.text_input("Physician Address")
    home_hospital_both = student_data.text_input("Home/Hospital/Both")
    consecutive_recurring_basis = student_data.text_input("Consecutive/Recurring/Basis")
    admittance_date = student_data.date_input("Admittance Date")
    regular_reduced_workload = student_data.text_input("Regular/Reduced Workload")
    return_date = student_data.date_input("Return Date")
    submit_button = student_data.form_submit_button("Submit")

    if submit_button:
        insert_student(conn, (
            student_name, student_dob, student_address, school_district, physician_name,
            physician_phone_number, type_of_authorizer, license_num, physician_address,
            home_hospital_both, consecutive_recurring_basis, admittance_date,
            regular_reduced_workload, return_date
        ))
        st.success("Student added successfully.")

    # Query students by return date
    st.write("Query students by return date:")
    date = st.date_input("Select a date", datetime.now())
    if st.button("Query"):
        df = query_students_by_return_date(conn, date.strftime('%Y-%m-%d'))
        st.write(df)

    # Query newly added students
    st.write("Query newly added students:")
    if st.button("Query Newly Added"):
        df = query_newly_added_students(conn)
        st.write(df)

    conn.close()

if __name__ == "__main__":
    initialize_db() # Initialize the database
    main() # Run the Streamlit application