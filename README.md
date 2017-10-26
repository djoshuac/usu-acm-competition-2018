# Problems for Spring 2018 ACM Code Competition

We're planning on having 20 questions to choose from, so write a lot of them!

Each problem should have:

- a description
- an estimated difficulty level
- 4-6 test cases
- a solution in at least C++, Python, and Java

Put each problem in it's own directory named with following conventions:

    snake_case_name-<difficulty level in minutes>

For example, `best_words-20` is a problem named "Best Words" that has a
difficulty of 20 minutes.

### Test cases format (for Hackerrank zip upload)

Test cases for each problem should be stored in a subdirectory called `tests`.
Within that subdirectory there should be two folders `input` and `output`.

All the inputs for each test cases should be stored in the `input` directory
following this format:

> inputXX.txt

*Where `X` is a digit from 0-9*

All the outputs for each test cases should be stored in the `output` directory
following this format:

> outputXX.txt

*Where `XX` mirrors the respective input*

--------------

### Running test cases

To run a test case on a solution, pipe the test case to the solution's
executable (TODO write a script that automates this for every test case):

C++

    cat input00.txt | ./solution

Python

    cat input00.txt | python solution.py

Java

    cat input00.txt | java Solution

----------------

### Difficulty Scale

We want a wide variety of problems. There should be enough easy problems that
CS1 students will be able to have a good time. There should be enough medium
difficulty problems that CS3 students have a good time. There should be enough
hard problems, so that people who actually invest themselves have a good time.

Gauge the difficulty of problems in the estimated number of minutes that
it would take **one person** to solve the question. For example:

> If a problem takes one person 25 minutes, it has a difficulty of 25

Time Estimates should be made under the assumption that a CS3 Student is attempting the problem.

_NOTE: We need to make sure we don't overestimate or underestimate difficulty_
