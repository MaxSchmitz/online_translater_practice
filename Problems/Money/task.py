transactions = [(38177, 34.38), (876, 999.99), (654276, 653678), (54366, 0.99),
                (546, 987.65), (876, 3456), (654276, 0.55), (38177, 876.75), (876, 98.7)]

# create transaction_dict
# Python code to convert into dictionary

def Convert(tup, di):
    for a, b in tup:
        di.setdefault(a, []).append(b)
    return di


# Driver Code

transaction_dict = {}
transaction_dict = Convert(transactions, transaction_dict)