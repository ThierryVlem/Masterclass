import random

highest = 10
answer = random.randint(1, highest)
print(answer)    # TODO: remove after testing

print("Please guess a number between 1 and {}: ".format(highest))
guess = int(input())
guess_count = 1
if guess != answer:
    # if guess < answer:
    #     print("Please guess higher")
    # else:    # guess must be greater than answer
    #     print("Please guess lower")
    # guess = int(input())
    # if guess == answer:
    #     print("Well done, you guessed it!")
    # else:
    while guess != answer:
        if guess == 0:
            break
        if guess < answer:
            print("Please guess higher")
        else:
            print("Please guess lower")
        guess = int(input())
        guess_count += 1

    if guess == answer:
        print("Well done, you guessed it in {} times:)".format(guess_count))
else:
    print("You got it first time! :)")

# if guess == answer:
#     print("You got it first time! :)")
# else:
#     if guess < answer:
#         print("Please guess higher")
#     else:    # guess must be greater than answer
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it!")
#     else:
#         print("Sorry,you have not guessed correctly")

# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it!")
#     else:
#         print("Sorry you have not guessed correctly :( ")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it!")
#     else:
#         print("Sorry you have not guessed correctly :(")
# else:
#     print("You got it first time")
