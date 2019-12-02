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


#there is a indent error in the for part so just make the indents proper . use an ide or an editor dont edit here in github
# if u use an editor u will be able to see the indent lines to follow
def ceaserD(cipher, key):
     message = ""
    for letter in cipher:
        a = 1
        while(a == 1):
            if letter == " ":
                message = message + " "
                b = 1
                a = 0
            elif letter in "0123456789":
                print("Numbers are not allowed in message")
                a = 0
                b = 0
                break
            else:
                message = message + chr(ord(letter)+key)
                a = 0
                b = 1
        if b == 0:
            break
    print("Here is your encrypted message: "+message)

   





