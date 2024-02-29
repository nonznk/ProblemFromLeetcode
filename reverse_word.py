txt = input("Input: ")

new_string = ""

for i in range(len(txt)):
    if txt[i] != '"':
        new_string = new_string + txt[i]

text_sep = new_string.split(" ")
# print(text_sep)

new_text = ""

for j in range(len(text_sep)):
    num = len(text_sep)
    for k in range(len(text_sep[j]) - 1, -1, -1):
        new_text = new_text + text_sep[j][k]

    if j < num - 1:
        new_text = new_text + " "

new_text = '"' + new_text + '"'

# print("Output: {}".format(new_text))
print(new_text)
