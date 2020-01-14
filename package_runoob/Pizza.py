class Pizza:
    size = 0
    def __init__(self, size):
        self.size=size

    def get_size(self):
        return self.size

    @classmethod
    def get_size_class(cls):
        return cls.size;

    @staticmethod
    def get_size_static():
        Pizza.size += 1;

pizza = Pizza(43)
a=Pizza(10)
a.size +=1
Pizza.get_size_static()
print(Pizza.get_size_class())
b=Pizza.size;
print(a.get_size())
print(b)
        