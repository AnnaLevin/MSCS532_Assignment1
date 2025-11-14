Quicksort Algorithm – Deterministic and Randomized Versions
Overview

This project contains two Python implementations of the Quicksort algorithm:

Deterministic Quicksort – uses the last element of the list as the pivot.
Randomized Quicksort – selects a pivot randomly to improve consistency and reduce the chance of worst-case performance.
This repository also includes a written report explaining the implementation, time complexity, and performance comparison.

##Files Included

assignment5_quicksort.py — contains both deterministic and randomized Quicksort implementations
assignment5_LevinskaiaAnna
README.md — summary and instructions

##How to Run the Program

Install Python 3
Open the project in PyCharm

##Run the script:
python quicksort.py

The program will display the sorted output using both Quicksort versions.

##Summary of Results:

Deterministic Quicksort works well on random input but performs poorly on sorted or reverse-sorted data because the pivot choice produces unbalanced partitions.
Randomized Quicksort performs more consistently because the randomly selected pivot avoids predictable worst-case behavior.
In practice, the randomized version stays close to O(n log n) for most input types.