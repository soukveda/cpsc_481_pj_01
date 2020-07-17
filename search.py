# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))

     psuedocode:
    begin
        open:=[start]
        closed:=[]
        while open != [] do
            begin
                remove leftmost state from open, call it X
                if X is a goal then return SUCCESS
                    else begin
                        generate children of X
                        put X on closed
                        discard children of X if already on open or closed
                        put remaining children on left end of open
                        end
        end
    return FAIL
    end
    """
    "*** YOUR CODE HERE ***"
    # print("Start:", problem.getStartState())
    # print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    # print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    # children = [problem.getSuccessors(problem.getStartState())]
    # for child in children:
    #     print(child[0][0])

    op = util.Stack()                                 # initialize the open stack
    startState = problem.getStartState()              # save the start state
    op.push((startState, [], []))                     # push the start state into the open state

    while not op.isEmpty():                           # keep searching while there are states in the open stack
        (X, actions, closed) = op.pop()           # save the front state 

        if problem.isGoalState(X):                 # check to see if we have reached the goal state
            return route
        else:
            children = problem.getSuccessors(X)                                  # retrieve the children of the current state
            for successor, direction, cost in children:
                if not successor in closed:                                     # checks to see if children are in open/closed
                    op.push((successor, actions + [direction], closed + [X]))   
                route = actions + [direction]

    return route
    #util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
<<<<<<< HEAD
    """
    ALGORITHM: Breadth-First Search
    Step 1: Declare the queue 'op' and initialize it with the starting state of the search
    Step 2: Declare a list called closed and initialize it with an empty list
    Step 3: Condition statement: if the op queue is empty, jump to step 8. Otherwise, proceed to step 4
    Step 4: If a child state is not in closed, put the state in the closed queue
    Step 5: If the leftmost state is a goal, terminate the search and return actions. Otherwise proceed to next step.
    Step 6: Generate the children of the leftmost state and push them onto the op queue.
    Step 7: Return to step 4. 
    Step 8: Once there are no more open states, return empty list. 
    """

    op = util.Queue() # Declare the queue of open states
    start = problem.getStartState() # Declares the start state for the bfs
    op.push((start, [], []))  # Pushes the start state onto the op queue
    closed = [] # Initialize 
    

    while not op.isEmpty(): # Indicates the remaining states in 'op'
        
        (children, actions, current_cost) = op.pop()

        if not children in closed: 

            # Push children onto closed list
            closed.append(children)

            if problem.isGoalState(children): # Indicates if the leftmost state is a goal
                return actions

            for child, direction, cost in problem.getSuccessors(children):

                # Put any remaining children on the right end of the op queue
                op.push((child, actions + [direction], current_cost + [cost]))

    # Return empty list once no states are left
    return [] 

    # util.raiseNotDefined()
=======
    util.raiseNotDefined()
>>>>>>> andrew

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
