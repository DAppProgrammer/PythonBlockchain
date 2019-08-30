blockchain = [[1]]


def get_last_blockchain_value():
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    blockchain.append([last_transaction, transaction_amount])
    print(blockchain)


add_value(5.5)
add_value(last_transaction=get_last_blockchain_value(), transaction_amount=8.7)
add_value(3.9, get_last_blockchain_value())
