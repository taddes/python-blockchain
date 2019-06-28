"""
f = open('demo.txt', mode='r')
file_content = f.readlines()


for line in file_content:
  # [:-1] removes newline character
  print(line[:-1])

f.close()

# line = f.readline()
# while line:
#   print(line)
#   line = f.readline()
"""
with open('demo.txt', mode='w') as f:
  f.write('Testing this')

