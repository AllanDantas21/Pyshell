import os

def exec_builtins(cmd, env):
    s_cmd = cmd.split(" ")
    
    if s_cmd[0] == 'exit':
        exit(0)
    elif s_cmd[0] == 'echo':
        my_echo(s_cmd)
    elif s_cmd[0] == 'env':
        my_env(env)
    elif s_cmd[0] == 'pwd':
        my_pwd()
    elif s_cmd[0] == 'cd':
        my_cd(s_cmd)
    elif s_cmd[0] == 'export':
        my_export(s_cmd, env)
    else:
        print("Error: Command not found")

def my_echo(s_cmd):
    cmd = " ".join(s_cmd[1:])
    print(cmd)

def my_pwd():
    print(os.getcwd())

def my_env(env):
    if env is None:
        print("Error: Environment variables not provided")
        return
    for key, value in env.items():
        print(f"{key}={value}")
        
def my_cd(s_cmd):
    try:
        if len(s_cmd) == 1:
            os.chdir(os.environ['HOME'])
            return
        os.chdir(s_cmd[1])
    except Exception as e:
        print(f"Error: {e}")

def my_export(s_cmd, env):
    try:
        if len(s_cmd) == 1:
            print("Error: No environment variable provided")
            return
        key, value = s_cmd[1].split("=")
        env[key] = value
    except Exception as e:
        print(f"Error: {e}")