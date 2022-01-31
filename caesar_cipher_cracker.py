'''I have defined a function named decryption which takes the text as the parameter
when the function is called. In the process, I have used for loop to iterate over
text and used for loop, while loop, if…elif…else conditions accordingly to get the
desired output.
In the Output, I got the readable output in the 17th iteration. So the key value(shift value) has to be 17.'''

def decryption(text):
    key=1
    res = []
    while key<=26:
        result = ''
        for letter in text:
            i = ord(letter)
            #For including special characters other than alphabets in the text
            if i < 65 or i > 90 and i < 97 or i > 122:
                result += letter
            #For including Capital letters
            while i >= 65 and i <= 90:
                j = i - key
                if j < 65:
                    i = j + 26
                    result += chr(i)
                elif j <= 90:
                    i -= key
                    result += chr(i)
                break
            #For including small case letters
            while i >= 97 and i <= 122:
                j = i - key
                if j < 97:
                    i = j + 26
                    result += chr(i)
                elif j <= 122:
                    i -= key
                    result += chr(i)
                break
        res.append(result)
        key += 1
    return res

#Calling function decryption and passing text as parameter.
decrypt = decryption("Yrzc Trvjri")
for x in decrypt:
    print(x)