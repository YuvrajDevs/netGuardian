def check_users(file):
    user_count = 0
    usernames=[]
    with open(file, 'r') as file:
        for line in file:
            if line.strip().startswith('username'):
                usernames.append(line.split()[1])
                user_count += 1
            if user_count >= 3:
                return f"Severity:2\nDescription:Too many users present --> {user_count}, Found {usernames}"


print(check_users('conf_2038.rtf'))