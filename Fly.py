import InsectClass as I

wings = int(input("How many wings does the insect have?"))
legs = int(input("How many legs does the insect have?"))

mosquito = I.Insect(2, 4)
housefly = I.Insect(3, 6)

mosquito.flight_length()
housefly.flight_length()

print("The mosquito can fly", mosquito.get_miles(), "miles.")
print("The housefly can fly", housefly.get_miles(), "miles.")
