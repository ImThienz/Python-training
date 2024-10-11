#w3schools.com/python/python_classes.asp
from tkinter.font import names


#Create a Class
class MyClass:
    x=5

#Create Object
p1 = MyClass()
print(p1.x)

#The __init__() Function
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Đạt", 21)
print(p1.name)
print(p1.age)

#The __str__() Function
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # def __str__(self):
    #     return f"{self.name}({self.age})"

p1 = Person("Đạt", 21)
print(p1)

#Object Methods
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("Đạt", 21)
p1.myfunc()

#Delete Object Properties
del p1.age

"9. Write a Python class named Student with two attributes student_name, marks. Modify the attribute values of the said class and print the original and modified values of the said alinibutes."
# Tạo một lớp Student trong Python với hai thuộc tính student_name và marks,
# sau đó sửa đổi giá trị của các thuộc tính đó và in ra giá trị ban đầu cũng như giá trị đã sửa đổi.

class Student:
    def __init__(self, student_name, marks):
        self.student_name = student_name
        self.marks = marks

# Tạo đối tượng của lớp Student với các giá trị ban đầu
student = Student("Vũ Thành Đạt", 85)

# In các giá trị ban đầu
print("\nGiá trị ban đầu:")
print("Tên học sinh:", student.student_name)
print("Điểm số:", student.marks)

# Thay đổi giá trị của các thuộc tính
student.student_name = "Vũ Thành Đạt"
student.marks = 95

# In các giá trị đã được sửa đổi
print("\nGiá trị sau khi sửa đổi:")
print("Tên học sinh:", student.student_name)
print("Điểm số:", student.marks)


"10. Write a Python class named Student with two attributes student _id, student_name. Add a new attribute student_class and display the entire attribute and the values of the class. Now remove the student name attribute and display the entire attribute with values."
# Tạo lớp Student với các thuộc tính student_id, student_name.
# Thêm thuộc tính mới: student_class.
# Hiển thị tất cả các thuộc tính và giá trị của đối tượng.
# Xóa thuộc tính student_name và hiển thị lại các thuộc tính còn lại.

class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

# Tạo đối tượng của lớp Student với các giá trị ban đầu
student = Student(101, "John Doe")

# Thêm thuộc tính mới student_class
student.student_class = "10A"

# Hiển thị tất cả các thuộc tính và giá trị ban đầu
print("\nCác thuộc tính và giá trị ban đầu:")
print(student.__dict__)  # In toàn bộ các thuộc tính của đối tượng

# Xóa thuộc tính student_name
del student.student_name

# Hiển thị các thuộc tính và giá trị sau khi xóa student_name
print("\nCác thuộc tính và giá trị sau khi xóa 'student_name':")
print(student.__dict__)


"11. Write a Python class named Student with two attrbutes: student id, student _name. Add a new attribute: student _class. Create a function to display all attributes and their values in the Student class."
# Tạo lớp Student với hai thuộc tính: student_id và student_name.
# Thêm thuộc tính mới: student_class.
# Tạo một hàm trong lớp để hiển thị toàn bộ các thuộc tính và giá trị của lớp Student.

class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = None  # Khởi tạo thuộc tính mới student_class là None

    # Hàm để hiển thị tất cả thuộc tính và giá trị
    def display_info(self):
        print("Student ID:", self.student_id)
        print("Student Name:", self.student_name)
        print("Student Class:", self.student_class)

# Tạo đối tượng của lớp Student với giá trị ban đầu
student = Student(101, "John Doe")

# Gán giá trị cho thuộc tính mới student_class
student.student_class = "10A\n"

# Hiển thị tất cả thuộc tính và giá trị
student.display_info()

"Flow Chart"
class Student:
    student_id = "V10"
    student_name = "Jacqueline Barnett"

# Original attributes and values
print("Original attributes and their values of the Student class:")
for attr, value in Student.__dict__.items():
    if not attr.startswith('_'):
        print(f'{attr} -> {value}')

# Adding a new attribute
Student.student_class = "V"
print("\nAfter adding the student_class, attributes and their values:")
for attr, value in Student.__dict__.items():
    if not attr.startswith('_'):
        print(f'{attr} -> {value}')

# Removing an attribute
del Student.student_name
print("\nAfter removing the student_name, attributes and their values:")
for attr, value in Student.__dict__.items():
    if not attr.startswith('_'):
        print(f'{attr} -> {value}')