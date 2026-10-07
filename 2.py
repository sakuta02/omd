from collections import Counter


queries = [
    "чехол",
    "iphone",
    "чехол",
    "наушники",
    "iphone",
    "iphone",
    "кабель",
    "чехол",
    "iphone",
]
# ---

a1 = len(queries)
a2 = Counter(queries).most_common()
a3 = a2[0][0]
a4 = '~' + str(int((a2[0][1] / a1) * 100)) + '%'
a5 = [q for q, c in a2 if c == 1]
print(a1, a2, a3, a4, a5, sep='\n')

# 9
# [('iphone', 4), ('чехол', 3), ('наушники', 1), ('кабель', 1)]
# iphone
# ~44%
# ['наушники', 'кабель']