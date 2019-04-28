from functions import *

run = True
new_input = True
while run == True:
    while new_input == True:
        N = input("Enter a positive integer for the value of N.\n")
        new_input = False
        try:
            N = int(N)
        except ValueError:
            print("{0} is not valid input.".format(N))
            new_input = True

    new_input = True     
    while new_input == True:
        M = input("Enter a positive integer for the length of the palindrome you want to find.\n")
        new_input = False
        try:
            M = int(M)
        except ValueError:
            print("{0} is not valid input.".format(M))
            new_input = True
        
    #Do DFA stuff
    


    run_again = input("Do you want to run the program again?(yes or no)")
    if run_again == "yes":
        run = True
        new_input = True
    else:
        run = False
        
