#DFA class that can be used to create any DFA
import numpy as np
import queue
import array

class DFA:
    current_state = None;
    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states;
        self.alphabet = alphabet;
        self.transition_function = transition_function;
        self.start_state = start_state;
        self.accept_states = accept_states;
        self.current_state = start_state;
        return;
    
    def transition_to_state_with_input(self, input_value):
        if ((self.current_state, input_value) not in self.transition_function.keys()):
            self.current_state = None;
            return;
        self.current_state = self.transition_function[(self.current_state, input_value)];
        return;
    
    def in_accept_state(self):
        return self.current_state in accept_states;
    
    def go_to_initial_state(self):
        self.current_state = self.start_state;
        return;
    
    def run_with_input_list(self, input_list):
        self.go_to_initial_state();
        for inp in input_list:
            self.transition_to_state_with_input(inp);
            continue;
        return self.in_accept_state();

    def report_current_state(self):
        return self.current_state;

    def get_next_states(self):
        outArray = array.array('i', range(len(self.alphabet)));
        count = 0;
        for i in self.alphabet:
            outArray[count] = self.transition_function[(self.current_state, i[0])];
            count = count + 1;   
        return outArray;
    pass;
