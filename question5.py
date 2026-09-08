
# QUESTION 5: UNIVERSITY COURSE ENROLLMENT
def calculate_average(marks):
    """
    Calculate average of a list of marks.
    Example: [75, 80, 78] -> 77.67
    """
    if len(marks) == 0:
        return 0
    total = 0
    for mark in marks:
        total = total + mark
    return total / len(marks)


def assign_grade(average):
    """
    Assign letter grade based on average.
    85-100: A
    70-84.99: B
    60-69.99: C
    Below 60: F
    """
    if average >= 85:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    else:
        return "F"


def determine_status(grades):
    """
    Determine student's academic status.
    Critical: At least one F
    At-Risk: No F but at least one C
    Good Standing: All A or B
    """
    if "F" in grades:
        return "Critical"
    elif "C" in grades:
        return "At-Risk"
    else:
        return "Good Standing"


def calculate_course_statistics(students):
    """
    Calculate statistics for each course.
    Returns: Dictionary with course stats
    """
    course_data = {}  # Stores: {"Math": {"marks": [75,80,78, ...], "students": [...]}}
    
    # Collect all marks for each course
    for student in students:
        name = student["name"]
        courses = student["courses"]
        
        for course, marks in courses.items():
            if course not in course_data:
                course_data[course] = {
                    "marks": [],
                    "students": []
                }
            # Add all marks from this student
            for mark in marks:
                course_data[course]["marks"].append(mark)
            # Add student name
            if name not in course_data[course]["students"]:
                course_data[course]["students"].append(name)
    
    # Calculate statistics for each course
    course_stats = {}
    for course, data in course_data.items():
        marks = data["marks"]
        students_enrolled = data["students"]
        
        # Calculate average
        avg = calculate_average(marks)
        
        # Count passing students (grade >= 60)
        passing = 0
        for mark in marks:
            if mark >= 60:
                passing = passing + 1
        
        course_stats[course] = {
            "average": avg,
            "students": len(students_enrolled),
            "passing": passing,
            "total_marks": len(marks)
        }
    
    return course_stats


def generate_report(students):
    """
    Main function that generates the complete report.
    """
    
   
    # PART A: INDIVIDUAL STUDENT PERFORMANCE
   
    
    print("=" * 70)
    print("         UNIVERSITY ACADEMIC PERFORMANCE REPORT")
    print("=" * 70)
    
    print("\n" + "=" * 70)
    print("PART A: INDIVIDUAL STUDENT PERFORMANCE")
    print("=" * 70)
    
    student_statuses = []  # For Part C ranking
    
    for student in students:
        name = student["name"]
        courses = student["courses"]
        
        print("\n" + "-" * 50)
        print(" STUDENT: " + name.upper())
        print("-" * 50)
        
        course_averages = {}
        course_grades = {}
        
        # Calculate average and grade for each course
        for course, marks in courses.items():
            avg = calculate_average(marks)
            grade = assign_grade(avg)
            course_averages[course] = avg
            course_grades[course] = grade
            
            print("  " + course + ": " + str(marks) + " -> Average: " + str(round(avg, 1)) + " (Grade: " + grade + ")")
        
        # Determine status
        grades_list = list(course_grades.values())
        status = determine_status(grades_list)
        
        # Calculate overall average
        overall_avg = 0
        for course, avg in course_averages.items():
            overall_avg = overall_avg + avg
        overall_avg = overall_avg / len(course_averages)
        
        print("   Overall Average: " + str(round(overall_avg, 1)))
        print("   Status: " + status)
        
        # Identify courses needing improvement (C or F)
        needs_improvement = []
        for course, grade in course_grades.items():
            if grade == "C" or grade == "F":
                needs_improvement.append(course + " (" + grade + ")")
        
        if needs_improvement:
            print("   Needs Improvement in: " + ", ".join(needs_improvement))
        else:
            print("  No courses need improvement")
        
        # Recommendation for tutoring
        if status == "Critical" or status == "At-Risk":
            print("   RECOMMENDATION: Tutoring recommended")
        else:
            print("   No tutoring needed")
        
        # Store for Part C
        student_statuses.append({
            "name": name,
            "status": status,
            "overall_avg": overall_avg,
            "grades": course_grades
        })
    
   
    # PART B: COURSE STATISTICS
  
    
    print("\n" + "=" * 70)
    print("PART B: COURSE STATISTICS")
    print("=" * 70)
    
    course_stats = calculate_course_statistics(students)
    
    # Display course statistics
    print("\n COURSE PERFORMANCE SUMMARY:")
    print("-" * 50)
    
    for course, stats in course_stats.items():
        print("\n  " + course + ":")
        print("    Overall Average: " + str(round(stats["average"], 1)))
        print("    Students Enrolled: " + str(stats["students"]))
        print("    Total Marks: " + str(stats["total_marks"]))
        print("    Passing Marks: " + str(stats["passing"]))
        pass_rate = (stats["passing"] / stats["total_marks"]) * 100 if stats["total_marks"] > 0 else 0
        print("    Pass Rate: " + str(round(pass_rate, 1)) + "%")
    
    # Find course with lowest average
    lowest_course = None
    lowest_avg = 999
    for course, stats in course_stats.items():
        if stats["average"] < lowest_avg:
            lowest_avg = stats["average"]
            lowest_course = course
    
    print("\nCOURSE WITH LOWEST OVERALL AVERAGE:")
    print("  " + lowest_course + " (Average: " + str(round(lowest_avg, 1)) + ")")
    
    print("\n COURSE REQUIRING GREATEST ACADEMIC ATTENTION:")
    print("  " + lowest_course + " - Lowest performing course")
    print("  Recommendation: Additional support and resources needed")
    
   
    # PART C: INTERVENTION PRIORITY
   
    
    print("\n" + "=" * 70)
    print("PART C: INTERVENTION PRIORITY LIST")
    print("=" * 70)
    
    # Sort by priority: Critical first, then At-Risk, then Good Standing
    priority_order = {
        "Critical": 1,
        "At-Risk": 2,
        "Good Standing": 3
    }
    
    # Sort students by status priority, then by overall average (highest first)
    student_statuses.sort(key=lambda x: (priority_order[x["status"]], -x["overall_avg"]))
    
    print("\n INTERVENTION PRIORITY LIST:")
    print("-" * 50)
    
    rank = 1
    for student in student_statuses:
        # Show priority icon
        if student["status"] == "Critical":
            icon = ""
        elif student["status"] == "At-Risk":
            icon = ""
        else:
            icon = ""
        
        print("  #" + str(rank) + ": " + icon + " " + student["name"])
        print("     Status: " + student["status"])
        print("     Overall Average: " + str(round(student["overall_avg"], 1)))
        print("     Grades: " + ", ".join([course + "=" + grade for course, grade in student["grades"].items()]))
        rank = rank + 1
    
    # Summary counts
    critical_count = 0
    at_risk_count = 0
    good_count = 0
    
    for student in student_statuses:
        if student["status"] == "Critical":
            critical_count = critical_count + 1
        elif student["status"] == "At-Risk":
            at_risk_count = at_risk_count + 1
        else:
            good_count = good_count + 1
    
    print("\n STATUS SUMMARY:")
    print("-" * 50)
    print("  Critical: " + str(critical_count) + " students")
    print("   At-Risk: " + str(at_risk_count) + " students")
    print("  Good Standing: " + str(good_count) + " students")
    
    print("\n" + "=" * 70)
    print("            END OF REPORT")
    print("=" * 70 + "\n")
    
    return student_statuses, course_stats



# SUPPLIED DATA


students = [
    {
        "name": "Amos",
        "courses": {
            "Math": [75, 80, 78],
            "English": [85, 88, 90]
        }
    },
    {
        "name": "Betty",
        "courses": {
            "Math": [60, 58, 62],
            "English": [92, 94, 89]
        }
    },
    {
        "name": "Charles",
        "courses": {
            "Math": [85, 88, 90],
            "Science": [80, 82, 85]
        }
    },
    {
        "name": "Diana",
        "courses": {
            "Math": [45, 48, 50],
            "English": [70, 72, 68]
        }
    }
]


# RUN THE PROGRAM

print(" TEST 1: Supplied Dataset")
print("=" * 70)
generate_report(students)



# TEST 2: Additional test data (normal case)

print("\n" + " TEST 2: Additional Test Data - Mixed Performance")
print("=" * 70)

extra_students = [
    {
        "name": "Eve",
        "courses": {
            "Math": [95, 92, 98],
            "Physics": [88, 85, 90],
            "Chemistry": [90, 92, 94]
        }
    },
    {
        "name": "Frank",
        "courses": {
            "Math": [55, 50, 48],
            "English": [65, 62, 60]
        }
    },
    {
        "name": "Grace",
        "courses": {
            "Biology": [82, 85, 88],
            "Chemistry": [78, 80, 82]
        }
    }
]

generate_report(extra_students)



# TEST 3: Edge case - All failing

print("\n" + "TEST 3: Edge Case - All Students Failing")
print("=" * 70)

failing_students = [
    {
        "name": "Poor1",
        "courses": {
            "Math": [30, 25, 35],
            "English": [40, 38, 42]
        }
    },
    {
        "name": "Poor2",
        "courses": {
            "Math": [20, 22, 18],
            "Science": [35, 30, 28]
        }
    }
]

generate_report(failing_students)



# TEST 4: Edge case - All excellent students

print("\n" + " TEST 4: Edge Case - All Excellent Students")
print("=" * 70)

excellent_students = [
    {
        "name": "Smart1",
        "courses": {
            "Math": [95, 98, 100],
            "English": [92, 95, 96]
        }
    },
    {
        "name": "Smart2",
        "courses": {
            "Math": [88, 90, 92],
            "Science": [95, 96, 98]
        }
    }
]

generate_report(excellent_students)