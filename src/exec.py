import subprocess

def simple_exec(cmd_list):
    try:
        result = subprocess.run(cmd_list, capture_output=True, text=True, shell=True)

        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(result.stderr)

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")