# Wodoku_AI_Agent
In this section, an AI agent was designed to solve the Wordoku puzzle game. The core technique to
focus on is the Constraint Satisfaction Problem (CSP). Implemented two methods to
solve the Wordoku puzzle and compare the implementations. Wordoku is an extension of Sudoku
where we have alphabets in place of digits. Some basics about the CSP approach for solving the same
are given below.
## Puzzle Background
The Wordoku puzzle has a 9x9 grid and a set of possible alphabets
with some of the positions filled with those alphabets to ensure a
solution can be reached. The goal is to find and fill remaining cells
with alphabets such that each row, column and the 3x3 square
(sub-grid) all must contain the alphabets, exactly once.
Note: There are exactly nine alphabets among which one of the
characters is needed to be filled in blank space.
Helping note:
## Solving Sudoku as Constraint Satisfaction Problems
A constraint satisfaction problem (CSP) consists of
● a set of variables,
● a domain for each variable, and
● a set of constraints.
The aim is to choose a value for each variable such that the resulting possible world satisfies

the constraints; we want a model of the constraints. The method in CSP should use the
constraint propagation approaches as the inference to reduce the domain of each variable
while using the Backtracking search with other suitable heuristics in order to find a
solution.
## Another approach 
 Local Search based method - The MIN_CONFLIT algorithm. You can consider improving the Local Search method by
incorporating Tabu Search.
