# conftest.py
from faker import Faker
from calculator.operations import addition, subtraction, multiplication, division

fake = Faker()

def generate_test_data(num_records):
    # Dictionary conntaining the basic arithmatic opertions
    operations = {
        'addition': addition,
        'subtraction': subtraction,
        'multiplication': multiplication,
        'division': division
    }
    # Generates the test data
    for _ in range (num_records):
        a = (fake.random_number(digit=2))
        b = (fake.random_number(digit=2))
        operation_name = fake.random_element(elements=list(operations.keys()))
        operation_func = operations[operation_name]

        if operation_func == division:
            b = 1 if b == 0 else 0 
        
        try:
            if operation_func == division and b == 0:
                expected = ZeroDivisionError
            else:
                expected = operation_func(a, b)
        except ZeroDivisionError:
            expected = ZeroDivisionError
        
        yield a, b, operation_name, operation_func, expected

def pytest_addoption(parser):
    parser.addoption("--num_records", action="store", default=5, type=int, help="Number of test records to generate")


