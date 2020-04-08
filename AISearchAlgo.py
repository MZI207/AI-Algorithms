#Mohammed Iqbal
#Mzi207
#Create a A* Search Algorithm for the 15 puzzle problem using the Manhattan 
#distance as a heuristic
import copy
state = {} #The initial state of the 15 puzzle
finalState = {} #goal State

# We use a dictionary where the key is value and the pair is the coordinates
#of the state, for example (1,[1,1]), the value 1 can be found at 1, 1
#Trying to get a valid file

originalFile = ""

while True:
    try:
        filename = input ("Filename: ")
        fstream = open(filename, "r")
        lines = ""
        #Getting the initial state
        for x in range(4):
            lines = fstream.readline()
            temp = lines.strip().split(" ")
            temp = [int(i) for i in temp]
            for position in range(len(temp)):
                state[temp[position]] = [x, position]
        #Getting the final state
        fstream.readline()
        for x in range(4):
            lines = fstream.readline()
            temp = lines.strip().split(" ")
            temp = [int(i) for i in temp]
            for position in range(len(temp)):
                finalState[temp[position]] = [x, position]
        #Getting the original file to be put in the output file
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

#The heurisitc function the manhattan distance, calculates how far a square is from its goal state
def manhattanDistance(val, tempState):
    result = 0
    result += abs(finalState[val][0] - tempState[val][0]) + abs(finalState[val][1] - tempState[val][1])
    return result


#Setting up the node class
class Node:
    def __init__(self, val, depth = 0, path = []):
        self.val = val #The state of the node
        self.h  = 0 #The h(x) value of myself
        for i in range(16):
            self.h += manhattanDistance(i, self.val)
        self.depth = 0 #To get f(x) add self.h + self.depth
        self.path = copy.copy(path) #Path to reach me, in directions from initial state


#Setting up the output file
outputFileName = "OutputOf"+filename
fstream = open(outputFileName, "w+")
fstream.write(originalFile)

#The A* search algorithm
done = True #Check to see if the state is equal to the goal state


instructions = []
nodes = [] 
nodesExplored = []
currNode = Node(state) #Node to check the nodes of the children and where to move
for i in range(16):
    currNode.h += manhattanDistance(i,currNode.val)
nodes.append(currNode)


#Expands the current node and checks where to move 
while (done):
    if currNode.h == 0: #If the initial is already the goal
        done = True
        break
    else:
        emptySpace = currNode.val[0]
        stateLeft = {}
        stateRight = {}
        stateUp = {}
        stateDown = {}
        keys = list(currNode.val.keys())
        vals = list(currNode.val.values())
        #State Up
        if (emptySpace[0] != 0):
            upCoordinate = [emptySpace[0] - 1, emptySpace[1]]
            valUp = vals.index(upCoordinate)
            for i in range(16):
                if (i == valUp):
                    stateUp[i] = emptySpace
                elif (i == 0):
                    stateUp[i] = upCoordinate
                else:
                    stateUp[i] = currNode.val[i]
        #State down
        if (emptySpace[0] != 3):
            downCoordinate = [emptySpace[0] + 1, emptySpace[1]]
            valDown = vals.index(downCoordinate)
            for i in range(16):
                if (i == valDown):
                    stateDown[i] = emptySpace
                elif (i == 0):
                    stateDown[i] = downCoordinate
                else:
                    stateDown[i] = currNode.val[i]
        #State Left
        if (emptySpace[1] != 0):
            leftCoordinate = [emptySpace[0], emptySpace[1] - 1]
            valLeft = vals.index(leftCoordinate)
            for i in range(16):
                if (i == valLeft):
                    stateLeft[i] = emptySpace
                elif (i == 0):
                    stateLeft[i] = leftCoordinate
                else:
                    stateLeft[i] = currNode.val[i]
        #State Right
        if (emptySpace[1] != 3):
            rightCoordinate = [emptySpace[0], emptySpace[1] + 1]
            valRight = vals.index(rightCoordinate)
            for i in range(16):
                if (i == valRight):
                    stateRight[i] = emptySpace
                elif (i == 0):
                    stateRight[i] = rightCoordinate
                else:
                    stateRight[i] = currNode.val[i]
        #Out of the for loop
        if stateLeft != {}:
            nodeLeft = Node(stateLeft, currNode.depth + 1, currNode.path)
            nodeLeft.path.append("L")
            repeat = False
            for node in nodesExplored:
                if node.val == nodeLeft:
                    repeat = True
            if not repeat:
                nodes.append(nodeLeft)
        if stateRight != {}:
            nodeRight = Node(stateRight, currNode.depth + 1, currNode.path)
            nodeRight.path.append("R")
            repeat = False
            for node in nodesExplored:
                if node.val == nodeRight:
                    repeat = True
            if not repeat:
                nodes.append(nodeRight)
        if stateUp != {}:
            nodeUp = Node(stateUp, currNode.depth + 1, currNode.path)
            nodeUp.path.append("U")
            repeat = False
            for node in nodesExplored:
                if node.val == nodeUp:
                    repeat = True
            if not repeat:
                nodes.append(nodeUp)
        if stateDown != {}:
            nodeDown = Node(stateDown, currNode.depth + 1, currNode.path)
            nodeDown.path.append("D")
            repeat = False
            for node in nodesExplored:
                if node.val == nodeDown:
                    repeat = True
            if not repeat:
                nodes.append(nodeDown)
        nodesExplored.append(nodes.pop(nodes.index(currNode)))
        for node in range(len(nodes)):
            if node == 0:
                currNode = nodes[node]
            elif currNode.h + currNode.depth > nodes[node].h + nodes[node].depth:
                currNode = nodes[node]


#Test code
for x in range(16):
    print(str(x) +":" + str(currNode.val[x]))
print(currNode.path)
"""
for x in range(16):
    print(str(x) +":" + str(finalState[x]))
for x in range(16):
    print(str(x) +":" +  str(manhattanDistance(x,currNode.val)))
    """