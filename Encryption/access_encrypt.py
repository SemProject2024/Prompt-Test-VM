import encrypt
message = input("Enter message: ")

enc = encrypt.encrypt('normal-message',message)
print(encrypt.decrypt('normal-message',enc))
