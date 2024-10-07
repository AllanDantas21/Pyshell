import os

def completer(text, state):
    options = [cmd for cmd in os.listdir('.') if cmd.startswith(text)] + [cmd for cmd in os.environ.keys() if cmd.startswith(text)]
    if state < len(options):
        return options[state]
    return None