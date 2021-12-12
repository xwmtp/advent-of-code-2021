# https://adventofcode.com/2021/day/12

with open('input12.txt', 'r') as file:
    lines = file.read().splitlines()

cave_edges = [(line.split('-')[0], line.split('-')[1]) for line in lines]


class CaveSolver:

    def __init__(self, edges, allow_one_smol_cave_double_visit):
        self.edges = edges
        self.all_found_routes = []
        self.allow_one_smol_cave_double_visit = allow_one_smol_cave_double_visit

    def reset(self):
        self.all_found_routes = []

    def find_all_routes(self):
        self.reset()
        self.route_step('start', ['start'])

    def route_step(self, current_cave, current_route):
        for option in self.cave_options(current_cave):
            if option == 'end':
                self.all_found_routes.append(current_route.copy() + ['end'])
                continue
            if option == 'start':
                continue
            if is_smol_cave(option) and not self.smol_cave_allowed(option, current_route):
                continue
            self.route_step(option, current_route.copy() + [option])

    def cave_options(self, from_cave):
        options = set()
        for edge in self.edges:
            if edge[0] == from_cave:
                options.add(edge[1])
            if edge[1] == from_cave:
                options.add(edge[0])
        return options

    def smol_cave_allowed(self, smol_cave, route):
        if not smol_cave in route:
            return True
        if not self.allow_one_smol_cave_double_visit:
            return False
        smol_caves_in_route = [cave for cave in route if is_smol_cave(cave)]
        return len(smol_caves_in_route) == len(set(smol_caves_in_route))


def is_smol_cave(cave):
    return all(char.islower() for char in cave)


# --- Part 1 --- #
cave_solver = CaveSolver(cave_edges, False)
cave_solver.find_all_routes()
print(len(cave_solver.all_found_routes))

# --- Part 2 --- #
cave_solver = CaveSolver(cave_edges, True)
cave_solver.find_all_routes()
print(len(cave_solver.all_found_routes))
