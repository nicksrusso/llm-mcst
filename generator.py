import ollama


class Generator():
    """Generates children nodes from a given node"""
    
    def __init__(self, model, settings) -> None:
        self.model = model  # Set model we want to ping in ollama
        
        # stolen from Rstar
        self.num_subquestions = settings['num_subquestions']
        #self.num_a1_steps = settings['num_a1_steps']
        self.num_votes = settings['num_votes']
        #self.max_tokens = settings['max_tokens']
        #self.enable_potential_score = settings['enable_potential_score']
        
        
        pass