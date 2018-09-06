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

def multiplyList(myList) :
    
    # Multiply elements one by one
    result = 1
    for x in myList:
         result = result * x 
    return result 

def crypt(*equation):
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



        if kappa == 'a' or 'A':
            try:
                if sum(get_value(word, sol) for word in left) == get_value(right, sol):
                     print("  (crypto addition result is: {})".format( sol))
                         
            except :
                print("iska solution hi nahi he ")
                input("Press enter to exit ;)")

        if kappa == 'm' or 'M':
            try:
                if multiplyList(get_value(word, sol) for word in left) == get_value(right, sol):
                    print("  (crypto multiplication result is: {})".format( sol))
            except :
                print("iska solution hi nahi he ")
                input("Press enter to exit ;)")

            
if __name__ == '__main__':
    alpha = input("please enter the first word ")
    beta = input("please enter the second word ")
    gamma = input("please enter the output word  ")
    kappa = input("enter 'a' for addtiton or 'm' for multiplication ")
    crypt(alpha,beta,gamma,kappa)
