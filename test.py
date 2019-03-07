# List Comprehension
blockchain = [5, 10, 15, 20]
blockchain_double = []

for key in blockchain: 
    blockchain_double.append(key * 2)

print(blockchain_double)

# Comprehension Example
print('Enumeration Example')
blockchain_double = [key * 2 for key in blockchain]

print(blockchain_double)