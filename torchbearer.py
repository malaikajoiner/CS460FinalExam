"""
CS 460 – Algorithms: Final Programming Assignment
The Torchbearer

Student Name: Malaika Joiner
Student ID:   130036319

INSTRUCTIONS
------------
- Implement every function marked TODO.
- Do not change any function signature.
- Do not remove or rename required functions.
- You may add helper functions.
- Variable names in your code must match what you define in README Part 5a.
- The pruning safety comment inside _explore() is graded. Do not skip it.

Submit this file as: torchbearer.py
"""

import heapq


# =============================================================================
# PART 1
# =============================================================================

def explain_problem():
    """
    Returns
    -------
    str
        Your Part 1 README answers, written as a string.
        Must match what you wrote in README Part 1.

    TODO
    """
    str = """
            - Even if you know the shortest path from S to each individual relic chamber, 
            it cannot decide the order you need to go in order to reach each relic and end up at T.

            - We need to calculate the optimal order to visit each relic chamber.

            - We must find the minimum of the overall path/orders because they may differ in cost.
          """
    
    return str


# =============================================================================
# PART 2
# =============================================================================

def select_sources(spawn, relics, exit_node):
    """
    Parameters
    ----------
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    list[node]
        No duplicates. Order does not matter.

    TODO
    """
    sources = set()
    sources.add(spawn)
    sources.add(exit_node)

    for relic in relics:
        sources.add(relic)

    return list(sources)


def run_dijkstra(graph, source):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
        graph[u] = [(v, cost), ...]. All costs are nonnegative integers.
    source : node

    Returns
    -------
    dict[node, float]
        Minimum cost from source to every node in graph.
        Unreachable nodes map to float('inf').

    TODO
    """

    V = len(graph)
    Pqueue = []
    dist = {}
    for node in graph:
        dist[node]= float('inf')
    dist[source] = 0
    heapq.heappush(Pqueue, (0, source))

    while Pqueue:
        d, u = heapq.heappop(Pqueue)

        if d > dist[u]:
            continue

        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u]+w
                heapq.heappush(Pqueue, (dist[v], v))

    return dist


def precompute_distances(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    dict[node, dict[node, float]]
        Nested structure supporting dist_table[u][v] lookups
        for every source u your design requires.

    TODO
    """

    sources = select_sources(spawn, relics, exit_node)

    dist_table = {}

    for source in sources:
        distances = run_dijkstra(graph, source)

        for node in distances:
            d = distances[node]
            dist_table[(source, node)] = d
    
    return dist_table


# =============================================================================
# PART 3
# =============================================================================

def dijkstra_invariant_check():
    """
    Returns
    -------
    str
        Your Part 3 README answers, written as a string.
        Must match what you wrote in README Part 3.

    TODO
    """
    str = '''

        - Uses greedy logic to assume that the smallest path is optimal.
        - In the case that all distances are nonnegative, once a shortest distance is found, a better path cannot be found later.


        - For nodes already finalized, the distance is the finalized shortest path.

        - For nodes not yet finalized, their distance is the shortest path discovered so far.


        - Initialization : When starting at the start node, the distance from S to S is 0, which is the final shortest path. The other nodes havent been found yet, so their default shortest distance is the only one discovered, thus the shortest so far.

        - Maintenance : All weights are nonnegative, so once a node is visited, there isnt a way to lower the distance, so the shortest path is final.

        - Termination : At the end of the algorithm, when all nodes are finalized, all the finalized nodes will have their optimal shortest path recorded.


        Knowing the correct shortest paths from each node will help make the decison to create the optimal route from S, the relic chambers, and T.

        '''
    return str


# =============================================================================
# PART 4
# =============================================================================

def explain_search():
    """
    Returns
    -------
    str
        Your Part 4 README answers, written as a string.
        Must match what you wrote in README Part 4.

    TODO
    """

    str = '''
            - The failure is being unable to find a better path that chooses different orders.

            - Counter example: 

            | From \ To | B   | C   | D   | T   |
            |-----------|-----|-----|-----|-----|
            | S         | 1   | 2   | 2   | --  |
            | B         | --  | 100 | 100 | 1   |
            | C         | 1   | --  | 1   | 1   |
            | D         | 1   | 1   | --  | 1   |

            Route 1 -  S > B > C > D > T = 1 + 100 + 1 + 1 = 103
            Route 2 - S > D > C > B > T = 2 + 1 + 1 + 1 = 5

            - Greedy will choose to visit B first and end up in a route like route 1, but optimal is route like route 2.
            - Greedy loses because it just picks the current best option and cannot analyze future options.

            The algorithm must explore how the order will affect the total cost.

        '''
    return str


# =============================================================================
# PARTS 5 + 6
# =============================================================================

def find_optimal_route(dist_table, spawn, relics, exit_node):
    """
    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
        Output of precompute_distances.
    spawn : node
    relics : list[node]
        Every node in this list must be visited at least once.
    exit_node : node
        The route must end here.

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    currBest = [float("inf"), []]

    _explore(dist_table, spawn, relics, [], 0, exit_node, currBest)
    
    return (currBest[0],currBest[1])


def _explore(dist_table, current_loc, relics_remaining, relics_visited_order,
             cost_so_far, exit_node, best):
    """
    Recursive helper for find_optimal_route.

    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
    current_loc : node
    relics_remaining : collection
        Your chosen data structure from README Part 5b.
    relics_visited_order : list[node]
    cost_so_far : float
    exit_node : node
    best : list
        Mutable container for the best solution found so far.

    Returns
    -------
    None
        Updates best in place.

    TODO
    Implement: base case, pruning, recursive case, backtracking.

    REQUIRED: Add a 1-2 sentence comment near your pruning condition
    explaining why it is safe (cannot skip the optimal solution).
    This comment is graded.
    """

    # pruning: costs will only increase/stay the same in the future
    #          so once it is >= best, it is impossible to be more optimal than the current best.
    if cost_so_far >= best[0]:
        return
    
    if not relics_remaining:
        exit = dist_table[(current_loc),(exit_node)]

        if exit == float("inf"):
            return
        
        total = cost_so_far + exit
        if total < best[0]:
            best[0] = total
            best[1] = relics_visited_order[:]
        return
    
    for relic in relics_remaining:
        d = dist_table[(current_loc),(relic)]
        if d == float("inf"):
            continue
        new_remaining = relics_remaining[:]
        new_remaining.remove(relic)
        relics_visited_order.append(relic)

        _explore(dist_table, relic, new_remaining, relics_visited_order, (cost_so_far+d) , exit_node, best)
        relics_visited_order.pop()
        new_remaining.append(relic)
# =============================================================================
# PIPELINE
# =============================================================================

def solve(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    dist_table = precompute_distances(graph, spawn, relics, exit_node)
    return find_optimal_route(dist_table, spawn, relics, exit_node)


# =============================================================================
# PROVIDED TESTS (do not modify)
# Graders will run additional tests beyond these.
# =============================================================================

def _run_tests():
    print("Running provided tests...")

    # Test 1: Spec illustration. Optimal cost = 4.
    graph_1 = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 1), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }
    cost, order = solve(graph_1, 'S', ['B', 'C', 'D'], 'T')
    assert cost == 4, f"Test 1 FAILED: expected 4, got {cost}"
    print(f"  Test 1 passed  cost={cost}  order={order}")

    # Test 2: Single relic. Optimal cost = 5.
    graph_2 = {
        'S': [('R', 3)],
        'R': [('T', 2)],
        'T': []
    }
    cost, order = solve(graph_2, 'S', ['R'], 'T')
    assert cost == 5, f"Test 2 FAILED: expected 5, got {cost}"
    print(f"  Test 2 passed  cost={cost}  order={order}")

    # Test 3: No valid path to exit. Must return (inf, []).
    graph_3 = {
        'S': [('R', 1)],
        'R': [],
        'T': []
    }
    cost, order = solve(graph_3, 'S', ['R'], 'T')
    assert cost == float('inf'), f"Test 3 FAILED: expected inf, got {cost}"
    print(f"  Test 3 passed  cost={cost}")

    # Test 4: Relics reachable only through intermediate rooms.
    # Optimal cost = 6.
    graph_4 = {
        'S': [('X', 1)],
        'X': [('R1', 2), ('R2', 5)],
        'R1': [('Y', 1)],
        'Y': [('R2', 1)],
        'R2': [('T', 1)],
        'T': []
    }
    cost, order = solve(graph_4, 'S', ['R1', 'R2'], 'T')
    assert cost == 6, f"Test 4 FAILED: expected 6, got {cost}"
    print(f"  Test 4 passed  cost={cost}  order={order}")

    # Test 5: Explanation functions must return non-placeholder strings.
    for fn in [explain_problem, dijkstra_invariant_check, explain_search]:
        result = fn()
        assert isinstance(result, str) and result != "TODO" and len(result) > 20, \
            f"Test 5 FAILED: {fn.__name__} returned placeholder or empty string"
    print("  Test 5 passed  explanation functions are non-empty")

    print("\nAll provided tests passed.")


if __name__ == "__main__":
    _run_tests()
