import pandas as pd


reviews = [
    {"id": 1, "product": "Чехол", "stars": 5},
    {"id": 1, "product": "Чехол", "stars": 3},
    {"id": 1, "product": "Чехол", "stars": 4},
    {"id": 2, "product": "Наушники", "stars": 2},
    {"id": 2, "product": "наушники", "stars": 2},
    {"id": 2, "product": "НАУШНИКИ", "stars": 5},
    {"id": 3, "product": "Планшет", "stars": 5},
    {"id": 4, "product": "Колонка", "stars": 4},
    {"id": 4, "product": "Колонка", "stars": 4},
    {"id": 5, "product": "Кабель", "stars": 1},
]

if __name__ == '__main__':
    df = pd.DataFrame(reviews)
    df['product'] = df['product'].str.lower()

    stats = df.groupby('product').stars.agg(['mean', 'count'])

    a1 = stats['mean']
    a2 = stats.loc[stats['count'] >= 2, 'mean'].idxmin()
    a3 = (df.stars <= 2).sum()
    a4 = a3 / len(df)

    print(a1, a2, a3, a4, sep='\n')

# product
# кабель      1.0
# колонка     4.0
# наушники    3.0
# планшет     5.0
# чехол       4.0
# Name: mean, dtype: float64
# наушники
# 3
# 0.3