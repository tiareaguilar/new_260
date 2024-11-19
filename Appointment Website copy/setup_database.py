import sqlite3

# Database file
DB_FILE = 'app.db'

# SQL commands for creating tables
CREATE_TABLES_SQL = """
-- Create Students Table
CREATE TABLE IF NOT EXISTS Students (
    Student_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Student_Name VARCHAR(100) NOT NULL,
    Email VARCHAR(255) NOT NULL
);

-- Create Exams Table
CREATE TABLE IF NOT EXISTS Exams (
    Exam_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Exam_Name VARCHAR(100) NOT NULL
);

-- Create Exam_Locations Table
CREATE TABLE IF NOT EXISTS Exam_Locations (
    Exam_Location_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Location_Name VARCHAR(100) NOT NULL,
    Address TEXT NOT NULL
);

-- Create Registrations Table
CREATE TABLE IF NOT EXISTS Registrations (
    Registration_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Student_ID INTEGER,
    Exam_ID INTEGER,
    Exam_Date DATE NOT NULL,
    Exam_Time TIME NOT NULL,
    Exam_Location_ID INTEGER NOT NULL,
    Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (Student_ID) REFERENCES Students(Student_ID),
    FOREIGN KEY (Exam_ID) REFERENCES Exams(Exam_ID),
    FOREIGN KEY (Exam_Location_ID) REFERENCES Exam_Locations(Exam_Location_ID)
);

-- Create Authentication Table
CREATE TABLE IF NOT EXISTS Authentication (
    Auth_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Student_ID INTEGER,
    Username VARCHAR(100) UNIQUE NOT NULL,
    Password_Hash VARCHAR(255) NOT NULL,
    Role TEXT CHECK(Role IN ('admin', 'student', 'faculty')) DEFAULT 'student',
    FOREIGN KEY (Student_ID) REFERENCES Students(Student_ID)
);
"""

def setup_database():
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Execute the table creation commands
    cursor.executescript(CREATE_TABLES_SQL)
    print(f"Database setup completed. Tables created in {DB_FILE}.")

    # Close connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()
