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
    
    while not_found:
        for i in range(half):
            for k in range(10):
               print(no)
    return 0

def couldnt_figure(M, N):
    num_list = [0 for i in range(200)]
    for i in range(1,200):
        num_list[i] = (num_list[i-1]+N)
    return num_list

def change_to_pal(num_list, M):
    str_list = ['0']
    rev_num = ['0']
    pal_list = ['0']
    good_pal = ['0']
    for i in range(1,200):
        new = str(num_list[i])
        while len(new) < M//2:
            new = '0' + new
        str_list.append(new)
    for i in range(1,200):
        rev_num.append(str_list[i][::-1])
    for i in range(1,200):
        pal_list.append(rev_num[i]+str_list[i])
    
    #print(str_list)
    #print(rev_num)
    #print(pal_list)

    for i in range(1,200):
        if len(pal_list[i]) == M and pal_list[i][0] != '0':
            good_pal.append(pal_list[i])
    #print(good_pal)
    return good_pal
