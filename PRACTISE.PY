"""class Student:
	def __init__(self, name, age, regno, gender, email, program):
		self.name = name
		self.age = age
		self.regno = regno
		self.gender = gender
		self.email = email
		self.program = program

	def __str__(self):
		return (
			f"Name: {self.name}\n"
			f"Age: {self.age}\n"
			f"Registration number: {self.regno}\n"
			f"Gender: {self.gender}\n"
			f"Email: {self.email}\n"
			f"Program: {self.program}"
		)


students = []

while True:
	print("\n1. Add Student")
	print("2. View stored students")
	print("3. Exit")
	choice = input("Choose an option: ")

	if choice == "1":
		name = input("Enter name: ")

		while True:
			try:
				age = int(input("Enter age: "))
				if age < 0:
					raise ValueError
				break
			except ValueError:
				print("Please enter a valid positive age.")

		regno = input("Enter registration number: ")
		gender = input("Enter gender: ")
		email = input("Enter email: ")
		program = input("Enter program: ")

		students.append(Student(name, age, regno, gender, email, program))
		print("student stored successfully.")

	elif choice == "2":
		if not students:
			print("No kids have been stored yet.")
		else:
			for number, kid in enumerate(students, start=1):
				print(f"\nstudent {number}")
				print(kid)

	elif choice == "3":
		print("Goodbye.")
		break

	else:
		print("Invalid option. Choose 1, 2, or 3.")"""


        
