from encryptor_module import encrypt
import encryptor_module as e_m
import essencials


alphabet = []

for letter__, value in e_m.alphabet_l.items():
    alphabet.append(letter__)
for letter__, value in e_m.alphabet_u.items():
    alphabet.append(letter__)


def find_shift(encrypted_message, original_message):
    encrypted_message = essencials.prepare(encrypted_message)
    original_message = essencials.prepare(original_message)

    for letter in alphabet:
        for letter_, value_ in e_m.alphabet_l.items():
            if letter != letter_:
                if encrypt(original_message, value_) == encrypted_message:
                    return value_
        for letter_, value_ in e_m.alphabet_u.items():
            if letter != letter_:
                if encrypt(original_message, value_) == encrypted_message:
                    return value_
    return None


if __name__ == "__main__":
    str_a = "abc"
    str_b = encrypt(str_a, 25)
    print(find_shift(str_b, str_a))

    essencials.terminate()
