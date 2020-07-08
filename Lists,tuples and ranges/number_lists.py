empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
print(numbers)

sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

digits = list("432985617")
print(digits)

# more_number = list(numbers)
# more_number = numbers[:]
more_number = numbers.copy()
print(more_number)
print(numbers is more_number)
print(numbers == more_number)
