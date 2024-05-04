class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age(self):
        return self.age


class Driver(Person):
    def __init__(self, name, age, license_number):
        super().__init__(name, age)
        self.license_number = license_number


if __name__ == "__main__":
    person1 = Person("Nazar", 26)
    print("Person:", person1.name)
    print("Age:", person1.get_age())

    driver1 = Driver("Max", 22, "929402842")
    print("Driver:", driver1.name)
    print("Age:", driver1.get_age())
    print("License Number:", driver1.license_number)
