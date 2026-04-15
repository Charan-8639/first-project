import random
import string

def generate_password(length):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

print("🔐 Password Generator")

length = int(input("Enter password length: "))
password = generate_password(length)

print("Your secure password is:", password)
