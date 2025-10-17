import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassword",   # change this
    database="school"
)
cursor = conn.cursor()

def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = input("Enter grade: ")
    sql = "INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)"
    values = (name, age, grade)
    cursor.execute(sql, values)
    conn.commit()
    print("✅ Student added successfully!")

def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    print("\n--- Student List ---")
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Grade: {row[3]}")
    print("--------------------\n")

while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("❌ Invalid choice. Try again.")

cursor.close()
conn.close()
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",   # leave empty
    database="school"
)
