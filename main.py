import queue
from problem import Problem

def misplaced(problem: Problem, queueFunc):
    print("misplaced tile")

    nodes = queue.PriorityQueue()
    nodes.put(problem.initialState)

    operators = [problem.shiftLeft, problem.shiftRight, problem.shiftUp, problem.shiftDown]

    # loop here1
    if (nodes.empty):
        print("no solution")
        return -1
    else:
        node = nodes.get()
        if (tilesMisplaced(problem.goalState, node) == 0): 
            return node
        else:
            # find the index of the blank and pass it to the operations
            blankIndex = node.index(0) 

            nodes = queueFunc(nodes, expand(node, blankIndex, operators))

# iterate through problem's operators and run each of them with the same aruguments
# if they return a non-empty list, append to the children list
# return children
def expand(node, blankIndex, operators):
    children = []
    for shift in operators:
        child = shift(node, blankIndex)
        if (child):
            children.append(child)
    return children

# enqueue heuristic cost and node as a list
# iterate through children and call tilesMisplaced() or manhattan to calculate heueristic cost 
def queueFunc(queue, children):
    goal = Problem.goalState
    for child in children:
        cost = tilesMisplaced(goal, child)
        queue.put([cost, child])
    return queue


# compares two lists and returns the amount of differences between the list
# excludes the blank space
# used for calculating amount of misplaced tiles as well as to compare node with goal state
def tilesMisplaced(list1, list2):
    differences = 0
    for i in range(len(list1)):
        if (list1[i] != list2[i] and list2[i] != 0):
            differences += 1
    return differences

def manhattan(problem, queueFunc):
    print("manhattan distance");
    nodes = queue.PriorityQueue()
    nodes.put(problem.initialState)

def manhattanCost(node):
    return 1

def main():
    print("Welcome to the Eight Tile Puzzle Solver!")
    userChoice = input("Enter '1' to solve the default puzzle or '2' to create your own puzzle.\n")

    # create a problem space
    # the problem's initial state is set to either the predefined one or user input
    problem = Problem
    nodes = queue.PriorityQueue()

    if (userChoice == '1'):
        # print("Initial: ")
        # problem.print(problem.initialState)
        operators = [problem.shiftDown, problem.shiftLeft, problem.shiftRight, problem.shiftUp]
        children = expand(problem.initialState, 4, operators)
        
        nodes = queueFunc(nodes, children)
        print(nodes.get())
        print(nodes.get())
        print(nodes.get())
        print(nodes.get())

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
        problem.initialState = rowInput
        print("\nYour puzzle: ")
        problem.print(problem.initialState)

    # choose algorithm to solve default or custom puzzle
    print("Select a search algorithm to solve your puzzle:")
    algorithm = input("Enter \'1\' for Uniform Cost Search\nEnter \'2\'for Misplaced Tile A*\nEnter \'3\' for Manhattan Distance A*\n")

    if (algorithm == '1'):
        print("uniform cost algorithm")
        # call corresponding algorithm
    elif (algorithm == '2'):
        print("misplaced tile algorithm")
        # call corresponding algorithm
    elif (algorithm == '3'):
        print("manhattan distance algorithm")
        # call corresponding algorithm

if __name__ == "__main__":
    main()