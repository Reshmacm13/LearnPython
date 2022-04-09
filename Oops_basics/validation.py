# make ponter immutable

class Point:
    def __init__(self, a, b):
        print('constructor calling...')
        super().__setattr__("a", a)
        super().__setattr__("b", b)

    def __setattr__(self, key, value):
        raise Exception()

p = Point(1, 2)
l = [1, 2]

# getter and setter