import subprocess
from my_builtins import exec_builtins

lst_builtins = ['exit', 'echo', 'env', 'pwd', 'cd', 'export', 'unset']

def executor(cmd, env):
    s_cmd = cmd.split(" ")
    
    if s_cmd[0] in lst_builtins:
        exec_builtins(cmd, env)
    else:
        simple_exec(cmd, env)

def simple_exec(cmd, env):
    try:
        subprocess.run(cmd, shell=True, env=env)
    except Exception as e:
        print(f"Error: {e}")