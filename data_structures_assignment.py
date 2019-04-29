# 1) Create a list of “person” dictionaries with a name, age and list of hobbies for each person. Fill in any data you want.

person = [{'name': 'Taddes', 'age': 30, 'hobbies': ['bass', 'coding', 'reading', 'exercise']}, 
          {'name': 'Sarah', 'age': 30, 'hobbies': ['exercise', 'writing', 'crafting']},
          {'name': 'Pepper', 'age': 5, 'hobbies': ['hunting', 'eating plants', 'napping']}]
# 2) Use a list comprehension to convert this list of persons into a list of names (of the persons).
name_list = [name['name'] for name in person ]
print(name_list)
# 3) Use a list comprehension to check whether all persons are older than 20.
age_check = all([age['age'] > 20 for age in person ])
print(age_check)
# 4) Copy the person list such that you can safely edit the name of the first person (without changing the original list).
copied_person = person[:]
print(copied_person)
print(person)
# 5) Unpack the persons of the original list into different variables and output these variables.
name, age, hobbies = person
print(name)
print(age)
