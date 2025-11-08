def caesar_encrypt(text, shift):
    """
    Encrypts text using Caesar cipher with given shift value.
    
    Args:
        text: String to encrypt
        shift: Number of positions to shift (positive integer)
    11
    Returns:
        Encrypted string
    """
    result = ""
    
    for char in text:
        if char.isalpha():
            # Determine if uppercase or lowercase
            start = ord('A') if char.isupper() else ord('a')
            # Shift character and wrap around alphabet
            shifted = (ord(char) - start + shift) % 26
            result += chr(start + shifted)
        else:
            # Keep non-alphabetic characters unchanged
            result += char
    
    return result



def caesar_decrypt(text, shift):
    """
    Decrypts text using Caesar cipher with given shift value.
    
    Args:
        text: String to decrypt
        shift: Number of positions that were shifted during encryption
    
    Returns:
        Decrypted string
    """
    # Decryption is just encryption with negative shift
    return caesar_encrypt(text, -shift)


def main():
    print("=== Caesar Cipher ===\n")
    
    # Get user input
    choice = input("Choose operation (1-Encrypt, 2-Decrypt): ")
    message = input("Enter your message: ")
    shift = int(input("Enter shift value (1-25): "))
    
    # Perform operation
    if choice == "1":
        encrypted = caesar_encrypt(message, shift)
        print(f"\nEncrypted message: {encrypted}")
    elif choice == "2":
        decrypted = caesar_decrypt(message, shift)
        print(f"\nDecrypted message: {decrypted}")
    else:
        print("Invalid choice!")


# Example usage
if __name__ == "__main__":
    # Demo examples
    print("Demo Examples:")
    original = "Hello World!"
    shift_value = 3
    
    encrypted = caesar_encrypt(original, shift_value)
    print(f"Original: {original}")
    print(f"Encrypted (shift {shift_value}): {encrypted}")
    
    decrypted = caesar_decrypt(encrypted, shift_value)
    print(f"Decrypted: {decrypted}")
    
    print("\n" + "="*40 + "\n")
    
    # Interactive mode
    main()