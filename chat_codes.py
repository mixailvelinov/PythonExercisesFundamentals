# Peter is a programming enthusiast who wants to create a chat where people will send messages via number codes.
# He starts by creating a program for only four messages.
# Create a program that receives the n number of messages sent. On the following n lines, it will receive integer
# numbers. For each number, the program should print a different message:
# •	If the number is 88 - "Hello"
# •	If the number is 86 - "How are you?"
# •	If the number is not 88 nor 86, and it is below 88 - "GREAT!"
# •	If the number is over 88 - "Bye."


def chat_codes(number):
    message = ''

    if number == 88:
        message = "Hello"
    elif number == 86:
        message = "How are you?"
    elif number != 86 and number < 88:
        message = "GREAT!"
    else:
        message = "Bye."

    return message


count = int(input())

for n in range(count):
    secret_number = int(input())
    print(chat_codes(secret_number))
