import os
import sqlite3
import pandas as pd
import streamlit as st

# Function to read and parse the Excel file
def read_and_parse_excel(file_path):
    # Assuming the Excel file is named 'HHSE.xlsx' and is located in a folder named 'HHSE'
    df = pd.read_excel(file_path)
    return df

# Function to insert data into the SQLite database
def insert_data_into_db(df):
    # Assuming the database file is named 'database.db'
    conn = sqlite3.connect('database.db')
    df.to_sql('students', conn, if_exists='append', index=False)
    conn.close()
    print("Data inserted into the SQLite database.")

# Main function to read the Excel file and insert its data into the SQLite database
def main():
    # Define the path to the Excel file
    file_path = os.path.join('HHSE', 'HHSE.xlsx')
    
    # Check if the file exists
    if os.path.exists(file_path):
        print("File exists.")
    else:
        print("File does not exist.")
    
    # Read and parse the Excel file
    df = read_and_parse_excel(file_path)
    
    # Insert data into the SQLite database
    insert_data_into_db(df)

# Streamlit application to view the data
def run_streamlit_app():
    st.title('HHSE Data Viewer')
    conn = sqlite3.connect('database.db')
    df = pd.read_sql_query("SELECT * FROM students", conn)
    st.write(df)
    conn.close()

if __name__ == '__main__':
    main()
    run_streamlit_app()
