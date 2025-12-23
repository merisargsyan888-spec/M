text = input("Input: ")
v = 'aeiouAEIOU'
res = ""

for char in text:
    if char not in v:
        res += char

print ("Output: ", res)
