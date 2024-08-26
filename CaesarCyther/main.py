import encryptor_module
from shift_finder import find_shift
from essencials import prepare
import explain


def main():
    print("Caesar Cyther\n\n"
          " To encrypt, input: encrypt\n"
          " To decrypt, input: decrypt\n"
          " To find the shift, input: find shift\n"
          "\n For more info in Caesar Cyther, input: help\n\n")

    while True:
        input_ = prepare(input("-> "))

        if input_ == "encrypt":
            input_a = input("Input Message: ").strip()
            input_b = input("Input Shift: ").strip()
            try:
                input_b = int(input_b)
            except ValueError:
                input_b = int(encryptor_module.enc(input_b))

            output = encryptor_module.encrypt(input_a, input_b)
            print(output)

        elif input_ == "decrypt":
            input_a = input("Input Message: ").strip()
            input_b = input("Input Shift: ").strip()
            try:
                input_b = int(input_b)
            except ValueError:
                input_b = int(encryptor_module.enc(input_b))

            output = encryptor_module.decrypt(input_a, input_b)
            print(output)

        elif input_ == "findshift":
            input_a = prepare(input("Encrypted Message: "))
            input_b = prepare(input("Original Message: "))

            output = find_shift(input_a, input_b)
            print(f"The shift is {output}")

        elif input_ == "help":
            print(explain.caesar_cyther)

        elif input_ == "exit":
            break


if __name__ == '__main__':
    main()

exit()
