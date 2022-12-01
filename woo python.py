character_name = "John"
character_age = "35"

print("there once was a man named " + character_name + ",")
print("he was " + character_age + " years old")

character_name = "mike"
character_age = "70"
print("he like his name," + character_name + ",")
print("but he didn\'t like being " + character_age + ".")

print("hello\nworld")

phrase = "Hello there"
print(phrase)
print(phrase.upper())
print(len(phrase))
print(phrase[0])
print(character_name[0])
print(len(character_name))
print(character_name.upper())
print(character_name.capitalize())
print(phrase.index("e"))
print(phrase.replace("Hello", "Hi"))
print("Hey there everyone\nI am learning python today\nCheers")

print("NUMBERS")
print(-2.0987)
print(3.856 * 281.2)
print("wow that works")
print(3 + (4*5))
print(10 % 3)
print("mod- divide then give remainder %-sign")
my_num = -3.142
print(my_num)
print("variables work with numbers")
print("str makes numbers into strings")
print(str(my_num) + " my favorite number")
print("str used to print a number next to a string")
print(abs(my_num))
print(pow(3, 3))
print("pow used for powers")
print(max(4, 5))
print("max give you the larger of the two numbers")
print(min(4, 5))
print(round(3.142))

from math import*
print("imports other math functions")
print(floor(3.142))
print(ceil(3.142))
print("floor lowers to previous whole number ceil does opp")
print(sqrt(36))


print("LISTS!!!")

animal_list = ["dog", "cat", "monkey", "fish", "bird"]
print(animal_list)
print(animal_list[0])
print(animal_list[2])
print(animal_list[1:])
print(animal_list[1:4])
animal_list[1] = "bee"
print(animal_list[1])
random_numbers = [2, 3, 5, 9, 27]
animal_list.extend(random_numbers)
print(animal_list)
animal_list.append("horse")
print(animal_list)
animal_list.insert(1, "shrimp")
print(animal_list)
animal_list.remove("bee")
print("list name.clear removes everything")
animal_list.pop()
print(animal_list)
print(animal_list.index("fish"))
animal_list = ["dog", "dog", "shrimp", "monkey", "fish", "bird"]
print(animal_list.count("dog"))
animal_list.sort()
print(animal_list)
animal_list.reverse()
print(animal_list)
animal_list2 = animal_list.copy()
print(animal_list2)
print()
print()
print("TUPLES")
print()
coordinates = (4, 5)
print(coordinates[0])
print("tuples can\'t be changed and use normal brackets lists use square brackets")
print()
print("functions")


