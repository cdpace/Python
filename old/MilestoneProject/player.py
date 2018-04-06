class Player:
    
    #Attributes
    name = ""

    #private attributes
    __balance = 0

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
    

    def topup_balance(self, amount):
        self.__balance += amount
        return self.__balance
    
    def detuct_from_balance(self, amount):
        self.__balance -= amount
        
        if self.__balance <= 0:
            self.__balance = 0
        
        return self.__balance
    
    def get_balance(self):
        return self.__balance