import random
def make_shuffle(word):
    new_word = random.sample(word,k=len(word))
    new_word = ''.join(new_word)
    return new_word
def puzzle_words(score,word):
    new_word = make_shuffle(word)
    print("\nArrange the letters to form a valid words")
    print(new_word)
    user_word = input()
    if user_word.upper() == word:
        print("Correct")
        score+=1
    else:
        print("Wrong")
        score-=1
    return score
def main():
    score = 0
    words = ['FATHER','BREAK','COUNTRY','GREEN','AEROPLANE']
    words = random.sample(words,k=len(words))
    for word in words:
        score = puzzle_words(score,word)
    print("Net Score is ",score)
main()
