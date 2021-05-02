import numpy as np

# All permutation / substitution tables

initial = np.array([58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8, 57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7])
final = np.array([40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31, 38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29, 36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27, 34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25])
expansion = np.array([32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1])
expansion_inv = np.array([2, 3, 4, 5, 6, 9, 10, 11, 12, 15, 16, 17, 18, 21, 22, 23, 24, 27, 28, 29, 30, 33, 34, 35, 36, 39, 40, 41, 42, 45, 46, 1])
straight = np.array([16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10, 2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25])
choice1_left = np.array([57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36])
choice1_right = np.array([63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4])
choice2 = np.array([14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32])
drop_permutation = np.array([57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36, 63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4])
left_shift = np.array([1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1])
key_compress = np.array([14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32])
s_boxes = np.array([
    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7], [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8], [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0], [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],
    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10], [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5], [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15], [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],
    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8], [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1], [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7], [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],
    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15], [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9], [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4], [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],
    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9], [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6], [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14], [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],
    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11], [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8], [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6], [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],
    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1], [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6], [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2], [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],
    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7], [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2], [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8], [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
])


def xor(x, y):
    # produce bit string by appending an xor of each corresponding bit in x and y
    return "".join([str(int(a) ^ int(b)) for a, b in zip(x, y)])


def permute(value, permutation):
    # produce bit string of length len(perm) with the elements of value in the permutation specified in perm
    return "".join([value[permutation[i] - 1] for i in range(len(permutation))])


def s_box(value, boxes):
    # divide input into chunks of 6, one chunk for each sbox
    chunks = [value[i:i+6] for i in range(0, len(value), 6)]

    out = ""
    for i in range(len(chunks)):
        # get column from middle 4 bits
        column = int(chunks[i][1:-1], 2)
        # get row from first and last bits
        row = int(chunks[i][0]+chunks[i][-1], 2)

        # get the value at the row and column in sbox i
        box_val = boxes[i][row][column]

        # format as binary (without 0b prefix)
        bin_val = format(box_val, "b")

        # pad with leading zeroes if necessary
        while len(bin_val) < 4:
            bin_val = "0" + bin_val

        # add to output string
        out += bin_val

    return out


def left_circular(value, n):
    # move first n bits to the end of the string
    return value[n:]+value[:n]


def generate_keys(key, rounds, verbose=False):
    # split key using permutation choice 1
    left_key = permute(key, choice1_left)
    right_key = permute(key, choice1_right)

    round_keys = []

    for i in range(0, rounds):
        shift = left_shift[i]
        left_key = left_circular(left_key, shift)
        right_key = left_circular(right_key, shift)
        round_keys.append(permute(left_key + right_key, choice2))

    return round_keys


def des0(plaintext, key, rounds=16, encrypt=True, log_level=0):

    round_keys = generate_keys(key, rounds)

    # If decrypting, reverse round keys
    if not encrypt:
        round_keys = round_keys[::-1]

    init_permute = permute(plaintext, initial)

    left = init_permute[:len(init_permute)//2]
    right = init_permute[len(init_permute)//2:]

    round_texts = []

    for i in range(rounds):
        start = left+right

        # Expansion/permutation (E table)
        e_permutation = permute(right, expansion)
        # XOR with round key
        XOR = xor(e_permutation, round_keys[i])
        # Substitution/choice (S-box)
        s_permutation = s_box(XOR, s_boxes)
        # Permutation (P)
        permuted = permute(s_permutation, straight)
        # XOR with left
        round_end = xor(permuted, left)

        # switch sides
        left = right
        right = round_end

        round_texts.append(left + right)

        # logging
        if log_level > 0:
            print("\npre", i, ":", start)
            print("key", i, ":", round_keys[i])
        if log_level > 1:
            print("exp", i, ":", e_permutation)
            print("xor", i, ":", XOR)
            print("sbx", i, ":", s_permutation)
            print("prm", i, ":", permuted)
        if log_level > 0:
            print("end", i, ":", left+right)

    # switch left and right one last time
    flipped = right+left

    final_permute = permute(flipped, final)

    return final_permute, round_texts


def avalanche(base_rounds, all_permuted_rounds):
    all_diff_sums = np.zeros([len(all_permuted_rounds), len(base_rounds)])
    # perform avalanche test on each permutation
    for i in range(len(all_permuted_rounds)):
        permuted_rounds = all_permuted_rounds[i]
        diff_sums = []
        for j in range(len(base_rounds)):
            # compute the bitwise difference between the base rounds and permuted rounds
            bit_diff = xor(base_rounds[j], permuted_rounds[j])
            # convert to a list of ints
            list_diff = list(map(int, list(bit_diff)))
            # if bits are different, the output is 1 so we can sum this list to get the number of different bits
            diff_sums.append(sum(list_diff))
        all_diff_sums[i] = diff_sums

    # average all tests
    avg = sum(all_diff_sums)/len(all_diff_sums)

    return avg


file = open("input.txt", "r")
plaintext = file.readline().rstrip("\n")
key = file.readline().rstrip("\n")
file.close()

# create all off-by-one permutations of plaintext
plain_perms = []
for i in range(len(plaintext)):
    # start with plaintext as list
    perm = list(plaintext)
    # flip bit i
    perm[i] = '1' if plaintext[i] == '0' else '0'
    # convert back to list and append
    plain_perms.append("".join(perm))

# create all off-by-one strings of key
key_perms = []
for i in range(len(key)):
    # skip parity dropped bits
    if i+1 not in drop_permutation:
        continue
    # start with plaintext as list
    perm = list(key)
    # flip bit i
    perm[i] = '1' if key[i] == '0' else '0'
    # convert back to list and append
    key_perms.append("".join(perm))

# compute round outputs for original plaintext
base_cipher, base_rounds = des0(plaintext=plaintext, key=key)

# compute round outputs for each plaintext variant
plain_perm_rounds = [des0(plain_perms[i], key)[1] for i in range(len(plain_perms))]
# perform avalanche tests comparing the rounds from each plaintext variant with the rounds of the base plaintext
plain_avg_diff = avalanche(base_rounds, plain_perm_rounds)

# compute round outputs for each key variant
key_perm_rounds = [des0(plaintext, key_perms[i])[1] for i in range(len(key_perms))]
# perform avalanche tests comparing the rounds from each key variant with the rounds of the base key
key_avg_diff = avalanche(base_rounds, key_perm_rounds)

print(plain_avg_diff)
print(key_avg_diff)

"""
print("ENCRYPT")
ciphertext = des0(plaintext=plaintext, key=key, rounds=16, encrypt=True, log_level=1)
print("\nDECRYPT")
recovered_text = des0(plaintext=ciphertext, key=key, rounds=16, encrypt=False, log_level=0)
print("\nSUMMARY")
print("plaintext:           ", plaintext)
print("recovered plaintext: ", recovered_text)
print("plaintexts match:    ", plaintext == recovered_text)
print("ciphertext:          ", ciphertext)
"""
