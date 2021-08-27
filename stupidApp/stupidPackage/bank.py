class Bank:

    def __init__(self, hasher, context):
        self.current_username = ''
        self.context = context
        self.hasher = hasher
        self.users = self.context.load_data()

    def get_username(self):
        return self.current_username
    
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
    
    def save(self):
        self.context.save_data(self.users)
