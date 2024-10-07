
def valid_quotes(prompt: str) -> bool:
    double_quotes = prompt.count('"')
    single_quotes = prompt.count('\'')
    if double_quotes % 2 == 0 and single_quotes % 2 == 0:
        return True
    return False

def valid_prompt(prompt: str) -> bool:
    ret: bool = valid_quotes(prompt)
    return ret