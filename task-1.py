def caesar_cipher(text, shift, mode):
    result = ""
    if mode == "decrypt":
        shift = -shift

    for char in text:
        if char.isalpha():  
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char  
    return result


def main():
    print("Caesar Cipher: Encrypt and Decrypt")
    while True:
        mode = input("Choose mode ('encrypt' or 'decrypt', or 'exit' to quit): ").strip().lower()
        if mode == 'exit':
            print("Exiting the program. Goodbye!")
            break
        if mode not in ['encrypt', 'decrypt']:
            print("Invalid mode! Please choose 'encrypt' or 'decrypt'.")
            continue

        text = input("Enter the message: ")
        try:
            shift = int(input("Enter the shift value (integer): "))
        except ValueError:
            print("Invalid shift value! Please enter an integer.")
            continue

        result = caesar_cipher(text, shift, mode)
        print(f"The {mode}ed message is: {result}")
        print("-" * 50)


if __name__ == "__main__":
    main()
