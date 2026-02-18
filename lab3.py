"""This program computes the max value among a set of numbers."""

from typing import List
import argparse


def max_2(a: float, b: float) -> float:
    """Return the larger of a and b. If a and b are equal, return that value."""
    # Your implementation here
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return a


def max_list(x: List[float]) -> float:
    """Return the largest element in xs. If all elements are equal, return that value.

    Raises:
        ValueError: If x is empty.
    """
    # Your implementation here
    if not x:
        raise ValueError("List is empty")
    largest = x[0]
    for i in x:
        if i > largest:
            largest = i
    return largest


def max_variable(*args: float) -> float:
    """Return the largest value among a variable-length list of numbers.
    If all values are equal, return that value.

    Raises:
        ValueError: If no arguments are provided.
    """
    # Your implementation here
    if not args:
        raise ValueError("No arguments provided")
    return max_list(list(args))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Compute the max value among a set of numbers."
    )
    parser.add_argument("--a", type=float, help="First number for max_2 function.")
    parser.add_argument("--b", type=float, help="Second number for max_2 function.")
    parser.add_argument(
        "--list",
        nargs="+",
        type=float,
        help="A list of numbers to find the maximum value from.",
    )
    parser.add_argument(
        "--varargs",
        nargs="+",
        type=float,
        help="A variable-length list of numbers to find the maximum value from.",
    )
    args = parser.parse_args()

    # Your implementation here
    if args.a is not None and args.b is not None:
        print(f"max_2({args.a}, {args.b}) = {max_2(args.a, args.b)}")
    if args.list is not None:
        print(f"max_list({args.list}) = {max_list(args.list)}")
    if args.varargs is not None:
        print(f"max_variable({args.varargs}) = {max_variable(*args.varargs)}")