
class NodeExpander():
    def __init__(self, parent_node):
        self.parent_node = parent_node
        self.child_nodes = []
        self.available_actions = []
        
    # Helper functions to do expansion------------------------
    def generate_one_step_thought(self):
        """A1 from paper, take one step towards an answer"""
        
    def generate_direct_answer(self):
        """A2 from paper, answers some query"""
    
    def generate_subquestions_with_answer(self):
        """A3 from paper, think of subquestions and answer them"""
        
    def generate_new_subquestion_answers(self):
        """A4 from paper, Re-Answer previously written subquestions"""
        
    def generate_rephrased_question(self):
        """A5 from paper, rephrase a question"""
        
    #---------------------------------------------------------
        
    def expand_parent(self):
        """Main function to expand parent based on appropriate actions"""
        
    