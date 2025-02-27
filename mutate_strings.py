first_word = input()
second_word = input()
words = [first_word]

for i in range(len(first_word)):
    if first_word == second_word:
        break

    if first_word[i] != second_word[i]:
        first_word = first_word[:i] + second_word[i] + first_word[i+1:]

        if first_word not in words:
            words.append(first_word)
            print(first_word)

