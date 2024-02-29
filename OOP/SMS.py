class Student:

    def __init__(self,name, age, roll_number):
        self.name=name
        self.age=age
        self.roll_number=roll_number


class School:
    def __init__(self):
        self.students=[]
    def add_student(self,name,age,roll):
        student=Student(name,age,roll)
        self.students.append(student)
    def display_students(self):
        for student in self.students:
            print("----------------------------")
            print(f"Name: {student.name}")
            print(f"Age: {student.age}")
            print(f"Roll number: {student.roll_number}")
            print("----------------------------")
    def edit_student(self,roll_number, new_name,new_age):
        for student in self.students:
            if student.roll_number==roll_number:
                student.name=new_name
                student.age=new_age
                print(f"Student {student.name} successfully updated")
                return
    def delete_student(self,roll_number):
        for student in self.students:
            if student.roll_number==roll_number:
                self.students.remove(student)
                print(f"Student {student.rollnumber} successfully deleted")
                return



#Creating school object
school=School() 

while True:
    choice=input("Enter your choice: \n1) Add student \n2) Display list of students \n3) Edit student  \n4) Delete register \n5) Quit. \n")

    if choice=="1":
        #Accepting data from the user to create a student object 
        name=input("Enter name of the student: ")
        age=input("Enter age: ")
        roll=input("Enter roll number: ")
        school.add_student(name,age,roll)
    elif choice=="2":
        school.display_students()
    elif choice=="3":
        roll_number=input("Enter roll number which you want to edit: ")
        new_name=input("Enter new name for the student: ")
        new_age=input("Enter new age for the student: ")
        school.edit_student(roll_number, new_name, new_age)
    elif choice=="4":
        roll_number=input("Enter roll number you want to delete: ")

    elif choice=="5":
        break





#Creating a student object 


        