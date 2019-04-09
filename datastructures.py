simple_list = [1 ,2, 3, 4]
simple_list.extend([5,6,7])
print(simple_list)

d = {'name': 'Taddes'}
# Get keys and values
print(d.items())
for k, v in d.items():
  print(k,v)

# tuple is immutable
t = (1,2,3)

# del() can be run on any data structure to remove an element, except for tuple and sets
