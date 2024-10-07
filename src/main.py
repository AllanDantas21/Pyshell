from src.validator import valid_prompt
from src.exec import simple_exec
import platform
import sys

def main():
    # if platform.system() != 'Linux':
    #     print("Este programa só pode ser executado em sistemas Linux.")
    #     sys.exit(1)

    while 42:
        cmds = list()
        prompt = input("pyshell> ")
        if prompt == "exit":
            break
        if not valid_prompt(prompt):
            continue
        simple_exec(prompt)

if __name__ == "__main__":
    main()