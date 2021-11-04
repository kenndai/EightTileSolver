import queue
from problem import Problem

# Parameter Legend
# nodes --> priority queue
# node --> total cost, state, and depth
# state --> list representing the puzzle board 
# children --> list of states resulting from a shift
# child --> a singular state from children

def aStar(problem: Problem, addNodes):
    nodes = queue.PriorityQueue()

    # enqueues a node corresponding to initial state
    nodes.put(makeNode(problem.initialState, 0))

    while(1):
        if (nodes.empty()):
            print("no solution")
            return -1
        else:
            node = nodes.get()
            if (tilesMisplaced(problem.goalState, node[1] == 0)): 
                return node[1]
            else:
                nodes = addNodes(nodes, expand(node[1]), node[2] + 1)

# creates nodes corresponding to the children states and enqueue
def addNodes(queue, children, depth: int):
    for child in children:
        queue.put(makeNode(child, depth))
    return queue

# creates a node by assigning a function cost, uniform cost + heuristic cost, to a state
def makeNode(state, depth: int):
    return [tilesMisplaced(Problem.goalState, state) + depth, state, depth]
    
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
def tilesMisplaced(goal, state):
    differences = 0
    for i in range(len(state)):
        if (goal[i] != state[i] and state[i] != 0):
            differences += 1
    return differences

def manhattan(problem, addNodes):
    print("manhattan distance");
    nodes = queue.PriorityQueue()
    nodes.put(problem.initialState)

def manhattanCost(state):
    return 1

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
    print("Select a search algorithm to solve your puzzle:")
    algorithm = input("Enter \'1\' for Uniform Cost Search\nEnter \'2\'for Misplaced Tile A*\nEnter \'3\' for Manhattan Distance A*\n")

    if (algorithm == '1'):
        print("uniform cost algorithm")
        # call corresponding algorithm
    elif (algorithm == '2'):
        print("misplaced tile algorithm")
        puzzle.print(aStar(puzzle, addNodes))

    elif (algorithm == '3'):
        print("manhattan distance algorithm")
        # call corresponding algorithm

if __name__ == "__main__":
    main()