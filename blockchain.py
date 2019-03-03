blockchain = []

def get_last_blockchain_value():
  """ Returns the last value of the current blockchain. """
  if len(blockchain) < 1:
    return None
  return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
  """ Append a new value, as well as the last blockchain value to the blockchain

  Arguments:
    :transaction_amount: The amount that should be added.
    :last_transaction: The last blockchain transation (default[1]).
  """
  if last_transaction ==  None:
    last_transaction = [1]
  blockchain.append([last_transaction,  transaction_amount])

def get_transaction_value():
  """ Returns the input of the user (a new transaction amount) as a float """
  # Get the user input, transform it from a string to a float and store it
  user_input = float(input('Your transaction amount, please: '))
  return user_input

def get_user_choice():
  user_input = input('Your choice: ')
  return user_input

def verify_chain():
  block_index = 0
  is_valid = True
  for block in blockchain:
    if block[0] == blockchain[block_index - 1]:
      is_valid = True
    else:
      is_valid = False
      break



def print_blockchain_elements():
  for block in blockchain:
    print('Outputting block:')
    print (block)

tx_amount = get_transaction_value()
add_value(tx_amount)

while True:
    print('Please choose an option:')
    print('1: Add a new transaction value')
    print('2: Output the blockchain blocks')
    print('h: Manipulate the chain')
    print('q: Output the blockchain blocks')
    user_choice = get_user_choice()
    if user_choice == '1':
      tx_amount = get_transaction_value()
      add_value(tx_amount, get_last_blockchain_value())
    elif user_choice == '2':
      print_blockchain_elements()
    elif user_choice == 'h':
      if len(blockchain) >= 1:
        blockchain[0] = [2]
    elif user_choice == 'q':
      break
    else:
      print('Invalid input')

print('Done!')
