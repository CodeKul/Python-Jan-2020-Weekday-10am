class Account:

    def __init__(self, name, acc_no, phone, type):
        super().__init__()
        self.name = name
        self.acc_no = acc_no
        self.phone = phone
        self.type = type
        self.__balance = 0

    def account_info(self):
        print("Name:", self.name)
        print("Account no:", self.acc_no)
        print("Phone:", self.phone)
        print("Type:", self.type)
        print("Balance:", self.__balance)

    def withdraw(self, amt):
        self.__balance -= amt
        
    def __calc_interest(self):
        self.__balance += self.__balance * 0.06

    def deposite(self, amt):
        self.__balance += amt
        self.__calc_interest()

acc1 = Account("ABC", 123454321, 12345555, "Savings")
acc1.account_info()
acc1.deposite(1000)
acc1.deposite(50000)
acc1.account_info()

acc1.__balance = 100000
# acc1._Account__balance = 100000

acc1.account_info()

# acc1.__calc_interest()
acc1._Account__calc_interest()
