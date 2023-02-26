def first_non_repeated_char(string):
    
    char_counts = {}

   
    for char in string:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    for char in string:
        if char_counts[char] == 1:
            return char

    return None 

string = "aabbcdeeffgghh"
non_repeated_char = first_non_repeated_char(string)
if non_repeated_char:
    print("The first non-repeated character in", string, "is", non_repeated_char)
else:
    print("There are no non-repeated characters in", string)
