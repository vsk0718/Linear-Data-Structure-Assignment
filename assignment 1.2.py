def reverse_array(array):
    # Get the length of the array
    n = len(array)

    # Swap elements from both ends of the array
    for i in range(n // 2):
        array[i], array[n - i - 1] = array[n - i - 1], array[i]

# Example usage
array = [1, 2, 3, 4, 5]
print("Original array:", array)
reverse_array(array)
print("Reversed array:", array)
