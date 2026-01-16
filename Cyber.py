def check_password(password):
    if len(password) < 6:
        return "Zəif parol ❌"

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)

    if has_upper and has_lower and has_digit:
        return "Güclü parol ✅"
    else:
        return "Orta parol ⚠️"


pwd = input("Parolu daxil et: ")
print(check_password(pwd))
