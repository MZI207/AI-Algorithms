#Mohammed Iqbal
#Mzi207
from collections import deque
import copy

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

#Changes the domain of the cell based on the vertical values
def reduceVDomain(row, col):
    vList = []
    for x in range(5):
        if x != row:
            vList.append(initialNums[x][col])
    for x in range(len(vList)):
        if vList[x] in tableofDomains[row][col]:
            tableofDomains[row][col].pop(tableofDomains[row][col].index(vList[x]))

#Changes the domain of the cell based on the horizontal values
def reduceHDomain(row, col):
    for x in range(len(initialNums[row])):
        if initialNums[row][x] in tableofDomains[row][col] and x != col:
            tableofDomains[row][col].pop(tableofDomains[row][col].index(initialNums[row][x]))
    return 0

queue = deque()
#Adding the vertical components to the queue
for rows in range(4):
    for cols in range(5):
        if vConstraints[rows][cols] != "0":
            queue.append([rows,cols, vConstraints[rows][cols], "down"] )
            if vConstraints[rows][cols] == "^":
                queue.append([rows + 1, cols, "v", "up"])
            else:
                queue.append([rows+1, cols, "^", "up"]) 
#Adding the horinzontal components to the queue
for rows in range(5):
    for cols in range(4):
        if hConstraints[rows][cols] != "0":
            queue.append( [rows, cols, hConstraints[rows][cols], "right"] )
            if hConstraints[rows][cols] == "<":
                queue.append( [rows, cols + 1, ">", "left"] )
            else:
                queue.append([rows, cols + 1, "<", "left"])

#Forward Checking, reducing the domains for each cell using the horizontal and vertical values
for row in range(5):
    for col in range(5):
        reduceVDomain(row,col)
        reduceHDomain(row,col)

#Determines if it the futoshiki is possible based on the vertical numbers and horiziontal numbers
def domainCheck(domain):
    for x in domain:
        for y in x:
            if len(y) == 0:
                return False
    return True
possible = domainCheck(tableofDomains)
previousConstraints = []
#use the CP3 ALGO
#Forward Checking with the vertical and horizontal constraints
#Reducing based off the queue, eliminate appropriate values for every domain
while len(queue) != 0 and possible:
    change = False
    elem = queue.popleft()
    if elem[2] == ">":
        pos = 0
        while pos < len(tableofDomains[elem[0]] [elem[1]]):
            if  elem[3] == "right" and tableofDomains[elem[0]][elem[1]][pos] <= tableofDomains[elem[0]][elem[1] + 1][0]:
                tableofDomains[elem[0]][elem[1]].pop(pos)
                change = True
            elif elem[3] == "left" and tableofDomains[elem[0]][elem[1]][pos] <= tableofDomains[elem[0]][elem[1] - 1][0]:
                tableofDomains[elem[0]][elem[1]].pop(pos)
                change = True
            else:
                pos += 1
    elif elem[2] == "<":
        pos = 0
        while pos < len(tableofDomains[elem[0]] [elem[1]]):
            if  elem[3] == "right" and tableofDomains[elem[0]][elem[1]][pos] >= tableofDomains[elem[0]][elem[1] + 1][-1]:
                tableofDomains[elem[0]][elem[1]].pop(pos)
                change = True
            elif elem[3] == "left" and tableofDomains[elem[0]][elem[1]][pos] >= tableofDomains[elem[0]][elem[1] - 1][-1]:
                tableofDomains[elem[0]][elem[1]].pop(pos)
                change = True
            else:
                pos += 1
    elif elem[2] == "^":
        pos = 0
        while pos < len(tableofDomains[elem[0]] [elem[1]]):
            if  elem[3] == "down" and tableofDomains[elem[0]][elem[1]][pos] >= tableofDomains[elem[0] + 1][elem[1]][-1]:
                tableofDomains[elem[0]][elem[1]].pop(pos)
                change = True
            elif elem[3] == "up" and tableofDomains[elem[0]][elem[1]][pos] >= tableofDomains[elem[0] - 1][elem[1]][-1]:
                tableofDomains[elem[0]][elem[1]].pop(pos)
                change = True 
            else:
                pos += 1
        pos = 0
    elif elem[2] == "v":
        pos = 0
        while pos < len(tableofDomains[elem[0]] [elem[1]]):
            if  elem[3] == "down" and tableofDomains[elem[0]][elem[1]][pos] <= tableofDomains[elem[0] + 1][elem[1]][0]:
                tableofDomains[elem[0]][elem[1]].pop(pos)
                change = True
            elif elem[3] == "up" and tableofDomains[elem[0]][elem[1]][pos] <= tableofDomains[elem[0] - 1][elem[1]][0]:
                tableofDomains[elem[0]][elem[1]].pop(pos)
                change = True
            else:
                pos += 1
    if change:
        for x in previousConstraints:
            if (elem[0] == x[0] and x[1] == elem[1] - 1) or \
            (elem[0] == x[0] and x[1] == elem[1] + 1) or \
            (x[0] == elem[0] + 1 and x[1] == elem[1]) or \
            (x[0] == elem[1] - 1 and x[1] == elem[1]):
                queue.append(x)
        for x in range(5):
            for y in range(5):
                if len(tableofDomains[x][y]) == 1 and initialNums[x][y] == 0:
                    initialNums[x][y] = tableofDomains[x][y][0]
                    #Updating horizontal 
                    for col in range(5):
                        if tableofDomains[x][y][0] in tableofDomains[x][col] and col != y:
                            tableofDomains[x][col].pop(tableofDomains[x][col].index(tableofDomains[x][y][0]))
                            for prev in previousConstraints:
                                if prev[0] == x and prev[1] == col:
                                    queue.append(prev)
                    #Updating Vertical:
                    for row in range(5):
                        if tableofDomains[x][y][0] in tableofDomains[row][y] and row != x:
                            tableofDomains[row][y].pop(tableofDomains[row][y].index(tableofDomains[x][y][0]))
                            for prev in previousConstraints:
                                if prev[0] == x and prev[1] == col:
                                    queue.append(prev)
    previousConstraints.append(elem)
    

#Determines if the domains are possible
possible = domainCheck(tableofDomains)

#Returns true if every element in the row is different, otherwise False
def rowDif(row, world):
    rowVals = []
    for col in range(5):
        if world[row][col] in rowVals:
            return False
        if world[row][col] != 0:
            rowVals.append(world[row][col])
    return True

#Return true if every element in the column is different, otherwise False
def colDif(col, world):
    colVals = []
    for row in range(5):
        if world[row][col] in colVals:
            return False
        if world[row][col] != 0:
            colVals.append(world[row][col])
    return True

def alldif(world):
    for x in range(5):
        if not colDif(x, world):
            return False
        if not rowDif(x, world):
            return False
    return True
#Used to check if the nums have worked and are correct
def check(world):
    for x in range(5):
        if not colDif(x, world):
            return False
        if not rowDif(x, world):
            return False
    for x in range(5):
        for y in range(5):
            if world[x][y] == 0:
                
                return False
    return True

#Setting up backtracking 
class Node:
    def __init__(self, domain, parent, children):
        self.domain = domain
        self.parent = parent
        self.children = children
        self.world = []
        self.check = False #Determines if all the children in this Node has been checked and if so set as True 
        for x in range(5):
            self.world.append([])
            for y in range(5):
                if len(domain[x][y]) == 1:
                    self.world[x].append(domain[x][y][0])
                else:
                    self.world[x].append(0)
        #Determine which cell in the domain has the most contrained variable (Heuristic)
        self.h = [0,0] #The heuristic holds the coordinates of the most constrained variable
        row = 0
        col = 1
        while row < 5:
            while col < 5:
                if len( domain[self.h[0]][self.h[1]] )== 1:
                    self.h = [row, col]
                elif (len(domain[row][col]) < len( domain[self.h[0]][self.h[1]] ) and len(domain[row][col]) != 1):
                    self.h = [row, col]
                elif len(domain[row][col]) == len( domain[self.h[0]][self.h[1]] ) and len(domain[row][col]) != 1:
                    self.h = self.mostConstrainingVar([row,col], self.h)
                col += 1
            row += 1
            col = 0
    #Given two coordinates in list form (s.t [row, col]) find the most contraining coordinate
    def mostConstrainingVar(self, coor1, coor2):
        coorVal1 = 0
        coorVal2 = 0
        #horizontal component
        for col in range(5):
            if coor1[1] != col:
                for val in self.domain[coor1[0]][coor1[1]]:
                    if val in self.domain[coor1[0]][col]:
                        coorVal1 += 1
            if coor2[1] != col:
                for val in self.domain[coor2[0]][coor2[1]]:
                    if val in self.domain[coor2[0]][col]:
                        coorVal2 += 1
        #vertical component
        for row in range(5):
            if coor1[0] != row:
                for val in self.domain[coor1[0]][coor1[1]]:
                    if val in self.domain[row][coor1[1]]:
                        coorVal1 += 1
            if coor2[0] != row:
                for val in self.domain[coor2[0]][coor2[1]]:
                    if val in self.domain[row][coor2[1]]:
                        coorVal2 += 1
        if coorVal1 >= coorVal2:
            return coor1
        return coor2

nodes = []
nodesExplored = []
currNode = Node(tableofDomains, None, [])

#Backtracking
while check(currNode.world) == False and possible:
    if currNode.check == False:
        for vals in currNode.domain[currNode.h[0]][currNode.h[1]]:
            tempDomain = copy.deepcopy(currNode.domain)
            tempDomain[currNode.h[0]][currNode.h[1]] = [vals]
            updatequeue = deque()
            updatequeue.append( [ currNode.h[0], currNode.h[1], vals ] ) #Adding to what needs to be updated in the queue with (row, col, val)
            while len(updatequeue) != 0:
                if domainCheck(tempDomain) == False:
                    break
                elem = updatequeue.popleft()
                for pos in range(5):
                    #Update the horizontal components of the domain based of vals
                    if pos != elem[1] and elem[2] in tempDomain[elem[0]][pos]:
                        tempDomain[elem[0]][pos].pop(tempDomain[elem[0]][pos].index(elem[2]))
                        if currNode.world[elem[0]][pos] == 0 and len(tempDomain[elem[0]][pos]) == 1:
                            updatequeue.append( [elem[0], pos, tempDomain[elem[0]][pos][0] ] )
                    #Update the vertical components of the domain based of vals
                    if pos != elem[0] and elem[2] in tempDomain[pos][elem[1]]:
                        tempDomain[pos][elem[1]].pop(tempDomain[pos][elem[1]].index(elem[2]))
                        if currNode.world[pos][elem[1]] == 0 and len(tempDomain[pos][elem[1]] )  == 1:
                            updatequeue.append( [pos, elem[1], tempDomain[pos][elem[1]][0] ] ) 
            #Determine if the node is possible based on the domains, if so add it to the children
            tempNode = Node(tempDomain, currNode, [])
            if domainCheck(tempDomain) and alldif(tempNode.world):
                currNode.children.append(Node(tempDomain, currNode, []))
        #backtrack to the parent node        
        if len(currNode.children) == 0:
            currNode.parent.children.pop(currNode.parent.children.index(currNode))
            currNode = currNode.parent
            if len(currNode.children) == 0:
                currNode.check = True
            else:
                currNode = currNode.children[0]
        else:
            currNode = currNode.children[0]
    else:
        currNode.parent.children.pop(currNode.parent.children.index(currNode))
        currNode = currNode.parent

#Setting up the output file
outputFileName = "OutputOf" + filename
if "Input" in filename:
    outputFileName = filename.replace("Input", "Output")
fstream = open(outputFileName, "w+")
result = ""
if possible:
    for x in currNode.world:
        for y in x:
            result += str(y) + " "
        result += "\n"
else:
    result = "The Futoshiki is not possible given the constraints"
fstream.write(result)
fstream.close()