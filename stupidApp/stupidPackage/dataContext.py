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
