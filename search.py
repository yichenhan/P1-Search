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
    """
    s = util.Stack() #Stack
    s.push((problem.getStartState(), [])) #Start node of the stack to store dfs nodes, has path in second index
    v = set() #Visited set

    while not s.isEmpty(): #While not empty, iterate graph dfs
        cur = s.pop() #Current node being visited
        if cur[0] in v: continue #If already visited, continue to next
        v.add(cur[0]) #Add to visited

        if problem.isGoalState(cur[0]): return cur[1] #If current visited is goal state, return path 

        successors = problem.getSuccessors(cur[0]) #Gets the successors of the current visited dfs node
        for nodes in successors: #Iteratively add next nodes in successors to the stack
            if nodes[0] in v: continue
            moveset = list(cur[1])
            moveset.append(nodes[1])
            s.push((nodes[0], moveset))
            
    return None


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    s = util.Queue() #Queue
    s.push((problem.getStartState(), [])) #Start node 
    v = set() #Visited set

    while not s.isEmpty(): #While not empty, iterate graph dfs
        cur = s.pop() #Current node being visited
        if cur[0] in v: continue #If already visited, continue to next
        v.add(cur[0]) #Add to visited

        if problem.isGoalState(cur[0]): return cur[1] #If current visited is goal state, return path 

        successors = problem.getSuccessors(cur[0]) #Gets the successors of the current visited dfs node
        for nodes in successors: #Iteratively add next nodes in successors to the stack
            if nodes[0] in v: continue
            moveset = list(cur[1])
            moveset.append(nodes[1])
            s.push((nodes[0], moveset))
            
    return None
    util.raiseNotDefined()
    util.raiseNotDefined()

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
