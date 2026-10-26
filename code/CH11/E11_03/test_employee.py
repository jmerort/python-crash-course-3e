"""
11-3. Employee: Write a class called Employee. The __init__() method should
take in a first name, a last name, and an annual salary, and store each of these
as attributes. Write a method called give_raise() that adds $5,000 to the
annual salary by default but also accepts a different raise amount.
Write a test file for Employee with two test functions, test_give_default
_raise() and test_give_custom_raise(). Write your tests once without using a
fixture, and make sure they both pass. Then write a fixture so you don’t have to
create a new employee instance in each test function. Run the tests again, and
make sure both tests still pass.

test_employee.py : Test file for the Employee class defined in employee.py

Oct 2026
@jmerort
"""
import pytest
from employee import Employee


@pytest.fixture 
def my_employee():
    """Create a fixture employee that test functions can use"""
    my_employee = Employee("Joe", "Schmo", 30000)
    return my_employee


def test_give_default_raise(my_employee):
    my_employee.give_raise()
    assert my_employee.salary == 35000


def test_give_custom_raise(my_employee):
    my_employee.give_raise(4000)
    assert my_employee.salary == 34000
