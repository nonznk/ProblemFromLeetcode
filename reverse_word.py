s = input("Input: ")

new_string = ""

for i in range(len(s)):
    if s[i] != '"':
        new_string = new_string + s[i]

print(new_string)
