import hashlib

class Hash:
    def hash(self, string:str):
        return hashlib.sha256(string.encode('utf-8')).hexdigest()
