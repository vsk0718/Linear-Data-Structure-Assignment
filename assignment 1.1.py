def find_pairs(array, target_sum):
    pairs = []
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == target_sum:
                pairs.append((array[i], array[j]))
    return pairs

# Example usage
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_sum = 11
pairs = find_pairs(array, target_sum)
print(pairs)
