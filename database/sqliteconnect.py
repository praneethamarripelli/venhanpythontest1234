import sqlite3
def insert_student(name: str, grade: float):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            grade REAL NOT NULL
        )
    ''')
    
    # Insert the new student into the students table
    cursor.execute('''
        INSERT INTO students (name, grade) 
        VALUES (Rani, 88.5)
    ''', (name, grade))
    
    # Commit the transaction
    conn.commit()
    
    # Close the connection
    conn.close()
insert_student("Praneetha", 90.5)
