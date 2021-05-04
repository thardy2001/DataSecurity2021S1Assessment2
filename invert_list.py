import pyperclip
import numpy as np

expansion = np.array([32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1])

inverse = np.zeros(32)

for i in range(len(expansion)):
    if not i%6 == 0 and not i%6==5:
        inverse[expansion[i]-1] = i + 1

out = "["

for i in range(len(inverse)):
    out += str(int(inverse[i]))
    if i < len(inverse) - 1:
        out += ", "

out += "]"

pyperclip.copy(out)
print("copied to clipboard")
print(out)
