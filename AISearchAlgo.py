#Mohammed Iqbal
#Mzi207
#Create a A* Search Algorithm for the 15 puzzle problem using the Manhattan 
#distance as a heuristic

state = {} #The state of the 15 puzzle
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
def manhattanDistance(val):
    result = 0
    result += abs(finalState[val][0] - state[val][0]) + abs(finalState[val][1] - state[val][1])
    return result

#Setting up the output file
outputFileName = "OutputOf"+filename
fstream = open(outputFileName, "w+")
fstream.write(originalFile)

#The A* search algorithm
done = False #Check to see if the state is equal to the goal state

depth = 0
instructions = []
numNodes = 0
fNodesVals = []
while (done):
    heurisitcVal = 0
    for i in range(16):
        heurisitcVal += manhattanDistance(x)
    if heurisitcVal == 0: #If the initial is already the goal
        done = True
        break
    else:
        #pseudocode
        findNext() #Increments num nodes generated in the tree and the instruction the tree takes
        for i in range(16):
            heurisitcVal += manhattanDistance(x)
        done = heurisitcVal == 0
        depth+=1
        fNodesVals.append(depth + heurisitcVal)

    

def findNext():
    return 0


#Test code
for x in range(16):
    print(str(x) +":" + str(state[x]))
print()
for x in range(16):
    print(str(x) +":" + str(finalState[x]))

for x in range(16):
    print(str(x) +":" +  str(manhattanDistance(x)))