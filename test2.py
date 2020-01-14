registry = []
def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func
@register
def f1():
    print('running f1()')
@register
def f2():
    print('running f2()')
def f3():
    print('running f3()')
def main():
    print('running main()')
    print('registry ->', registry)

def factorial(n):
    '''returns n!'''
    return 1 if n < 2 else n * factorial(n-1)
f1()
f2()
f3()
print(factorial.__doc__)
print(factorial(3))

fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
sorted()

if __name__=='__main__':
    main()