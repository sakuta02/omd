import pandas as pd

orders = [
    {"id": 1, "buyer": "anya", "status": "delivered", "amount": 900},
    {"id": 2, "buyer": "boris", "status": "returned", "amount": 4_500},
    {"id": 3, "buyer": "anya", "status": "delivered", "amount": 1_500},
    {"id": 4, "buyer": "vera", "status": "delivered", "amount": 3_200},
    {"id": 5, "buyer": "boris", "status": "delivered", "amount": 700},
    {"id": 6, "buyer": "gleb", "status": "returned", "amount": 2_100},
]


df = pd.DataFrame(orders)
a1 = df[df['status'] == 'returned'].amount.sum()
a2 = ' '.join(df[df['status'] == 'returned'].buyer.unique())
a3 = len(df[df['status'] == 'delivered'])
a4 = df[df['status'] == 'delivered'].amount.mean()


print(a1, a2, a3, a4, sep='\n')
# 6600
# boris gleb
# 4
# 1575.0