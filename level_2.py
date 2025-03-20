def str_xor(secret, key):
    new_key = list(key)
    i = 0
    while len(new_key) < len(secret):
        new_key.append(key[i])
        i = (i + 1) % len(key)
    return "".join(chr(ord(a) ^ ord(b)) for a, b in zip(secret, new_key))

# Read the encrypted flag file
with open("level2.flag.txt.enc", "rb") as f:
    flag_enc = f.read().decode()

# The cracked password
password = "39ce"

# Decrypt the flag
flag = str_xor(flag_enc, password)

print("Decrypted Flag:", flag)
