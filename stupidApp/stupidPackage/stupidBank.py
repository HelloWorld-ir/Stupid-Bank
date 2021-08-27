import getpass

class StupidBank:
    def __init__(self, bank):
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
            print(f'logged in user {self.bank.get_username()}')

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
            self.bank.add(amount)
            self.balance_handler()

    @login_required
    def withdraw_handler(self):
        amount = int(input('enter your amount: '))
        try:
            if amount < 0: raise ValueError("amount cannot be negative")
            balance = self.bank.get_balance()
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