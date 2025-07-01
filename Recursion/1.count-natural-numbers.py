# 🧪 Practice Problem 1:
# Write a recursive function to compute the sum of the first n natural numbers.

# Example: sum_n(5) → 5 + 4 + 3 + 2 + 1 = 15

def sum(n):
    if n in [0, 1]:
        return n
    else:
        return n + sum(n-1)


print(sum(5))