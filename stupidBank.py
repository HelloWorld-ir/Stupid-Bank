import getpass

current_username = ''
users = {}

def login_required(func):
    def wrapper():
        if is_logged_in():
            func()
        else:
            raise ValueError("login is required")
    return wrapper

def not_login(func):
    def wrapper():
        if not is_logged_in():
            func()
        else: 
            raise ValueError("you should not be logged in")
    return wrapper

def is_logged_in():
    return current_username != ''

def user_exists(username):
    return username in users

def login(username, password):
    if (username not in users) or users[username]['password'] != password:
        raise ValueError("username or password is not correct")

    global current_username
    current_username = username

def register(username, password):
    users[username] = {'password': password, 'balance': 0}

def logout():
    global current_username
    current_username = ''
    print('loged out sucessfuly.')

def get_balance():
    return users[current_username]['balance']

def add(amount:int):
    users[current_username]['balance'] += amount

def withdraw(amount:int):
    users[current_username]['balance'] -= amount

def delete_account():
    users.pop(current_username)
    print('account deleted')

@not_login
def register_handler():
    while True:
        username = input('enter your username: ')
        try:
            if username.isspace() or username == '':
                raise ValueError("username is not valid")
            if user_exists(username):
                raise ValueError(f'{username} exists. please try another one')
        except ValueError as err:
            print(err)
            continue
        else:
            break

    while True:
        password = getpass.getpass('enter your password: ')
        confirm = getpass.getpass('confirm your password: ')
        try:
            if password.isspace() or password == '':
                raise ValueError("password is not valid")
            if password != confirm:
                raise ValueError("passwords dont't match!")
        except ValueError as err:
            print(err)
            continue
        else:
            register(username, password)
            print('registered sucessfuly. you can login now.')
            break

@not_login
def login_handler():
    username = input('enter username: ')
    password = getpass.getpass('enter password: ')
    try: 
        login(username, password)
    except ValueError as err:
        print(err)
    else:
        print(f'logged in user {current_username}')

@login_required
def logout_handler():
    logout()
    print('user logged out')

@login_required
def balance_handler():
    print('your current balance:', get_balance())

@login_required
def add_handler():
    amount = int(input('enter your amount: '))
    try:
        if amount < 0: raise ValueError("amount cannot be negative")
    except ValueError as err:
        print(err)
        add_handler()
    else:
        add(amount)
        balance_handler()

@login_required
def withdraw_handler():
    amount = int(input('enter your amount: '))
    try:
        if amount < 0: raise ValueError("amount cannot be negative")
        balance = get_balance()
        if balance < amount: raise ValueError("not enough balance")
    except ValueError as err:
        print(err)
        withdraw_handler()
    else:
        withdraw(amount)
        balance_handler()

@login_required
def delete_handler():
    delete_account()

def exit_handler():
    print('see you later')
    exit(0)

commands = {
    'register': register_handler,
    'login': login_handler,
    'logout': logout_handler,
    'balance': balance_handler,
    'add': add_handler,
    'withdraw': withdraw_handler,
    'delete': delete_handler,
    'exit': exit_handler
}

print('wellcome to STUPID BANK!')
while True:
    command = input('what can we do for you? ').lower()
    try:
        commands[command]()

    except ValueError as err:
        print(err)
        continue
    except KeyError:
        print('command not found')