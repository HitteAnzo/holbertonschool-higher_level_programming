# Python - More Classes and Objects

This repository contains Python projects focusing on advanced object-oriented programming (OOP) concepts, particularly working with classes and objects. Each project demonstrates different OOP features, including class attributes, instance methods, special methods, and the use of static and class methods, all implemented in a `Rectangle` class.

## Table of Contents

- [Requirements](#requirements)
- [Files](#files)
- [Usage](#usage)

## Requirements

- Python 3.x
- PEP 8 style guide

## Files

| Filename         | Description                                                                                     |
| ---------------- | ----------------------------------------------------------------------------------------------- |
| `0-rectangle.py`  | Defines an empty class `Rectangle`.                                                             |
| `1-rectangle.py`  | Defines a class `Rectangle` with private instance attributes `width` and `height`, with validation. |
| `2-rectangle.py`  | Adds public methods `area()` and `perimeter()` to calculate the rectangle's area and perimeter.  |
| `3-rectangle.py`  | Adds `__str__()` method to print the rectangle using the `#` character.                         |
| `4-rectangle.py`  | Adds `__repr__()` method to return a string representation of the rectangle for recreation.      |
| `5-rectangle.py`  | Adds `__del__()` method to print a message when an instance of `Rectangle` is deleted.          |
| `6-rectangle.py`  | Adds a public class attribute `number_of_instances` to track the number of instances created.    |
| `7-rectangle.py`  | Adds a public class attribute `print_symbol` to define the symbol used to print the rectangle.   |
| `8-rectangle.py`  | Adds a static method `bigger_or_equal()` to return the bigger rectangle based on area.           |
| `9-rectangle.py`  | Adds a class method `square()` to return a new `Rectangle` instance where `width` and `height` are equal. |

## Usage

To run the Python scripts, use:

```bash
$ python3 <filename>.py
```

Each file represents a different stage in building and extending the functionality of a 'Rectangle' class in Python. You can experiment with the provided files to understand how each enhancement contributes to the overall functionality of the class.