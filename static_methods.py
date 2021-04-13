
class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    
    def set_raise_amt(self, amount):
        self.raise_amt = amount

    
    def from_string(self, emp_str):
        first, last, pay = emp_str.split('-')
        return self(first, last, pay)

   
    def is_workday(self,day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('007', 'Bond', 100)
emp_2 = Employee('Test', 'Employee', 50)

Employee.set_raise_amt(1.05)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

emp_str_1 = '007'
emp_str_2 = 'Bond'
emp_str_3 = 'James'

first, last, pay = emp_str_1.split('-')

#new_emp_1 = Employee(first, last, pay)
new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)

import datetime
my_date = datetime.date(2020, 7, 11)

print(Employee.is_workday(my_date))