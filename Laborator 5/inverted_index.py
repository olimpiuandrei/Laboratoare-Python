def inverted_index(documents):
    index = {}

    for i in range(len(documents)):
        words = documents[i].split()

        for word in words:
            if word not in index:
                # daca cuvantul nu este creez o intrare noua cu un set gol
                index[word] = set()
            index[word].add(i)

    return index



documents = [
    "pisica a stat pe covor",
    "cainele a stat în ceata",
    "pisica si cainele s-au jucat impreuna"
]

print(inverted_index(documents))
