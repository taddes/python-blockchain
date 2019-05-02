import functools
# Genesis block - hard coded start chain
MINING_REWARD = 10

genesis_block =  {
    'previous_hash': '',
    'index': 0,
    'transactions': []
  }
  # Initialize our empty blockchain
blockchain = [genesis_block]
open_transactions = []
owner = 'Taddes'
participants = {'Taddes'}


def hash_block(block):
    return  '-'.join([str(block[key]) for key in block])


def get_balance(participant):
    """ Find out how much participant has sent (how many transactions they are sender)
        and to determine how much the participant has recieved (how many transactions they are recipient)
        :tx_sender: returned variable that gives 
    """
    tx_sender = [[tx['amount'] for tx in block['transactions'] if tx['sender'] == participant] for block in blockchain]
    open_tx_sender = [tx['amount'] for tx in open_transactions if tx['sender'] == participant] 
    tx_sender.append(open_tx_sender)
    amount_sent = functools.reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0, tx_sender, 0)
    # This fetches received coin amounts of transactions that were already in the block
    # We ignore open transactions here because you shouldn't be able to spend
    tx_recipient = [[tx['amount'] for tx in block['transactions'] if tx['recipient'] == participant] for block in blockchain]
    amount_received =  functools.reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0, tx_recipient, 0)

    # Return total balance
    return amount_received - amount_sent


def get_last_blockchain_value():
  """ Returns the last value of the current blockchain. """
  if len(blockchain) < 1:
    return None
  return blockchain[-1]


def verify_transaction(transaction):
    sender_balance = get_balance(transaction['sender'])
    return sender_balance >= transaction['amount']



def add_transaction(recipient, sender=owner, amount=1.0):
  """ Append a new value, as well as the last blockchain value to the blockchain

  Arguments:
    :recipient: The recipient of the coins.
    :sender: The sender of the coins.
    :amount: The amount of coins sent with transaction (default=1.0)
  """
  transaction = {
    'sender': sender,
    'recipient': recipient,
    'amount': amount
  }

  if not verify_transaction(transaction):
      open_transactions.append(transaction)
      # Since this is defined as a set, any duplicate vlaues will be ignored!
      participants.add(sender)
      participants.add(recipient)
      return True
  return False
      

def mine_block():
    """ All open transactions taken, added to a new block, then added to blockchain.
        Can invalidate following block if hash does not match previous.
    """  
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    reward_transaction = {
        'sender': 'MINING',
        'recipient': owner,
        'amount': MINING_REWARD
    }
    copied_transactions = open_transactions[:]
    copied_transactions.append(reward_transaction)
    # for key in last_block:
    #   value = last_block[key]
      # hashed_block = hashed_block + str(value)
    block = {
      'previous_hash': hashed_block,
      'index': len(blockchain),
      'transactions': open_transactions
    }
    blockchain.append(block)
    return True

def get_transaction_value():
    """ Returns the input of the user (a new transaction amount) as a float """
    # Get the user input, transform it from a string to a float and store it
    tx_recipient = input('Enter the recipient of the transaction: ')
    tx_amount = float(input('Enter the transaction amount, please: '))
    return (tx_recipient, tx_amount)

def get_user_choice():
    """Prompts the user for their choice and returns it."""
    user_input = input('Your choice: ')
    return user_input

def verify_chain():
    """ Verify the current blockchain and return True if it's valid, False if not """
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index - 1]):
            return False
    return True

def verify_transactions():
    return all([verify_transaction(tx) for tx in open_transactions])
        

waiting_for_input = True

def print_blockchain_elements():
  for block in blockchain:
    print('Outputting block:')
    print (block)
  else:
    print('-' * 20)

# tx_amount = get_transaction_value()


while waiting_for_input:
    print('Please choose an option:')
    print('1: Add a new transaction value')
    print('2: Mine a new block')
    print('3: Output the blockchain blocks')
    print('4: Output the participants')
    print('5: Check Transaction Validity')
    print('h: Manipulate the chain')
    print('q: Output the blockchain blocks')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        # Add the transaction amount to the blockchain
        if add_transaction(recipient, amount=amount):
            print('Added Transaction')
        else:
            print('Transaction Failed')
            print(open_transactions)
    elif user_choice == '2':
        if mine_block():
            open_transactions = []
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == '4':
        print(participants)
    elif user_choice == '5':
        if verify_transactions():
            print('All transactions are valid')
        else:
            print('There are invalid transactions')
    elif user_choice == 'h':
        if len(blockchain) >= 1:
          blockchain[0] =  {
            'previous_hash': '',
            'index': 0,
            'transactions': [{'sender': 'Chris', 'recipient': 'Max', 'amount': 100 }]
          }
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Invalid input')
    if not verify_chain():
        print_blockchain_elements()
        print('Invalid blockchain!')
        break
    print('Balance of {}: {:6.2f}'.format('Taddes', get_balance('Taddes')))
else:
  print('User left')


print('Done!')
