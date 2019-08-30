# Initializing out blockchain list
blockchain = []


def get_last_blockchain_value():
    """ Returns last value of current blockchain """
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    """ Append a new value as well as the last blockchain value to the blockchain 

    Arguments:
        transaction_amount: The amount that should be added
        last_transaction: The last blockchain transaction (default [1])
    """
    blockchain.append([last_transaction, transaction_amount])


def get_user_input():
    return input('Your transaction amount please: ')


tx_amount = get_user_input()
add_value(tx_amount)

while True:
    tx_amount = get_user_input()
    add_value(last_transaction=get_last_blockchain_value(),
              transaction_amount=tx_amount)

    # Output the blockchain list to the console
    for block in blockchain:
        print('Outputing Block')
        print(block)


print('Done!!!')
