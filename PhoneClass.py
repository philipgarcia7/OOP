from re import A, M


class Phone:
    def __init__(self, m, o, r):
        self.__manufact = m
        self.__model = o
        self.__retail_price = r

    def set__manufact(self):
        self.__manufact = input("What is the manufacturer?")

    def set__model(self):
        self.__model = input("What is the model?")

    def set__retail_price(self):
        self.__retail_price = float(input("What is the retail price?"))

    def get__manufact(self):
        return self.__manufact

    def get__model(self):
        return self.__model

    def get__retail_price(self):
        return self.__retail_price
