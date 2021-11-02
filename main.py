import queue
from problem import Problem

# function general-search(problem, QUEUEING-FUNCTION)  
# nodes = MAKE-QUEUE(MAKE-NODE(problem.INITIAL-STATE)) 
# loop do
#  if EMPTY(nodes) then return "failure" (we have proved there is no solution!)
#    node = REMOVE-FRONT(nodes) 
#  if problem.GOAL-TEST(node.STATE) succeeds then return node
#     nodes = QUEUEING-FUNCTION(nodes, EXPAND(node, problem.OPERATORS))  
#  end

# use a prioqueue for the "greedy aspect", choosing the lowest cost path
# need a function to calculate the amount of misplaced tiles or the manhattan distance  
def misplaced(problem, queueFunc):
    print("misplaced tile")

    nodes = queue.PriorityQueue()
    nodes.put(problem.initialState)

    # loop here1
    if (nodes.empty):
        print("no solution")
        return -1
    else:
        node = nodes.get()
        if (compare(problem.goalState, node)):
            return node
        else:
            # find the index of the blank and pass it to the operations
            blankIndex = node.index(0) 
            nodes.put(problem.initialState)


def manhattan(problem, queueFunc):
    print("manhattan distance");
    nodes = queue.PriorityQueue()
    nodes.put(problem.initialState)

def compare(list1, list2):
    for i in range(len(list1)):
        if (list1[i] != list2[i]):
            return False
    return True


def main():
    print("Welcome to the Eight Tile Puzzle Solver!")
    userChoice = input("Enter '1' to solve the default puzzle or '2' to create your own puzzle.\n")

    # create a problem space
    # the problem's initial state is set to either the predefined one or user input
    problem = Problem

    if (userChoice == '1'):
        print("Initial: ")
        problem.print(problem.initialState)

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