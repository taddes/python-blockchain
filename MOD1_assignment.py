import math 


#1 Create two variables – one with your name and one with your age
age = 30
name = 'Taddes Korris'
#2 Create a function which prints your data as one string
def print_name_and_age(age, name):
  print(f'I\'m {name} and am {age} years old.')


print_name_and_age(age, name)

#3 Create a function which prints ANY data (two arguments) as one string
def printer(arg1, arg2):
  print(arg1 + ' ' + arg2)

printer("Test", "Print")


#4 Create a function which calculates and returns the number of decades you already lived (e.g. 23 = 2 decades)
def decades(age):
  print(math.floor(age/10)) 

decades(37)