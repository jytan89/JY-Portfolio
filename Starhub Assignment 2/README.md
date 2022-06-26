# Assignment 2

### Packages needed:
1) unittest
2) json

If you do not have these packages, install them by running this lines in your Terminal/Command Line:

```bash
pip install 'PackageName'
```

with 'PackageName' being the names of the above packages.

### Instructions:
1) Download **solution.py** and **solution_tests.py** onto your local directory/folder.
2) Open your Terminal/Command Line.
3) Navigate/change directory to the directory where the Python files (**solution.py** and **solution_tests.py**) are located.
4) To run the actual function itself, enter the following line in your Terminal/Command Line:

```bash
python solution.py
```
- run it a few times to input different kinds of values into the function and check the output

4) To run the unit test script, enter the following line in your Terminal/Command Line:

```bash
python solution_tests.py
```

- 2 unit tests would be run:
    - One is to check on the ouput from inputting value = 127 into the function.
    - The other is to check on exception handling for erroneous input values, such as non-integer types, or integers <= 1.
    
Both tests should return "OK" results.