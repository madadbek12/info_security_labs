from cryptography.fernet import Fernet

# Загружаем ключ
with open('key.key', 'rb') as f:
    key = f.read()

cipher = Fernet(key)

# Дешифруем файл
with open('secret_encrypted.txt', 'rb') as f:
    encrypted_data = f.read()

decrypted_data = cipher.decrypt(encrypted_data)

with open('secret_decrypted.txt', 'wb') as f:
    f.write(decrypted_data)

print("Файл дешифрован!")
