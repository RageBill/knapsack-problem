# Knapsack Problem
In this project, we particularly talk about "0-1 Knapsack Problem".

You can read more about the problem in [here](https://en.wikipedia.org/wiki/Knapsack_problem).

# Datasets
Datasets p01 - p08 are taken from [here](https://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/knapsack_01.html).

The suggested solutions are exact in the above datasets.

Datasets c08 - c11 are credited from another similar project on Github [here](https://github.com/andresakata/0-1-knapsack).

Some suggested solutions may not be optimal in the above datasets.

# Solutions
In this project, 3 different ways of solving the problem are demonstrated.

Solution 1 is the simplest, yet slowest brute-force method using recursion.

Solution 2 is the most widely-used dynamic programming solution. This provides an exact optimal solution to the problem.

However, when number of items go beyond a certain number, or an extra constraint is added, it will easily time out.

Solution 3 is the main method we want to demonstrate here - using genetic algorithm. It is a very simplified implementation to demonstrate how simple and powerful it can be in solving such problems.
