from validator import valid_prompt
from exec import simple_exec
from env import getenv
import platform
import sys

def main():
    env = getenv()

    while 42:
        cmds = list()
        prompt = input("pyshell> ")
        if prompt.lower() == 'exit':
            break
        if not valid_prompt(prompt):
            continue
        simple_exec(prompt, env)

if __name__ == "__main__":
    main()