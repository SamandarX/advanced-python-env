class Person:
    def __init__(self, name, age):
        self.name = name      
        self.age = age

    def get_info(self):
        return "Name: " + self.name + ", Age: " + str(self.age)

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def get_info(self):
        return (
            "Name: " + self.name +
            ", Age: " + str(self.age) +
            ", Student ID: " + str(self.student_id)
        )

person1 = Person("Sam", 19)
student1 = Student("Almas", 20, 101)

print(person1.get_info())   
print(student1.get_info())
