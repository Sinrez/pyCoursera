import re

def is_password_hard(password: str) -> bool:
    """This function return True, if `password` hard, otherwise return False!"""
    if len(password) < 12:
        return False
    else: 
        down_register_pattern = re.search('[a-z]', password) 
        #print(down_register_pattern)
        up_register_pattern = re.search('[A-Z]', password)
        #print(up_register_pattern)
        is_digit_pattern = re.search('[\d]', password)
        #print(is_digit_pattern)
        if down_register_pattern and up_register_pattern and is_digit_pattern:
            return True
        else:
            return False  