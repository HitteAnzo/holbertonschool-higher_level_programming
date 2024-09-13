#!/usr/bin/python3
"""
This module defines the function text_indentation.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines.
    After each of these characters: '.', '?' and ':'.
    Args:
        text (str): The text to be processed.
    Raises:
        TypeError: If the text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.strip()

    result = ""
    skip_space = False

    for char in text:
        if skip_space and char == ' ':
            continue

        result += char
        skip_space = False

        if char in ".?:":
            result += "\n\n"
            skip_space = True

    print(result.strip(), end="")
