def ceaserE(message, key):
    cipher = ""
    for letter in message:
        a = 1
        while(a == 1):
            if letter == " ":
                cipher = cipher + " "
                b = 1
                a = 0
            elif letter in "0123456789":
                print("Numbers are not allowed in message")
                a = 0
                b = 0
                break
            else:
                cipher = cipher + chr(ord(letter)+key)
                a = 0
                b = 1
        if b == 0:
            break
    print("Here is your encrypted message: "+cipher)



def ceaserD(message, key):
    cipher = ""
    for letter in message:
        if letter == " ":
            cipher = cipher + " "
        elif letter in "0123456789":
            print("Numbers are not allowed in message")
            break
        else:
            cipher = cipher + chr(ord(letter) - key)
    print(cipher)






