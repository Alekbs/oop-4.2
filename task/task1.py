#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Pair:
    def __init__(self, first, second):
        if not isinstance(first, float) or not isinstance(second, float):
            raise ValueError("Both 'first' and 'second' should be numbers")
        self.first = first
        self.second = second

    def __pow__(self, other):
        if isinstance(other, Pair):
            return Pair(self.first**other.first, self.second**other.second)
        else:
            raise ValueError("Illegal type of the argument")

    def __str__(self):
        return f"Pair: first = {self.first}, second = {self.second}, result = {self.first**self.second}"

    @classmethod
    def read(cls):
        try:
            first = float(input("Enter the first number: "))
            second = float(input("Enter the second number: "))
            return cls(first, second)
        except ValueError:
            print("Invalid input")
            return None


if __name__ == "__main__":
    pair = Pair.read()
    print(pair)
    pair1 = Pair(3.0, 4.0)
    pair2 = pair**pair1
    print(pair2)
