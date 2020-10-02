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

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    action_stack = util.Stack()
    visited = []
    action_stack.push((problem.getStartState(),[]))
    while ( not action_stack.isEmpty()):
        popInfo = action_stack.pop()
        state = popInfo[0]
        visited.append(state)
        if (problem.isGoalState(state)):
            return popInfo[1]
            break
        for next in problem.getSuccessors(state):
            new_state = next[0]
            if not visited.count(new_state):
                action_stack.push((next[0],popInfo[1]+[next[1]]))
    return None

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    action_queue = util.Queue()
    visited = []
    action_queue.push((problem.getStartState(),[]))

    (state,direction) = action_queue.pop()

    visited.append(state)

    while not problem.isGoalState(state): 
        for next in problem.getSuccessors(state):
            if not next[0] in visited: 
                action_queue.push((next[0],direction + [next[1]])) 
                visited.append(next[0]) 
        (state,direction) = action_queue.pop()

    return direction

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    action_queue = util.PriorityQueue()
    visited = [(problem.getStartState(),0)]
    action_queue.push((problem.getStartState(),[],0),0)
    while ( not action_queue.isEmpty()):
        popInfo = action_queue.pop()
        if (problem.isGoalState(popInfo[0])):
            return popInfo[1]
            break
        for next in problem.getSuccessors(popInfo[0]):
            origin = False
            cost = popInfo[2] + next[2]
            for (old_pos,old_cost) in visited:
                if (next[0] == old_pos) and (cost >= old_cost): 
                    origin = True 
                    break

            if not origin:        
                action_queue.push((next[0],popInfo[1] + [next[1]],popInfo[2] + next[2]),popInfo[2] + next[2]) 
                visited.append((next[0],popInfo[2] + next[2])) 
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
    action_queue = util.PriorityQueue()
    visited = [(problem.getStartState(),0)]
    action_queue.push((problem.getStartState(),[],0),0 + heuristic(problem.getStartState(),problem))
    while ( not action_queue.isEmpty()):
        popInfo = action_queue.pop()
        state = popInfo[0]
        direction = popInfo[1]
        step = popInfo[2]
        if (problem.isGoalState(state)):
            break
        for next in problem.getSuccessors(state):
            origin = False
            cost = step + next[2]
            for (old_state,old_cost) in visited:
                if (next[0] == old_state) and (cost >= old_cost): 
                    origin = True 
                    break
            if not origin:        
                action_queue.push((next[0],direction + [next[1]],step + next[2]),step + next[2] + heuristic(next[0],problem)) 
                visited.append((next[0],step + next[2])) 
    return direction
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
