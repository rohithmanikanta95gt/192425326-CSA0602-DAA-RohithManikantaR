# Experiment 1: Find the first palindromic string

words = ["abc", "car", "ada", "racecar", "cool"]

for word in words:
    if word == word[::-1]:
        print("First palindrome:", word)
        break
else:
    print("No palindrome found")
