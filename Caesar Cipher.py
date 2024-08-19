def encrypt(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
      
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
       
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    print("Caesar Cipher")
    print("1. Encrypt")
    print("2. Decrypt")
    choice = input("Choose an option (1/2): ")

    if choice not in ['1', '2']:
        print("Invalid choice")
        return

    text = input("Enter your message: ")
    shift = int(input("Enter shift value (0-25): "))

    if choice == '1':
        print("Encrypted message:", encrypt(text, shift))
    else:
        print("Decrypted message:", decrypt(text, shift))

if __name__ == "__main__":
    main()
