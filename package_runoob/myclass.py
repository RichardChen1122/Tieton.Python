class Employee:
    empCount = 0
    '所有员工的基类'

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.empCount += 1

    def displayCount(self):
        print(self)
        print(self.__class__)
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self, something):
        print("Name : ", self.name,  ", Salary: ", self.salary, something)
