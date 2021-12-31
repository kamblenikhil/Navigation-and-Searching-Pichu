# Author : Nikhil Kamble
#
# Based on skeleton code provided in CSCI B551, Fall 2021.

import sys

# Parse the map from a given filename
def parse_map(filename):
        with open(filename, "r") as f:
                return [[char for char in line] for line in f.read().rstrip("\n").split("\n")][3:]
                
# Check if a row,col index pair is on the map
def valid_index(pos, n, m):
        return 0 <= pos[0] < n  and 0 <= pos[1] < m

# Find the possible moves from position (row, col)
def moves(map, row, col):
        moves=((row+1, col), (row-1, col), (row, col-1), (row, col+1))
        # Return only moves that are within the house_map and legal (i.e. go through open space ".")
        return [ move for move in moves if valid_index(move, len(map), len(map[0])) and (map[move[0]][move[1]] in ".@" )]

#to check the direction of next moving location and returning a String Value  (U for Up | D for Down | R for Right | L for Left)
def path(row, col, next):
        if(row>next[0] and col==next[1]):
                return "U"
        if(row<next[0] and col==next[1]):
                return "D"
        if(row==next[0] and col<next[1]):
                return "R"
        if(row==next[0] and col>next[1]):
                return "L"

# Perform search on the map
# 
# This function MUST take a single parameter as input -- the house map --
# and return a tuple of the form (move_count, move_string), where:
# - move_count is the number of moves required to navigate from start to finish, or -1
#    if no such route exists
# - move_string is a string indicating the path, consisting of U, L, R, and D characters
#    (for up, left, right, and down)

def search(house_map):
        # Find pichu start position
        pichu_loc=[(row_i,col_i) for col_i in range(len(house_map[0])) for row_i in range(len(house_map)) if house_map[row_i][col_i]=="p"][0]
        fringe=[(pichu_loc, 0, "")]
        #to store the location of the visited location of pichu
        visited_location_of_pichu  = []

        while fringe:
                (curr_move, curr_dist, optimal_path) = fringe.pop()
                for move in moves(house_map, *curr_move):
                        #to store the location of the next node to be visited (temporary attribute)
                        next_visiting_node = (move[0], move[1])
                        if house_map[move[0]][move[1]]=="@":
                                return (curr_dist + 1, optimal_path + str(path(curr_move[0], curr_move[1], next_visiting_node)))
                        #to check if the next location is in the visited location list
                        if next_visiting_node not in visited_location_of_pichu:
                                visited_location_of_pichu.append(next_visiting_node)
                                fringe.append((next_visiting_node, curr_dist + 1, optimal_path + str(path(curr_move[0], curr_move[1], next_visiting_node)) ) )
        return -1,""

# Main Function
if __name__ == "__main__":
        house_map = parse_map(sys.argv[1])
        #print(house_map)
        print("Shhhh... quiet while I navigate!")
        solution = search(house_map)
        print("Here's the solution I found:")
        # print(str(solution[0]), " ", )
        print(str(solution[0]), " ", str(solution[1]))