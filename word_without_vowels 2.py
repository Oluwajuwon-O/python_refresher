word_without_vowels = ""

# Prompt the user to enter a word
# and assign it to the user_word variable.
user_word = input('enter a word: ')

for letter in user_word:
    # Complete the body of the loop.
    if letter.upper() == 'A' or letter.upper() == 'E' or letter.upper() == 'I' or letter.upper() == 'O' or letter.upper() == 'U':
        continue
    for i in letter:
        word_without_vowels += letter.upper()
        
# Print the word assigned to word_without_vowels.
print(word_without_vowels)
