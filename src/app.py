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

while True:

    print("\n===== HostelPulse =====")
    print("1. View Students")
    print("2. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        view_students()

    elif choice == "2":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
