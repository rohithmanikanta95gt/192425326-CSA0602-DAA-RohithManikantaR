# Experiment 6: Sort the list and find the maximum element

numbers = [5, 2, 8, 1, 9]

numbers.sort()

if len(numbers) == 0:
    print("The list is empty")
else:
    print("Sorted list:", numbers)
    print("Maximum:", numbers[-1])
