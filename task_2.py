from PIL import Image
import numpy as np

def encrypt_image(image_path, key, output_path):
    """Encrypts an image by applying a mathematical operation on its pixel values."""
    image = Image.open(image_path)
    image_array = np.array(image)

    
    encrypted_array = (image_array + key) % 256  
    encrypted_image = Image.fromarray(np.uint8(encrypted_array))
    encrypted_image.save(output_path)
    print(f"Image encrypted and saved to {output_path}")


def decrypt_image(encrypted_path, key, output_path):
    """Decrypts an image by reversing the encryption operation."""
    encrypted_image = Image.open(encrypted_path)
    encrypted_array = np.array(encrypted_image)

    decrypted_array = (encrypted_array - key) % 256  
    decrypted_image = Image.fromarray(np.uint8(decrypted_array))
    decrypted_image.save(output_path)
    print(f"Image decrypted and saved to {output_path}")


def main():
    print("Image Encryption Tool")
    while True:
        mode = input("Choose mode ('encrypt', 'decrypt', or 'exit'): ").strip().lower()
        if mode == 'exit':
            print("Exiting the program. Goodbye!")
            break
        if mode not in ['encrypt', 'decrypt']:
            print("Invalid mode! Please choose 'encrypt' or 'decrypt'.")
            continue

        image_path = input("Enter the path of the image file: ").strip()
        output_path = input("Enter the output file path: ").strip()
        try:
            key = int(input("Enter an encryption/decryption key (integer): "))
        except ValueError:
            print("Invalid key! Please enter an integer.")
            continue

        try:
            if mode == 'encrypt':
                encrypt_image(image_path, key, output_path)
            elif mode == 'decrypt':
                decrypt_image(image_path, key, output_path)
        except Exception as e:
            print(f"An error occurred: {e}")
        print("-" * 50)


if __name__ == "__main__":
    main()
