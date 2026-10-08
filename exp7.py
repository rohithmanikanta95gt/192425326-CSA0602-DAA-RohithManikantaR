# Experiment 7: Create a list containing only unique elements

numbers = [3, 7, 3, 5, 2, 5, 9, 2]
unique = []

for number in numbers:
    if number not in unique:
        unique.append(number)

print("Unique elements:", unique)
print("Space complexity: O(n)")
