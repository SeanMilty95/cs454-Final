#Authors: Sean Miltenberger, Spencer Greco, Joe Haun
#Problem #7

from dfa_class import *

#Used to generate a list of states for dfa
def generate_DFA_Table(M,N):
    states = [[0 for i in range(N)]for k in range(N)]
    for i in range(N):
        for k in range(N):
            states[i][k] = ((10*i) + k) %N
        
            
    
            
    return states

def GetSmallestPalindrome(DFA, M, N):
    smallest_palindrome = 0
   
    return smallest_palindrome


def breadth_first_search(DFA): #Requires testing with whatever function that is working 
    #Function takes in a DFA and returns a string that is accepted and of minimum length
    ToVisit = queue.Queue(0); #Setup queue of states to be visited
    Visited = set() #Setup queue of states visited, initially empty

    Info = dict(); #Information about the state

    Begin = DFA.report_current_state(); #Get current state in the DFA, should be first state if initialized properly
    Info[str(Begin)] = None #Enter none for beginning state
    ToVisit.put(Begin) #Place Begin on ToVisit queue
    Count = 0; #Set Count to zero
    inputList = list(); #Setup inputList to empty
    while not ToVisit.empty(): #While there are still elements to visit
        Cur = ToVisit.get(); #Get next queue element

        if DFA.in_accept_state and Count != 0: #If in accept state place values onto inputList and then return it
            while(Info[str(Cur)] is not None):
                  Cur, inputVal = Info[Cur];
                  print(inputVal);
                  inputList.append(inputVal);
            return inputList.reverse();

        for (Next, InputVal) in DFA.get_next_states(): #Get next states and place onto ToVisit queue if not previously visited
            if Next in Visited:
                continue
            if Next not in ToVisit:
                Info[Next] = (Cur, InputVal);
                ToVisit.put(Next);
        Count = Count + 1; #Increment count to keep moving through the DFA
        Visited.add(Cur);
        return inputList; #Return the inputList queue regardless of what is in it
