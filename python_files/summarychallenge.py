choice = "-"
while choice != "0":
    if choice in "12345":
        print("You chose {}".format(choice))
    else:
        print("Please choose your option from the list below: ")
        print("1:\tLearn Python")
        print("2:\tLearn Java")
        print("3:\tLearn Php")
        print("4:\tLearn Html")
        print("5:\tLearn Css")
        print("0:\tExit")
    choice = input()
