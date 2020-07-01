#
#         01234567890123
#         43210987654321
# parrot = "Norwegian Blue"
#
# print(parrot[0:6:2])  # Nre
# print(parrot[0:6:3])  # Nw

# number = "9,223;372:036 854,775;807"
number = input("Please enter a series of numbers using separators: ")
separators = ""
for char in number:
    if not char.isnumeric():
        separators = separators + char

print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print(sum([int(val) for val in values]))
#
# quote = """
# Alright, but apart from the Sanitation, the Medicine, Education, Wine,
# Public Order, Irrigation, Roads, the Fresh-Water System,
# and Public Health, what have the Romans ever done for us?
# """
#
# # Use a for loop and an if statement to print just the capitals in the quote above.
# capitals = ""
# for char in quote:
#     if char.isupper():
#         capitals = capitals + char
# print(capitals)





# """print(parrot[0:6])  # Norweg
# print(parrot[3:5])
# print(parrot[0:9])
# print(parrot[:9])
# print(parrot[10:])
# print(parrot[-4:])
#
# letters = "abcdefghijklmnopqrstuvwxyz"
#
#
# print(parrot)
#
# print(parrot[3])
# weWin = 'We win'
# print(weWin[1])
# print(weWin[2])
# print(weWin[3])
# print(weWin[4])
# print(weWin[5])
# print()
#
# for elem in weWin[1:6]:
#     print(elem)
#
# print()
#
# print(parrot[3])
# print(parrot[4])
# print(parrot[9])
# print(parrot[3])
# print(parrot[6])
# print(parrot[8])
#
# print()
#
# print(parrot[-11])
# print(parrot[-10])
# print(parrot[-5])
# print(parrot[-11])
# print(parrot[-8])
# print(parrot[-6])
# """

