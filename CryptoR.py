from moduleTest import ceaserE
from moduleTest import ceaserD
# THIS IS THE DESIGNING PART UP TO LINE 10
print("\n")
print("-"*79)
print("                         WELCOME TO CryptoR")
print("-"*79)
print("\n")
print("#1. Encoders\n#2. Decoders")
print("\n")
a = 1
while(a == 1):  # THIS IS THE MAIN LOOP TO KEEP THE USER IN THE PROGRAM UNTIL THEY EXIT
    try:  # MAIN TRY STATEMENT TO CATCH VALUE ERRORS (ENDS ON LINE 54)
        option = int(input("\nChoose if you wanna Encode/Decode\n#Enter 1 or 2: "))
        if option == 1:  # IF THE USER CHOOSE TO ENCODE
            print("\n")  # DESIGN FROM LINE 16 TO 22
            print("-"*79)
            print("              ENCRYPTIONS")
            print("-"*79)
            print("\n")
            print("#1. Ceasers Cipher\n#2. XOR Encryption")
            print("\n")
            option = int(input("Choose your Encryption Method: "))  # THIS OPTION VARIABLE IS NOT THE OPTION VARIABLE DEFINED ABOVE ( ITS VALUE CHANGED )

            if option == 1:  # IF THE USER CHOOSE TO USE CEASERS CIPHER
                print("\n")
                message = input("Enter your message: ")
                key = int(input("Enter your key: "))
                ceaserE(message, key)  # CEASER ENCRYPTION FUNCTION IMPORTED FROM moduleTest.py
                answer = input("Do you want to go back to the main menu[Y/N]: ")  # PROMPT IF USER WANT TO CONTINUE WITH PROGRAM OR NOT
                if answer in ["Y","y"]:  # IF YES! THE MAIN LOOP WILL CONTINUE CUZ( a = 1 )
                    a = 1
                elif answer in ["N","n"]:  # IF NO! a WILL BE 0 SO MAIN LOOP WILL BREAK! AND PROGRAM EXITS
                    print("Thank you for using CryptoR")
                    a = 0
                else:  # IDK WHAT THE FUCK I SHOULD PUT IN HERE...
                    print("\nCongrats you broke the program ;)\n")
                    a = 0
            elif option == 2:
                print("test")
                a = 0
            else:
                print("There ain't no encryption methods like that!")




        elif option == 2:  # IF USER WANTS TO GO FOR DECRYPTION INSTEAD
            print("test")
            a = 0
        else:  # TO DEAL WITH TARDS WHO TRY TO BREAK MY PROGRAM
            print("\nI AM SMARTER !\n")

    except ValueError:  # END OF EXCEPT STATEMENT
        print("\nValue Error ! Lets head back to main!\n")
