print(("This code helps you to find a word from a txt file and prints out its line.").upper())
def findw():
    filen = str(input("Enter your file name:"))
    # file must be in current directory
    if ".txt" not in filen:
        txtf = filen+".txt"
    else:
        txtf = filen
    try:
        otxt = open(txtf, "r")
    except FileNotFoundError:
        print('{} not found ,Make sure file is a txt file and file is this directory'.format(txtf))
        findw()
    else:
        word = input("Enter word here: ")
        word = word.lower()
        for line in otxt:
            if word in line:
                line = str(line)
                print(line)
        if line not in otxt:
            print("{} not found in {}.".format(word,txtf))
        otxt.close()
findw()
print(" you're welcome")
