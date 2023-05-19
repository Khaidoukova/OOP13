import datetime


class Employee:
    raise_coeff = 1.5

    def __init__(self, name, surname, pay):
        self.name = name
        self.surname = surname
        self.__pay = pay

    def raise_pay(self):
        self.__pay *= self.raise_coeff

    @classmethod
    def from_string(cls, data_string):
        name, surname, pay = data_string.split(" ")
        pay = int(pay)

        return cls(name, surname, pay)

    @classmethod
    def set_raise_amount(cls, new_coeff):
        cls.raise_coeff = new_coeff

    @staticmethod
    def is_work_day():
        now = datetime.datetime.now()
        if now.weekday() == 6 or now.weekday() == 7:
            return False
        return True

    @property
    def email(self):
        return f'{self.name.lower()}.{self.surname.lower()}@jobmail.com'

    @property
    def pay(self):
        return self.__pay

    @property
    def fullname(self):
        return f'{self.name} {self.surname}'

    @fullname.setter
    def fullname(self, data_string):
        name, surname = data_string.stlit(" ")
        self.name = name
        self.surname = surname





if __name__ == "__main__":
    emp1 = Employee("Ivan", "Ivanov", 60000)

 #Test1
emp1.name = "Semen"
assert emp1.email == "semen.ivanov@jobmail.com"

#Test2
emp1.raise_pay()
assert 60000 * Employee.raise_coeff == emp1.pay

#Test3
emp2 = Employee.from_string("Petr Petrov 70000")
assert isinstance(emp2, Employee)
assert emp2.name == "Petr"
assert emp2.surname == "Petrov"
assert emp2.pay == 70000

#Test4
Employee.set_raise_amount(2)
assert Employee.raise_coeff == 2

#Tesr
assert Employee.is_work_day() == True
