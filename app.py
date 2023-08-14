# PYHTON DOCUMENTATION

#author @jeevan hr

# FisrtName = 'john'
# LastName = 'Smith'
# name = FisrtName + LastName
# AGE = '20'
# patient='new'
# print(name+ patient+AGE)
# print('whats your name ?')
# print('what is your favorite color?')
# print('mosh likes blue')

# Getting Input
# name = input('What is your name? ')
# fav_color = input('what is your fav color? ')
# print(name + ' likes '+ fav_color)
#

# Type Conversion
# 1 asking birth year from user and finding there age
# birth_year = input('Birth year :')
# print(type(birth_year))
# age = 2023 -int (birth_year)
# print(type(age))
# print(age)
# 2 Ask
# a user their weight in (in pounds ), convert it to kilograms and print o terminal
# weight_in_pounds = input('enter your weight in pounds: ')
# weight_in_kilogram = int(weight_in_pounds) / 2.205
# print('weight in kg is '+ str(weight_in_kilogram))

# Strings
#1
#course = '''
#Hola Soya DORA

#WE WELCOME YOU TO THE WORLDS BEST GANGSTA MONK  PAGE AVIALBEL ON THE INTERNET

#THANK YOU
#THE SUPPORT TEAM
# '''
#another = course[:]

#print(another)
#formatted string
#first = 'jhon'
#last = 'smith'
#message = first + ' [ ' + last + '] is a coder'
#msg = f'{first} [{last}] is a coder'
#print(msg)

#string methods
#course = 'Python for beginners'
# len function is used to total number of char in sting
#genral purpose function
#print(len(course.upper()))

#To print the string in uppercase
#print(course.upper())

# To print the string in lowercase
#print(course.lower())

# To find the charactor in the string
#print(course.find('the charactor'))

#To replace
#print(course.replace('P' , 'z'))

#To check whether the given charactors in string are true or false
#print('....' in course)


# Arthimatic operator
#x = 10 + 34* 24
#print(x)

#operation prodrecure
#x= 10 + 3 * 2 ** 2
#print(x)

#order of operation
#parenthesis
#exponentiation 2 ** 3
#multiplication or division
#addition or subtraction
#example 1
#x= (2+3) * 10-3
#print(x)


#this roundup the function to the nearest value
#x = 2.9
#print(round(x))

#To get absolute value  of the finction(given any -ve value it will return only postive value)
#x = -2.9
#print(abs(x))

#to import math libary in the program we use
# import math       -- then we go thorugh the libary
#math module libary link -- https://docs.python.org/3/library/math.html
#import math
#print(math.ceil(3.4))  -- rounds up the value to next value
#print(math.floor(3.4)) -- rounds up the value to previous value

#if statements
#ex.1
#is_hot = False
#is_cold = False
#if is_hot:
#    print("It's a hot day")
#   print("Drink  plenty if water")
#   print("enjoy your day")
#elif is_cold:
#   print("it's a cold day")
#  print("Wear warm clothes")
# print("enjoy your day")
#else:
 #   print("it'fs a lovely day")
 #ex.2
#price_of_house=100000
#has_goodcredit = True

#if has_goodcredit:
#     down_payment = 0.1* price_of_house
#else :
 #    down_payment = 0.2* price_of_house
#print(f"Down payment: ${down_payment}")


#logical operator
#ex1
#has_high_income  = False
#has_good_credit = True
#if has_good_credit and has_high_income:
# print("Eligible for loan")

 #AND: BOTH
 #OR: at least one
 #ex2
#has_good_credit = True
#has_criminal_record = False

#if has_good_credit and not has_criminal_record:
 #   print("eligble for loan")

 #AND NOT
#has_good_credit = True
#has_criminal_record = False

#if has_good_credit and not has_criminal_record:
#     print("eligible for loan")

#tip: avoid spaces in the begining



#COMPARSION OPERATOR\
#eg 1:

#git temperature = 35

#if temperature != 30:
 #   print("Its a HOT DAY")
#else:
 #   print("its not a hot day")

#eg 2
#if temperature == 35:
#print("its a good day")
#else:
#print("its not a good day")
#this will be contiuned
