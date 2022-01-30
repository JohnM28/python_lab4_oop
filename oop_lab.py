from email_composer import email_tempalte
import re
class Person:
    moods = ('happy','tired','lazy')
    def __init__(self, name, money, mood, healthRate):
        self.name = name
        self.money = money
        self.mood = mood
        self.healthRate = healthRate

    def sleep(self,hours):
        if isinstance(hours, int) and hours < 24:
            if hours == 7:
                self.mood = "happy"
            elif hours > 7:
                self.mood = "tired"
            else:
                self.mood = "lazy"
        else:
            print("invalid input")

    def eat(self,meals):
        if isinstance(meals, int) and meals <= 4:
            if meals == 1:
                self.healthRate = 50
            elif meals > 2:
                self.healthRate = 75
            else:
                self.healthRate = 100
        else:
            print("invalid input")

    def buy(self,items):
        if isinstance(items, int):
            while(items > 0):
                self.money -= 10
                items -= 1
        else:
            print("invalid input")

class Employee(Person):

    def __init__(self, name, money, mood, healthRate, id, car, email ,salary,distanceToWork):
        super().__init__(name=name, money=money, mood=mood, healthRate=healthRate)
        self.id = id
        self.car = car
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
        if not re.match(regex, value):
            raise ValueError("It's not an email address.")
        self._email = value

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 1000:
            raise ValueError("Salary must be more than 1000.")
        self._salary = value

    @property
    def healthRate(self):
        return self._healthRate

    @healthRate.setter
    def healthRate(self, value):
        if value < 0 and value > 100:
            raise ValueError("Health mist be between 0 to 100")
        self._healthRate = value

    def work(self,hours):
        if isinstance(hours, int) and hours < 24:
            if hours == 8:
                self.mood = "happy"
            elif hours > 8:
                self.mood = "tired"
            else:
                self.mood = "lazy"
        else:
            print("invalid input")

    def drive(self):
        pass

    def refuel(self):
        pass

    def send_mail(self, to, subject, msg, receiver_name):
        email_tempalte(subject,self.email,to,receiver_name,msg)

class Office:
    def __init__(self,name, employees):
        self.name = name
        self.employess = employees

    def get_all_employees(self):
        pass

    def get_employee(self):
        pass

    def hire(self):
        pass

    def fire(self):
        pass

    def calculate_lateness(self):
        pass

    def deduct(self):
        pass

    def reward(self):
        pass

class Car:
    def __init__(self, name, fuelRate, velocity):
        self.name= name
        self.fuelRate = fuelRate
        self.velocity = velocity

    def run(self):
        pass

    def stop(self):
        pass




