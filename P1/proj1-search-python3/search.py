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
    """
    "*** YOUR CODE HERE ***"
    # initialize fringe stack
    fringe = util.Stack()
    # initialize visited nodes set
    visited = set()

    # get start state
    start = problem.getStartState()
    # initial subpath is going to be empty
    path = []

    visited.add(start)
    
    # push first node to fringe stack
    fringe.push((start,path,visited))

    # loop through all fringe nodes
    while not fringe.isEmpty():
        state, path, visited = fringe.pop()
        # if we have reached the goal, return the path
        if problem.isGoalState(state):
            return path
        # all possible moves from the state of the current node
        successors = problem.getSuccessors(state)
        # add nodes to fringe stack if they do not revisit nodes
        for s in successors:
            tmp_state = s[0]
            move = s[1]
            if tmp_state not in visited:
                # make a copy of the visited nodes set and add the successor state
                tmp_visited = visited.copy()
                tmp_visited.add(tmp_state)
                fringe.push((tmp_state, path+[move],tmp_visited))
    return None

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # initialize fringe queue
    fringe = util.Queue()
    # initialize visited nodes set
    visited = set()

    # get start state
    start = problem.getStartState()
    # initial subpath is going to be empty
    path = []

    visited.add(start)
    
    # push first node to fringe stack
    fringe.push((start,path))

    while not fringe.isEmpty():
        state, path = fringe.pop()
        # if we have reached the goal, return the path
        if problem.isGoalState(state):
            return path
        # all possible moves from the state of the current node
        successors = problem.getSuccessors(state)
        # add nodes to fringe stack if they do not revisit nodes
        for s in successors:
            tmp_state = s[0]
            move = s[1]
            if tmp_state not in visited:
                # make a copy of the visited nodes set and add the successor state
                visited.add(tmp_state)
                fringe.push((tmp_state, path+[move]))
    return None

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    # initialize fringe priority queue
    fringe = util.PriorityQueue()
    # initialize visited nodes set
    visited = set()

    # get start state
    start = problem.getStartState()
    # initial subpath is going to be empty
    path = []
    # initial cost is 0
    cost = 0
    
    # push first node to fringe stack
    fringe.push((start,path,cost), cost)

    while not fringe.isEmpty():
        state, path, cost = fringe.pop()
        # if we have reached the goal, return the path
        if problem.isGoalState(state):
            return path
        elif state not in visited:
            visited.add(state)
            # all possible moves from the state of the current node
            successors = problem.getSuccessors(state)
            # add nodes to fringe stack if they do not revisit nodes
            for s in successors:
                tmp_state = s[0]
                move = s[1]
                tmp_cost = s[2]+cost
                if tmp_state not in visited:
                    fringe.push((tmp_state, path+[move],tmp_cost),tmp_cost)
    return None

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # initialize fringe priority queue
    fringe = util.PriorityQueue()
    # initialize visited nodes set
    visited = set()

    # get start state
    start = problem.getStartState()
    # initial subpath is going to be empty
    path = []
    # initial cost
    cost = heuristic(start,problem)
    
    # push first node to fringe stack
    fringe.push((start,path,cost), cost)

    while not fringe.isEmpty():
        state, path, cost = fringe.pop()
        # if we have reached the goal, return the path
        if problem.isGoalState(state):
            return path
        elif state not in visited:
            visited.add(state)
            # all possible moves from the state of the current node
            successors = problem.getSuccessors(state)
            # add nodes to fringe stack if they do not revisit nodes
            for s in successors:
                tmp_state = s[0]
                move = s[1]
                tmp_cost = s[2] + cost
                if tmp_state not in visited:
                    fringe.push((tmp_state, path+[move], tmp_cost),heuristic(tmp_state,problem)+tmp_cost)
    return None


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
