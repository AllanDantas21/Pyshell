from validator import valid_prompt
from exec import simple_exec
from env import getenv
from my_builtins import exec_builtins
import platform
import os
import sys

def main():
    env = os.environ

    while 42:
        cmds = list()
        prompt = input("pyshell> ")
        if not valid_prompt(prompt):
            continue
        exec_builtins(prompt, env)
        # simple_exec(prompt, env)

if __name__ == "__main__":
    main()