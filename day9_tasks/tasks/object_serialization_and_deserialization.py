
"""
2. Build a program that can serialize Python objects (convert them to a JSON
representation) and then deserialize them back to their original form. Create a class
hierarchy to demonstrate the serialization and deserialization of different types of
objects.
"""
import json


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def to_json(self):
        return json.dumps({
            "name": self.name,
            "age": self.age
        })

    @classmethod
    def from_json(cls, json_data):
        data = json.loads(json_data)
        return cls(data["name"], data["age"])


class Employee(Person):
    def __init__(self, name, age, company):
        super().__init__(name, age)
        self.company = company

    def to_json(self):
        return json.dumps({
            "name": self.name,
            "age": self.age,
            "company": self.company
        })

    @classmethod
    def from_json(cls, json_data):
        data = json.loads(json_data)
        return cls(data["name"], data["age"], data["company"])


# User input for Person
person_name = input("Enter person's name: ")
person_age = int(input("Enter person's age: "))

person = Person(person_name, person_ages)
person_json = person.to_json()
print(person_json)

deserialized_person = Person.from_json(person_json)
print(deserialized_person.name, deserialized_person.age)

# User input for Employee
employee_name = input("Enter employee's name: ")
employee_age = int(input("Enter employee's age: "))
employee_company = input("Enter employee's company: ")

employee = Employee(employee_name, employee_age, employee_company)
employee_json = employee.to_json()
print(employee_json)

deserialized_employee = Employee.from_json(employee_json)
print(deserialized_employee.name, deserialized_employee.age, deserialized_employee.company)