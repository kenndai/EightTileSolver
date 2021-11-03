class Problem:
    goalState = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    initialState = [1, 2, 3, 4, 0, 5, 6, 7, 8]

    # prints current state of a puzzle by passing in a list
    def print(node):
        for i in range(0, len(node), 3):
            print(node[i:i+3])
        print()

    # operations
    # checks if blank is at any boundaries before swapping positions
    # if blank cannot be shifted, return a copy of the original list so it's not
    # modified for the other possible operations
    def shiftLeft(node, blankIndex):
        if (blankIndex != 0 and blankIndex != 3 and blankIndex != 6):
            return swap(node, blankIndex, blankIndex - 1)
        else:
            return []

    def shiftRight(node, blankIndex):
        if (blankIndex != 2 and blankIndex != 5 and blankIndex != 8):
            return swap(node, blankIndex, blankIndex + 1)
        else:
            return []

    def shiftUp(node, blankIndex):
        if (blankIndex != 0 and blankIndex != 1 and blankIndex != 2):
            return swap(node, blankIndex, blankIndex - 3)
        else:
            return []

    def shiftDown(node, blankIndex):
        if (blankIndex != 6 and blankIndex != 7 and blankIndex != 8):
            return swap(node, blankIndex, blankIndex + 3)
        else:
            return []

# makes a copy 
def swap(node, pos1, pos2):
    # don't modify the existing node
    newNode = node.copy()
    newNode[pos1], newNode[pos2] = node[pos2], node[pos1]
    return newNode