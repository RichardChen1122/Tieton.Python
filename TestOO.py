from package_runoob.Pizza import Pizza
from package_runoob.tombola import Tombola
from functools import wraps
import inspect

@Tombola.register
class Fake(list):
    def test(self):
        print(1333)

def corotine(func):
    @wraps(func)
    def primer(*args, **kwargs):
        gen=func(*args, **kwargs)
        next(gen)
        return gen

    return primer


def simple_coroutine():
    print("-> coroutine started")
    x=yield
    print('-> coroutine received:', x)

def simple_coro2(a):
    print("-> coroutine started a=",a)
    b=yield a
    print('-> coroutine received b =', b)
    c=yield a+b
    print('-> coroutine received c =',c)

@corotine
def average():
    total=0
    count =0
    avarage=None
    while True:
        term = yield avarage
        total +=term
        count +=1
        avarage=total/count

f=Fake()
f.test()

avg=average()
a1=avg.send(10)
print(a1)
a2=avg.send(20)
print(a2)
a3=avg.send('SPAM')
avg.send(60)

# my_coro=simple_coro2(16)
# print(inspect.getgeneratorstate(my_coro))
# k = my_coro.send(None)
# print(k)
# print(inspect.getgeneratorstate(my_coro))
# a= my_coro.send(14)
# print(a)
# print(inspect.getgeneratorstate(my_coro))
# my_coro.send(15)
my_coro=simple_coroutine()
k = my_coro.send(None)
print(k)

