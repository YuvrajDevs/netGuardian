# def check_users(file):
#     user_count = 0
#     usernames=[]
#     with open(file, 'r') as file:
#         for line in file:
#             if line.strip().startswith('username'):
#                 usernames.append(line.split()[1])
#                 user_count += 1
#             if user_count >= 3:
#                 return f"Severity:2\nDescription:Too many users present --> {user_count}, Found {usernames}"
#
#
# print(check_users('conf_2038.rtf'))



import re


def check_weak_passwords(file):
    weaks=[]
    with open(file, 'r') as file:
        for line in file:
            if line.strip().startswith('username'):
                parts = line.strip().split()
                if len(parts) >= 4:
                    username = parts[1]
                    # password_type = parts[3]
                    password = parts[-1] if len(parts) > 4 else ""
                    if is_weak_password(password):
                        weaks.append(f"Weak password for user {username}: {password}")
    return f"Severity:1\nDescription:\n{weaks}"

def is_weak_password(password):
    if len(password) < 8:
        return True
    if not re.search(r'[A-Z]', password) or \
            not re.search(r'[a-z]', password) or \
            not re.search(r'[0-9]', password) or \
            not re.search(r'[!@#$%^&*()_+{}|:"<>?~\-\[\]\\;\'`,./]', password):
        return True
    if re.search(r'(.)\1{2,}', password):
        return True
    if re.search(r'123|234|345|456|567|678|789|890|098|987|876|765|654|543|432|321|210', password):
        return True
    return False


print(check_weak_passwords('conf_2038.rtf'))