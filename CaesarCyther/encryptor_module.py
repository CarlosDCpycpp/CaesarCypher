import essencials


alphabet_l = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
              'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23,
              'x': 24, 'y': 25, 'z': 26}
alphabet_l_num = {v: k for k, v in alphabet_l.items()}

alphabet_u = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12,
              'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23,
              'X': 24, 'Y': 25, 'Z': 26}
alphabet_u_num = {v: k for k, v in alphabet_u.items()}


def enc(value):
    if value.isupper():
        value = value.lower()
    return ''.join(str(alphabet_l[char]) for char in value if char in alphabet_l)


def enc_rev(value):
    return ''.join(alphabet_l_num[int(char)] for char in value if int(char) in alphabet_l_num)


def encrypt(str_, shift):
    if isinstance(shift, str):
        shift = int(enc(shift))
    shift -= 1
    shift %= 26

    encrypted_str = []

    for char in str_:
        if char in alphabet_l:
            new_value = (alphabet_l[char] + shift) % 26
            if new_value == 0:
                new_value = 26
            encrypted_char = alphabet_l_num[new_value]
            encrypted_str.append(encrypted_char)
        elif char in alphabet_u:
            new_value = (alphabet_u[char] + shift) % 26
            if new_value == 0:
                new_value = 26
            encrypted_char = alphabet_u_num[new_value]
            encrypted_str.append(encrypted_char)
        else:
            encrypted_str.append(char)

    return ''.join(encrypted_str)


def decrypt(str_, shift):
    if isinstance(shift, str):
        shift = int(enc(shift))
    shift -= 1
    shift %= 26

    decrypted_str = []
    for char in str_:
        if char in alphabet_l:
            original_value = (alphabet_l[char] - shift) % 26
            if original_value == 0:
                original_value = 26
            decrypted_char = alphabet_l_num[original_value]
            decrypted_str.append(decrypted_char)
        elif char in alphabet_u:
            original_value = (alphabet_u[char] - shift) % 26
            if original_value == 0:
                original_value = 26
            decrypted_char = alphabet_u_num[original_value]
            decrypted_str.append(decrypted_char)
        else:
            decrypted_str.append(char)

    return ''.join(decrypted_str)


if __name__ == "__main__":
    abc = "AaBbCc!"
    print(abc)
    print(encrypt(abc, 25))
    print(decrypt(encrypt(abc, 25), 25))
    print(f"\n {abc == decrypt(encrypt(abc, 25), 25)}")

    essencials.terminate()
