# http://www.pythonchallenge.com level 1
# The challenge presents us with a string that is unreadable by humans.
# Hints are given that suggest that each character in the string needs to to shift by two letters in the alphabet.
# The code below does exactly that without touching any digits, punctuation marks or whitespaces.


unformatted_text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq " \
                   "glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw " \
                   "ml rfc spj. "
unformatted_url = "map"


def charshift(unformatted_string):
    resultlist = list()  # create list for results
    for character in list(unformatted_string):  # iterate through each character of the string
        if str.isalpha(character):  # check if we are dealing with letters only
            charval = ord(character)  # convert the character to its unicode integer value
            if charval > 120:  # if the integer of the value character is higher than 120 (the letter x)
                resultlist.append(chr(charval - 24))  # subtract 24 from the integer to keep within alphabetical range
            else:
                resultlist.append(chr(charval + 2))  # else add 2 to the integer value of the character
        else:
            resultlist.append(character)  # add to the resultlist if the character is not a letter
    return resultlist


def printcharshift(results):
    newstring = "".join(charshift(results))  # convert list to string
    print(newstring)  # print the string


printcharshift(unformatted_text)
printcharshift(unformatted_url)
