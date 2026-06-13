import psycopg2

try:
    conn = psycopg2.connect(
        dbname="hostelpulse",
        user="postgres",
        password="hostelpulse123",
        host="localhost",
        port="5432"
    )

    print("Connected to HostelPulse Database!")

    cur = conn.cursor()

    cur.execute("SELECT * FROM students")

    students = cur.fetchall()

    print("\nStudents List:")
    for student in students:
        print(student)

    cur.close()
    conn.close()

except Exception as e:
    print("Error:", e)
