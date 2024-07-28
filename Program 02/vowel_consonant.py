vowel = 'aeiouAEIOU'

letter = input('Enter a Alphabet: ')
if not letter.isalpha():
    print('INVALID!')
else:
    if letter in vowel:
        print(letter,"is Vowel")
    else:
        print(letter,"is Consonant")
