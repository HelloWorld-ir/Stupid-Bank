import getpass

current_username = ''
users = {}

def login_required(func):
    def wrapper(*args, **kwargs):
        if current_username != '':
            func(args, kwargs)
        else:
            print('you are not logged in. please login')
    return wrapper

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

@login_required
def logout():
    global current_username
    current_username = ''
    print('loged out sucessfuly.')

@login_required
def get_balance():
    print('your account balance:', users[current_username]['balance'])

@login_required
def add(amount:int):
    users[current_username]['balance'] += amount

@login_required
def withdraw(amount:int):
    users[current_username]['balance'] -= amount

@login_required
def delete_account():
    users.pop(current_username)
    print('account deleted')

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
        password = getpass.ge('enter password: ')
        if login(username, password):
            print(f'wellcome {username}.')
        else:
            print('username or password is wrong')

    elif command == "logout":
        logout()

    elif command == "balance":
        get_balance()

    elif command == "add":
        amount = int(input('enter your amount: '))
        add(amount)
        get_balance()

    elif command == "withdraw":
        amount = int(input('enter your amount: '))
        withdraw(amount)
        get_balance()

    elif command == "delete":
        delete_account()

    elif command == "exit":
        print('see you later')

    else:
        print('command not found.')
