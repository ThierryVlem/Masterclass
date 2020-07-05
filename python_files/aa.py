options = ["Learn python", "Learn java", "Go swimming", "Have dinner", "Go to bed", "Exit"]
count = 0

choice = input("Please choose your option from the list below: ")
for option in options:
    if option == "Exit":
        print("0    {}".format(option))
    count += 1
    print("{}    {}".format(count, option))

