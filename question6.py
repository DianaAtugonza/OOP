#Python could allow us to represent a student as a single programming entity using classes.
#  A class acts as a blueprint that combines both the student's data (attributes) and the operations (methods) into one object.

#Currently, our solution uses dictionaries to store student data and separate functions like calculate_average(), assign_grade(), and determine_status() that work on that data. 
#This separates the data from the operations.

#In an object-oriented approach, we would create a Student class. This class would contain:

#· Attributes (data): name, courses, marks
#· Methods (functions): calculate_average(), assign_grade(), determine_status(), get_overall_average()

#This would allow us to create individual student objects. Each student object would own both its data and the functions that operate on that data. For example:

#python
#amos = Student("Amos", {"Math": [75, 80, 78], "English": [85, 88, 90]})
#amos.determine_status()  # The student object calculates its own status
#This makes the code more organized because each student is a self-contained unit. The student object "knows" how to calculate its own averages, assign its own grades, and determine its own status without needing external functions.
#This approach is also more reusable. If we need to add new functionality (like calculating a student's GPA or sending a report), we simply add a new method to the Student class instead of creating a new separate function.

#This is the fundamental idea behind Object-Oriented Programming: grouping data and the functions that operate on that data together into objects to create more organized, modular, and maintainable code.