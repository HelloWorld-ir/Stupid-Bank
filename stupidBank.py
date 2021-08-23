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

def register_handler():
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

def login_handler():
    username = input('enter username: ')
    password = getpass.ge('enter password: ')
    if login(username, password):
        print(f'wellcome {username}.')
    else:
        print('username or password is wrong')

def logout_handler():
    logout()

def balance_handler():
    get_balance()

def add_handler():
    amount = int(input('enter your amount: '))
    add(amount)
    get_balance()

def withdraw_handler():
    amount = int(input('enter your amount: '))
    withdraw(amount)
    get_balance()

def delete_handler():
    delete_account()

def exit_handler():
    print('see you later')
    exit(0)

commands = {
    'register': register_handler,
    'login': login_handler,
    'logout': login_handler,
    'balance': balance_handler,
    'add': add_handler,
    'withdraw': withdraw_handler,
    'delete': delete_handler,
    'exit': exit_handler
}

print('wellcome to STUPID BANK!')
while True:
    command = input('what can we do for you? ').lower()

    if command in commands:
        commands[command]()
    else:
        print('command not found.')