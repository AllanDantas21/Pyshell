import os

def exec_builtins(cmd, env):
    s_cmd = cmd.split(" ")
    
    if s_cmd[0] == 'exit':
        exit(0)
    elif s_cmd[0] == 'echo':
        my_echo(s_cmd)
    elif s_cmd[0] == 'env':
        print_env()
    elif s_cmd[0] == 'pwd':
        my_pwd()
    else:
        print("Error: Command not found")

def my_echo(s_cmd):
    cmd = " ".join(s_cmd[1:])
    print(cmd)

def my_pwd():
    print(os.getcwd())

def my_env():
    printf("env chamado")
        