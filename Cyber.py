def check_password(password):
    if len(password) < 6:
        return "Weak password"

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)

    if has_upper and has_lower and has_digit:
        return "Secure password"
    else:
        return "Medium password"

password=input("Enter the password: ")
print(check_password(password))
