'''As Python gives some easy ways to convert between numeric values and their ASCII equivalents,
I have made best use of that feature and also built-ins to distinguish between special characters,
numbers, and alphabets. Using the above feature, I have used while loops, if..elif..else conditions,
accordingly to get the desired output. Also included exception handling mechanism (FileNotFound),
if the user types the wrong file name to encrypt that does not exist.'''
import optparse

# Takes in a plaintext message
# and an integer key and encrypts
# using the Caesar cipher approach
def encrypt(msg, key):
    #TODO implement encryption approach
    result = ''
    for letter in msg:
        i = ord(letter)
        # For including special characters other than letters in the encrypting file.
        if i < 65 or i > 90 and i < 97 or i > 122:
            result += letter
        # For capital letters
        while i >= 65 and i <= 90:
            j = i + key
            if j > 90:
                while j > 90:
                    j -= 26
                result += chr(j)
            elif j <= 90:
                i += key
                result += chr(i)
            break
        # For small case letters
        while i >= 97 and i <= 122:
            j = i + key
            if j > 122:
                while j > 122:
                    j -= 26
                result += chr(j)
            elif j <= 122:
                i += key
                if i < 97:
                    i += 26
                result += chr(i)
            break
    print(result)

def decrypt(msg, key):
    # Takes in an encrypted message
    # and an integer key and decrypts
    # using the Caesar cipher approach
    result = ''
    #TODO implement decryption approach
    for letter in msg:
        i = ord(letter)
    # For including special characters other than letters in the encrypting file.
        if i < 65 or i > 90 and i < 97 or i > 122:
            result += letter
        # For capital letters
        while i >= 65 and i <= 90:
            j = i - key
            if j < 65:
                while j < 65:
                    j += 26
                result += chr(j)
                # print(chr(i))
            elif j <= 90:
                i -= key
                result += chr(i)
                # print(chr(i))
            break
        # For small case letters
        while i >= 97 and i <= 122:
            j = i - key
            if j < 97:
                while j < 97:
                    j += 26
                # print(chr(i))
                result += chr(j)

            elif j <= 122:
                i -= key
                # print(chr(i))
                result += chr(i)
            break
    print(result + '\n')

def main():
    parser = optparse.OptionParser("usage%prog "+ "-f <decrypt | encrypt> -m <message> -k <key>")
    parser.add_option('-f', dest='function', type='string', help='[ decrypt | encrypt ]')
    parser.add_option('-m', dest='msg', type='string',  help='message to encrypt (plaintext) or decrypt (encrypted)')
    parser.add_option('-k', dest='key', type='int', help='cipher key as an integer')
    (options, args) = parser.parse_args()
    function = options.function
    if ((function != "encrypt" and function != "decrypt") or function == None):
        print('[-] You must specify a valid function: "encrypt" or "decrypt"')
        exit(0)
    msg = str(options.msg)
    key = int(options.key)
    if (msg == None) | (key == None):
        print('[-] You must specify a message and key.')
        exit(0)
    if function == "encrypt":
        encrypt(msg, key)
    elif function == "decrypt":
        decrypt(msg, key)

if __name__ == '__main__':
    main()

