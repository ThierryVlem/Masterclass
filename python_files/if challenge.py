name = input("Please enter you're name: ")
age = int(input("Please enter you're age: "))

if 18 <= age < 31:
    print("Welcome to the holiday {}".format(name))
elif age < 18:
    print("Sorry you are to young {}".format(name))
else:
    print("Sorry you are to old {}".format(name))
