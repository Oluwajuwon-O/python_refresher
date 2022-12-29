input_word = input('enter the word: ')
right_word = 'chupacabra'

while True:
    if input_word == right_word:
        print("You've successfully left the loop")
        break
    else:
        input_word = input('Wrong! enter another word: ')
        