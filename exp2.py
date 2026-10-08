# Experiment 2: Count common elements in two arrays

nums1 = [2, 3, 2]
nums2 = [1, 2]

answer1 = 0
answer2 = 0

for x in nums1:
    if x in nums2:
        answer1 += 1

for x in nums2:
    if x in nums1:
        answer2 += 1

print([answer1, answer2])
