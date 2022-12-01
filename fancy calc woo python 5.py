num = float(input("Enter a number: "))
op = input("Enter an operator: ")
num2 = float(input("Enter another number: "))


if op == "+":
    print(num + num2)
elif op == "-":
    print(num - num2)
elif op == "*":
    print(num * num2)
elif op == "/":
    print(num / num2)
else:
    print("Invalid operator" )

print()
print()
print("DICTIONARIES: ")
print()
monthconversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthconversions["Nov"])
print(monthconversions.get("Dec"))
print(monthconversions.get("hi", "not a valid key"))

print()
print("LOOPS")
print()



i = 1
while i <= 10:
    print(i)
    i += 1

print("done with loop!")

print()

secret_word = "Holidays"
guess = ""
guess_count = 0
guess_limit = 5
out_of_guesses = False
2
while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter a guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("Out of guesses, YOU LOSE! ")
else:
    print("You win!")
print()
print()

for letter in "Learning Python":
    print(letter)
print()

names = ["John", "Jim", "Oscar", "Alex"]
for name in names:
    print(name)
print(names[3])
for name in range(2, 10):
    print(name)

print()
print()
for name in range(5):
    if name == 4:
        print("First name")
    else:
        print("Not first name")

print()
print()

python_code = "Code work"
if python_code == "Work code":
    n = "Error user does not have sufficient intelligence to run me!"
    while n != "cool right?":
        print(n)

    print(n)




 











