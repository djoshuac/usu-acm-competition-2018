# Problems for Spring 2018 ACM Code Competition

We're planning on having 20 questions to choose from, so write a lot of them!

Each problem should have:

- a description
- an estimated difficulty level
- 4 or more test cases
- a solution in at least C++, Python, and Java

Put each problem in a directory named with following conventions:

    snake_case_name-<difficulty level in minutes>

For example, `best_words-20` is a problem named "Best Words" that has a
difficulty of 20 minutes.

Each problem should have two subdirectories: `tests` and `solutions`

### `tests`

Store the inputs and outputs for each test case in `<PROBLEM>\tests\input` and
`<PROBLEM>\tests\output`

All the inputs for the problem should be stored in the `<PROBLEM>\tests\input` directory
following this format:

> inputXX.txt

*Where `X` is a digit from 0-9*

All the outputs for the problem should be stored in the `<PROBLEM>\tests\output` directory
following this format:

> outputXX.txt

*Where `XX` mirrors the respective input*

### `solutions`

We need sample solutions using at least C++, Python, and Java. This is to ensure that a
solution is possible using any of these standard programming languages. A person
who uses an unverified language does so at their own discretion.

This directory must have three subdirectories: `C++`, `Python`, and `Java`. Within
each, store the code for the solution. (Multiple solutions are encouraged! Especially
  if they follow different strategies. Thus name solution accordingly.)

--------------

### Running test cases

To run a test case on a solution, pipe the test case to the solution's
executable (TODO write a script that automates this for every test case):

C++

    cat tests/input/input00.txt | ./solutions/C++/solution

Python

    cat input00.txt | python solutions/Python/solution.py

Java

    cat input00.txt | java ./solutions/Java/Solution

----------------

### Difficulty Scale

We want a wide variety of problems. There should be enough easy problems that
CS1 students will be able to have a good time. There should be enough medium
difficulty problems that CS3 students have a good time. There should be enough
hard problems, so that people who deeply invest themselves have a good time.

Gauge the difficulty of problems in the estimated number of minutes that
it would take **one person** to solve the question. For example:

> If a problem takes one person 25 minutes, it has a difficulty of 25

Time Estimates should be made under the assumption that a post-CS3 Student is
attempting the problem.

_NOTE: We need to make sure that we don't overestimate or underestimate difficulty_
