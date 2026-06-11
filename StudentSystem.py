class Address:
    def __init__(self, street, city, zip_code):
        self.street = street
        self.city = city
        self.zip_code = zip_code

    def display(self):
        return f"{self.street}, {self.city} - {self.zip_code}"


class Student:
    def __init__(self, name, age, address):
        self.name = name
        self._age = None
        self.age = age
        self.address = address
        self.courses = []

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value <= 0 or value > 120:
            raise ValueError("Age must be a valid positive integer (1–120)")
        self._age = value

    def add_course(self, course):
        if not course:
            raise ValueError("Course name cannot be empty")
        self.courses.append(course)

    def display(self):
        print(f"Name    : {self.name}")
        print(f"Age     : {self.age}")
        print(f"Address : {self.address.display()}")
        print(f"Courses : {', '.join(self.courses) if self.courses else 'None'}")


class ScholarshipStudent(Student):
    def __init__(self, name, age, address, scholarship_amount):
        super().__init__(name, age, address)
        self.scholarship_amount = scholarship_amount

    def display(self):
        super().display()
        print(f"Scholarship Amount: {self.scholarship_amount}")


if __name__ == "__main__":
    addr1 = Address("Street 1", "City 1", "101")
    addr2 = Address("Street 2", "City 2", "321")

    student1 = Student("Rahul", 20, addr1)
    student1.add_course("Math")
    student1.add_course("Physics")

    student2 = ScholarshipStudent("Anita", 22, addr2, 50000)
    student2.add_course("Computer Science")

    students = [student1, student2]

    for s in students:
        print("\n--- Student Details ---")
        s.display()

    print("\n--- Mutable Behavior Test ---")
    student1.add_course("Chemistry")
    student1.display()