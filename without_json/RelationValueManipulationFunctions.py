def importTest():
    print("Imported Successfully!!!")

def getRelationTable():
    """returns file text to avoid problems, when file name changes"""
    text = open("My_1text.txt", "r")
    return text.read()

def relValue(relation, relationAppearenceCounter):
    """This method returns the division of relation by the number of appearences the relations has made so far
        - tiring means getting sick of or bored
        Exemple: a person does the same relation again and again, and that person becomes bored of that relation,
        like eating same food everyday"""
    print("RelationValue method")
    relationValue = (relation/relationAppearenceCounter)
    return relationValue

def findValue(text):
    """This method receives a string, but it will ignore
        everything that is not between this [ ], and return what is between [ ]"""
    line = text
    i = 0
    var = ""
    for i in range(len(line)): # for loop where i will go up to the length of string line
        if(line[i] == "["): # line[i] will check character by character, if it is "["
            var += line[i]
            while line[i] != "]": # will continue to run until it finds "]"
                i += 1 # increment 1 in i, so for loop can continue
                var += line[i] # var will save character that are between [ ]
            var += "\n" # this adds "\n" after each line, without this, it would a single long line
    return var # finally returns the var with string that was between [ ]
# temp = "Hello [ text ] and [ text 2 ] and bye afasfaca [ kjhjkgkjgjhgkjgh ] [ [ [ test 3 ] ] ]"
# print(findValue(temp))

def relation():
    text = getRelationTable()
    line = text
    i = 0
    var = ""
    value = ""
    for i in range(len(line)):
        if(line[i] == "["):
            while line[i] != "]":
                var += line[i]
                i += 1
        if(line[i] == "("):
            while line[i] != ")":
                value += line[i]
                i += 1
    floatVar = float(var.replace("[", ""))
    floatValue = float(value.replace("(", ""))
    totalValue = (floatVar/floatValue)
    text.close()
    return totalValue

def findText(relName):
    text = getRelationTable()
    var = ""
    value = ""
    textByte = text.find(relName)
    i = textByte
    while(text[i] != ")"):
        i += 1
        if(text[i] == "["):
            while(text[i] != "]"):
                var += text[i]
                i += 1
        if(text[i] == "("):
            while(text[i] != ")"):
                value += text[i]
                i += 1
    floatVar = float(var.replace("[", ""))
    intValue = int(value.replace("(", ""))
    return (floatVar/intValue)

def findRelValue(relName): # function receives one string
    text = getRelationTable()
    i = 0 # inicilizing variable i with 0
    relLine = "" # string var called relLine
    relInitialValue = "" # this string will contain initial value of the relation
    relInteractions = "" # this string will contain number of interactions that relation has
    for name in text.split("\n"): # loops through whole text and split the text when it finds "\n" means end of line
        # print(text.split("\n"))
        # print(name)
        if relName in name: # checks, if that relName inside that name
            # print(relName)
            # print(name.strip())
            relLine = name.strip() # if yes, that it will save that in relLine
            # I DON'T KNOW WHAT THAT .strip() DOES
            # print(relLine)
    while(relLine[i] != ")"): # loops each character of that string util finding ")"
        # this loop will get us relInitialValue and relIntercations
        # print(relLine[i])
        i += 1 # to go to the next character
        if(relLine[i] == "["): # if char == "["
            # print(relLine[i])
            while(relLine[i] != "]"): # then another loop that goes to "]"
                # this loop gives us the relInitialValue
                # print(relLine[i])
                relInitialValue += relLine[i]
                i += 1
                # print(relLine[i])
        if(relLine[i] == "("):
            # this loop gives us the number of interactions
            # print(relLine[i])
            while(relLine[i] != ")"):
                # print(relLine[i])
                relInteractions += relLine[i]
                i += 1
        # these to (if)s chects "[" and "(", because in text file, relation value is stored inside [ value ]
        # and number of interations inside of ( numberInteractions )
    floatRelInitialValue = float(relInitialValue.replace("[", ""))
    # will erase that extra [ in and convert that to float value
    intRelInteractions = int(relInteractions.replace("(", ""))
    # will erase that extra ( in and convert that to integer number
    # return f"{ relLine } : { (floatRelOriginalValue/intRelInteractions) }"
    return (floatRelInitialValue/intRelInteractions)

# print(relation())
# print("--------------------------------------")
# print(findRelValue("apple["))
# print("--------------------------------------")
# print(findRelValue("banana["))

def interactionIncrement(interactionValue):
    return 0
