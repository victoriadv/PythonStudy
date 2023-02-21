# int - integer - 1, 2, 20, 35, 4
# str - string - 'hello', "h"
# float - 1.25, 2.5, 1.0
# bool - bolean - True/False
# print(2 + 2)
# print("hello " + "world!")
# 2 + 2 = 4
# "2" + "2" = "22"
# print(first_number + second_number)
# print(int(1.25))
# print(int(False))
# first_number = int(input("Please type a first number: ")) # "15"
# second_number = int(input("Please type a second number: ")) # "25"
# operator = input("Please type a operation: ")
# if operator == "+":
#     print(first_number + second_number)
# elif operator == "-":
#     print(first_number - second_number)
# elif operator == "*":
#     print(first_number * second_number)
# elif operator == "/":
#     print(first_number / second_number)
# else:
#     print("Our calculator don't know this operation!")

# b = False
# if not b:
#     print(True)

# weather = input("Which weather do you have ? ")
# if weather == "rainy" or weather == "cold":
#     print("Take a jacket!")
# elif weather == "sunny":
#     print("Take a t-shirt!")
# else:
#     print("I don't know what you need to take :(")


# a = int(input("type number: "))
# if a > 1 and a < 5:
#     print("hello small A")
# elif a > 5 and a < 15:
#     print("hello middle A")
# elif a >15 and a < 1000:
#     print("hello big A")

# firstNumber = 5 # camelCase
# first_number = 5 # snake_case
# a = [1, 2, 3, 4, 5, 6]
# for el in a:
#     print(el)

# file = open("test.txt", "r")
# print(file.read())
# file.close()

def suma(x, y=5):
    return x + y


first_number = int(input("Hello"))
abc = suma(first_number, 10)

print(abc)