class StudentGPA:
    def __init__(self, name, gpa):
        # 1. name is public
        self.name = name
        
        # 2. GPA is internal (use a single underscore to indicate "internal")
        self._gpa = 0.0
        
        # 5. The constructor should also validate the starting GPA.
        # We do this by calling our setter (which handles validation)
        self.set_gpa(gpa)

    # 3. A getter should read the GPA. (Uses RETURN, not print!)
    def get_gpa(self):
        return self._gpa

    # 4. A setter should change the GPA ONLY when the new value is valid (0.0 - 5.0)
    def set_gpa(self, new_gpa):
        if 0.0 <= new_gpa <= 5.0:
            self._gpa = new_gpa
        else:
            print(f"Error: Invalid GPA '{new_gpa}'. GPA must be between 0.0 and 5.0.")

            # --- TESTING ---

# --- TESTING ---

# 1. A valid GPA (Initialization)
print("--- Test 1: Valid Initial GPA ---")
student1 = StudentGPA("Alice", 3.8)
print(f"Student: {student1.name}")
print(f"Current GPA: {student1.get_gpa()}") 
# Notice we had to use print() outside because get_gpa() RETURNS the value.


# 2. A valid update
print("\n--- Test 2: Valid Update ---")
student1.set_gpa(4.2)  # This should succeed silently
print(f"Updated GPA: {student1.get_gpa()}")


# 3. An invalid update
print("\n--- Test 3: Invalid Update ---")
student1.set_gpa(6.5)  # This should trigger the error and NOT change the GPA
print(f"GPA after invalid update attempt: {student1.get_gpa()}") # Should still be 4.2

