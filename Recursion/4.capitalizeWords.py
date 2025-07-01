def capitalize(arr):
    res = []
    if len(arr) == 0:
        return res
    res.append(arr[0].upper())
    return res + capitalize(arr[1:])

words = ['i', 'am', 'learning', 'recursion']
print(capitalize(words))