import subprocess

def simple_exec(cmd, env):
    try:
        subprocess.run(cmd, shell=True, env=env)
    except Exception as e:
        print(f"Error: {e}")