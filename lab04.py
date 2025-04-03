from cryptography.fernet import Fernet
import itertools
import string

def brute_force_decrypt(encrypted_file, max_length=5):
    with open(encrypted_file, 'rb') as f:
        encrypted_data = f.read()

    chars = string.ascii_letters + string.digits
    for length in range(1, max_length + 1):
        for candidate in itertools.product(chars, repeat=length):
            key_candidate = ''.join(candidate).encode()
            try:
                cipher = Fernet(key_candidate)
                decrypted_data = cipher.decrypt(encrypted_data)
                print(f"Ключ найден: {key_candidate}")
                print(f"Расшифрованные данные: {decrypted_data.decode()}")
                return
            except:
                continue
    print("Ключ не найден.")

brute_force_decrypt('secret_encrypted.txt')
