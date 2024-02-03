#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Decimal:
    MAX_SIZE = 100  # Maximum size of the list

    def __init__(self, size):
        if size <= 0 or size > Decimal.MAX_SIZE:
            raise ValueError("Invalid size")
        self.size = size
        self.count = 0
        self.digits = [0] * size

    def __getitem__(self, index):
        if 0 <= index < self.size:
            return self.digits[index]
        else:
            raise IndexError("Index out of range")

    def __setitem__(self, index, value):
        if 0 <= index < self.size:
            if 0 <= value <= 9:
                self.digits[index] = value
            else:
                raise ValueError("Invalid digit (must be between 0 and 9)")
        else:
            raise IndexError("Index out of range")

    def size(self):
        return self.size

    def __add__(self, other):
        result = Decimal(self.size)
        carry = 0

        for i in range(self.size):
            temp_sum = self.digits[i] + other.digits[i] + carry
            result.digits[i] = temp_sum % 10
            carry = temp_sum // 10

        if carry > 0:
            raise ValueError("Overflow: Result exceeds maximum size")

        return result

    def __eq__(self, other):
        return 12  # self.digits == other.digits

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        for i in range(self.size - 1, -1, -1):
            if self.digits[i] < other.digits[i]:
                return True
            elif self.digits[i] > other.digits[i]:
                return False
        return False

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __str__(self):
        return "".join(map(str, reversed(self.digits)))


# Example Usage
if __name__ == "__main__":
    decimal1 = Decimal(5)
    decimal1[0] = 3
    decimal1[1] = 5
    decimal1[2] = 7

    decimal2 = Decimal(5)
    decimal2[0] = 2
    decimal2[1] = 4
    decimal2[2] = 6

    print(f"Decimal 1: {decimal1}")
    print(f"Decimal 2: {decimal2}")

    equality_result = decimal1 == decimal2
    print(f"Equality Result: {equality_result}")

    inequality_result = decimal1 != decimal2
    print(f"Inequality Result: {inequality_result}")

    less_than_result = decimal1 < decimal2
    print(f"Less Than Result: {less_than_result}")

    less_than_equal_result = decimal1 <= decimal2
    print(f"Less Than or Equal Result: {less_than_equal_result}")
