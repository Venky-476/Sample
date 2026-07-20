#functions to define -- def

'''def great():
    print("hello world")
great()'''

'''def add(a,b):
    print(a+b)
add(2,7)
add(10,30)'''

'''def square(num):
    return num*num
print(square(6))'''

def student(*name,age):
    print(name,age)
student("venky", "ven", age=22)

'''def greet(name):
    print("Hello", name)
greet("venky")
greet("sneha")'''

def total(*num):
    print(sum(num))
total(1,23,5,6,7)