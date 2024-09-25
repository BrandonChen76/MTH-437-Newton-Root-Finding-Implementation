import numpy as np

#bisection method from before
def bisectionRootFinding(g, pos, neg, t):

    #Start iteration at 0, choose one of the 2 bounds to be the approximation to start
    n = 0
    approximation = pos

    #Just in case parameters are entered wrong
    if g(pos) <= 0 and g(neg) >= 0:
        print("Swap the second and third parameters!")
        return None
    elif g(pos) < 0:
        print("Second parameter is wrong!")
        return None
    elif g(neg) > 0:
        print("Third parameter is wrong!")
        return None
    
    #Maybe starting bounds are the answer already
    if g(pos) == 0:
        print("\nFinal approximation:\n" + str(approximation))
        return approximation
    elif g(neg) == 0:
        approximation = neg
        print("\nFinal approximation:\n" + str(approximation))
        return approximation

    #Continue iteration if PC doesnt doesnt reach "0"
    while ((pos - neg) / 2) != 0:

        #Update new approximation using bisection
        approximation = (pos + neg) / 2
        yValue = g(approximation)

        #Check to see the new approximation is within tolerance
        if(abs(yValue) < t):
            break

        #Otherwise update the new pos or neg
        elif yValue > 0:
            pos = approximation
        else:
            neg = approximation

        n += 1

        #Log each iteration
        print("Iteration:", n, "\t\tApproximation:", approximation)

    return approximation

#function: f(x) = x^3 - 6
def f(x):
    return x ** 3 - 6

#derivative of f(x)
def F(x):
    return 3 * x ** 2

#input: g is function; pos and neg is for bisection part; t is tolerance
#output: final approximation
def newtonRootFinding(g, pos, neg, t):

    n = 0

    #Get initial guess with bisection method
    guess = bisectionRootFinding(g, pos, neg, .01)

    #Keep iterating if approximation isn't the root
    while g(guess) != 0:
        
        #Get new guess
        newGuess = guess - f(guess) / F(guess)

        #Get error
        error = abs(newGuess - guess) / abs(newGuess)

        n += 1

        #Log each iteration
        print("Iteration:", n, "\t\tApproximation:", newGuess, "\t\tRelative error:", error,)

        #Check if guess is within tolerance
        if abs(newGuess - guess) < t:
            break

        guess = newGuess
    
    #Print final approximation
    print("\nFinal approximation:\n" + str(guess))
    return guess

answer = newtonRootFinding(f, 2, 1, .000000000001)