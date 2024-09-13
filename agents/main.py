import ollama
import argparse
import os
import json
import generator


if __name__=="__main__":
    model="phi-3.5"
    
    prompt = "James creates a media empire. He creates a movie for $2000. Each DVD cost $6 to make. He sells it for 2.5 times that much. He sells 500 movies a day for 5 days a week. How much profit does he make in 20 weeks?"
    
    '''
    Correct answer:
    
    Maria - 1996
    Fifth child (Sarah) - 1997
    Carol - 1998
    John - 2000
    Michael - 2000
    '''
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    arg_file = os.path.join(script_dir, "input_files", "basic.json")
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-af", "--argument-file", help="file holding settings for this run", default=arg_file)
    
    args = parser.parse_args()
    
    with open(args.argument_file, 'r') as f:
        settings = json.load(f)
        
    gen = generator.Generator(model=settings['model'], settings=settings)
    print()