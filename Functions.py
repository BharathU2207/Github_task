from math import*

name = input("Enter your name: ")
age = input(("Enter your age: "))
result = int(age)
def say_hi():
    print("Hello, " + name + " you are " + str(result) + " years old!")
say_hi()

print()

number = input("Enter a number: ")
result2 =float(number)
def num(number):
    return pow(result2, 3)

print(num(number))

print()
print()
print("another way...")

num2 = input("Enter a number: ")
result3 = float(num2)
def cube(num2):
    return result3*result3*result3

print(cube(num2))
print()
print()



