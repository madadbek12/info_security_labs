from cryptography.fernet import Fernet

# Генерация ключа
key = Fernet.generate_key()
cipher = Fernet(key)

# Сохраняем ключ
with open('key.key', 'wb') as f:
    f.write(key)

# Шифруем файл
with open('secret.txt', 'rb') as f:
    data = f.read()

encrypted_data = cipher.encrypt(data)

with open('secret_encrypted.txt', 'wb') as f:
    f.write(encrypted_data)

print("Файл зашифрован!")
