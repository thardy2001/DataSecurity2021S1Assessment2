import pyperclip

file = open("list.txt", "r")

lines = file.readlines()

array = []

flatten = True

for line in lines:
    str_list = line.strip().replace("\t", " ").split(" ")

    int_list = list(map(int, str_list))

    if not flatten:
        array.append(int_list)
    else:
        for i in int_list:
            array.append(i)

pyperclip.copy(str(array))
print("copied to clipboard")
print(array)

"""
output = []
for line in array:
output = ""
output = output + "["
for i in range(len(array)):
    output = output + "["
    output = output + ','.join(array[i])
    output = output + "]"
    if i < len(array)-1:
        output = output + ", "
output = output + "]"

print(output)
"""
