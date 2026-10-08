# Experiment 8: Bubble sort

numbers = [5, 3, 8, 1, 2]

for i in range(len(numbers)):
    for j in range(0, len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("Sorted array:", numbers)
print("Time Complexity: O(n^2)")
