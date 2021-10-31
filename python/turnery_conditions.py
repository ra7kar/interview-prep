# # Turnery conditions
from getpass import getpass

# condition = False

# x = 1 if condition else 0

# print(x)

# print()
# print("--------------------------")
# print()


# # large numbers with underscore for better reading

# num1= 10_000_000_000
# num2 = 100_000_000
# total = num1 + num2

# print(f'{total:,}')


# # Context Managers - meant to manager resources for you.
# # file open close, lock unlock, database connection

# with open('test.txt', 'a+') as f:
#     f.write("\n next line")

# #with open('/Users/rct/src/temp/test.txt', 'r+') as f:
#     ef.flush()
#     print(f.read())

#---------------------------------
# Enumerate function

# names = ['First Name', 'Second Name', 'Thrid name', 'Fourth name', 'Fifth Name']
# heroes = ['first_super', 'second_super', 'third_super', 'fourth_super', '5th']
# universes = ['1', '2','3','4']
# for values in zip(names,heroes, universes):
#     print(values)


#-------------------
# Unpack

# a, b, *c= ( 1, 2, 3,4, 5, )

# print(a)
# print(b)
# print(c)

#----------------------
# Getting and Setting attributes on objects

# class Person():
#     pass

# person = Person()

# person_info = {'first':'Corey', 'last':'Schafer'}

# for key, value in person_info.items():
#     setattr(person, key, value)

# for key in person_info.keys():
#     print(getattr(person, key))


# print(person.first)
# print(person.last)

#-----------------------------
# Secret inputs

username = input("Username : ")
password = getpass("Password : ")