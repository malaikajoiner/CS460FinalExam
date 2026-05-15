# Development Log – The Torchbearer

**Student Name:** Malaika Joiner
**Student ID:** 130036319

---

## Entry 1 – [5-12-26]: Initial Plan

I first answered the problem analysis, design, and correctness questions to understand why and how we are making an algorithm to decide the order to reach relic chambers. I will probably implement the dijkstras algortithm first. The hardest part might be figuring out how to calculate the proper order. I will test using the testing function given in the assignment.

---

## Entry 2 – [5-14-26]: [Short description]

I added the code for part 1 and 2, the implementation of dijkstras and the function to make it run on all the sources. Also added the string returns for part 3 and 4.

---

## Entry 3 – [5-14-26]: [Short description]

Changed precompute distances and implemented the remainging parts. Also changed variable names from README to have more understandable names.

I ran into a bug where I accidentally used the same variable name for the distance table and the shortest distance, which created errors. Similarly, my run dijkstras algorithm accidently returned the distance variable instead of the distance table. I solved that by renaming them different things. I also made the mistake of editing a list while looping through the for each, so instead I changed the design to create a new copy list.

---

## Entry 4 – [5-14-25]: Post-Implementation Reflection

If i were to improve my already written code, I think there should be a way to possibly prevent the need of recomputing similar subproblems if the algorithm can remember the already calculated routes and use it for the larger problems.

---

## Final Entry – [5-14-25]: Time Estimate

| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis | 3 min |
| Part 2: Precomputation Design | 20 min |
| Part 3: Algorithm Correctness | 10 min |
| Part 4: Search Design | 10 min |
| Part 5: State and Search Space | 10 min |
| Part 6: Pruning | 10 min |
| Part 7: Implementation | 5 hours |
| README and DEVLOG writing | 1.5 hour |
| **Total** | 8 hours |
