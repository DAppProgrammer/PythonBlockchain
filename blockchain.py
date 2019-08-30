# Initializing out blockchain list
blockchain = []


def get_last_blockchain_value():
    """ Returns last value of current blockchain """
    if len(blockchain) < 1:
        return None

    return blockchain[-1]


def add_transaction(transaction_amount, last_transaction=[1]):
    """ Append a new value as well as the last blockchain value to the blockchain 

    Arguments:
        transaction_amount: The amount that should be added
        last_transaction: The last blockchain transaction (default [1])
    """
    if last_transaction == None:
        last_transaction = [1]

    blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    return input('Your transaction amount please: ')


def get_user_choice():
    return input('Your choice: ')


def print_blockchain_elements():
    # Output the blockchain list to the console
    for block in blockchain:
        print('Outputing Block')
        print(block)


tx_amount = get_transaction_value()
add_transaction(tx_amount)

while True:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Output the blockchain blocks')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == 1:
        tx_amount = get_transaction_value()
        add_transaction(last_transaction=get_last_blockchain_value(),
                        transaction_amount=tx_amount)
    elif user_choice == 2:
        print_blockchain_elements()
    elif user_choice == 'q':
        break
    else:
        print('Input was invalid, please pick a value from the list!')

print('Done!!!')
