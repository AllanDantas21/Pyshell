from validator import valid_prompt
from exec import simple_exec
from env import getenv
from exec import executor
import platform
import os
import sys

def main():
    env = os.environ

    while 42:
        cmds = list()
        curr_path = os.getcwd().replace(os.environ['HOME'], '~')
        prompt = input(f"{curr_path}$> ")
        if not valid_prompt(prompt):
            continue
        executor(prompt, env)
      

if __name__ == "__main__":
    main()