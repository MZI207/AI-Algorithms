#Mohammed Iqbal
#Mzi207

initialNums = [] 
finalNums = []

hConstraints = [] # Horinzontal COnstraint
vConstraints = [] # Vertical Constraint

while True:
    try:
        filename = input ("Filename: ")
        fstream = open(filename, "r")
        lines = ""
        #Getting the initial numbers
        for x in range(5):
            lines = fstream.readline()
            temp = lines.strip().split(" ")
            temp = [int(i) for i in temp]
            initialNums.append(temp)
        #Getting the horizontal constraints
        fstream.readline()
        for x in range(5):
            lines = fstream.readline()
            temp = lines.strip().split(" ")
            hConstraints.append(temp)
        fstream.readline()
        for x in range(4):
            lines = fstream.readline()
            temp = lines.strip().split(" ")
            vConstraints.append(temp)
    except NameError:
        print("Please use quotes around the file name")
        continue
    except IOError:
        print("Please enter a valid .txt file, with the correct formatting.")
        continue
    else:
        break

for x in vConstraints:
    print(x)
