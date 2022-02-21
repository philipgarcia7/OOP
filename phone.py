import PhoneClass as p


def main():

    my_phone = p.Phone("Apple", "12", 1000)

    print("The manufacturer of the phone is:", my_phone.get__manufact())

    print("The model of the phone is:", my_phone.get__model())

    print("This retail price of the phone is: $", my_phone.get__retail_price())

    my_phone.set__manufact()
    my_phone.set__model()
    my_phone.set__retail_price()

    print("The manufacturer of the new phone is:", my_phone.get__manufact())

    print("The model of the new phone is:", my_phone.get__model())

    print("This retail price of the new phone is: $", my_phone.get__retail_price())


main()
