# Question: Given a sequence numbers print the median of the sequence.

"""This program will generate a list of numbers with random limits and
print the median as result output"""

from random import randint

numbers = []
num_range = randint(1, 30)
for num in range(1, num_range):
    numbers.append(num)

numbers.sort()
print(numbers)

if len(numbers) % 2 != 0:
    median = numbers[int(len(numbers)/2)]
    print(f"Odd median is {int(median)}")
elif len(numbers) % 2 == 0:
    a, b = numbers[int(len(numbers)/2) - 1], numbers[int(len(numbers)/2)]
    median = (a + b) / 2
    print(f"Even median is {median}")
else:
    print("something is wrong")
