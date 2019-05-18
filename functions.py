#Authors: Sean Miltenberger, Spencer Greco, Joe Haun
#Problem #7


#Used to generate a list of states for dfa
def generate_DFA_Table(M,N):
    states = [[0 for k in range(10)]for i in range(N)]
    for i in range(N):
        for k in range(10):
            states[i][k] = ((10*i) + k) %N
  
    return states

def GetSmallestPalindrome(DFA, M, N):
    visited = [[0 for k in range(10)]for i in range(N)]
    not_found = True
    num_list = []
    num = []
    half = M//2
    visited = queue()#used to keep track of what numbers have already been generated
    
    while not_found:
        for i in range(half):
            for k in range(10):
               #loop through matrix indecies for paths that reach 0(accepting state)
                #in half transitions.
                #consider using BFS
                print("")
    return 0

def breadth_first_search(DFA): #Requires testing with whatever function that is working 
    #Function takes in a DFA and returns a string that is accepted and of minimum length
    ToVisit = queue.Queue(0); #Setup queue of states to be visited
    Visited = set() #Setup queue of states visited, initially empty

    Info = dict(); #Information about the state

    Begin = DFA.report_current_state(); #Get current state in the DFA, should be first state if initialized properly
    Info[Begin] = (None, None) #Enter none for beginning state
    ToVisit.put(Begin) #Place Begin on ToVisit queue
    Count = 0; #Set Count to zero
    inputList = list(); #Setup inputList to empty
    while not ToVisit.empty(): #While there are still elements to visit
        Cur = ToVisit.get(); #Get next queue element

        if M.in_accept_state: #If in accept state place values onto inputList and then return it
            while(Info[Cur][0] is not None):
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
    
def couldnt_figure(M, N, go_to):
    num_list = [0 for i in range(go_to)]
    for i in range(1,go_to):
        num_list[i] = (num_list[i-1]+N)
    return num_list

def change_to_pal(num_list, M, go_to):
    str_list = ['0']
    rev_num = ['0']
    pal_list = ['0']
    good_pal = ['0']
    for i in range(1,go_to):
        new = str(num_list[i])
        while len(new) < M//2:
            new = '0' + new #add leading zeroes for numbers < half M
        str_list.append(new)
    for i in range(1,go_to):
        rev_num.append(str_list[i][::-1])
    for i in range(1,go_to):
        pal_list.append(rev_num[i]+str_list[i])

    for i in range(1,go_to):
        if len(pal_list[i]) == M and pal_list[i][0] != '0':
            good_pal.append(pal_list[i])
   
    return good_pal
