import random
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
while 1:
    key_len = int(input("What length would you like your key to be?: "))
    key_count = int(input("How many keys would you like?: "))
    for x in range(0,key_count):
        key = ""
        for x in range(0,key_len):
            key_char = random.choice(chars)
            key = key + key_char
        print("Here's your key: ",key)