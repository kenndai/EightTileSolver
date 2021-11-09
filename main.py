import queue
from problem import Problem
import time

# Parameter Legend
# node --> h(n), g(n), "family"
# nodes --> priority queue 
# state --> list representing the puzzle board 
# families --> list of "family"
# family --> a list containing "child" state and its "parent" state,
#            family at index 0, parent at index 1

def aStar(problem: Problem, addNodes):
    global maxQueueSize
    global nodesExpanded

    nodes = queue.PriorityQueue()
    # enqueues a node corresponding to initial state
    nodes.put(makeNode([problem.initialState, [0]], 0))
    while(1):
        if (nodes.empty()):
            print("no solution")
            return -1
        else:
            node = nodes.get()
            print(f"The best state to expand with a g(n) = {node[1]} and h(n) = {node[0] - node[1]} is...")
            problem.print(node[2][0])
            if (tilesMisplaced(node[2][0]) == 0): 
                return node
            else:
                nodesExpanded += 1
                nodes = addNodes(nodes, expand(node[2]), node[1] + 1)
                if nodes.qsize() > maxQueueSize:
                    maxQueueSize = nodes.qsize()

# creates nodes corresponding to the families states and enqueue
def addNodes(queue, families, depth):
    for family in families:
        queue.put(makeNode(family, depth))
    return queue

# creates a node by assigning a function cost, uniform cost + heuristic cost, to a state
# return based on if family is the initial state, i.e. has no parent
def makeNode(family, depth):
    return [heuristicFunction(family[0]) + depth, depth, family]

# returns a generated list of family states
# iterates through Problem's operators and runs each
# only non-empty states are appended
def expand(family):
    families = []
    operators = [Problem.shiftDown, Problem.shiftLeft, Problem.shiftRight, Problem.shiftUp]
    child = family[0]
    parent = family[1]
    blankIndex = child.index(0) 

    # apply operators to child state to make "grandchildren"
    # reduce branching factor by not allowing grandchildren to match the "grandparent"
    for shift in operators:
        grandchild = shift(family, blankIndex)
        if (not isEqual(grandchild, parent)):
            families.append([grandchild, child])
    return families

def isEqual(state1, state2):
    for i in range(len(state1)):
        if (state1[i] != state2[i] or len(state1) != len(state2)):
            return False
    return True

# returns the sum of the amount of differences between the current state and the goal
# excludes the blank space
def tilesMisplaced(state):
    differences = 0
    for i in range(len(state)):
        if (state[i] != 0 and state[i] != i + 1):
            differences += 1
    return differences

# returns the sum of the manhattan cost between the current state and goal
# excludes the blank space
def manhattanCost(state):
    cost = 0
    for i in range(len(state)):
        value = state[i]
        if (value != 0 and value != i + 1):
            # use // to for row and % to for column to find coordinates of tile
            # sum the differnce between the coordinates to find manhattan cost for a tile
            valueRow = i // 3 
            valueColumn = i % 3
            goalRow = (value - 1) // 3
            goalColumn = (value - 1) % 3
            cost += abs(goalRow - valueRow) + abs(goalColumn - valueColumn)
    return cost

# for a-star search, the heuristic for uniform cost is hard coded to 0 
# returns 0
def uniformCost(state):
    return 0

# main functions

def enterPuzzle():
    row1 = input("Enter the first row or the entire puzzle all at once: ")
    if (len(row1) == 9):
        row1 = list(row1)
        for i in range(len(row1)):
            row1[i] = int(row1[i])
        return row1
    elif (len(row1) != 3):
        return -1

    row2 = input("Second row: ")
    if (len(row2) != 3):
        return -1

    row3 = input("Third row: ")
    if (len(row3) != 3):
        return -1

    rowInput = list(row1 + row2 + row3)
    for i in range(len(rowInput)):
        rowInput[i] = int(rowInput[i])
    
    return rowInput

def printStatistics(node, start, end):
        print(f"\nGoal state!")
        print(f"\nSolution depth was: {node[1]}")
        print(f"Number of nodes expanded: {nodesExpanded}")
        print(f"Max queue size: {maxQueueSize}")

# global variable assigned to a heuristic function, modified depending on user input 
heuristicFunction = uniformCost
maxQueueSize = 0
nodesExpanded = 0

def main():
    global heuristicFunction 
    print("Welcome to the Eight Tile Puzzle Solver!")
    userChoice = input("Enter '1' to solve the default puzzle or '2' to create your own puzzle.\n")

    # create a problem space
    # the problem's initial state is set to either the predefined one or user input
    puzzle = Problem

    if (userChoice == '1'):
        print("Initial: ")
        puzzle.print(puzzle.initialState)

    elif (userChoice == '2'):
        print("\nEnter your puzzle, entering three values at a time or nine values all at once.")
        print("Please use a zero to represent the blank space.") 

        puzzleInput = enterPuzzle()
        if (puzzleInput == -1):
            print("Invalid input. Exiting program.")
            return -1

        # set intial state to input
        puzzle.initialState = puzzleInput
        print("\nYour puzzle: ")
        puzzle.print(puzzle.initialState)

    # choose algorithm to solve default or custom puzzle
    print("\nSelect a search algorithm to solve your puzzle:")
    algorithm = input("Enter \'1\' for Uniform Cost Search\nEnter \'2\'for Misplaced Tile A*\nEnter \'3\' for Manhattan Distance A*\n")

    if (algorithm == '1'):
        print("\nRunning Uniform Cost Algorithm...\n")
        heuristicFunction = uniformCost

        start = time.time()
        node = aStar(puzzle, addNodes)
        end = time.time()

        printStatistics(node, start, end)

    elif (algorithm == '2'):
        print("\nRunning Misplaced Tile Algorithm...\n")
        heuristicFunction = tilesMisplaced

        start = time.time()
        node = aStar(puzzle, addNodes)
        end = time.time()

        printStatistics(node, start, end)

    elif (algorithm == '3'):
        print("\nRunning Manhattan Distance Algorithm...\n")
        heuristicFunction = manhattanCost

        start = time.time()
        node = aStar(puzzle, addNodes)
        end = time.time()

        printStatistics(node, start, end)

if __name__ == "__main__":
    main()