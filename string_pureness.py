# You will be given the number n. After that, you'll receive different strings n times. Your task is to check if the
# given strings are pure, meaning that they do NOT consist of any of the
# characters: comma ",", period ".", or underscore "_":
# •	If a string is pure, print "{string} is pure."
# •	Otherwise, print "{string} is not pure!"


number = int(input())
forbidden_signs = [",", ".", "_"]


def pureness_checker(a):
    for sign in forbidden_signs:
        if sign in a:
            return f"{a} is not pure!"

    return f"{a} is pure."


for i in range(number):
    word = input()
    print(pureness_checker(word))
