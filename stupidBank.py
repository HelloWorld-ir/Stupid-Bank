import getpass
import hashlib

class Hash:
    def hash(self, string:str):
        return hashlib.sha256(string.encode('utf-8')).hexdigest()

class DataContext:
    def __init__(self, file_path):
        self.file_path = file_path
    
    def load_data(self) -> dict:
        users = {}
        with open(self.file_path, "r") as file:
            for line in file.readlines():
                username, password, balance = line.split()
                users[username] = {'password': password, 'balance': balance}

        return users

    def save_data(self, users:dict):
        with open(self.file_path, "w") as file:
            for username, val in users.items():
                file.write(f"{username} {val['password']} {val['balance']}\n")

class Bank:

    def __init__(self, hasher:Hash, context:DataContext):
        self.current_username = ''
        self.context = context
        self.hasher = hasher
        self.users = self.context.load_data()

    def is_logged_in(self):
        return self.current_username != ''

    def user_exists(self, username:str):
        return username in self.users

    def login(self, username:str, password:str):
        password = self.hasher.hash(password)
        if (username not in self.users) or self.users[username]['password'] != password:
            raise ValueError("username or password is not correct")

        self.current_username = username

    def register(self, username:str, password:str):
        self.users[username] = {'password': hash(password), 'balance': 0}

    def logout(self):
        self.current_username = ''

    def get_balance(self):
        return self.users[current_username]['balance']

    def add(self, amount:int):
        self.users[self.current_username]['balance'] += amount

    def withdraw(self, amount:int):
        self.users[self.current_username]['balance'] -= amount

    def delete_account(self):
        self.users.pop(self.current_username)
    
    def __del__(self):
        self.context.save_data(self.users)

class StupidBank:
    def __init__(self, bank:Bank):
        self.bank = bank
        self.commands = {
            'register': self.register_handler,
            'login': self.login_handler,
            'logout': self.logout_handler,
            'balance': self.balance_handler,
            'add': self.add_handler,
            'withdraw': self.withdraw_handler,
            'delete': self.delete_handler,
            'exit': self.exit_handler
        }
    
    def start(self):
        print('wellcome to STUPID BANK!')
        while True:
            command = input('what can we do for you? ').lower()
            try:
                self.commands[command]()

            except ValueError as err:
                print(err)
                continue
            except KeyError:
                print('command not found')

    def login_required(func):
        def wrapper(self):
            if self.bank.is_logged_in():
                func(self)
            else:
                raise ValueError("login is required")
        return wrapper

    def not_login(func):
        def wrapper(self):
            if not self.bank.is_logged_in():
                func(self)
            else: 
                raise ValueError("you should not be logged in")
        return wrapper

    @not_login
    def register_handler(self):
        while True:
            username = input('enter your username: ')
            try:
                if username.isspace() or username == '':
                    raise ValueError("username is not valid")
                if self.bank.user_exists(username):
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
                self.bank.register(username, password)
                print('registered sucessfuly. you can login now.')
                break

    @not_login
    def login_handler(self):
        username = input('enter username: ')
        password = getpass.getpass('enter password: ')
        try: 
            self.bank.login(username, password)
        except ValueError as err:
            print(err)
        else:
            print(f'logged in user {current_username}')

    @login_required
    def logout_handler(self):
        self.bank.logout()
        print('user logged out')

    @login_required
    def balance_handler(self):
        print('your current balance:', self.bank.get_balance())

    @login_required
    def add_handler(self):
        amount = int(input('enter your amount: '))
        try:
            if amount < 0: raise ValueError("amount cannot be negative")
        except ValueError as err:
            print(err)
            self.add_handler()
        else:
            add(amount)
            self.balance_handler()

    @login_required
    def withdraw_handler(self):
        amount = int(input('enter your amount: '))
        try:
            if amount < 0: raise ValueError("amount cannot be negative")
            balance = get_balance()
            if balance < amount: raise ValueError("not enough balance")
        except ValueError as err:
            print(err)
            self.withdraw_handler()
        else:
            self.bank.withdraw(amount)
            self.balance_handler()

    @login_required
    def delete_handler(self):
        self.bank.delete_account()
        print('account deleted')

    def exit_handler(self):
        print('see you later')
        exit(0)

stupid_bank = StupidBank(Bank(Hash(), DataContext("data.txt")))
stupid_bank.start()