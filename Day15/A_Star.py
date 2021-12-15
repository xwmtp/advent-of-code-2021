class Node:

    def __init__(self, state=None, parent=None):
        self.parent = parent
        # state is for example x, y position
        self.state = state

        # g(n) cost from start node to n
        self.g = 0
        # h(n) heuristic that estimates cost of cheapest path from n to the goal
        self.h = 0
        # f(n) = g(n) + h(n) (find path that minimizes this)
        self.f = 0

    def __eq__(self, other):
        return self.state == other.state


class A_star:

    def __init__(self):
        self.open = []
        self.closed = []

    def search(self, start, end, search_object, return_path=True):
        """
        search_object has to implement:
        adjacents(state): all adjacent states of state
        neighbour_cost(state1, node2): the 'cost' from moving from state1 to state2. If no weights, it's always 1.
        heuristic(state): estimated distance from state to end. Should always underestimate real distance!
        """
        self.open = {}
        self.closed = {}

        start_node = Node(start, None)
        end_node = Node(end, None)

        self.open[start_node.state] = start_node

        while len(self.open) > 0:
            current_node = min(self.open.values(), key=lambda node: node.f)
            del self.open[current_node.state]

            if current_node.state in self.closed:
                continue
            self.closed[current_node.state] = current_node

            if current_node == end_node:
                if return_path:
                    return self.backtrack(current_node)
                else:
                    return current_node

            children = search_object.adjacents(current_node.state)
            for child in children:
                child_node = Node(child, current_node)

                if child_node.state in self.closed or (
                        (current_node.parent is not None) and (child_node == current_node.parent)):
                    continue

                child_node.g = current_node.g + search_object.neighbour_cost(child_node.state, current_node.state)
                child_node.h = search_object.heuristic(child_node.state, end_node.state)
                child_node.f = child_node.g + child_node.h

                if child_node.state not in self.open or child_node.g < self.open[child_node.state].g:
                    self.open[child_node.state] = child_node

    def backtrack(self, node):
        path = []
        current = node
        while current is not None:
            path.append(current.state)
            current = current.parent
        return path[::-1]
