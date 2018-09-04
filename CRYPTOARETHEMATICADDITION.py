#CTRPTOARETHEMATIC ADDITION DEVELOPED BY SHUBHAM PANCHAL
#https://github.com/shubham314/cryptoarithematic-solver

import itertools

def get_value(word, substitution):
    s = 0
    factor = 1
    for letter in reversed(word):
        s += factor * substitution[letter]
        factor *= 10
    return s


def crypt(*equation):
    # split equation in left and right
    ## left, right = equation.lower().replace(' ', '').split('=')
    # split words in left part
    ## left = left.split('+')
    # create list of used letters
    left = equation[0].lower() +"+"+ equation[1].lower()
    left = left.split('+')
    right = equation[2].lower()
    print("alpha,beta == ", left)
    print("gamma == ", right)
    print("starting processing...")
    letters = set(right)
    for word in left:
        for letter in word:
            letters.add(letter)
    letters = list(letters)

    digits = range(10)
    for perm in itertools.permutations(digits, len(letters)):
        sol = dict(zip(letters, perm))
 
        try:
            if sum(get_value(word, sol) for word in left) == get_value(right, sol):
                print(' + '.join(str(get_value(word, sol)) for word in left) + " = {} (result is: {})".format(get_value(right, sol), sol))

        except :
            print("iska solution nahi he ")
if __name__ == '__main__':
    alpha = input("please enter the first word of addition ")
    beta = input("please enter the second word of addition ")
    gamma = input("please enter the output word  ")
    crypt(alpha,beta,gamma)
