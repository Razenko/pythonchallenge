# http://www.pythonchallenge.com level 2
# Rare characters taken from http://www.pythonchallenge.com/pc/def/ocr.html page sourcecode as hinted by the challenge.
# These characters are pasted in a separate text file to improve readability (rarechars.txt).


filename = "rarechars.txt"


def findchars(file):
    rarefile = open(file, "r")  # open file
    resultlist = list()  # create new list to store filtered results
    for character in list(rarefile.read()):  # read the file and iterate through each individual character
        if str.isalpha(character):  # check if character is a letter
            resultlist.append(character)  # store results in list
    return "".join(resultlist)  # convert the list to a string and return it


print(findchars(filename))  # print the result
