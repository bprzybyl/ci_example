# Brooks Przybylek
# CS_362_C400_S2020 A2: TDD Hands On
# 05/12/2020
#
# This function should return True only if the following conditions
# are met:
# - Must be between 8 and 20 characters (inclusive)
# - Must contain at least one lowercase letter
# - Must contain at least one uppercase letter
# - Must contain at least one digit
# - Must contain at least one symbol from: ~`!@#$%^&*()_+-=
# - You may assume that only strings will be sent to the check_pwd.


def check_pwd(pwd):
    accepted_symbols = ["~", "`", "!", "@", "#", "$", "%", "^",
                        "&", "*", "(", ")", "_", "+", "-", "="]
    if len(pwd) < 8 or len(pwd) > 20:
        return False
    elif not any(map(str.islower, pwd)):
        return False
    elif not any(map(str.isupper, pwd)):
        return False
    elif not any(map(str.isdigit, pwd)):
        return False
    elif not any(symbol in pwd for symbol in accepted_symbols):
        return False
    return True
