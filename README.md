# The Torchbearer

**Student Name:** Malaika Joiner
**Student ID:** 130036319
**Course:** CS 460 – Algorithms | Spring 2026

---

## Part 1: Problem Analysis

- Even if you know the shortest path from S to each individual relic chamber, 
  it cannot decide the order you need to go in order to reach each relic and end up at T.

- We need to calculate the optimal order to visit each relic chamber.

- We must find the minimum of the overall path/orders because they may differ in cost.

---

## Part 2: Precomputation Design

### Part 2a: Source Selection

| Source Node Type | Why it is a source |
|---|---|
| Start Node | The first move will be from the start node. |
| Relic Chamber Node | After visiting a relic chamber, the next move will be from that chamber |

### Part 2b: Distance Storage

| Property | Your answer |
|---|---|
| Data structure name | HashMap |
| What the keys represent | ordered pairs of 2 nodes |
| What the values represent | shortest distance between starting node to destination node |
| Lookup time complexity | O(1) |
| Why O(1) lookup is possible | hashmap search functions are O(1) if keys are all different |

### Part 2c: Precomputation Complexity

- Dijkstra runs n+1 times
- Each run costs O((V+E)log V)
- Do a run of dijkstras on each source node (S and relic chambers)
- The total cost is O((n+1)((V+E)log V))

---

## Part 3: Algorithm Correctness

- Uses greedy logic to assume that the smallest path is optimal.
- In the case that all distances are nonnegative, once a shortest distance is found, a better path cannot be found later.

### Part 3a: What the Invariant Means

- For nodes already finalized, the distance is the finalized shortest path.

- For nodes not yet finalized, their distance is the shortest path discovered so far.

### Part 3b: Why Each Phase Holds

- Initialization : When starting at the start node, the distance from S to S is 0, which is the final shortest path. The other nodes havent been found yet, so their default shortest distance is the only one discovered, thus the shortest so far.

- Maintenance : All weights are nonnegative, so once a node is visited, there isnt a way to lower the distance, so the shortest path is final.

- Termination : At the end of the algorithm, when all nodes are finalized, all the finalized nodes will have their optimal shortest path recorded.

### Part 3c: Why This Matters for the Route Planner

Knowing the correct shortest paths from each node will help make the decison to create the optimal route from S, the relic chambers, and T.

---

## Part 4: Search Design

### Why Greedy Fails

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

### What the Algorithm Must Explore

The algorithm must explore how the order will affect the total cost.

---

## Part 5: State and Search Space

### Part 5a: State Representation

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | node | str | the current location can be Start or a relic chamber node named "S" or "R1" "R2" etc |
| Relics already collected | visited | set | set contains the names of the relic chamber nodes visited |
| Fuel cost so far | cost | int | amount of cost used to reach the current location |

### Part 5b: Data Structure for Visited Relics

| Property | Your answer |
|---|---|
| Data structure chosen | Hash set |
| Operation: check if relic already collected | Time complexity: O(1) |
| Operation: mark a relic as collected | Time complexity: O(1) |
| Operation: unmark a relic (backtrack) | Time complexity: O(1) |
| Why this structure fits | it makes accessing information about the relic chambers have an optimal time complexity. |

### Part 5c: Worst-Case Search Space

- The worst case is O(V*(2^k))
- You must explore possibilities of costs with all possibilities of orders and which nodes you have already visited.

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

- The current minimum paths to reach each state are tracked. 
- You use this information everytime you visit a state.
- If it already has a cheaper state, the algorithm will know to prune the new, less optimal paths.

### Part 6b: Lower Bound Estimation

- The current state holds the current node and the set of relics
- The lower bound should account the minimum cost needed to visit the relics and exit using the shortest distances found.
- Because it uses the shortest path, it cannot be more than the true remaining cost

### Part 6c: Pruning Correctness

- Pruning is safe because it will only get rid of routes that are guarenteed to lead to a worse solution.

---

## References

- Lecture notes from CS460.