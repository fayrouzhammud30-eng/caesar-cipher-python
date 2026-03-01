
message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            start = ord("A") if char.isupper() else ord("a")
            new_char = chr((ord(char)-start + shift) % 26 + start)
            result += new_char
        else:
            result +=char

    return result
def decrypt(text, shift):
    return encrypt(text, -shift)  
choice = input("Type E t encrypt or D to decrypt: ").upper()
if choice == "E":
    encrypted = encrypt(message, shift)
    print("Encrypted message:", encrypted)
elif choice == "D":
    decrypted = decrypt(message, shift)
    print("Decrpted message:", decrypted)             
else:
    print("Invalid choice")    