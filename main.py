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


# def secureAccessProtocols(file):
#     warning = set()
#     with open(file, 'r') as file:
#         for line in file:
#             if line.startswith('tftp-server'):
#                 warning.add(f"tftp {line}")
#             elif line.startswith('ip ftp'):
#                 warning.add(f"ftp {line}")
#             elif line.startswith('ip http'):
#                 warning.add(f"http {line}")
#         if len(warning) > 0:
#             return f"Severity:2\nInsecure access protocol in lines -->\n{''.join(warning)}"  # Join elements with newlines
#
# text = secureAccessProtocols('conf_2033.rtf')
# def remove_backslashes():
#     lines = text.splitlines()
#     clean_lines = [line.rstrip("\\") for line in lines]
#     return "\n".join(clean_lines)
# print(remove_backslashes())


# def remove_backslashes(lines):
#     lines = lines.splitlines()
#     clean_lines = [line.rstrip("\\") for line in lines]
#     return "\n".join(clean_lines)
# def check_insecure_snmp(file):
#     lines = []
#     with open(file, 'r') as file:
#         for line in file:
#             if line.startswith('snmp-server'):
#                 parts = line.strip().split()
#                 if parts[-2] in ['v3 noauth', 'v1', 'v2c']:
#                     lines.append(f"Insecure SNMP configuration: {line.strip()}")
#                 else:
#                     if parts[1] == "community":
#                         if parts[-2] == 'public':
#                             lines.append(f"Insecure SNMP configuration: {line.strip()}")
#     text = remove_backslashes("\n".join(lines))
#     if len(text)>0:
#         return f"Severity:2\nInsecure SNMP access detected --> \n{text}"
# print(check_insecure_snmp('conf_2038.rtf'))


# def check_weak_encryption(file):
#     weak_encryption_algorithms = ['des', '3des', 'rc2', 'rc4', 'md5', 'sha-1', 'wep', 'ssl 2.0', 'ssl 3.0', 'tls 1.0',
#                                   'tls 1.1', 'pptp']
#     with open(file, 'r') as file:
#         for line in file:
#             line = line.lower()  # Convert line to lowercase
#             words = line.split()  # Split line into words
#         for algorithm in weak_encryption_algorithms:
#             if algorithm in words:
#                 print(f"Weak encryption algorithm found: {algorithm}")
#
# check_weak_encryption('Sample_configs/conf_2034.rtf')


# def remove_backslashes(lines):
#     lines = lines.splitlines()
#     clean_lines = [line.rstrip("\\") for line in lines]
#     return "\n".join(clean_lines)
# def check_host_authentication(file):
#     interface_up = True
#     authentication_enabled = False
#     interface_name = ''
#
#     with open(file, 'r') as file:
#         list = []
#         for line in file:
#             line = line.strip()
#             if line.startswith('interface'):
#                 if interface_up and not authentication_enabled and interface_name:
#                     list.append(f"Missing host authentication on access port: {interface_name}")
#                 interface_name = line.split()[1]
#                 interface_up = True
#                 authentication_enabled = False
#             elif line == 'shutdown':
#                 interface_up = False
#             elif line == 'dot1x pae authenticator':
#                 authentication_enabled = True
#         if interface_up and not authentication_enabled and interface_name:
#             list.append(f"Missing host authentication on access port: {interface_name}")
#     final =  "\n".join(list)
#     return f"Severity:1\n{remove_backslashes(final)}"
#
#
# print(check_host_authentication('conf_2038.rtf'))


# def control_plane(file):
#     found = False
#     with open(file, 'r') as file:
#         for line in file:
#             if line.strip().startswith('control-plane'):
#                 found = True
#         if not found:
#             return "Control-plane missing"
#
# print(control_plane('conf_2033.rtf'))


def remove_backslashes(lines):
    lines = lines.splitlines()
    clean_lines = [line.rstrip("\\") for line in lines]
    return "\n".join(clean_lines)
def interface_block(config_file_path):
    list=[]
    with open(config_file_path, 'r') as file:
        config_data = file.read()
        config_data=config_data.replace("!         \\","")
        blocks=config_data.split("!\\")
        for x in blocks:
            x=x.strip()
            if x.lstrip().startswith("interface"):
                if (("shutdown" not in x)):
                    if (("storm-control multicast" not in x) and("storm-control unicast" not in x)):
                        xword=x.splitlines()
                        list.append(f"Missing Storm Control on access ports --> {remove_backslashes(xword[0])})")
    final = "\n".join(list)
    return f"Severity:2\nDescription:\n{final}"
print(interface_block('conf_2038.rtf'))



# def remove_backslashes(lines):
#     lines = lines.splitlines()
#     clean_lines = [line.rstrip("\\") for line in lines]
#     return "\n".join(clean_lines)
#
# def port_security(config_file_path, num):
#     list = []
#     desc = 1
#     with open(config_file_path, 'r') as file:
#         config_data = file.read()
#         config_data = config_data.replace("!         \\", "")
#         blocks = config_data.split("!\\")
#         for x in blocks:
#             x = x.strip()
#             xlines = x.splitlines()
#             if x.lstrip().startswith("interface"):
#                 if "shutdown" not in x:
#                     if "switchport port-security" not in x:
#                         list.append(f"Does not contain port security:{xlines[0]}")
#                     for y in xlines:
#                         y = y.lstrip()
#                         if y.startswith('switchport port-security maximum'):
#                             parts = y.split()
#                             if len(parts) >= 4:
#                                 desc = 2
#                                 max = int(parts[3].strip("\\"))
#                             if max > num:
#                                 list.append(f"Number of mac addresses configured on switch are more than what is "
#                                             f"specified:{xlines[0]}")
#     final = "\n".join(list)
#     return f"Severity:{desc}\nDescription:\n{remove_backslashes(final)}"
#
#
# print(port_security("conf_2034.rtf", 4))
