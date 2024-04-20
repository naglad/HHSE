import streamlit as st
import sqlite3
from datetime import datetime

# Function to connect to the SQLite database
def connect_to_db():
    conn = sqlite3.connect('HHSE.db')
    return conn

# Function to query students based on return date
def query_students_by_return_date(conn, date):
    query = f"SELECT * FROM students WHERE Return_Date = '{date}'"
    df = pd.read_sql_query(query, conn)
    return df

# Function to trigger notification if return date matches today's date
def check_and_notify(conn):
    today = datetime.now().strftime('%Y-%m-%d')
    df = query_students_by_return_date(conn, today)
    if not df.empty:
        st.write(f"Notification: Students with return date matching today's date found.")
        st.write(df)
    else:
        st.write("No students with return date matching today's date.")

# Main Streamlit application
def main():
    st.title('HHSE Data Viewer')
    conn = connect_to_db()

    # Query students based on return date
    st.write("Query students by return date:")
    date = st.date_input("Select a date", datetime.now())
    if st.button("Query"):
        df = query_students_by_return_date(conn, date.strftime('%Y-%m-%d'))
        st.write(df)

    # Check and notify for today's date
    check_and_notify(conn)

    conn.close()

if __name__ == "__main__":
    main()