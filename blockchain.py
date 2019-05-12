from functools import reduce
import hashlib as hl
import json
from collections import OrderedDict

# reward given to a miner (for creating a new block)
MINING_REWARD = 10
# Genesis block - hard coded start chain
genesis_block =  {
    'previous_hash': '',
    'index': 0,
    'transactions': [],
    'proof': 100
  }

# Initialize our empty blockchain list
blockchain = [genesis_block]
# Unhandled Transactions
open_transactions = []
# We are the owner of this blockchain node, hence this is our identifier (e.g. for sending coins)
owner = 'Taddes'

participants = {'Taddes'}


def hash_block(block):
    """Hashes a block and returns a string representatio of it.

    Arguments:
        :block: The block that should be hashed
    """
    return hl.sha256(json.dumps(block, sort_keys=True).encode()).hexdigest()


def valid_proof(transactions, last_hash, proof):
    guess = (str(transactions) + str(last_hash) + str(proof)).encode()
    guess_hash = hl.sha256(guess).hexdigest()
    print(guess_hash)
    return guess_hash[0:2] == '00'

def proof_of_work():
    last_block = blockchain[-1]
    last_hash = hash_block(last_block)
    proof = 0
    while not valid_proof(open_transactions, last_hash, proof):
        proof += 1
    return proof



def get_balance(participant):
    """ Find out how much participant has sent (how many transactions they are sender)
        and to determine how much the participant has recieved (how many transactions they are recipient)
        :tx_sender: returned variable that gives 
    """
    # Fetch a list of all sent coin amounts for the given person (empty lists are returned if the person was NOT the sender)
    # This fetches sent amounts of transactions that were already included in blocks of the blockchain
    tx_sender = [[tx['amount'] for tx in block['transactions'] if tx['sender'] == participant] for block in blockchain]
    # Fetch a list of all sent coin amounts for the given person (empty lists are returned if the person was NOT the sender)
    # This fetches sent amounts of open transactions (to avoid double spending)
    open_tx_sender = [tx['amount'] for tx in open_transactions if tx['sender'] == participant] 
    tx_sender.append(open_tx_sender)
    amount_sent = reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0, tx_sender, 0)
    # This fetches received coin amounts of transactions that were already in the block
    # We ignore open transactions here because you shouldn't be able to spend
    tx_recipient = [[tx['amount'] for tx in block['transactions'] if tx['recipient'] == participant] for block in blockchain]
    amount_received =  reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0, tx_recipient, 0)

    # Return total balance
    return amount_received - amount_sent


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain. """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def verify_transaction(transaction):
    """Verify a transaction by checking whether the sender has sufficient coins.

    Arguments:
        :transaction: The transaction that should be verified.
    """
    sender_balance = get_balance(transaction['sender'])
    return sender_balance >= transaction['amount']

# This function accepts two arguments.
# One required one (transaction_amount) and one optional one (last_transaction)
# The optional one is optional because it has a default value => [1]


def add_transaction(recipient, sender=owner, amount=1.0):
    """ Append a new value, as well as the last blockchain value to the blockchain

    Arguments:
        :recipient: The recipient of the coins.
        :sender: The sender of the coins.
        :amount: The amount of coins sent with transaction (default=1.0)
    """
        # transaction = {
        #     'sender': sender,
        #     'recipient': recipient,
        #     'amount': amount
        # }

    transaction = OrderedDict([('sender', sender), ('recipient', recipient), ('amount', amount)])

    if verify_transaction(transaction):
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
    # Fetch the current last block of blockchain
    last_block = blockchain[-1]
    # Hash th elast block (=> to be able to compare it to stored hash value)
    hashed_block = hash_block(last_block)
    proof = proof_of_work()
    print(hashed_block)
    # Miners should be rewarded, so here is reward
    # reward_transaction = {
    #     'sender': 'MINING',
    #     'recipient': owner,
    #     'amount': MINING_REWARD
    # }
    reward_transaction = OrderedDict([('sender', 'MINING'), ('recipient', owner), ('amount', MINING_REWARD)])
    copied_transactions = open_transactions[:]
    copied_transactions.append(reward_transaction)

    block = {
      'previous_hash': hashed_block,
      'index': len(blockchain),
      'transactions': copied_transactions,
      'proof': proof
    }
    blockchain.append(block)
    return True

def get_transaction_value():
    """ Returns the input of the user (a new transaction amount) as a float """
    # Get the user input, transform it from a string to a float and store it
    tx_recipient = input('Enter the recipient of the transaction: ')
    tx_amount = float(input('Enter the transaction amount, please: '))
    return tx_recipient, tx_amount

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
        # Here [:-1] excludes the reward from being a part of validation
        if not valid_proof(block['transactions'][:-1], block['previous_hash'], block['proof']):
            print('Proof of work is invalid.')
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
          blockchain[1] =  {
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
