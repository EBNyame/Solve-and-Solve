# 🧪 Practice Problem 3:
# Write a recursive function that reverses a string.

# Example:
# reverse("code") → "edoc"

def reverse(word):
    if word == "":
        return word
    else:
        return reverse(word[1:]) + word[0]


print(reverse("code"))