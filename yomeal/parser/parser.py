# import re


def is_word(msg):
    mySet = set(line.strip() for line in open(
        '/Users/bittu/Downloads/gito/YoMeal/yomeal/parser/food.txt'
        ))

    for word in msg.split():
        if word in mySet:
            print(word)


test = "this is banana"
is_word(test)
