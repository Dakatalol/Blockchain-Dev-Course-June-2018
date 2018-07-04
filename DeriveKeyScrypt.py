import scrypt, binascii
# scrypt.windll.LoadLibrary("C:\\Users\\Jordan\\PycharmProjects\\blockchain\\venv\lib\\site-packages\\scrypt\\depends.dll")

passwd = "p@$$w0rd~3"
salt = "7b07a2977a473e84fc30d463a2333bcfea6cb3400b16bec4e17fe981c925ba4f"

key=scrypt.hash(passwd,salt, 16384, 16, 1, 32)
print("key:", binascii.hexlify(key))
