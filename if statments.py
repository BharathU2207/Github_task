is_male = False
is_tall = False

if is_male and is_tall:
    print("you are a tall male")
    print("you are a short male")
elif not(is_male) and is_tall:
    print("you are not a male and are tall")
else:
    print("you are not male nor tall")

print()
print("and, or")
print()
print()
print("Comparisions")
print()
print()


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
print(max_num(234, 345, 234))


print()
print()

num11 = input("Enter a number: ")
num22 = input("Enter another number: ")
num33 = input("Enter another number :")

def max_num2(num11, num22, num33):
    return max(num11, num22, num33)

print(max_num2(num11, num22, num33))





















