import pandas as pd


days = [
    {"day": "пн", "orders": 20, "revenue": 40_000, "returns": 2},
    {"day": "вт", "orders": 16, "revenue": 19_200, "returns": 4},
    {"day": "ср", "orders": 25, "revenue": 55_000, "returns": 1},
    {"day": "чт", "orders": 10, "revenue": 12_000, "returns": 3},
    {"day": "пт", "orders": 30, "revenue": 48_000, "returns": 3},
]

df = pd.DataFrame(days)
df = df.set_index('day')

a1 = df.revenue.sum()
a2 = df.loc[df.revenue.idxmax()].name
a3 = df.revenue / df.orders
a3.index = df.index
a4 = ' '.join(df[df.returns / df.orders > 0.2].index)

print(a1, a2, a3, a4, sep='\n')
# 174200
# ср
# day
# пн    2000.0
# вт    1200.0
# ср    2200.0
# чт    1200.0
# пт    1600.0
# dtype: float64
# вт чт