CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    hostel VARCHAR(50) NOT NULL,
    room_no VARCHAR(20),
    phone VARCHAR(15)
);
CREATE TABLE leave_requests (
    leave_id SERIAL PRIMARY KEY,
    student_id INT REFERENCES students(student_id),
    leave_date DATE NOT NULL,
    return_date DATE NOT NULL,
    status VARCHAR(20) DEFAULT 'Pending'
);
CREATE TABLE meal_preferences (
    preference_id SERIAL PRIMARY KEY,
    student_id INT REFERENCES students(student_id),
    meal_date DATE NOT NULL,
    breakfast BOOLEAN DEFAULT TRUE,
    lunch BOOLEAN DEFAULT TRUE,
    dinner BOOLEAN DEFAULT TRUE
);

CREATE TABLE occupancy_logs (
    log_id SERIAL PRIMARY KEY,
    log_date DATE NOT NULL,
    hostel VARCHAR(50),
    present_students INT
);
