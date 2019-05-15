#Authors: Sean Miltenberger, Spencer Greco, Joe Haun
#Problem #7

from dfa_class import *

#Used to generate a list of states for dfa
def generate_DFA_Table(N):
    #dfa = ['q'+str(i) for i in range(N)]
    S = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}; #Possible Symbol Choices for DFA from 0-9
    States = dict(); #Initialize States to place values into it
    TranTable = dict(); #Initialize Transition Table to place values into it
    for i in range(0, N):
        States[i] = i; #Set each state 
        for j in S:
            TranTable[(i,j)]=j%N; #Each transition should be the state value modulos N
    
    Final = {0};
    dfa = DFA(States, S, TranTable, N, Final);
    #Will possibly need to make a NxN matrix
    
    return dfa

def smallTransferFunctionCalc():
    return 

def GetSmallestPalindrome(dfa_list, M):
    is_full = False
    smallest_palindrome = 0
    half = int(M/2)
    
    #List to hold the last half of the palidrome
        #puts a 0 at every index
    num_list = [0 for i in range(half)]
    """
    I think we will need a list of digits to use the dfa table but I could be wrong.
    Also it may be faster to increment an integer and listify it when we test it.
    """

    #Loop to add to the list of digits 
    while is_full != True:
        stop = False
        for i in range(half):
            if not stop:
                num_list, stop = change_number_value((half-1-i), num_list)

        #Uncomment the below print function to see what is being generated here     
        """
        print(num_list)
        """
        """
        Might have to abandon this and create an NxN Dfa table and use BFS
        """
        
        #check number list for is modulus N using the dfa list

        #if true flip it aroud and add to current number list

        #check if smaller than smallest palindrome variable
            #If smaller assign lower number

        #Checks if list is full (ex. [9,9,9]
        is_full = check_isFull(num_list, half)
        
    print(num_list)
    return smallest_palindrome

#This function takes a list and adds one to the appropriate place
def change_number_value(index, num_list):
    #If a number was added it returns True so the list will be tested
        #without more additions
    stop_loop = False
    if num_list[index] == 9 and index != 0:
        if num_list[index-1] == 9:
            return num_list, False
        else:
            num_list[index] = 0
            num_list[index-1] += 1
            stop_loop = True
    elif num_list[index] == 9 and index == 0:
        return num_list, False
    else:
        num_list[index] += 1
        stop_loop = True

    return num_list, stop_loop

#Checks if list is full of 9's
def check_isFull(num_list, half):
    is_full = True
    for k in range(half):
        if num_list[k] != 9:
            is_full = False
    return is_full
