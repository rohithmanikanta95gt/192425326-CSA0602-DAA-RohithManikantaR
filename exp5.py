# Experiment 5: Find the maximum number

numbers = [1, 2, 3, 4, 5]

maximum = numbers[0]

for number in numbers:
    if number > maximum:
        maximum = number

print("Maximum:", maximum)
