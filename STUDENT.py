# class Student:#created a class
#     pass# MEANS THE CLASS CURRENTLY HAS NO ATTRIBUTES. HAS NOTHING INSDIE THE CLASS BODY SO TEMPORARILY USE PASS

# # CREATE AN OBJECT CCALLED STUDENT1 FROM THE STUDENT CLASS
# student1 = Student()
# # Display the object
# print(student1)

# #The_init_() method is a special method in Python classes that is automatically called when a new instance of the class is created.
# #  It is used to initialize the attributes of the object with specific values. 
# # The init method allows you to set up the initial state of an object by assigning values to its attributes.
# class student:
#   def __init__(self,name, age):# its a reference for a current instance for a class (self).
#     self.name=name#store
#     self.age=age

#   def introduce(self): # this is a method that exists to define a student class.
#     print(f"Name: {self.name}")
#     print(f"Age: {self.age}")


# student1 = student("Diana Atugonza", 20)
# student1.introduce()
# student2 = student("Brendah", 21)
# student2.introduce()


class Phone:
   def __init__(self, brand, storage):
      self.brand = brand
      self.storage = storage

   def _introduce(self):
      print(f"Brand: {self.brand}")
      print(f"Storage: {self.storage} GB")

   def _make_call(self, number):
      print(f"Calling {number} from {self.brand}")

class battery(Phone):      

phone1 = Phone("Samsung", 128)
phone2 = Phone("iPhone", 256)

phone1.introduce()
phone1.make_call(788509509)

phone2.introduce()
phone2.make_call(772900677)




    

"""student1.name="Diana Atugonza"
student1.age=20
print(f"name:{student1.name} age:{student1.age}")"""
