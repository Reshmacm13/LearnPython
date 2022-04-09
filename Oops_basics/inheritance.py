# 1.. single level Inheritance
class Parent:
    def __init__(self, value):
        self.value = value

    def apple(self):
        print(f"executing Parent Apple{self.value}")


class Child1(Parent):
    def __init__(self, value):
        super().__init__(value)

    def yahoo(self):
        print(f"executing child Yahoo....")


class Child2(Parent):
    def __init__(self, value):
        super().__init__(value)

    def apple(self):
        print("Running child2 Apple....")


class Child3(Parent):
    def __init__(self, value):
        super().__init__(value)

    def apple(self):
        print("Running child3 Apple....")
        super().apple()

c1 = Child1(10)
c2 = Child2(20)
c3 = Child3(30)


# class having extra attributes
class child4(Parent):
    def __init__(self, value, a, b):
        super().__init__(value)
        self.a = a
        self.b = b

    def demo(self):
        print(self.a, self.b, self.value)

c4 = child4(10, 20, 30)


# Multiple Inheritance
class Parent2:
    def __init__(self, value, fname, lname, age):
        self.value = value
        self.fname = fname
        self.lname = lname
        self.age = age

    def par(self):
        print(f"parent2 value--{self.value}, {self.fname}, {self.lname}, {self.age}")


class Child5(Parent, Parent2):
    def __init__(self, value, fname, lname, age):
        Parent.__init__(self, value)
        Parent2.__init__(self, value, fname, lname, age)

    def whatsapp(self):
        print("child whatsapp")

c5 = Child5(10, "reshma", "kc", 30)