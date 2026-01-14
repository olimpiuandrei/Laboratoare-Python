def unique_pair_sum(numbers, target):
    # set nu permite dublicate
    pairs = set()

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                a = min(numbers[i], numbers[j])
                b = max(numbers[i], numbers[j])
                pairs.add((a, b))

    return pairs

numbers = [1, 2, 3, 4, 3, 5, 6]
target = 7
print(unique_pair_sum(numbers, target))
