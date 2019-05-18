
class DFA2:

    def __init__(self, M, N,):
        self.alphabet = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.dfa_dictionary = self.make_dict(M, N)

    def make_dict(self, M, N):
        states = {}
        transitions = {}
        for i in range(N):
            si = str(i)
            states.update({si:0})
            for k in range(N):
                sk = str(k)
                for a in range(len(self.alphabet)):
                    transitions.update({sk:((10*i+int(self.alphabet[a])) % N)})
                    print(transitions)
            states.update({si:transitions})
            
        return states

    def print(self):
        print(self.dfa_dictionary)
              
