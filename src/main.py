from src.validator import valid_prompt

def main():
    while 42:
        prompt = input("pyshell> ")
        if prompt == "exit":
            break
        valid_prompt(prompt)

if __name__ == "__main__":
    main()