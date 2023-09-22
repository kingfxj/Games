import random


class Gallows:
    def __init__(self):
        self.step = 0

    def increment(self):
        self.step = self.step + 1

    def show(self):
        l1 = l2 = l3 = l4 = l5 = l6 = ''
        if self.step > 0:
            l2 = l3 = l4 = l5 = l6 = '|'
        if self.step > 1:
            l1 = ' _____'
        if self.step > 2:
            l6 = '/|\\'
        if self.step > 3:
            l2 = '|/    |'
        if self.step == 5:
            l3 = '|     o'
            l4 = '|    /|\\'
            l5 = '|    / \\'
        print(l1, l2, l3, l4, l5, l6, sep='\n')

    def get(self):
        return self.step


class Template:
    def __init__(self, word):
        self.dashes = ['_'] * len(word)

    def show(self):
        # prints the template
        # - self is the Template object
        print(' '.join(self.dashes))

    def update(self, word, char):
        # update the template - if the template is updated the method return True otherwise it returns False
        # - self is the Template object
        # - word is the string that the user is trying to guess
        # - char is a string - it is the letter that the user has entered
        update = False
        for i in range(len(word)):
            if word[i] == char:
                self.dashes[i] = char
                update = True
        return update

    def isComplete(self):
        if '_' in self.dashes:
            return False
        else:
            return True

    def existsIn(self, char):
        # it checks if guess is in the template or no - it returns True or False
        if char in self.dashes:
            return True
        else:
            return False


def main():
    # wordshint.txt is a file that contains a list of word and hint
    infile = open('wordshint.txt', 'r')
    content = infile.read()
    infile.close()
    alist = content.splitlines()
    # Choose a random entry
    entry = random.choice(alist)
    print(entry)

    # Separate the word and the hint
    word, hint = entry.split(',')
    # Display the hint
    print('HINT: ', hint)

    # Set gameOver to False, set up incorrect list, create myTemplate and hangman
    gameOver = False
    incorrect = []
    # Object is created by calling a function hat has the same name as the class
    myTemplate = Template(word)
    hangman = Gallows()
    myTemplate.show()

    while not gameOver:
        # Ask player to enter guess and validate the guess
        guess = input('Enter a letter: ')
        while guess in incorrect or myTemplate.existsIn(guess):
            guess = input('Invalid guess! Enter letter again: ')
        result = myTemplate.update(word, guess)
        myTemplate.show()
        if not result:
            incorrect.append(guess)
            incorrect.sort()
            print(','.join(incorrect))
            hangman.increment()
            hangman.show()
        if hangman.get() == 5 or myTemplate.isComplete():
            gameOver = True

    if myTemplate.isComplete():
        print('Congratulations !')
    else:
        print('RIP')

    print('The word is', word)
    infile.close()


main()
