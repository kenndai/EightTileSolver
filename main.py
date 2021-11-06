import queue
from problem import Problem
import time

# Parameter Legend
# nodes --> priority queue
# node --> total cost, state, and depth
# state --> list representing the puzzle board 
# children --> list of states resulting from a shift
# child --> a singular state from children

def misplacedTile(problem: Problem, addNodes):
    nodes = queue.PriorityQueue()
    # enqueues a node corresponding to initial state
    nodes.put(makeNode(problem.initialState, 0))
    while(1):
        if (nodes.empty()):
            print("no solution")
            return -1
        else:
            node = nodes.get()
            if (tilesMisplaced(node[1]) == 0): 
                return node
            else:
                nodes = addNodes(nodes, expand(node[1]), node[2] + 1)

# creates nodes corresponding to the children states and enqueue
def addNodes(queue, children, depth: int):
    for child in children:
        queue.put(makeNode(child, depth))
    return queue

# creates a node by assigning a function cost, uniform cost + heuristic cost, to a state
def makeNode(state, depth: int):
    return [tilesMisplaced(state) + depth, state, depth]
    
# returns a generated list of child states
# iterates through Problem's operators and runs each
# only non-empty states are appended
def expand(state):
    children = []
    operators = [Problem.shiftDown, Problem.shiftLeft, Problem.shiftRight, Problem.shiftUp]
    blankIndex = state.index(0) 
    for shift in operators:
        child = shift(state, blankIndex)
        if (child):
            children.append(child)
    return children

# compares two lists and returns the amount of differences between the list
# excludes the blank space
# used for calculating amount of misplaced tiles as well as to compare state with goal state
def tilesMisplaced(state):
    differences = 0
    for i in range(len(state)):
        if (state[i] != 0 and state[i] != i + 1):
            differences += 1
    return differences

def manhattanCost(state):
    cost = 0
    for i in range(len(state)):
        value = state[i]
        if (value != 0 and value != i + 1):
            # use // to find row, % to find column
            valueRow = i // 3 
            valueColumn = i % 3
            goalRow = (value - 1) // 3
            goalColumn = (value - 1) % 3
            cost += abs(goalRow - valueRow) + abs(goalColumn - valueColumn)
    return cost

def main():
    print("Welcome to the Eight Tile Puzzle Solver!")
    userChoice = input("Enter '1' to solve the default puzzle or '2' to create your own puzzle.\n")

    # create a problem space
    # the problem's initial state is set to either the predefined one or user input
    puzzle = Problem
    nodes = queue.PriorityQueue()

    if (userChoice == '1'):
        print("Initial: ")
        puzzle.print(puzzle.initialState)

    elif (userChoice == '2'):
        print("\nEnter your puzzle, using a zero to represent the blank.\nPlease only enter valid 8-puzzles.\n") 

        row1 = input("row 1: ")
        row2 = input("row 2: ")
        row3 = input("row 3: ")

        # checks that the length of each row is exactly 3
        if (len(row1) != 3 or len(row2) != 3 or len(row3) != 3 ):
            print("Invalid row length! Exiting Program.")
            return -1
        
        # converts rows into a list of integers
        rowInput = list(row1 + row2 + row3)
        for i in range(len(rowInput)):
            rowInput[i] = int(rowInput[i])
        
        # set intial state to input
        puzzle.initialState = rowInput
        print("\nYour puzzle: ")
        puzzle.print(puzzle.initialState)

    # choose algorithm to solve default or custom puzzle
    print("\nSelect a search algorithm to solve your puzzle:")
    algorithm = input("Enter \'1\' for Uniform Cost Search\nEnter \'2\'for Misplaced Tile A*\nEnter \'3\' for Manhattan Distance A*\n")

    if (algorithm == '1'):
        print("\nRunning Uniform Cost Algorithm...")
        # call corresponding algorithm
    elif (algorithm == '2'):
        print("\nRunning Misplaced Tile Algorithm...")
        start = time.time()
        node = misplacedTile(puzzle, addNodes)
        end = time.time()
        puzzle.print(node[1])
        print(f"Total Cost: {node[0]}")
        print(f"Depth: {node[2]}")
        print(end - start)

    elif (algorithm == '3'):
        print("\nRunning Manhattan Distance Algorithm...")
        # call corresponding algorithm

if __name__ == "__main__":
    main()