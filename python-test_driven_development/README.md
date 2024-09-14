<<<<<<< HEAD
empty
=======
# Python - Test-Driven Development (TDD)

This repository contains projects related to Python Test-Driven Development (TDD). Each project demonstrates the use of TDD methodology to write tests before implementing functions, ensuring correctness and robustness of the code.

## Table of Contents

- [Requirements](#requirements)
- [Files](#files)
- [Usage](#usage)

## Requirements

- Python 3.x
- `unittest` module
- PEP 8 style guide
- doctest module for documentation testing

## Files

| Filename | Description |
| -------- | ----------- |
| `0-add_integer.py` | A function that adds two integers. |
| `2-matrix_divided.py` | Divides all elements of a matrix by a number. |
| `3-say_my_name.py` | Prints a name in the format "My name is <first name> <last name>". |
| `4-print_square.py` | Prints a square of `#` characters of a given size. |
| `5-text_indentation.py` | Adds two new lines after each of these characters: `.`, `?`, and `:`. |
| `6-max_integer.py` | Finds and returns the maximum integer in a list. |
| `tests/` | Directory containing unit tests for each function. |

## Usage

To test the files, use the following command:

```bash
$ python3 -m unittest discover tests
```
To run doctests (embedded tests in the docstrings):

```bash
$ python3 -m doctest <filename>.py
```
>>>>>>> c53ba0dc31b078667e722636ede4ea1ffddeda45
