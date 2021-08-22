import getpass

current_username = ''
users = {}

def login(username, password) -> bool:
    if username not in users: return False
    if users[username]['password'] == password:
        global current_username
        current_username = username
        return True
    else:
        return False

def register(username, password):
    users[username] = {'password': password, 'balance': 0}

def logout():
    global current_username
    current_username = ''

def get_balance():
    return users[current_username]['balance']

def add(amount:int):
    users[current_username]['balance'] += amount

def withdraw(amount:int):
    users[current_username]['balance'] -= amount

def delete_account():
    users.pop(current_username)

print('wellcome to STUPID BANK!')
while True:
    command = input('what can we do for you? ').lower()
    if command == "register":
        while True:
            username = input('enter your username: ')
            if username in users:
                print(f'{username} exists. please try another one')
            else: break
        while True:
            password = getpass.getpass('enter your password: ')
            confirm = getpass.getpass('confirm your password: ')
            if password != confirm:
                print("passwords dont't match!")
            else:
                register(username, password)
                print('registered sucessfuly. you can login now.')
                break

    elif command == "login":
        username = input('enter username: ')
        password = input('enter password: ')
        if login(username, password):
            print(f'wellcome {username}.')
        else:
            print('username or password is wrong')

    elif command == "logout":
        logout()
        print('loged out sucessfuly.')

    elif command == "balance":
        print('your account balance:',get_balance())

    elif command == "add":
        amount = int(input('enter your amount: '))
        add(amount)
        print('your account balance:', get_balance())

    elif command == "withdraw":
        amount = int(input('enter your amount: '))
        withdraw(amount)
        print('added, your account balance:', get_balance())

    elif command == "delete":
        delete_account()
        print('account deleted')
        
    elif command == "exit":
        print('see you later')

    else:
        print('command not found.')
