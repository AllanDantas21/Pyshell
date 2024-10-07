import subprocess
from my_builtins import exec_builtins

lst_builtins = ['exit', 'echo', 'env', 'pwd', 'cd', 'export', 'unset']

def executor(cmd, env):
    s_cmd = cmd.split(" ")
    
    if s_cmd[0] in lst_builtins:
        exec_builtins(cmd, env)
    elif '<<' in cmd:
        exec_heredoc(cmd, env)
    else:
        simple_exec(cmd, env)

def simple_exec(cmd, env):
    try:
        subprocess.run(cmd, shell=True, env=env)
    except Exception as e:
        print(f"Error: {e}")

def exec_heredoc(cmd, env):
    try:
        parts = cmd.split('<<')
        if len(parts) != 2:
            raise ValueError("Invalid heredoc syntax")
        
        command = parts[0].strip()
        delimiter = parts[1].strip()
        
        heredoc_content = []
        while True:
            line = input(">> ")
            if line == delimiter:
                break
            heredoc_content.append(line)
        
        heredoc_content = '\n'.join(heredoc_content)
        
        process = subprocess.Popen(command, shell=True, env=env, stdin=subprocess.PIPE)
        process.communicate(input=heredoc_content.encode())
    except Exception as e:
        print(f"Error: {e}")