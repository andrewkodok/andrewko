from Oct2017_Jude.bank_homework.account_class import Account

class Customer:
    def __init__(self,firstname,lastname):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__account = Account()

    def getFirstName(self):
        return str(self.__firstname)

    def getLastName(self):
        return str(self.__lastname)

    def getAccount(self):
        return self.__account.getBalance()

    def setAccount(self, value):
        self.__account.initialBalance(value)

    def customer_deposit(self,num):
        self.__account.deposit(num)

    def customer_withdraw(self,num):
        self.__account.withdraw(num)
