# Simple word replacement program exercise 

def replace_word():
    str = "Hello World! I am Fidencio, hi hi hi"
    word_to_replace = input("Enter word you want to replace: ")
    word_replacement = input("Enter word replacement: ")
    print(str.replace(word_to_replace, word_replacement))

replace_word()