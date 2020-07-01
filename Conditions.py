age = int(input("How old are you? "))

# if age >= 16 and age <= 65:
# if 16 <= age <= 65:
if age in range(16, 66):
    print("Have a great day at work! :)")
else:
    print("You are to young")

print("-" * 80)

if age < 16 or age > 65:
    print("Enjoy you're free time")
else:
    print("Have a great day at work! :)")


