class Employee:
    _employee_count = 0

    def __init__(self, employee_id: str, name: str):
        if not self.validate_employee_id(employee_id):
            raise ValueError("Invalid employee ID format. Must be a string of digits.")
        self.employee_id = employee_id
        self.name = name
        Employee._increment_employee_count()

    @classmethod
    def _increment_employee_count(cls):
        cls._employee_count += 1

    @classmethod
    def get_employee_count(cls) -> int:
        return cls._employee_count

    @staticmethod
    def validate_employee_id(employee_id: str) -> bool:
        return employee_id.isdigit()
    
employee1 = Employee("12345", "Praneetha")
employee2 = Employee("67890", "Sandhya")

print("Number of employees:", Employee.get_employee_count())  # Output: Number of employees: 2

# Validation example
print("Is '12345' a valid ID?", Employee.validate_employee_id("12345"))  # Output: Is '12345' a valid ID? True
print("Is 'abc123' a valid ID?", Employee.validate_employee_id("abc123"))  # Output: Is 'abc123' a valid ID? False

try:
    invalid_employee = Employee("abc123", "Charlie")
except ValueError as e:
    print(e)  # Output: Invalid employee ID format. Must be a string of digits.
