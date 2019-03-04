# 1) Create a list of names and use a for loop to output the length of each name (len()).
names = ['Pepper', 'Sarah', 'Taddes']

for name in names:
  print(f'{name} name length: ' + str(len(name)))

# 2) Add an if check inside the loop to only output names longer than 5 characters.
for name in names:
  if len(name) > 5:
    print('Name printed if longer than 5 characters')
    print(f'{name} name length: ' + str(len(name)))

# 3) Add another if check to see whether a name includes a “n” or “N” character.
for name in names:
  if ('n' or 'N') in name:
    print('Name printed if longer than 5 characters')
    print(f'{name} contains n or N')

# 4) Use a while loop to empty the list of names (via pop())
while len(names) > 0:
  for name in names:
    print(names)
    names.pop()
