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

# import re
#
# def remove_backslashes(text):
#     lines = text.splitlines()
#     clean_lines = [line.rstrip("\\") for line in lines]
#     return "\n".join(clean_lines)
# def check_weak_passwords(file):
#     weaks = []
#     with open(file, 'r') as file:
#         for line in file:
#             if line.strip().startswith('username'):
#                 parts = line.strip().split()
#                 if len(parts) >= 4:
#                     username = parts[1]
#                     password = parts[-1] if len(parts) > 4 else ""
#                     if is_weak_password(password):
#                         weaks.append(f"Weak password for user {username}: {password}")
#
#     # Print weak passwords with newlines
#     print("Severity: 1\nDescription:")
#     for weak_password in weaks:
#         print(remove_backslashes(weak_password))
#
# def is_weak_password(password):
#     if len(password) < 8:
#         return True
#     if not re.search(r'[A-Z]', password) or \
#             not re.search(r'[a-z]', password) or \
#             not re.search(r'[0-9]', password) or \
#             not re.search(r'[!@#$%^&*()_+{}|:"<>?~\-\[\]\\;\'`,./]', password):
#         return True
#     if re.search(r'(.)\1{2,}', password):
#         return True
#     if re.search(r'123|234|345|456|567|678|789|890|098|987|876|765|654|543|432|321|210', password):
#         return True
#     return False
#
#
# print(check_weak_passwords('conf_2038.rtf'))


#
# import re
# def is_weak_password(password):
#     if len(password) < 8:
#         return True
#     if not re.search(r'[A-Z]', password) or \
#             not re.search(r'[a-z]', password) or \
#             not re.search(r'[0-9]', password) or \
#             not re.search(r'[!@#$%^&*()_+{}|:"<>?~\-\[\]\\;\'`,./]', password):
#         return True
#     if re.search(r'(.)\1{2,}', password):
#         return True
#     if re.search(r'123|234|345|456|567|678|789|890|098|987|876|765|654|543|432|321|210', password):
#         return True
#     return False
#
#
# def missing_configurationPassword(file):
#     found = False
#     with open(file, 'r') as file:
#         for line in file:
#             if line.startswith('enable password'):
#                 found = True
#                 password = line.split()[2]
#         if found:
#             if is_weak_password(password):
#                 return ("Severity:1\nConfiguration password is weak.")
#         else:
#             return ("Severity:1\nConfiguration password not found.")
#
#
# print(missing_configurationPassword('conf_2034.rtf'))



def secureAccessProtocols(file):
    warning = set()
    with open(file, 'r') as file:
        for line in file:
            if line.startswith('tftp-server'):
                warning.add(f"tftp {line}")
            elif line.startswith('ip ftp'):
                warning.add(f"ftp {line}")
            elif line.startswith('ip http'):
                warning.add(f"http {line}")
        if len(warning) > 0:
            return f"Severity:2\nInsecure access protocol in lines -->\n{''.join(warning)}"  # Join elements with newlines

text = secureAccessProtocols('conf_2033.rtf')
def remove_backslashes():
    lines = text.splitlines()
    clean_lines = [line.rstrip("\\") for line in lines]
    return "\n".join(clean_lines)
print(remove_backslashes())

