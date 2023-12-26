correct_word = 'chupacabra'

guess_word= input('guess the right word: ')

while guess_word != correct_word:
    guess_word = input('Wrong! try again: ')
    if guess_word == correct_word:
        print("You've successfully left the loop.")
        
        

correct = 'chupacabra'

while True:
    word = input('guess the word: ')
    if word == correct:
        print("You've successfully left the loop")
        break
    