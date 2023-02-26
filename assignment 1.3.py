def is_rotation(str1, str2):

    if len(str1) != len(str2):
        return False


    if str2 in str1 + str1:
        return True

    return False

str1 = "hello"
str2 = "lohel"
if is_rotation(str1, str2):
    print(str2, "is a rotation of", str1)
else:
    print(str2, "is not a rotation of", str1)
