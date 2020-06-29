name = input("Please enter you're name: ")
age = int(input("How old are you, {0}?: ".format(name)))
print(age)
# control + /
# if age >= 18:
#     print("You're old enough to vote!")
#     print('Please put an X in the box')
# else:
#     print("Please come back in {0} years {1}".format(18 - age, name))

if age < 18:
    print("Please come back in {0} years {1}".format(18 - age, name))
elif age == 900:
    print("Soryy, Yoda, you die in return of the Jedi!")
else:
    print("You're old enough to vote!")
    print('Please put an X in the box mate')
