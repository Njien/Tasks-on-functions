"""
Attendance Register

Task:
- Track attendance of students.
- Use a dictionary { "student_id": {"name": str, "present_days": list, "absent_days": list} }
- Functions to mark attendance, check history, and get reports.
- Use your head/logic to mark multiple students at once.
- Use **kwargs for flexible reporting (e.g., only_present=True).

// NOT FOR THIS ASSIGNMENT
Future OOP Extension:
- Student class with mark_present() and mark_absent().
- AttendanceRegister class that manages records.
"""

import datetime

attendance = {}

def register_student(student_id, *name):
    #Register a student in the system.
    if student_id in attendance:
        return f"student ID: {student_id} already exist"
    else:
        attendance[student_id] = {
            "name": name,
            "present_days": [],
            "absent_days": []
        }
        return f"Student {name} has been registered successfully!!"


def mark_present(student_ids):
    """Mark multiple students as present for today."""
    today = str(datetime.date.today())
    # implement logic
    for student_id in student_ids:
        if student_id in attendance:
            if today in attendance[student_id]["absent_days"]:
                attendance[student_id]["absent_days"].remove(today)
            elif today not in attendance[student_id]["present_days"]:
                attendance[student_id]["present_days"].append(today)

def mark_absent(student_ids):
    """Mark multiple students as absent for today."""
    today = str(datetime.date.today())
    #implement logic
    for student_id in student_ids:
        if student_id in attendance:
            if today in attendance[student_id]["present_days"]:
                attendance[student_id]["present_days"].remove(today)

            elif today not in attendance[student_id]["absent_days"]:
                attendance[student_id]["absent_days"].append(today)

def get_report(**kwargs):
    """Generate attendance report with optional filters."""
    report = {}
    # implement logic
    for student_id, data in attendance.items():
        # filter by student id if given
        if "student_id" in kwargs and kwargs["student_id"] != student_id:
            continue
        # apply presence/absence filters
        if kwargs.get("only_present") and not data["present_days"]:
            continue
        if kwargs.get("only_absent") and not data["absent_days"]:
            continue
        
        report[student_id] = {
            "name": data["name"],
            "present_days": data["present_days"],
            "absent_days": data["absent_days"],
            "total_present": len(data["present_days"]),
            "total_absent": len(data["absent_days"])
        }

    return report


# calling functions

