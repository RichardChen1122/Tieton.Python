from package_runoob.runoob1 import print_func, print_func2, name
from package_runoob.myclass import Employee
# 现在可以调用模块里包含的函数


class Parent:        # 定义父类
    _parentAttr = 100

    def __init__(self):
        print("调用父类构造函数")

    def _parentMethod(self):
        print('调用父类方法')

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print("父类的父类属性 :", self.parentAttr)
        print("父类的子类属性 :", "不存在")
        print("子类的父类属性 :", self.parentAttr)
        print("子类的子类属性 :", self.ChildProperty)


class Child(Parent):  # 定义子类
    childAttr = 103

    def __init__(self):
        print("调用子类构造函数")

    def childMethod(self):
        print('调用子类方法,设置父类属性')
        self._parentAttr = 101

    def childMethodSetChile(self):
        print('调用子类方法,设置子类属性')
        Child.childAttr = 1001


c = Child()          # 实例化子类
c.childMethod()      # 调用子类的方法
c._parentMethod()     # 调用父类方法
# c.setAttr(200)       # 再次调用父类的方法 - 设置属性值
c.childMethodSetChile()
c.getAttr()          # 再次调用父类的方法 - 获取属性值

print(isinstance(c, Parent))
