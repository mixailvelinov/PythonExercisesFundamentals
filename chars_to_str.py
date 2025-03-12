# Write a function that receives 3 characters. Concatenate all the characters into one string and print it on the
# console.

def concat_chars(a, b, c):
    result = a + b + c
    return result


char_1 = input()
char_2 = input()
char_3 = input()

print(concat_chars(char_1, char_2, char_3))