class Account:
    def __init__(self):
        self.__balance = float(0)

    def getBalance(self):
        return self.__balance

    def initialBalance(self,balance):
        self.__balance = float(balance)

    def deposit(self,amount):
        try:
            amount = float(amount)
            if amount <= 0:
                self.__balance = self.__balance + float(amount)
                return False
            else:
                self.__balance = self.__balance + float(amount)
        except:
            print("Please input integers only")

    def withdraw(self,amount):
        try:
            amount = float(amount)
            if amount > self.__balance:
                print("Insufficient funds")
                return False
            else:
                self.__balance = self.__balance - float(amount)
        except:
            print("Please input integers only")
