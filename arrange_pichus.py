# Author : Nikhil Kamble
# 
# Based on skeleton code in CSCI B551, Fall 2021.
# 

import sys

# Parse the map from a given filename
def parse_map(filename):
    with open(filename, "r") as f:
        return [[char for char in line] for line in
                f.read().rstrip("\n").split("\n")][3:]

# To check whether two agents(aka pichu) can see each other in a row/column/diagonal
def check_pichu_position(house_map, row, col):
    # checking for pichu on right side
    for i in range(col + 1, len(house_map[0])):
        #checking for 'p' at the current position, if yes it returns False - as Pichu exist in that direction
        if house_map[row][i] == 'p':
            return False
        #checking for 'X' and '@' at the current position to break the loop, as wall or you are present in that direction which is valid
        if house_map[row][i] == 'X' or house_map[row][i] == '@':
            break

    # checking for pichu on diagonal top_right
    temporary_row, temporary_column = row, col
    while True:
        #adding a temporary row and column for traversing top right diagonal
        temporary_row -= 1
        temporary_column += 1
        if not ( temporary_row >= 0 and temporary_column < len(house_map[0]) ):
            break
        #checking for 'p' at the current position, if yes it returns False - as Pichu exist in that direction
        if house_map[temporary_row][temporary_column] == 'p':
            return False
        #checking for 'X' and '@' at the current position to break the loop, as wall or you are present in that direction which is valid
        if house_map[temporary_row][temporary_column] == 'X' or house_map[temporary_row][temporary_column] == '@':
            break
        
    # checking for pichu on left side
    for i in range(col - 1, -1, -1):
        #checking for 'p' at the current position, if yes it returns False - as Pichu exist in that direction
        if house_map[row][i] == 'p':
            return False
        #checking for 'X' and '@' at the current position to break the loop, as wall or you are present in that direction which is valid
        if house_map[row][i] == 'X' or house_map[row][i] == '@':
            break

    # checking for pichu on diagonal top_left
    temporary_row, temporary_column = row, col
    while True:
        #adding a temporary row and column for traversing top left diagonal
        temporary_row -= 1
        temporary_column -= 1
        if not ( temporary_row >= 0 and temporary_column >= 0 ):
            break
        #checking for 'p' at the current position, if yes it returns False - as Pichu exist in that direction
        if house_map[temporary_row][temporary_column] == 'p':
            return False
        #checking for 'X' and '@' at the current position to break the loop, as wall or you are present in that direction which is valid
        if house_map[temporary_row][temporary_column] == 'X' or house_map[temporary_row][temporary_column] == '@':
            break

    # checking for pichu on upper side
    for i in range(row - 1, -1, -1):
        #checking for 'p' at the current position, if yes it returns False - as Pichu exist in that direction
        if house_map[i][col] == 'p':
            return False
        #checking for 'X' and '@' at the current position to break the loop, as wall or you are present in that direction which is valid
        if house_map[i][col] == 'X' or house_map[row][i] == '@':
            break

    # checking for pichu on diagonal bottom_left
    temporary_row, temporary_column = row, col
    while True:
        #adding a temporary row and column for traversing bottom left diagonal
        temporary_row += 1
        temporary_column -= 1
        if not ( temporary_row < len(house_map) and temporary_column >= 0 ):
            break
        #checking for 'p' at the current position, if yes it returns False - as Pichu exist in that direction
        if house_map[temporary_row][temporary_column] == 'p':
            return False
        #checking for 'X' and '@' at the current position to break the loop, as wall or you are present in that direction which is valid
        if house_map[temporary_row][temporary_column] == 'X' or house_map[temporary_row][temporary_column] == '@':
            break

    # checking for pichu at bottom side
    for i in range(row + 1, len(house_map)):
        #checking for 'p' at the current position, if yes it returns False - as Pichu exist in that direction
        if house_map[i][col] == 'p':
            return False
        #checking for 'X' and '@' at the current position to break the loop, as wall or you are present in that direction which is valid
        if house_map[i][col] == 'X' or house_map[row][i] == '@':
            break

    # checking for pichu on diagonal bottom_right
    temporary_row, temporary_column = row, col
    while True:
        #adding a temporary row and column for traversing bottom right diagonal
        temporary_row += 1
        temporary_column += 1
        if not ( temporary_row < len(house_map) and temporary_column < len(house_map[0]) ):
            break
        #checking for 'p' at the current position, if yes it returns False - as Pichu exist in that direction
        if house_map[temporary_row][temporary_column] == 'p':
            return False
        #checking for 'X' and '@' at the current position to break the loop, as wall or you are present in that direction which is valid
        if house_map[temporary_row][temporary_column] == 'X' or house_map[temporary_row][temporary_column] == '@':
            break

    return True

# Count total # of pichus on house_map
def count_pichus(house_map):
    return sum([row.count('p') for row in house_map])

# Return a string with the house_map rendered in a human-pichuly format
def printable_house_map(house_map):
    return "\n".join(["".join(row) for row in house_map])

# Add a pichu to the house_map at the given position, and return a new house_map (doesn't change original)
def add_pichu(house_map, row, col):
    return house_map[0:row] + [house_map[row][0:col] + 
        ['p', ] + house_map[row][col + 1:]] + house_map[row + 1:]

# Get list of successors of given house_map state
def successors(house_map):
    return [add_pichu(house_map, r, c) for r in range(0, len(house_map)) 
        for c in range(0, len(house_map[0])) 
            if house_map[r][c] == '.' and check_pichu_position(house_map, r, c)]

# check if house_map is a goal state
def is_goal(house_map, k):
    return count_pichus(house_map) == k

# Arrange agents on the map
#
# This function MUST take two parameters as input -- the house map and the value k --
# and return a tuple of the form (new_house_map, success), where:
# - new_house_map is a new version of the map with k agents,
# - success is True if a solution was found, and False otherwise.
#
def solve(initial_house_map, k):
    fringe = [initial_house_map]
    while len(fringe) > 0:
        for new_house_map in successors(fringe.pop()):
            if is_goal(new_house_map, k):
                return (new_house_map, True)
            fringe.append(new_house_map)
    return False, ''

# Main Function
if __name__ == "__main__":
    house_map = parse_map(sys.argv[1])
    # number of agents passed in user input argument
    k = int(sys.argv[2])
    print("Starting from initial house map:\n" + printable_house_map(house_map) + "\n\nLooking for solution...\n")
    solution = solve(house_map, k)
    print("Here's what we found:")
    print(printable_house_map(solution[0]) if solution[1] else "False")