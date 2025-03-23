
Student Information
--
Paulina Velásquez Londoño
Mariamny Del Valle Ramírez Telles
Class Number: 7309

System and Tools Used
--
Operating System: Any system supporting Python 3

Programming Language: Python 3.x

Development Environment: PyCharm, VS Code, or any Python-compatible IDE

Running the Implementation
--
Prerequisites

Ensure you have Python 3 installed on your system. You can check your Python version with:

Execution Steps
--
Clone this repository or download the files.

Open a terminal or command prompt and navigate to the project directory.

Run the programn in the main

Expected Output
--
The program generates valid and invalid palindrome strings.

It evaluates them using a Pushdown Automaton (PDA) and displays whether each string is accepted or rejected.

It provides a step-by-step breakdown of valid palindrome processing.

![image](https://github.com/user-attachments/assets/f6675c05-a6ad-4a77-8b11-522398c9cef3)

![image](https://github.com/user-attachments/assets/ef962686-1ce2-4ca5-9344-9ca22c6e0cdb)

Code Explanation
--
Algorithm 1: Generating Strings

ALGORITHM_1_LFCO_PVMR.py generates random valid palindromes and invalid strings.

A valid string follows the palindrome structure (reads the same forward and backward).

An invalid string is randomly generated to ensure it does not form a palindrome.

Algorithm 2: Pushdown Automaton (PDA) Validation

ALGORITHM_2_LFCO_PVMR.py implements a PDA to check if a given string is a palindrome.

The PDA pushes the first half of the string onto a stack and then verifies the second half against it.

If all characters match, the string is accepted; otherwise, it is rejected.

Algorithm 3: PDA Configuration Steps

ALGORITHM_3_LFCO_PVMR.py shows step-by-step PDA configurations for valid strings.

It details stack operations and transitions during palindrome validation.






[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/gjhNPQOm)
