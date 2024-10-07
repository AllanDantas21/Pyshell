import os

def getenv():
    env_list = [f"{key}={value}" for key, value in os.environ.items()]