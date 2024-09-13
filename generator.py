import ollama


class Generator():
    """Generates children nodes from a given node"""
    
    def __init__(self, model, args) -> None:
        self.model = model  # Set model we want to ping in ollama
        
        # stolen from Rstar
        self.num_subquestions = args.num_subquestions
        self.num_a1_steps = args.num_a1_steps
        self.num_votes = args.num_votes
        self.max_tokens = args.max_tokens
        self.enable_potential_score = args.enable_potential_score
        
        
        pass