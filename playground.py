from functions import square

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

'''for x in range(6):
    print(x)'''

rates = {"ja": 0.02, "fr": 0.03, "de": 0.04}
print(rates)



for i in range(5):
    print(f"The square of {i} is {square(i)}")