#
# Myles Tollefson
# 4/26/2025
# File Encryption and Decryption Programming Project
# COSC 1010

# variable to store the output string
output = ''

# dictionary for encription
encryption = {'A':'%','a':'9','B':'@','b':'#','C':'~',
              'c':'+','D':'=','d':')','E':'d','e':'1',
              'F':'*','f':'(','G':'$','g':'&','H':'^',
              'h':'|','I':':','i':';','J':'-','j':'_',
              'K':'"','k':"'",'L':'<','l':',','M':'>',
              'm':'.','N':'L','n':'P','O':']','o':'}',
              'P':'{','p':'[','Q':'?','q':'0','R':'2',
              'r':'3','S':'8','s':'4','T':'`','t':'7',
              'U':'5','u':'6','V':'Q','v':'I','W':'K',
              'w':'l','X':'p','x':'D','Y':'q','y':'i',
              'Z':'k','z':'J','0':'h','1':'G','2':'F',
              '3':'S','4':'A','5':'a','6':'s','7':'T',
              '8':'f','9':'t',',':'H','.':'O','-':'o'}

# Makes a reverse dictionary for the decryption process.
decryption = {value: key for key, value in encryption.items()}

# Asks weather you want to encrypt or decrypt a text document.
operation = input("enter 'E' for encryption and 'D' for decryption " )

# Tests if the user selected encryption or decryption.
if operation.lower() == 'e':
    
    # Opens the non encrypted file.
    encript_file = open('text.txt', 'r')
    
    # Priming read for the while loop.
    line = encript_file.readline()
    
    # Loops until the end of the file is reached.
    while line != '':
        
        # Each character in the line 
        # is checked to see if its in the dictionary,
        # if it is its replaced if it isn't
        # it is just added to the output.
        for ch in line:
            if ch in encryption:
                output += encryption[ch]
            else:
                output += ch        
        
        # Reads next line.
        line = encript_file.readline()
    # Closes the read file. 
    encript_file.close()
    
    # Opens/creates a file to export the encrypted text.
    export = open('encrypted.txt','w')
    
    # Exports into encripted.txt.
    export.write(output)

    # closes export file
    export.close()
    
    # prints encrypted successfully
    print('file encrypted successfully')

else:
    # Opens encrypted text.
    decrypt_file = open('encrypted.txt','r')
    
    # Priming read for the loop.
    line = decrypt_file.readline()
    
    while line != '':
        
        # Each character in the line 
        # is check to see if its in the dictionary,
        # if it is its replaced if it isn't
        # it is just added to the output.
        for ch in line:
            if ch in decryption:
                output += decryption[ch]
            else:
                output += ch
        
        # Reads the next line.
        line = decrypt_file.readline()
    
    # Closes the read file. 
    decrypt_file.close()
    
    # Prints decrypted successfully.
    print('file decrypted successfully')
    print(output)
    
    
    
    