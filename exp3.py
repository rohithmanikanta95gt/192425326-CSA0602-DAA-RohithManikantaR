# Experiment 3: Sum of squares of distinct counts of all subarrays

nums = [1, 2, 1]
total = 0

for i in range(len(nums)):
    unique = set()

    for j in range(i, len(nums)):
        unique.add(nums[j])
        count = len(unique)
        total += count * count

print("Answer:", total)
