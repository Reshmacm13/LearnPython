# to create custom methods/ user defined methods
class CustomMethod:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def reset(self):
        self.a = 0
        self.b = 0

    def move(self, ax, bx):
        self.a = self.a + ax
        self.b = self.b + bx

    def sort(self):
        if self.b < self.a:
            self.a, self.b = self.b, self.a
        return self.a, self.b

    def total(self):
        return self.a + self.b


c1 = CustomMethod(1, 2)
c2 = CustomMethod(3, 4)
c3 = CustomMethod(44, 4)
c4 = CustomMethod(5, 5)


# player
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health = 100

    def attack(self, pts):
        self.health -= pts


a1 = Player(1, 2)

#output:
# >>> a1.attack(20)
# >>> a1.__dict__
# {'x': 1, 'y': 2, 'health': 80}

# 3.. Employee


class Employee:
    def __init__(self, fname, lname, pay):
        # instance data
        self.fname = fname
        self.lname = lname
        self.pay = pay


    def email(self):
        return f"{self.fname}, {self.lname}@company.com"

    # output:
    # e1.email()
    # 'steve, job@company.com'

    def pay_hike(self, percentage):
        hike_amount = self.pay * percentage
        self.pay = self.pay + hike_amount

    # output:
    # >> > e1.pay_hike(0.1)
    # >> > e1.pay
    # 1100.0


e1 = Employee("steve", "job", 1000)


# constructor overloaded
# 1.. if we are not passing any value take default value

class Overload:
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

l1 = Overload()
l2 = Overload(1)
l3 = Overload(1, 2)

# 4.. Bank account
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transaction = []

    def deposit(self, amount):
        self.balance = self.balance + amount
        self.transaction.append(f"Amount Deposited: {amount}")

    # output:
    # c1.deposit(100)
    # >> > c1.__dict__
    # {'name': 'steve', 'balance': 200, 'transaction': ['Amount Deposited: 100']}

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance = self.balance - amount
            self.transaction.append(f"Amount Deposited: {amount}")
        else:
            print("Insufficent")

c1 = BankAccount("steve", 100)

