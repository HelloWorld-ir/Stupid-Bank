from stupidPackage.stupidBank import StupidBank
from stupidPackage.bank import Bank
from stupidPackage.hash import Hash
from stupidPackage.dataContext import DataContext

stupid_bank = StupidBank(Bank(Hash(), DataContext("data.txt")))
stupid_bank.start()