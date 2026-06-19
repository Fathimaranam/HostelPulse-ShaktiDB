import psycopg2

def connect_db():
    return psycopg2.connect(
        dbname="hostelpulse",
        user="postgres",
        password="hostelpulse123",
        host="localhost",
        port="5432"
    )

def view_students():
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM students")
    students = cur.fetchall()

    print("\n===== Students =====")
    for student in students:
        print(student)

    cur.close()
    conn.close()

def add_student():
    name = input("Enter Name: ")
    hostel = input("Enter Hostel: ")
    room_no = input("Enter Room Number: ")
    phone = input("Enter Phone Number: ")

    conn = connect_db()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO students(name, hostel, room_no, phone)
        VALUES (%s, %s, %s, %s)
    """, (name, hostel, room_no, phone))

    conn.commit()

    print("Student added successfully!")

    cur.close()
    conn.close()

def apply_leave():
    student_id = input("Enter Student ID: ")
    leave_date = input("Enter Leave Date (YYYY-MM-DD): ")
    return_date = input("Enter Return Date (YYYY-MM-DD): ")

    conn = connect_db()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO leave_requests(student_id, leave_date, return_date)
        VALUES (%s, %s, %s)
    """, (student_id, leave_date, return_date))

    conn.commit()

    print("Leave request submitted successfully!")

    cur.close()
    conn.close()

while True:

    print("1. View Students")
    print("2. Add Student")
    print("3. Apply Leave")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        view_students()

    elif choice == "2":
        add_student()

    elif choice == "3":
        apply_leave()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")


