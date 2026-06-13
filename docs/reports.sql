-- Students per Hostel
SELECT hostel, COUNT(*) AS total_students
FROM students
GROUP BY hostel;

-- Leave Statistics
SELECT status, COUNT(*) AS total_requests
FROM leave_requests
GROUP BY status;

-- Current Occupancy
SELECT SUM(present_students) AS total_occupancy
FROM occupancy_logs
WHERE log_date='2026-06-20';

-- Hostel-wise Occupancy
SELECT hostel, present_students
FROM occupancy_logs
WHERE log_date='2026-06-20';

-- Meal Preference Count
SELECT
COUNT(CASE WHEN breakfast=TRUE THEN 1 END) AS breakfast_count,
COUNT(CASE WHEN lunch=TRUE THEN 1 END) AS lunch_count,
COUNT(CASE WHEN dinner=TRUE THEN 1 END) AS dinner_count
FROM meal_preferences;
