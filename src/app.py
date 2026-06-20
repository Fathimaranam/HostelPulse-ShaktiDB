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

def view_leave_requests():
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("""
        SELECT leave_id, student_id,
               leave_date, return_date, status
        FROM leave_requests
        ORDER BY leave_id
    """)

    requests = cur.fetchall()

    print("\n===== Leave Requests =====")

    for req in requests:
        print(req)

    cur.close()
    conn.close()

def occupancy_summary():
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("""
        SELECT hostel, COUNT(*)
        FROM students
        GROUP BY hostel
        ORDER BY hostel
    """)

    results = cur.fetchall()

    print("\n===== Occupancy Summary =====")

    for hostel, count in results:
        print(f"{hostel}: {count} students")

    cur.close()
    conn.close()

def meal_preference_summary():
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            SUM(CASE WHEN breakfast THEN 1 ELSE 0 END),
            SUM(CASE WHEN lunch THEN 1 ELSE 0 END),
            SUM(CASE WHEN dinner THEN 1 ELSE 0 END)
        FROM meal_preferences
    """)

    result = cur.fetchone()

    print("\n===== Meal Preference Summary =====")
    print(f"Breakfast: {result[0]}")
    print(f"Lunch: {result[1]}")
    print(f"Dinner: {result[2]}")

    cur.close()
    conn.close()

while True:

    print("1. View Students")
    print("2. Add Student")
    print("3. Apply Leave")
    print("4. View Leave Requests")
    print("5. Occupancy Summary")
    print("6. Meal Preference Summary")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        view_students()

    elif choice == "2":
        add_student()

    elif choice == "3":
        apply_leave()
    
    elif choice == "4":
        view_leave_requests()

    elif choice == "5":
        occupancy_summary()    
    
    elif choice == "6":
        meal_preference_summary()
    
    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")


