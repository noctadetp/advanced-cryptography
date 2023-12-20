from cryptography.fernet import Fernet

class CryptographyTool:
    def __init__(self, key):
        self.key = key.encode()
        self.cipher_suite = Fernet(self.key)

    def encrypt(self, message):
        encrypted_message = self.cipher_suite.encrypt(message.encode())
        return encrypted_message.decode()

    def decrypt(self, encrypted_message):
        decrypted_message = self.cipher_suite.decrypt(encrypted_message.encode())
        return decrypted_message.decode()

# Example usage
key = Fernet.generate_key().decode()
tool = CryptographyTool(key)

message = input("Enter your message: ")
encrypted_message = tool.encrypt(message)
print("Encrypted message:", encrypted_message)

decrypted_message = tool.decrypt(encrypted_message)
print("Decrypted message:", decrypted_message)
