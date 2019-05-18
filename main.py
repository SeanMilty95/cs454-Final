#Authors: Sean Miltenberger, Spencer Greco, Joe Haun
#Problem #7

from functions import *
from dfa_class import *
from DFA import *

#Variables that keep the main program running
run = True
new_input = True

while run == True:
    #Ask for input until valid input is acquired
    while new_input == True:
        N = input("Enter a positive integer for the value of N.\n")
        new_input = False
        try:
            N = int(N)
        except ValueError:
            print("{0} is not valid input.".format(N))
            new_input = True

    new_input = True
    #Ask for input until valid input is acquired
    while new_input == True:
        M = input("Enter a positive integer for the length of the palindrome you want to find.\n")
        new_input = False
        try:
            M = int(M)
        except ValueError:
            print("{0} is not valid input.".format(M))
            new_input = True
        
    #Do DFA stuff
    dfa_array = generate_DFA_Table(M, N)
    #dfa = DFA2(M, N)
    print("\n")
    print(dfa_array)
    #dfa.print()
    print("\n")


    
    #Refer to the functions.py file for a list of functions used
    #smallest_palindrome = GetSmallestPalindrome(dfa, M, N)
    
    #smallest_palindrome = breadth_first_search(dfa)

    #print("The smallest palindrome divisible by {0} of length {1} is: {2}".format(N, M, smallest_palindrome))

    #Ask to run again
    run_again = input("\nDo you want to run the program again?(yes or no) ")
    if run_again == "yes" or run_again == 'y':
        run = True
        new_input = True
    else:
        run = False
        
