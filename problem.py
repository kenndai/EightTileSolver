class Problem:
    goalState = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    initialState = [1, 2, 3, 4, 0, 5, 6, 7, 8]

    # prints current state of a puzzle by passing in a list
    def print(state):
        for i in range(0, len(state), 3):
            print(state[i:i+3])

    # operations
    # checks if blank is at any boundaries before swapping positions
    # if blank cannot be shifted, return a copy of the original list so it's not
    # modified for the other possible operations

    def shiftLeft(family, blankIndex):
        if (blankIndex % 3 != 0):
            return swap(family[0], blankIndex, blankIndex - 1)
        else:
            return []

    def shiftRight(family, blankIndex):
        if (blankIndex % 3 != 2):
            return swap(family[0], blankIndex, blankIndex + 1)
        else:
            return []

    def shiftUp(family, blankIndex):
        if (blankIndex > 2):
            return swap(family[0], blankIndex, blankIndex - 3)
        else:
            return []

    def shiftDown(family, blankIndex):
        if (blankIndex < 6):
            return swap(family[0], blankIndex, blankIndex + 3)
        else:
            return []

# makes a copy 
def swap(state, pos1, pos2):
    # don't modify the existing state
    newState = state.copy()
    newState[pos1], newState[pos2] = state[pos2], state[pos1]
    return newState