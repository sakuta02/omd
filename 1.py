moscow = {201, 202, 203, 204}
kazan = {203, 204, 205, 206}

if __name__ == '__main__':
    a1 = moscow & kazan
    a2 = moscow - kazan
    a3 = kazan - moscow
    a4 = len(kazan | moscow)

    print(a1, a2, a3, a4, sep='\n')

# {203, 204}
# {201, 202}
# {205, 206}
# 6