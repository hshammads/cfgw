import sys
from collections import deque

# Node class from aimacode
class Node:
    """A node in a search tree. Contains a pointer to the parent (the node
    that this is a successor of) and to the actual state for this node. Note
    that if a state is arrived at by two paths, then there are two nodes with
    the same state. Also includes the action that got us to this state, and
    the total path_cost (also known as g) to reach the node. Other functions
    may add an f and h value; see best_first_graph_search and astar_search for
    an explanation of how the f and h values are handled. You will not need to
    subclass this class."""

    def __init__(self, state, parent=None, action=None, path_cost=0):
        """Create a search tree Node, derived from a parent by an action."""
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def __repr__(self):
        return "<Node {}>".format(self.state)

    def __lt__(self, node):
        return self.state < node.state

    def expand(self, problem):
        """List the nodes reachable in one step from this node."""
        return [self.child_node(problem, action)
                for action in problem.actions(self.state)]

    def child_node(self, problem, action):
        """[Figure 3.10]"""
        next_state = problem.result(self.state, action)
        next_node = Node(next_state, self, action, problem.path_cost(self.path_cost, self.state, action, next_state))
        return next_node

    def solution(self):
        """Return the sequence of actions to go from the root to this node."""
        return [node.action for node in self.path()[1:]]

    def path(self):
        """Return a list of nodes forming the path from the root to this node."""
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))

    # We want for a queue of nodes in breadth_first_graph_search or
    # astar_search to have no duplicated states, so we treat nodes
    # with the same state as equal. [Problem: this may not be what you
    # want in other contexts.]

    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state

    def __hash__(self):
        # We use the hash value of the state
        # stored in the node instead of the node
        # object itself to quickly search a node
        # with the same state in a Hash Table
        return hash(self.state)

# search functions from aimacode
def depth_first_graph_search(problem):
    frontier = [(Node(problem.initial))]  # Stack

    explored = set()
    while frontier:
        node = frontier.pop()
        if problem.goal_test(node.state):
            return node
        explored.add(node.state)
        frontier.extend(child for child in node.expand(problem)
                        if child.state not in explored and child not in frontier)
    return None

def breadth_first_graph_search(problem):
    node = Node(problem.initial)
    if problem.goal_test(node.state):
        return node
    frontier = deque([node])
    explored = set()
    while frontier:
        node = frontier.popleft()
        explored.add(node.state)
        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                if problem.goal_test(child.state):
                    return child
                frontier.append(child)
    return None

class WolfGoatCabbage:
    """ The problem of wolf goat cabbage will be treated as if we are focusing on the left bank.
    We don't have to worry about what the state of the right bank is, since we can always deduce from the status of left bank.
    At any given point, the max state size would be 4. If size of state is 0, we have reached goal state.
    A state is represented as a tuple of max length 4, with a combination of w, g, c, f.
    w - represents wolf, g - represents goat, c - represents cabbage, and f - represents farmer """

    # we plan to be inputting single characters, so let's have a mapping
    names = {'F': "Farmer",
             'W': "Wolf",
             'G': "Goat",
             'C': "Cabbage"}

    # define goal state and initialize problem
    def __init__(self, initial = frozenset({'F','W','G','C'}), goal = set()):
        """ Define goal state and initialize a problem """
        self.initial = initial
        self.goal = goal

    # check whether we have reached the goal state
    def goal_test(self, state):
        return state == self.goal

    # cost of solution path at state2 from state1, with cost c up to state1
    def path_cost(self, c, state1, action, state2):
        return c + 1

    # let's create a function that tells us whether the symbol is in our current state or not
    #   -> this will get used to calculate safe_state (the following function)
    def in_current_state(self, who, state):
        if who in state:
            return True
        else:
            return False

    # Given state and action, return a new state that is the result of the action.
    # Action is assumed to be a valid action in the state
    # figure out whether we need to add action or remove depending on where the farmer is
    def result(self, state, action):
        next_state = set()
        for i in state:
            next_state.add(i)

        for act in action:
            if act not in state:
                next_state.add(act)
            else:
                next_state.remove(act)
        return frozenset(next_state)

    # get list of possible actions at every state
    def actions(self, state):
        """ Return the actions that can be executed in the given state.
        Farmer has to move no matter what, and at most one other spot can move with the farmer
            that is, farmer must be one of the possible actions
        The remaining actions that can be executed; either of wolf, goat, cabbage moves
        The result would a list of possible actions """

        possible_actions = []
        elements_in_state = len(state)
        farmer_in_current_state = self.in_current_state('F', state)

        if elements_in_state % 2 == 0:
            if farmer_in_current_state:
                possible_actions = [{'F','G'}]
            else:
                possible_actions = [{'F'}]
        elif elements_in_state == 1:
            if state == {'G'}:
                possible_actions = [{'F'}]
            else:
                possible_actions = [{'F', 'G'}]
        elif elements_in_state % 3 == 0:
            possible_actions = [{'C', 'F'}, {'W', 'F'}]
        return possible_actions


if __name__ == '__main__':
    wgc = WolfGoatCabbage()
    solution = depth_first_graph_search(wgc).solution()
    print("Solution from depth first graph search: ", solution)
    solution = breadth_first_graph_search(wgc).solution()
    print("Solution from breadth first graph search: ", solution)
