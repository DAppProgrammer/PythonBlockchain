blockchain = [[1]]


def get_last_blockchain_value():
    return blockchain[-1]


def add_value(transaction_amount):
    blockchain.append([get_last_blockchain_value(), transaction_amount])
    print(blockchain)


add_value(5.5)
add_value(6.3)
add_value(3.9)
