import random
Chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_-~`=+}{[]';:.>,</?|"
while 1:
    password_len = int(input("Password length: "))
    password_count = int(input("How many passwords to generate: "))
    for x in range(0, password_count):
        password = ""
        for x in range(0, password_len):
            password_char = random.choice(Chars)
            password = password + password_char
        print("Generated password: ", password)
    break
