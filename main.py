name = input("What's your name?")
print ("Hello, " + name + ". This is a weight converter of two basic units. Those are Kg and Lbs.")
weight = input("Insert the amount of weight:")
unit = input("Kg(Kg) or Lbs(Lbs):")
if unit == "Kg":
    print (float(weight) * 2.20462)
    print ("Lbs")
    print ("**converted to lbs from kg")

elif unit == "Lbs":
    print (float(weight) * 0.453592)
    print ("Kg")
    print("**converted to kg from lbs")
