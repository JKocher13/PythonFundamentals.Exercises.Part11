class AliveStatus(Enum):
    def __init__(self,status):
        self.status =status
class Person:
    def __init__(self, first_name, last_name, dob, alive):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.alive = alive

    def update_first_name(self, new_fn):
        self.first_name = new_fn

    def update_first_name(self,new_first_name):
        self.first_name = new_first_name
    def update_last_name(self, new_last_name):
        self.last_name = new_last_name
    def update_dob(self, new_dob):
        self.dob = new_dob
    def update_status(self,new_status):
        self.status = new_status

class Instructor(Person):
    def __init__(self, id):
        self.id = str("Instructor_" + id)
        super().__init__(first_name, last_name, dob, alive)
class Student(Person):
    def __init__(self, id):
        self.id = str("Student_" + id)
        super().__init__(first_name, last_name, dob, alive)

class ZipCodeStudent(Student):
    def __init__(self):
        super().__init__(first_name, last_name, dob, alive)
class prek(Students):
    def __init__(self):
        super().__init__(first_name, last_name, dob, alive)
class Middle_School(Student):
    def __init__(self):
        super().__init__(first_name, last_name, dob, alive)
class College(Student):
    def __init__(self):
        super().__init__(first_name, last_name, dob, alive)

class Classroom():
    def __int__(self):
        students = []
        teachers = []

    def add_instructor(self, instructor):
        teachers.append(instructor)

    def remove_instructor(self, instructor):
        teachers.remover(instructor)

    def add_student(self, student):
        student.append(student)

    def remove_student(self,teacher):
        student.remove(student)

    def print_instructor(self):
        print(teachers)

    def print_students(self):
        print(students)

