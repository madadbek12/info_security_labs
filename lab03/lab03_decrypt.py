from cryptography.fernet import Fernet
import itertools
import string

# Функция для генерации всех возможных ключей
def generate_keys(length=5):
    characters = string.ascii_letters + string.digits  # Буквы и цифры
    for key_tuple in itertools.product(characters, repeat=length):
        yield ''.join(key_tuple)

# Функция для расшифровки данных с использованием ключа
def decrypt_data(encrypted_data, key):
    try:
        fernet = Fernet(key.encode())  # создаем объект Fernet с ключом
        decrypted = fernet.decrypt(encrypted_data)
        return decrypted.decode()  # возвращаем расшифрованные данные в виде строки
    except Exception as e:
        return None  # Если ошибка, возвращаем None

# Чтение зашифрованных данных
with open('secret_encrypted.txt', 'rb') as f:
    encrypted_data = f.read()

# Попытка расшифровки данных методом перебора ключей
key_found = False
for key in generate_keys():  # Перебираем ключи от 1 до 5 символов
    decrypted_data = decrypt_data(encrypted_data, key)
    if decrypted_data:
        print("Ключ найден:", key)
        print("Расшифрованные данные:", decrypted_data)
        key_found = True
        break

if not key_found:
    print("Ключ не найден.")
