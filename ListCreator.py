file = open("input.txt", "r")

lines = file.readlines()

array = []

for line in lines:
    str_list = line.strip().replace("\t", " ").split(" ")

    int_list = list(map(int, str_list))

    array.append(int_list)

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
