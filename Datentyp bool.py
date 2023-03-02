
age = int(input("Bitte gebe dein Alter ein:"))

if age < 16:
    print("Du bist so alt:")

if age < 18:
    print("Du bist Geschäftsfähig")
elif age == 18:
    print("Du bist genau 18")
else:
    print("Ende")
