#name = input("Name: ")
#print(f"Hello, {name}")

'''n = int(input("Number: "))
if n > 0:
    print(f"${n}")
elif n < 0:
    print (f"{n} is negative")
else:
    print("n is zero")'''

langs = ("jp", "fr", "de", "it", "es")
print(f"We translate {len(langs)} languages.")

for x in range(6):
    print(x)

houses = {"Harry": "Gryffindor", "Draco": "Slytherin"}
houses["Hermione"] = "Gryffindor"
print(houses["Harry"])
