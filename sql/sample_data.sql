INSERT INTO students (name, hostel, room_no, phone) VALUES
('Rana','A Block','A101','9876543210'),
('Anjum','A Block','A102','9876543211'),
('Athira','B Block','B201','9876543212'),
('Goutham','B Block','B202','9876543213'),
('Rasal','C Block','C301','9876543214'),
('Nihal','A Block','A103','9876543215'),
('Akhil','B Block','B203','9876543216'),
('Sreya','C Block','C302','9876543217'),
('Ameen','A Block','A104','9876543218'),
('Diya','B Block','B204','9876543219');

INSERT INTO leave_requests
(student_id, leave_date, return_date, status)
VALUES
(1,'2026-06-20','2026-06-23','Approved'),
(2,'2026-06-20','2026-06-22','Approved'),
(3,'2026-06-21','2026-06-24','Pending'),
(5,'2026-06-20','2026-06-25','Approved'),
(8,'2026-06-21','2026-06-22','Pending');

INSERT INTO meal_preferences
(student_id, meal_date, breakfast, lunch, dinner)
VALUES
(1,'2026-06-20',TRUE,FALSE,TRUE),
(2,'2026-06-20',TRUE,TRUE,TRUE),
(3,'2026-06-20',FALSE,TRUE,TRUE),
(4,'2026-06-20',TRUE,FALSE,FALSE),
(5,'2026-06-20',TRUE,TRUE,FALSE);

INSERT INTO occupancy_logs
(log_date, hostel, present_students)
VALUES
('2026-06-20','A Block',180),
('2026-06-20','B Block',150),
('2026-06-20','C Block',120),
('2026-06-21','A Block',160),
('2026-06-21','B Block',140),
('2026-06-21','C Block',110);
