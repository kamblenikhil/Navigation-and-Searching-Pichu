# Navigation and Searching

## Part 1: Navigation

### *Search Abstraction -* 

**Set of Valid States:** where the agent (pichu) can fly in open space '.' (cell of the house)

**The Successor Function:** this function gets a house-map in the form of a text file with the current agent's location (pichu) and returns the possible moves (in shortest path ie. optimal path) from the agent to us (@) with given constraints [like the wall (X)]

**The Cost Function:** The agent (pichu) can move one square cell at a time so we can consider it to be 1

**The Goal State:** A state where the agent (pichu) reaches to us [from p to @]

**The Initial State:** It is the starting point of the agent (pichu) given in the map (provided at runtime)

**Question -** Why does the program often fail to find a solution?
*Answer -* The skeleton code was stuck in an infinite loop because there was no track of visiting nodes by the agent. Therefore, the program was visiting the same number of nodes again and again.

To avoid the infinite loop and also to find the Goal State I implemented the following things and approaches in my way of understanding - 
1. By adding this list - 'visited_location_of_pichu', it keeps track of the visited location of the agent (pichu)
2. To find the path I added another function 'path()' which takes the current pichu location co-ordinates (row and column) and the next move location co-ordinates (row and column) as parameters. This function then checks the direction of next moving location and returns a String Value (U for Up | D for Down | R for Right | L for Left)
3. If the program finds a solution of the given map, it returns the number of possible optimal moves (example: 16) and the path in String format (example: UUURRDDDRRUURRDD)
4. If the program doesn't find a solution of the given map, it returns -1 (ie. no solution found)

==========================================================================

## Part 2: Hide-and-seek

### *Search Abstraction -* 

**State Space:** where the agent (pichu) can fly in open space '.' (cell of the house)

**Initial State:** It is the starting point of the agent (pichu) given in the map (provided at runtime)

**Goal State:** A state where, given number of agents (pichu) are successfully placed with respect to the constraints (ie. no two agents can see each other in the same row, same column and same diagonal)

**Successor Function:** this function gets a house-map in the form of a text file with the current agent's location (pichu) and checks the given number of agentss to be placed on the map with the given constraints (ie. no two agents can see each other in the same row, same column and same diagonal) and returns another map with the agents placed on the map if the solution exists.

**Cost Function:** The agent (pichu) can move one square cell at a time so we can consider it to be 1

### Things to Assume - 

1. If there is a wall 'X' or you '@' in the middle of two agent's, then the position of those two agent's is correct
2. If there is no wall 'X' or you '@' in the middle of two agent's (ie. in same row or same column or same diagonal), then those two positions are invalid and the other agent's position needs to be changed to next node '.'

### Working of the Code and Conditions - 

1. Unlike the previous Task 1 code, this existing skeleton code doesn't go in an infinite loop. But, after certain possible nodes '.' (which are limited as per the given map) the program will go in an infinite loop. For example: k agents are given to be placed on the map and the number of nodes '.' are less than k agents.
2. To fix the first issue, we simply need to put a condition where the program returns False after no solution is found.
3. The successors() is calling add_pichu() to add the agent in the given house-map and also I have added another condition/function check_pichu_position() to check the pichu position and the directions to validate if two agent's (pichu) are not looking at each other.
4. For checking the directions FROM [UP, DOWN, LEFT, RIGHT, UPPER LEFT, UPPER RIGHT, BOTTOM LEFT, BOTTOM RIGHT] it checks for the Agent's location (pichu) in all those given direction.
5. While looking at those directions for Agent (pichu) it also checks for the wall 'X' and you '@' to break the condition and return True as it is a valid position to add the Agent (Pichu)
#### _[Output for 1 Agent is False as the solution already exists in the given map with one agent placed in it.]_
#### _[Output will be False if there is no Solution for the given map and given number of Agent's to be placed in that map]_

==========================================================================

__[ I have discussed the logic of this code with one of my friend Rushikesh (rpharate). We basically discussed what would be the range and movement to check the pichu position in each direction. for example - to check the pichu in the upper right direction, we traverse the row-1 and column+, so on and so forth. ]__