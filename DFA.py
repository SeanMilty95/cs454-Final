
class DFA2:

    def __init__(self, M, N,):
        self.alphabet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.dfa_list = self.make_dict(M, N)

    def make_dict(self, M, N):
        states = []
        transitions = []
        for i in range(N):
            for k in range(N):
                transitions.append(((10*i)+k)%N)
                print(transitions)
            print(i)
            states.append(transitions)
            transitions.clear()
            
        return states

    def print(self):
        print(self.dfa_list)
              
