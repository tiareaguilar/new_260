import sqlite3

def seed_database():
    # Connect to the database
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()

    try:
        # Insert Locations
        locations = [
            ("West Charleston", "6375 W. Charleston Blvd., Las Vegas, NV 89146"),
            ("North Las Vegas", "3200 E. Cheyenne Ave., North Las Vegas, NV 89030"),
            ("Henderson", "700 College Dr., Henderson, NV 89002")
        ]
        cursor.executemany("INSERT INTO Exam_Locations (Location_Name, Address) VALUES (?, ?)", locations)

        # Insert Exams
        exams = [
            ("PHIL 114",),
            ("MATH 181",),
            ("ACC 201",),
            ("CS 202",),
            ("HIST 101",),
            ("PSY 101",)
        ]
        cursor.executemany("INSERT INTO Exams (Exam_Name) VALUES (?)", exams)

        # Commit the changes
        conn.commit()
        print("Database seeded successfully!")

    except sqlite3.Error as e:
        print(f"Error seeding database: {e}")

    finally:
        conn.close()

if __name__ == "__main__":
    seed_database()
