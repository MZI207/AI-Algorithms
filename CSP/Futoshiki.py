#Mohammed Iqbal
#Mzi207
from collections import deque
initialNums = [] 
hConstraints = [] # Horinzontal COnstraint
vConstraints = [] # Vertical Constraint

originalFile = ""
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
        fstream.close()
        fstream = open(filename, "r")
        originalFile = fstream.read()
        fstream.close()
    except NameError:
        print("Please use quotes around the file name")
        continue
    except IOError:
        print("Please enter a valid .txt file, with the correct formatting.")
        continue
    else:
        break


tableofDomains = [] #Contains a list of list of list representing the world with possible domains
#Setting up the initial domains

for row in range(5):
    tableofDomains.append([])
    for col in range(5):
        if initialNums[row][col] != 0:
            tableofDomains[row].append([ initialNums[row][col] ] )
        else:
            tableofDomains[row].append([1,2,3,4,5])
"""
Could remove
#Returns true if every element in the row is different, otherwise False
def rowDif(row):
    rowVals = []
    for col in range(5):
        if initialNums[row][col] in rowVals:
            return False
        rowvals.append(initialNums[row][col])
    return True

#Return true if every element in the column is different, otherwise False
def colDif(col):
    colVals = []
    for row in range(5):
        if initialNums[row][col] in colVals:
            return False
        colvals.append(initialNums[row][col])
    return True

"""
#Changes the domain of the cell based on the vertical values
def reduceVDomain(row, col):
    if len(tableofDomains[row][col]) == 1:
        return
    vList = []
    for x in range(5):
        vList.append(initialNums[x][col])
    for x in vList:
        if x in tableofDomains[row][col]:
            tableofDomains[row][col].pop(tableofDomains[row][col].index(x))
    return

#Changes the domain of the cell based on the horizontal values
def reduceHDomain(row, col):
    if len(tableofDomains[row][col]) == 1:
        return
    for x in initialNums[row]:
        if x in tableofDomains[row][col]:
            tableofDomains[row][col].pop(tableofDomains[row][col].index(x))
    return 0

queue = deque()
#Adding the vertical components to the queue
for rows in range(4):
    for cols in range(5):
        if vConstraints[rows][cols] != "0":
            queue.append([rows,cols, vConstraints[rows][cols]] )
#Adding the horinzontal components to the queue
for rows in range(5):
    for cols in range(4):
        if hConstraints[rows][cols] != "0":
            queue.append( [rows, cols, hConstraints[rows][cols]] )

#Forward Checking, reducing the domains for each cell using the horizontal and vertical constraints
for row in range(5):
    for col in range(5):
        reduceVDomain(row,col)
        reduceHDomain(row,col)

#Forward Checking with the vertical and horizontal constraints
#Reducing based off the queue, add to the queue if a square is changed and has a constraint as well
while len(queue) != 0:
    elem = queue.popleft()
    if elem[2] == ">":
        pos = 0
        while pos < len(tableofDomains[elem[0]] [elem[1]]):
            if  tableofDomains[elem[0]][elem[1]][pos] <= tableofDomains[elem[0]][elem[1] + 1][0]:
                tableofDomains[elem[0]][elem[1]].pop(pos)
            else:
                pos += 1
        pos = 0
        while pos < len(tableofDomains[elem[0]][elem[1] + 1]):
            if  tableofDomains[elem[0]][elem[1] + 1][pos] >= tableofDomains[elem[0]][elem[1]][-1]:
                tableofDomains[elem[0]][elem[1] + 1].pop(pos)
            else:
                pos += 1
    elif elem[2] == "<":
        pos = 0
        while pos < len(tableofDomains[elem[0]] [elem[1]]):
            if  tableofDomains[elem[0]][elem[1]][pos] >= tableofDomains[elem[0]][elem[1] + 1][-1]:
                tableofDomains[elem[0]][elem[1]].pop(pos)
            else:
                pos += 1
        pos = 0
        while pos < len(tableofDomains[elem[0]][elem[1] + 1]):
            if  tableofDomains[elem[0]][elem[1] + 1][pos] <= tableofDomains[elem[0]][elem[1]][0]:
                tableofDomains[elem[0]][elem[1] + 1].pop(pos)
            else:
                pos += 1
    elif elem[2] == "^":
        pos = 0
        while pos < len(tableofDomains[elem[0]] [elem[1]]):
            if  tableofDomains[elem[0]][elem[1]][pos] >= tableofDomains[elem[0] + 1][elem[1]][-1]:
                tableofDomains[elem[0]][elem[1]].pop(pos)
            else:
                pos += 1
        pos = 0
        while pos < len(tableofDomains[elem[0] + 1][elem[1]]):
            print(tableofDomains[elem[0]][elem[1]])
            if  tableofDomains[elem[0] + 1][elem[1]][pos] <= tableofDomains[elem[0]][elem[1]][0]:
                tableofDomains[elem[0] + 1][elem[1]].pop(pos)
            else:
                pos += 1
    elif elem[2] == "v":
        pos = 0
        while pos < len(tableofDomains[elem[0]] [elem[1]]):
            if  tableofDomains[elem[0]][elem[1]][pos] <= tableofDomains[elem[0] + 1][elem[1]][0]:
                tableofDomains[elem[0]][elem[1]].pop(pos)
            else:
                pos += 1
        pos = 0
        while pos < len(tableofDomains[elem[0] + 1][elem[1]]):
            print(tableofDomains[elem[0]][elem[1]])
            if  tableofDomains[elem[0] + 1][elem[1]][pos] >= tableofDomains[elem[0]][elem[1]][-1]:
                tableofDomains[elem[0] + 1][elem[1]].pop(pos)
            else:
                pos += 1
for x in range(5):
    for y in range(5):
        print(str(x) + "," + str(y) + ":" + str(tableofDomains[x][y]))
                    
    #Something about adding the queeue here
                
#Back Tracking 

#Setting up the output file
outputFileName = "OutputOf" + filename
fstream = open(outputFileName, "w+")
fstream.write(originalFile)




#---Test code---
for x in queue:
    print(x)

"""
fstream.write()
"""